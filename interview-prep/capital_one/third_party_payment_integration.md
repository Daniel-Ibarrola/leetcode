# Third-Party Payment Service Integration

## Overview

Integrating a third-party payment processor (Stripe, PayPal, ACH network, etc.) requires handling asynchronous settlement and ensuring the ledger remains the source of truth for all money movements. The **Outbox pattern** ensures that database updates and external API calls stay consistent even during failures.

## The Problem

Without careful handling, you risk money being processed by the third party but never recorded in your ledger (or vice versa):

```python
# ❌ DANGEROUS - not atomic
db.payments.update(payment.id, status="posted")
ledger.debit(account_id, amount, idempotency_key)  # <- crash here?
```

If the service crashes between the database update and the ledger call:
- Database says payment is posted ✓
- Ledger was never debited ✗
- Money wasn't actually moved, but customer thinks it was

## The Solution: Outbox Pattern

Instead of calling the ledger directly, **write an event record atomically with the database update**:

```python
# ✅ ATOMIC - both happen or neither does
with db.transaction():
    db.payments.update(payment.id, status="posted")
    db.outbox.insert({
        event_type: "payment.settled",
        payload: { payment_id, amount, account_id },
        idempotency_key: payment.idempotency_key,
        published: False
    })
# Transaction commits; both rows are in the DB
```

Then a **separate background process** drains the outbox and calls the ledger:

```python
# Background job (Outbox Processor) - runs continuously
def process_outbox():
    for event in db.outbox.find(published=False):
        try:
            # Call the external system
            ledger.debit(
                account_id=event.payload["account_id"],
                amount=event.payload["amount"],
                idempotency_key=event.idempotency_key
            )
            # Mark as published only after success
            db.outbox.update(event.id, published=True)
        except Exception as e:
            # Failed; retry next time
            log.error(f"Failed to process {event.id}: {e}")
            # Don't update published=True; the job will retry
```

## Architecture Diagram

```mermaid
flowchart TB
    Client["Customer"]
    
    subgraph Platform["Online Banking Platform"]
        PaymentSvc["Payment Service"]
        AuthSvc["Authorization Service<br/>(shared across payment types)"]
        PaymentDB[("payments table<br/>(pending/posted)")]
        Outbox["Outbox table<br/>(unpublished events)"]
        Processor["Outbox Processor<br/>(background job)"]
    end
    
    subgraph ThirdParty["Third Party<br/>(Stripe, ACH, etc.)"]
        TPGateway["Payment Gateway API"]
        TPWebhook["Webhook callback"]
    end
    
    subgraph Core["Core Services"]
        Ledger["Account Balance Service<br/>(source of truth)"]
        Fraud["Fraud Detection Service"]
    end
    
    subgraph Monitoring["Monitoring"]
        Recon["Reconciliation Job<br/>(nightly)"]
    end
    
    Client -->|POST /accounts/{id}/payments<br/>Idempotency-Key: {uuid}| PaymentSvc
    PaymentSvc -->|authorize(account_id, amount)| AuthSvc
    AuthSvc -->|check balance| Ledger
    AuthSvc -->|fraud score| Fraud
    AuthSvc -->|approve/decline| PaymentSvc
    
    PaymentSvc -->|if approved: charge()| TPGateway
    PaymentSvc -->|insert pending| PaymentDB
    PaymentSvc -->|202 Accepted| Client
    
    TPGateway -->|async processing| TPWebhook
    TPWebhook -->|webhook: charge.succeeded| PaymentSvc
    PaymentSvc -->|update status to posted| PaymentDB
    PaymentSvc -->|atomically insert event| Outbox
    
    Processor -->|drain unpublished<br/>events| Outbox
    Processor -->|debit(amount,<br/>idempotency_key)| Ledger
    Processor -->|mark published| Outbox
    
    Ledger -->|emit payment.posted| Client
    Ledger -->|event bus| Processor
    
    Recon -->|reconcile<br/>list_charges()| TPGateway
    Recon -->|verify against<br/>ledger| Ledger
    Recon -->|alert on<br/>mismatch| Monitoring
```

