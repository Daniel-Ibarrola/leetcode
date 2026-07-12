# Banking Platform

A reduced version of the online banking platform taking elements from the account balance service, online banking platform
and virtual credit card.

## Requirements

1. Apply for cards
2. Manage payments including using third party payment service
3. Payment Authorization
4. Support calculating daily, weekly and monthly statistics

## Estimations

Back-of-the-envelope sizing. The point is the **method** and knowing which number drives which design
decision — precision is secondary.

**Assumptions**

| Assumption | Value |
|--|--|
| Active customers | 100M |
| Card transactions / customer / day | 5 |
| Peak-to-average factor | ~4× (lunch, evenings, holidays) |
| Ledger entries / payment | ~3 (double-entry legs + auth hold) |
| Portal reads / active user / day | ~3 |

**Throughput**

| Path | Volume/day | Avg | Peak (~4×) |
|--|--|--|--|
| Payments (writes) | 500M | ~6k TPS | **~25k TPS** |
| Ledger entry writes | 1.5B | ~17k/s | **~70k/s** |
| Portal reads | ~120M | ~1.5k TPS | ~6k TPS (90%+ cache/read-model served) |

> Headline numbers: **~25k payments/sec and ~70k ledger writes/sec at peak.**

**Storage**

| Store | Row size | Per day | Notes |
|--|--|--|--|
| `payments` | ~300 B | ~150 GB | ~55 TB/yr |
| `ledger_entries` | ~150 B | ~225 GB | ~80 TB/yr, append-only system of record |
| DynamoDB read model | ~250 B | ~125 GB | TTL old items; cold history from lake |
| S3 lake (parquet) | compressed ~5–8× | ~50–75 GB | ~20 TB/yr archive |
| Idempotency (DynamoDB) | ~200 B, 48h TTL | ~200 GB steady | self-expiring |

The ledger grows **unbounded** (~137 TB/yr raw), so we keep a **rolling ~90-day hot window in Aurora (~34 TB,
across shards)** and age the rest to the S3 lake, which the portal falls back to for old history.

**What these numbers decide**