## Authorization Service (Separated Concern)

The **Authorization Service** is separate from Payment Service because:

1. **Different SLA/scale** — authorization is frequently called by multiple payment types; separates concerns from settlement
2. **Reuse across types** — used by external payments, internal transfers, card transactions, etc.
3. **Independent failure mode** — authorization can fail fast without blocking the payment orchestrator
4. **Cleaner testing** — authorization rules can be verified independently

### Authorization Service Contract

```python
class AuthorizationService:
    def authorize(self, account_id: str, amount: int, 
                  payment_type: str = "external") -> dict:
        """
        Check if a payment is allowed.
        
        payment_type: "external", "transfer", "card", etc.
        
        Returns: {
            "approved": bool,
            "reason": "error_code" (if rejected),
            "retry_after": seconds (if transient failure),
            "available": balance (if insufficient funds)
        }
        """
```

### Authorization Rules

```python
def authorize(self, account_id, amount, payment_type):
    account = ledger.get_account(account_id)
    
    # Rule 1: Account status
    if account.status != "active":
        return {
            "approved": False,
            "reason": f"account_{account.status}",  # frozen, closed, etc.
            "retry_after": None
        }
    
    # Rule 2: Sufficient balance/credit
    if account.balance < amount:
        return {
            "approved": False,
            "reason": "insufficient_funds",
            "available": account.balance
        }
    
    # Rule 3: Fraud check (fail-open: don't block on scoring delays)
    try:
        fraud_result = fraud_service.score(
            account_id=account_id,
            amount=amount,
            payment_type=payment_type,
            timeout=1.0  # 1 second timeout
        )
        if fraud_result.risk_level == "high":
            return {
                "approved": False,
                "reason": "fraud_risk",
                "retry_after": 300  # Can retry in 5 min
            }
    except TimeoutError:
        # Fraud service slow; fail open (allow payment)
        log.warn(f"Fraud check timeout for {account_id}")
    
    # Rule 4: Daily/monthly payment limits
    daily_used = db.get_daily_payment_volume(account_id)
    if daily_used + amount > account.daily_limit:
        return {
            "approved": False,
            "reason": "daily_limit_exceeded",
            "limit": account.daily_limit,
            "used": daily_used
        }
    
    # All checks passed
    return {
        "approved": True,
        "account_version": account.version
    }
```

### Payment Service calls Authorization Service

```python
def post_payment(account_id, amount, idempotency_key):
    # Step 1: Check authorization (synchronously)
    auth = authorization_service.authorize(
        account_id=account_id,
        amount=amount,
        payment_type="external"
    )
    
    if not auth["approved"]:
        return 422 {
            "error": auth["reason"],
            "retry_after": auth.get("retry_after"),
            "available": auth.get("available")
        }
    
    # Step 2: Authorization passed; proceed with third party
    third_party_ref = stripe.charge(
        amount=amount,
        idempotency_key=idempotency_key,
        metadata={"account_id": account_id}
    )
    
    # Step 3: Record and proceed with outbox pattern
    ...
```

---

## Data Flow

### 1. Customer initiates payment

```
POST /accounts/{id}/payments
Idempotency-Key: abc-123-def
{ "amount": 25000, "currency": "USD", "source": "bank_account_ref" }
```

### 2. Payment Service authorizes and calls third party

```python
# Payment Service handler
@app.post("/v1/accounts/<account_id>/payments")
def post_payment(account_id, amount, idempotency_key):
    # Step 1: Check idempotency (early return if already processed)
    existing = db.payments.find_by_idempotency_key(idempotency_key)
    if existing:
        return existing  # Replay original response
    
    # Step 2: Call Authorization Service
    auth = authorization_service.authorize(
        account_id=account_id,
        amount=amount,
        payment_type="external"
    )
    
    if not auth["approved"]:
        return 422 {
            "error": auth["reason"],
            "retry_after": auth.get("retry_after"),
            "available": auth.get("available")
        }
    
    # Step 3: Authorization passed; call third party with idempotency
    try:
        third_party_ref = stripe.charge(
            amount=amount,
            idempotency_key=idempotency_key,
            metadata={"account_id": account_id}
        )
    except StripeError as e:
        # Third party temporarily unavailable
        return 503 {
            "error": "payment_processor_unavailable",
            "retry_after": 60
        }
    
    # Step 4: Record as pending immediately
    payment = db.payments.insert({
        payment_id: generate_uuid(),
        account_id: account_id,
        amount: amount,
        status: "pending",
        third_party_ref: third_party_ref,
        idempotency_key: idempotency_key,
        created_at: now()
    })
    
    return 202 {
        payment_id: payment.payment_id,
        status: "pending",
        third_party_ref: third_party_ref
    }
```

### 3. Third party processes asynchronously

The payment processor takes time (ACH = 1-3 days, card = seconds to minutes). Once settled, it calls your webhook.

### 4. Webhook handler receives settlement notification

```python
# Webhook endpoint (called by Stripe/third party)
@app.post("/webhooks/third-party/charge")
def handle_charge_webhook(event):
    third_party_ref = event["charge_id"]
    
    # Find the pending payment
    payment = db.payments.find_by_third_party_ref(third_party_ref)
    if not payment:
        # Webhook arrived before we recorded the payment?
        # Return 202; third party will retry
        return 202
    
    if event["status"] == "succeeded":
        # ATOMIC: update status AND write to outbox
        with db.transaction():
            db.payments.update(payment.payment_id, status="posted")
            db.outbox.insert({
                event_id: generate_uuid(),
                event_type: "payment.settled",
                payload: {
                    payment_id: payment.payment_id,
                    account_id: payment.account_id,
                    amount: payment.amount,
                    third_party_ref: third_party_ref
                },
                idempotency_key: payment.idempotency_key,
                published: False,
                created_at: now()
            })
        return 200
    
    elif event["status"] == "failed":
        db.payments.update(payment.payment_id, status="failed", 
                          failure_reason=event.get("failure_reason"))
        # Emit failure event; notify user
        emit_event("payment.failed", { payment_id: payment.payment_id })
        return 200
    
    # Other statuses (pending): do nothing, wait for final callback
    return 200
```

### 5. Outbox Processor drains events and posts to ledger

```python
# Background job - runs every 1-5 seconds
class OutboxProcessor:
    def process(self):
        for event in db.outbox.find(published=False).limit(100):
            if event.event_type == "payment.settled":
                self._handle_payment_settled(event)
            elif event.event_type == "payment.failed":
                self._handle_payment_failed(event)
    
    def _handle_payment_settled(self, event):
        try:
            # Call ledger with idempotency key
            result = ledger.debit(
                account_id=event.payload["account_id"],
                amount=event.payload["amount"],
                idempotency_key=event.idempotency_key
            )
            
            if result.status == 201:
                # Success - mark as published
                db.outbox.update(event.event_id, published=True)
                # Emit event for downstream (notifications, etc.)
                emit_event("payment.posted", event.payload)
            else:
                # Ledger rejected (e.g., insufficient funds, account frozen)
                # This is a business error, not a retry scenario
                db.payments.update(
                    event.payload["payment_id"],
                    status="failed",
                    failure_reason=result.error
                )
                db.outbox.update(event.event_id, published=True)
                emit_event("payment.failed", event.payload)
        
        except Exception as e:
            # Transient failure (network, timeout, etc.)
            # Leave published=False; retry next cycle
            log.error(f"Failed to process event {event.event_id}: {e}")
            # Optionally: increment retry count, alert if too many retries
    
    def _handle_payment_failed(self, event):
        # Emit notification to user
        emit_event("payment.failed_notified", event.payload)
        db.outbox.update(event.event_id, published=True)

# Run continuously
if __name__ == "__main__":
    processor = OutboxProcessor()
    while True:
        processor.process()
        time.sleep(1)  # Poll every second
```