- **Shard count:** ~70k ledger writes/s ÷ ~10k/s per Aurora writer ≈ 8 → round to **16 shards** by `account_id` for headroom.
- **Outbox parallelism:** must drain ~6k settlements/s → `SELECT … FOR UPDATE SKIP LOCKED` with ~20 parallel workers (a single 100/poll loop can't keep up).
- **Hot/cold tiering:** the 137 TB/yr ledger is why archival + lake fallback exist.
- **Cache sizing:** ~40M DAU balances × ~100 B ≈ ~4 GB working set → fits one ElastiCache cluster, justifying cache-first balance reads.

*Caveats worth stating aloud:* card TPS is bursty (Black Friday spikes beyond 4×), and the read:write ratio
depends on portal engagement — reads assumed same order as writes, not the 10:1 of a pure browsing product.

## High Level Diagram

```mermaid
flowchart TB
    Client["customer"]

    subgraph Cloud["AWS"]
        APIGW["API Gateway"]
        Cognito["Cognito<br/>(authN)"]

        subgraph PortalReadPath["Portal Read Path (CQRS reads)"]
            QueryService["Query Service<br/>(BFF, EKS, read-only)"]
            ReadModelConsumer["Read Model Consumer<br/>(ECS Fargate)"]
            ReadModelDB[("Account Activity Read Model<br/>(DynamoDB)")]
        end


        subgraph PaymentPlatform["Payment Platform VPC"]
            PaymentService["Payment Service (EKS)"]
            AuthorizationService["Authorization Service<br/>(authorization, risk, fraud check)"]
            
            PaymentDB[("Aurora SQL<br/>(Payments and Outbox Table)")]

            OutboxProcessor["Outbox Processor (ECS Fargate)"]
        end

        subgraph ApplicationPlatform["Application Platform VPC"]
            ApplyService["Apply Service"]
            ApplicationKinesis["Kinesis"]
            ApplicationSF["Step Functions"]
            ApplicationDB[("Aurora SQL<br/>(applications, cards + outbox)")]
            KYCVault["KYC Vault<br/>(encrypted PII)"]
        end

        subgraph LedgerPlatform["Ledger VPC"]
            BalanceService["Balance Service (EKS)"]
            BalanceCache["Balance Cache<br/>(ElastiCache Redis)"]

            subgraph LedgerDB["Aurora PSQL"]
                Writer[("writer")]
                RR1[("Read Replica")]
                RR2[("Read Replica")]
            end 
        end

        subgraph ETLPlatform["ETL Platform"]
            KinesisETL["Kinesis Data Streams"]
            KinesisDFH["Kinesis DataFireHose"]
            S3Lake["S3 Data Lake<br/>(parquet files)"]
            ETLJob["ETL Job<br/>(Glue + Event Bridge)"]
        end

        subgraph AnalyticsPlatform["Analytics Platform"]
            DW["Data Warehouse<br/>(Redshift)"]
            AnalyticsSvc["Analytics Service<br/>(EKS)"]
        end

        NotificationService["Notification Service"]
    end

    PGW["Payment Gateway<br/>(third party)"]

    Client --> APIGW
    APIGW -.-> |authN| Cognito

    APIGW --> PaymentService
    APIGW --> ApplyService
    APIGW --> |balance + history reads| QueryService

    QueryService --> |balance| BalanceService
    QueryService --> |transaction history| ReadModelDB
    BalanceService --> |cached balance| BalanceCache
    KinesisETL --> ReadModelConsumer --> ReadModelDB
    
    PaymentService --> AuthorizationService
    PaymentService --> PGW
    PGW --> |webhook| PaymentService
    PaymentService --> |payment status pending + insert outbox| PaymentDB
    AuthorizationService --> BalanceService
    OutboxProcessor --> BalanceService
    OutboxProcessor --> PaymentDB
    PaymentDB --> |CDC| KinesisETL

    ApplyService --> |application state + outbox| ApplicationDB
    ApplyService --> |KYC PII| KYCVault
    ApplyService --> ApplicationKinesis --> ApplicationSF --> NotificationService

    BalanceService --> |balance reads + writes| Writer
    BalanceService --> |history reads| RR1 & RR2
    Writer -. replication .-> RR1 & RR2
    Writer --> |CDC| KinesisETL

    KinesisETL --> KinesisDFH --> S3Lake --> ETLJob --> DW

    DW --> AnalyticsSvc
```
---
## Storage Schema

Simplified storage schema for databases, only key columns are included

### Balance Service DB (Ledger)

This is the DB that contains the ledger — the **source of truth for balances**. It uses double-entry
bookkeeping: every money movement is a `ledger_transaction` made up of two or more balanced
`ledger_entries`. Not every entry comes from a payment (interest, fees, adjustments, chargebacks all
originate here), which is why this is a separate database from Payments — see
[Payments vs. Ledger](#payments-vs-ledger-why-two-databases).

Tables:

**ledger_transactions**

Groups the entries that make up a single balanced money movement.

| Column | Type | Notes |
|--------|------|-------|
| `transaction_id` | UUID | PK. Generated by the Balance Service. |
| `source_payment_id` | UUID | **Nullable.** FK reference to `payments.payment_id`. `NULL` for ledger-originated movements (interest, fees, adjustments). Not unique — one payment may span several transactions (e.g. a cross-shard transfer). |
| `dedupe_id` | UUID | **Unique.** The outbox `event_id`; makes ledger writes idempotent (see [Idempotency Boundary 2](#boundary-2--outbox-processor--balance-service-dedupe-ledger-writes)). |
| `reason` | ENUM | `payment`, `fee`, `interest`, `adjustment`, `reversal`, `transfer`. |
| `created_at` | TIMESTAMP | |

**Invariant:** the entries of a single `transaction_id` must **sum to zero** (Σ debits = Σ credits) — enforced
by a DB constraint/trigger. This is what makes it a real double-entry ledger. For a cross-shard transfer, each
shard writes its *own* balanced transaction (customer leg + a clearing leg), so the invariant holds **per
transaction within every shard**; the two shards' clearing legs net out during reconciliation.

**ledger_entries**

| Column | Type | Notes |
|--------|------|-------|
| `entry_id` | UUID | PK. |
| `transaction_id` | UUID | FK → `ledger_transactions`. |
| `account_id` | UUID | FK → `accounts`. Shard key. |
| `direction` | ENUM | `debit` or `credit`. |
| `amount` | BIGINT | Minor units, always **positive**; `direction` carries the sign. |
| `status` | ENUM | `pending` (authorization hold — affects *available* balance only) → `posted` (settled — affects *posted* balance) → `reversed` (compensated). |
| `created_at` | TIMESTAMP | Effective time of the entry; drives history ordering. |

**accounts**

| Column | Type | Notes |
|--------|------|-------|
| `account_id` | UUID | PK. Also the shard key. |
| `posted_balance` | BIGINT | **Minor units (cents).** Materialization of `posted` entries only. |
| `version` | BIGINT | Optimistic-lock / row version, bumped on every mutation. |

**Available balance** is derived, not stored: `available = posted_balance − Σ(pending debit holds)`. The
Authorization Service checks *available* (not posted) so in-flight holds block overspending.


### Payment DB

Tracks the **lifecycle of moving money through external rails** (the payment gateway / card network).
A payment records intent and status; a failed or declined payment is a valid row here that **never
touches the ledger**. One payment maps to at most one `ledger_transaction` (via `source_payment_id`).

**payments**

| Column | Type | Notes |
|--------|------|-------|
| `payment_id` | UUID | PK. |
| `type` | ENUM | `credit`, `debit`, `transfer`. |
| `status` | ENUM | `pending`, `posted`, `failed`, `reversed`. |
| `idempotency_key` | VARCHAR | **Unique.** Dedupes client retries. |
| `gateway_ref` | VARCHAR | Reference ID returned by the third-party gateway. |

**outbox**

Written atomically with `payments` in the same local transaction (see [Outbox Pattern](#outbox-pattern)).

| Column | Type | Notes |
|--------|------|-------|
| `event_id` | UUID | PK. Also the stable dedupe key passed to the Balance Service. |
| `event_type` | VARCHAR | e.g. `payment.settled`. |
| `payload` | JSONB | **Balanced legs**, e.g. `{ payment_id, entries: [{account_id, direction:"debit", amount}, {clearing_account_id, direction:"credit", amount}] }`. |
| `idempotency_key` | VARCHAR | The payment's client key (audit/trace). |
| `published` | BOOLEAN | `False` until the Outbox Processor confirms the ledger applied it. |
| `retry_count` | INT | Incremented on failed delivery. |

### Apply Service DB

Stores the card-application lifecycle (driven by Step Functions) plus provisioned cards. Sensitive KYC PII
lives in a separate encrypted **KYC Vault**, referenced by pointer — the high-churn tables stay free of
crown-jewel data. On approval, the funding account is created in the ledger `accounts` table.

**applications**

| Column | Type | Notes |
|--------|------|-------|
| `application_id` | UUID | PK. |
| `status` | ENUM | `submitted`, `identity_check`, `credit_check`, `approved`, `declined`. |
| `kyc_ref` | VARCHAR | **Pointer** to KYC Vault — not the PII itself. |

**cards** (provisioned on approval)

| Column | Type | Notes |
|--------|------|-------|
| `card_id` | UUID | PK. |
| `account_id` | UUID | FK → ledger `accounts`. |
| `pan_token` | VARCHAR | **Tokenized** PAN / vault reference — never the raw number. CVV never stored. |
| `status` | ENUM | `active`, `frozen`, `closed`. |

An **outbox** table (same shape as the Payment DB) carries the `application.approved` event so account/card
provisioning is a consistent downstream write rather than a risky dual write.

---

### Payments vs. Ledger (why two databases)

`payments.payment_id` and `ledger_entries.transaction_id` are **different concepts that were both once
called "transaction"** — the source of most confusion here.

| | Payment | Ledger transaction |
|--|---------|--------------------|
| **Owns** | Payment Service | Balance Service |
| **Represents** | Instruction moving through external rails | Accounting truth (double-entry) |
| **Grain** | One instruction | One balanced set of 2+ entries |
| **Failed/declined case** | Real row, `status=failed` | No row at all |
| **No-payment case** | n/a | Interest, fees, adjustments, chargebacks |
| **Scaling profile** | Status churn from gateway webhooks | Append-only, sharded by `account_id` |

They map **one-to-many, not one-to-one** (one payment → one *or more* ledger transactions, each of 2+ balanced
entries — a cross-shard transfer produces one per shard), have
different consistency and scaling needs, and are owned by different services in different VPCs. The
outbox pattern exists *because* they are separate transactional boundaries — merging the databases
would defeat it. The link between them is a nullable **reference** (`source_payment_id`), not a shared key.



## Data Flows

### Payment Flow

The ordering below is deliberate: the idempotency key is reserved **before** any external call, funds are
**held on the ledger at authorization time**, and the outbox event is written **only at settlement** — so a
declined payment never moves money.

1. Client sends payment request with an `Idempotency-Key` header
2. Payment Service **inserts a `payments` row as `pending` first.** The `UNIQUE(idempotency_key)` constraint
   reserves the key *before* any side effect, so two concurrent retries cannot both proceed to the gateway
3. Payment Service calls the Authorization Service, which **synchronously writes a balanced `pending` hold to
   the ledger** (reduces *available* balance, not *posted* balance) alongside account-status and fraud checks.
   Concurrent payments now contend on genuinely reserved funds → no overspend race
4. If authorized, Payment Service calls the third-party gateway (e.g. Stripe), **passing the same idempotency
   key** so the external charge is itself deduped on retry
5. Gateway returns immediately with a reference ID; Payment Service persists `gateway_ref` and returns 202 to the client
6. Gateway processes asynchronously and calls the webhook when settled
7. **Webhook handler** — signature-verified and idempotent on `gateway_ref` — transitions the payment and,
   **in the same local transaction, writes the outbox event** (Outbox pattern), so the outbox fires *only* for
   settled payments:
   - **Settled** → `pending → posted`, insert `payment.settled` outbox event
   - **Declined** → `pending → failed`, **release the hold**; no outbox event, the ledger keeps nothing
8. Outbox Processor drains the outbox continuously and calls the Balance Service to **convert the hold into a
   posted, balanced transaction** (both legs — see [Ledger API](#ledger-api-balanced-postings)), keyed by a stable dedupe id
9. Balance Service posts the balanced ledger transaction atomically and flips the hold entries to `posted`
10. Outbox Processor marks the event `published`
11. Data flows to Kinesis CDC → Redshift for analytics

### Card Application Flow
1. Client submits application with KYC info
2. Apply Service writes the sensitive PII to the **KYC Vault** (encrypted) and persists an `applications`
   row with `status=submitted` and `kyc_ref` pointing at the vault entry
3. Apply Service starts the Step Functions workflow, storing `sf_execution_arn` on the application row
4. Step Functions orchestrates: identity check → credit check → decision, and the Apply Service advances
   `status` on the `applications` row at each stage (`identity_check` → `credit_check` → `approved`/`declined`)
5. On approval, the Apply Service **atomically** (single local transaction) sets `status=approved` and inserts
   an `application.approved` **outbox** event — same pattern as payments, avoiding a risky dual write
6. Downstream provisioning drains the outbox and:
   - creates the funding account in the ledger `accounts` table (Balance Service)
   - inserts a `cards` row with a **tokenized** `pan_token` (raw PAN never stored)
7. The approval event also flows to **Kinesis** for the analytics pipeline / customer notification
8. On decline, `status=declined` with `decision_reason`; no provisioning occurs

### Portal Read Path (balance + transaction history)

Customer browsing is a **read-heavy CQRS path**, kept isolated from the payment/settlement write path.
Every query is scoped to the authenticated `account_id` (Cognito) — a customer can only ever read their own data.

**Balance**
1. Client requests balance → API Gateway → Query Service (BFF)
2. Query Service calls the **Balance Service** read API — it does **not** touch the ledger DB directly
   (that DB is encapsulated behind its owning service)
3. Balance Service serves from its **Redis cache** (write-through, invalidated on ledger mutation since it
   owns the writes), falling back to a **read replica** — never the writer
4. Response shows **available balance = posted − pending holds**, and lists in-flight (Saga `pending`) transactions distinctly

> The cache lives with the Balance Service, not the Query Service: the owner of the writes is the only
> component that knows precisely when balance changes, making invalidation trivial. Browsing is still kept
> off the write path — the isolation is at the data layer (cache + read replicas), not by bypassing the service.

**Transaction history**
1. A **Read Model Consumer** ingests the existing CDC streams from both the ledger Writer and Payment DB
2. It denormalizes double-entry `ledger_entries` + payment metadata (merchant, memo) into a display-ready
   `account_activity` item — one customer-friendly line per transaction
3. Stored in **DynamoDB**: PK = `account_id`, SK = `timestamp#entry_id` → "latest N transactions" is a single-partition, single-digit-ms query
4. Query Service serves history from this read model with **keyset (cursor) pagination** (never `OFFSET`)

**Separation from analytics:** this operational read model is distinct from the Redshift path. Same CDC source,
two sinks — Redshift for daily/weekly/monthly **stats** (OLAP), DynamoDB read model for low-latency **customer reads**.

---

## Key Patterns

### Ledger API (balanced postings)

The Balance Service exposes **one write primitive**: post a *transaction* of two or more entries, never a
single-sided `debit`/`credit`. This is what makes double-entry enforceable.

```
POST /transactions
{
  "dedupe_id": "<uuid>",              # idempotency: unique per transaction
  "source_payment_id": "<uuid|null>",
  "reason": "payment",
  "entries": [
    { "account_id": "<customer>",  "direction": "debit",  "amount": 4500 },
    { "account_id": "<clearing>",  "direction": "credit", "amount": 4500 }
  ]
}
```

The service **rejects any request whose entries don't sum to zero** (Σ debits = Σ credits) and applies all
entries in one DB transaction. Two variants used by the flows above:

- **Hold** (authorization): post the balanced transaction with `status=pending` → affects *available* balance only
- **Settle**: flip the hold's entries `pending → posted` (or post a fresh balanced transaction) → affects *posted* balance
- **Release / reverse**: post a compensating balanced transaction, mark `reversed`

Because the counterparty (clearing) leg is always supplied by the caller, the ledger can construct a balanced
transaction from the request alone — the outbox payload carries both legs for exactly this reason.

### Idempotency Key

Idempotency is needed at **two independent boundaries**, and each is best served differently. The mistake
to avoid is bolting a single idempotency store onto the ledger — when the operation being deduped is a write
to the *same* database, a separate store just recreates the dual-write problem the outbox was built to solve.

#### Boundary 1 — Client → Payment Service (dedupe client retries)

The risky side effect here is calling the **external gateway** (not in our DB), so we want to avoid a second
charge and be able to replay the prior response fast. The client generates the key (a UUID) and sends it in
the `Idempotency-Key` header.

- **Correctness:** `payments.idempotency_key` is `UNIQUE` — a retried request cannot create a second payment.
- **Optional caching:** a **DynamoDB** store (`idempotency_key → { payment_id, status, response }`, TTL 24–48h)
  can absorb read load and give sub-ms replay of the cached response *if* client retries are aggressive.
  Keep it only if you need that; the unique constraint alone gives correctness.

#### Boundary 2 — Outbox Processor → Balance Service (dedupe ledger writes)

The outbox is **at-least-once**: the processor can crash after the ledger applies but before marking the event
`published`, so `ledger.post_transaction(...)` will occasionally be called twice. Here the deduped operation
**is a write to the ledger's own database**, so we enforce idempotency *inside that write* with a unique
constraint on the stable `dedupe_id` (the outbox `event_id`) — no separate store:

```sql
ALTER TABLE ledger_transactions
  ADD CONSTRAINT uq_dedupe UNIQUE (dedupe_id);
```

> Keyed on `dedupe_id` (the outbox `event_id`), **not** `source_payment_id` — one payment can legitimately
> produce more than one ledger transaction (e.g. a cross-shard transfer posts one per shard), so a
> `source_payment_id` unique constraint would wrongly reject the second leg.

Dedupe and write now share one ACID transaction. A duplicate call hits the unique violation → the service
returns **409**, which the Outbox Processor already treats as success (`if result.status in [201, 409]`) →
event marked `published`. No cross-store consistency window, and a strictly stronger guarantee than a
DynamoDB store would give.

> The outbox payload must carry a **stable** dedupe key (`payment_id`, or the payment's `idempotency_key`) so
> the ledger's unique constraint keys off a value that survives retries.

**Why no DynamoDB store on the ledger side?** Its headline benefits — read-offload and sub-ms lookups — don't
apply here. The only caller is the Outbox Processor and duplicates are crash-rare; there is no client retry
storm to absorb.

### Outbox Pattern

When a payment is made we need to update both the payments table as well as the ledger. As they are different databases
we need a way to ensure an atomic update.

If we try to update both, something bad can happen:

```python
# ❌ DANGEROUS - not atomic
db.payments.update(payment.id, status="posted")
ledger.post_transaction(entries, dedupe_id)  # <- crash here?
```

If the service crashes between the database update and the ledger call:
- Database says payment is posted ✓
- Ledger was never debited ✗
- Money wasn't actually moved, but customer thinks it was

We write an event record to the payments db:

```python
# ✅ ATOMIC - both happen or neither does (runs inside the webhook handler, on settlement)
with db.transaction():
    db.payments.update(payment.id, status="posted")
    db.outbox.insert({
        event_id: uuid4(),                       # stable dedupe id for the ledger
        event_type: "payment.settled",
        payload: {                               # BOTH legs → ledger can post a balanced txn
            payment_id: payment.id,
            entries: [
                { account_id: payment.account_id,  direction: "debit",  amount: payment.amount },
                { account_id: CLEARING_ACCOUNT,    direction: "credit", amount: payment.amount },
            ],
        },
        published: False,
    })
# Transaction commits; both rows are in the DB
```

Then a **separate background process** drains the outbox and calls the ledger. The Outbox Processor runs on **ECS Fargate** (not Lambda) because:
- It continuously polls the database (not event-triggered)
- No 15-minute timeout limit
- Can handle batches of events efficiently
- Retries failed events without losing state

```python
# Background job (Outbox Processor) - runs continuously on ECS Fargate
def process_outbox():
    while True:
        for event in db.outbox.find(published=False).limit(100):
            try:
                # Post a BALANCED transaction (all legs); dedupe on the stable event_id
                result = ledger.post_transaction(
                    entries=event.payload["entries"],
                    dedupe_id=event.event_id,
                    source_payment_id=event.payload["payment_id"],
                )
                # Mark as published only after success
                if result.status in [201, 409]:  # 409 = already processed (safe retry)
                    db.outbox.update(event.id, published=True)
            except Exception as e:
                # On failure: increment retry_count, retry on next cycle
                db.outbox.increment_retry(event.id)
        
        time.sleep(1)  # Poll every second
```

### Sharding the Ledger

To scale writes across the ledger, we shard by `account_id`. The challenge is transfers between accounts in different shards.

**Why not 2-Phase Commit?**  
2PC holds locks for the entire transaction duration, blocking other operations and reducing throughput. Instead, we use the **Saga pattern**.

**Each shard stays internally balanced via a clearing account.** The key to keeping double-entry sound across
shards is that a transfer is **not** one debit in shard A and one credit in shard B (that would leave each
shard's transaction unbalanced). Instead each shard writes its *own* balanced transaction against a
**transfer-clearing account** that lives in that shard:

- Shard A: `debit customer_1` / `credit transfer_out_clearing` → sums to zero
- Shard B: `debit transfer_in_clearing` / `credit customer_2` → sums to zero

The two clearing legs are reconciled out-of-band; the invariant holds per-transaction in each shard.

**Saga orchestration (Account 1 → Account 2), driven by a durable coordinator** (Step Functions or a
`saga_state` table — *not* just "replay", which has no forward-recovery on crash):

1. **Reserve** — in shard A, post the balanced debit as a `pending` hold (cannot be spent)
2. **Credit destination** — in shard B, post the balanced credit as `posted`
3. **Confirm or compensate:**
   - Step 2 succeeds → flip shard A's hold to `posted`
   - Step 2 fails / times out → compensation: post a reversing transaction in shard A, mark `reversed`

The coordinator persists each step and **retries forward on crash with a timeout**, so a failure between
steps 2 and 3 cannot strand funds — it either completes or compensates.

**Consistency guarantees:**
- **Eventual consistency** — a window (ms to seconds) where Account 1 shows a `pending` hold
- **Authorization protection** — during this window the hold reduces *available* balance, blocking overspend
- **Durability** — every step is a balanced, recorded ledger transaction; state is reconstructable, and the
  Saga coordinator (not replay alone) guarantees the transfer terminates

This trades immediate consistency for horizontal scalability across shards.