## Database Schema

### `payments` table

| Column | Type | Notes |
|--------|------|-------|
| `payment_id` | UUID | PK. |
| `account_id` | UUID | FK → accounts. |
| `amount` | BIGINT | Minor units (cents). |
| `currency` | CHAR(3) | ISO 4217. |
| `status` | ENUM | `pending`, `posted`, `failed`. |
| `third_party_ref` | VARCHAR | External payment gateway reference. |
| `idempotency_key` | VARCHAR | **Unique.** Client-supplied key. |
| `failure_reason` | TEXT | Reason for failure (optional). |
| `created_at` | TIMESTAMPTZ | |
| `updated_at` | TIMESTAMPTZ | |

Indexes:
- `UNIQUE(idempotency_key)` — dedupes retries
- `(account_id, created_at DESC)` — payment history
- `(third_party_ref)` — lookup by external ref

### `outbox` table

| Column | Type | Notes |
|--------|------|-------|
| `event_id` | UUID | PK. |
| `event_type` | VARCHAR | e.g., `payment.settled`, `payment.failed`. |
| `payload` | JSONB | Event data (payment_id, amount, account_id, etc.). |
| `idempotency_key` | VARCHAR | From the original payment; ensures ledger debit is idempotent. |
| `published` | BOOLEAN | Has this event been successfully published to ledger? |
| `retry_count` | INT | Incremented on each retry attempt. |
| `last_error` | TEXT | Error message from last retry (debugging). |
| `created_at` | TIMESTAMPTZ | |
| `published_at` | TIMESTAMPTZ | When marked as published. |

Indexes:
- `(published, created_at)` — drain loop finds unpublished
- `(retry_count)` — monitor stuck events
- `(published_at DESC)` — track throughput

## Reconciliation Job

Because third parties and your system can diverge (flaky webhooks, network issues, bugs), run a **nightly reconciliation**:

```python
def reconcile_third_party_payments():
    """
    Verify that every settled payment in the third party system
    has been posted to our ledger.
    """
    # Fetch all transactions from third party (past 24-48 hours)
    third_party_txns = stripe.list_charges(
        created_after=now() - 48_hours,
        limit=10000
    )
    
    issues = []
    
    for txn in third_party_txns:
        if txn.status != "succeeded":
            continue  # Only care about settled
        
        # Check: do we have a record?
        payment = db.payments.find_by_third_party_ref(txn.id)
        
        if not payment:
            issues.append({
                type: "missing_payment",
                third_party_ref: txn.id,
                amount: txn.amount,
                message: f"Third party has settled {txn.id} but we have no record"
            })
            continue
        
        # Check: is it posted to the ledger?
        if payment.status != "posted":
            issues.append({
                type: "unposted_payment",
                payment_id: payment.payment_id,
                third_party_ref: txn.id,
                message: f"Payment {payment.payment_id} is {payment.status}, not posted"
            })
            continue
        
        # Check: ledger has the transaction
        ledger_txn = ledger.find_by_idempotency_key(payment.idempotency_key)
        if not ledger_txn:
            issues.append({
                type: "missing_ledger_entry",
                payment_id: payment.payment_id,
                third_party_ref: txn.id,
                message: f"Payment {payment.payment_id} is marked posted but not in ledger"
            })
    
    if issues:
        for issue in issues:
            log.error(f"Reconciliation issue: {issue}")
            alert(f"Payment reconciliation issue: {issue['type']}")
    
    return issues

# Run nightly
if __name__ == "__main__":
    schedule.every().day.at("02:00").do(reconcile_third_party_payments)
```

## Why This Design

| Aspect | Choice | Rationale |
|--------|--------|-----------|
| **Consistency model** | Eventual (pending → posted) | Third party is slow; ledger is source of truth once settled. |
| **Latency to customer** | Return 202 immediately | Don't block client on third-party latency; status is polled. |
| **Failure handling** | Webhook retry + outbox processor retry + nightly reconciliation | Third party may fail, webhooks may be lost, network may hiccup. Multiple layers catch misses. |
| **Idempotency** | End-to-end (client key → platform → third party → ledger) | Every step can retry safely without duplicating. |
| **Source of truth** | Ledger (Account Balance Service) | Only the ledger records settled money. Payments table is transient state. |

## Failure Scenarios and Recovery

| Scenario | What happens | Recovery |
|----------|---|---|
| **Webhook lost** | Payment stays pending; outbox has nothing | Nightly reconciliation detects it, manual override, or user retries manually |
| **Outbox processor crashes** | Events stay unpublished | Processor restarts, drains outbox from where it left off |
| **Ledger call times out** | Event stays unpublished; retry on next cycle | Ledger call is idempotent, so replay is safe |
| **Ledger rejects (insufficient funds)** | Outbox marks as published, payment marked failed | Business error; emit failure event, notify user |
| **Duplicate webhook** | Second webhook finds payment already marked posted | Webhook handler is idempotent; returns 200 |
| **Third party down** | Charge call times out; return 503 to customer | Customer retries with same idempotency key; third party dedupes |

## Monitoring & Alerting

```python
# Track key metrics
metrics = {
    "payments_pending": db.payments.count(status="pending"),
    "payments_posted": db.payments.count(status="posted"),
    "payments_failed": db.payments.count(status="failed"),
    "outbox_depth": db.outbox.count(published=False),
    "outbox_max_retry_count": db.outbox.max("retry_count"),
    "outbox_age_seconds": db.outbox.min_age(published=False),
}

# Alert if:
# - Outbox depth > 1000 (processor is stuck)
# - Outbox max retry > 5 (event keeps failing)
# - Outbox age > 300 seconds (event stuck for 5 min)
# - Reconciliation issues found
```

## Design Decisions

| Aspect | Choice | Why |
|--------|--------|-----|
| **Consistency model** | Eventual (pending → posted) | Third party is slow; ledger is source of truth once settled. |
| **Latency to customer** | Return 202 immediately | Don't block client on third-party latency; status is polled. |
| **Failure handling** | Webhook retry + outbox processor retry + nightly reconciliation | Third party may fail, webhooks may be lost, network may hiccup. Multiple layers catch misses. |
| **Idempotency** | End-to-end (client key → platform → third party → ledger) | Every step can retry safely without duplicating. |
| **Source of truth** | Ledger (Account Balance Service) | Only the ledger records settled money. Payments table is transient state. |
| **Authorization isolation** | Separate Authorization Service | Can be called by multiple payment types; independent scaling; reusable rules engine. |
| **Outbox pattern** | Events stored durably, processed async | Ensures no payment is lost even if services crash between DB update and ledger call. |

## Key Takeaways

1. **The Outbox pattern ensures atomicity** between database updates and external calls, even during failures.
2. **Payments are eventually consistent** — they go from pending → posted over seconds to days depending on the payment method.
3. **The ledger is the source of truth** — only posted payments are recorded there.
4. **Idempotency flows end-to-end** — client → platform → third party → ledger, so retries are safe.
5. **Authorization is isolated** — reusable across payment types (external, transfers, cards); independent scaling and failure modes.
6. **Reconciliation catches misses** — nightly job verifies every third-party settlement made it to the ledger.
7. **No payment is lost** — if it settled with the third party, it will eventually post to the ledger, even if services crash or network hiccups occur.
