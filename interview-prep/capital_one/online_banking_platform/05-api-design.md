# 5. API Design

REST over HTTPS, JSON bodies. Core endpoints only. Amounts are **integer minor
units** (cents). All mutations require an `Idempotency-Key` header.

## Conventions

- **Auth:** bearer JWT from the auth service, validated at API Gateway; MFA
  enforced at login for sensitive scopes.
- **Money:** `{ "amount": 1050, "currency": "USD" }` = \$10.50.
- **Idempotency:** replaying a key returns the original result without re-applying.
- **Errors:** `422` business rule, `409` conflict, `429` rate limited, `401/403`
  auth, `503` dependency unavailable (retry with same key).

## Auth

```
POST /v1/auth/login        { username, password }        → 200 { mfa_required, mfa_token }
POST /v1/auth/mfa/verify   { mfa_token, code }           → 200 { access_token, refresh_token }
```

## Applications (onboarding)

```
POST /v1/applications
{ applicant: { name, dob, ssn, address, income }, product: "cash-rewards" }
→ 202 { application_id, status: "submitted" }        # async workflow started

GET  /v1/applications/{id}
→ 200 { status: "credit_checked", decision: null }   # poll or receive webhook/push
```

`202`, not `201` — approval is asynchronous (KYC + credit check take seconds to
minutes). Client polls or gets a push notification.

## Accounts & cards

```
GET /v1/accounts/{id}
→ 200 { account_id, credit_limit, balance, available_credit,
        status, due_date, min_due }        # balance read strongly from ledger

GET /v1/accounts/{id}/cards
→ 200 { cards: [ { card_id, last4, exp, network, status } ] }   # never the PAN
```

## Transaction history

```
GET /v1/accounts/{id}/transactions?limit=50&cursor=<opaque>
→ 200 { entries: [ { txn_id, merchant, amount, direction, category,
                     status, posted_at } ], next_cursor }
```

Keyset (cursor) pagination on `(account_id, posted_at)` — stable and O(1) per
page over an ever-growing table.

## Statements

```
GET /v1/accounts/{id}/statements
→ 200 { statements: [ { statement_id, period, closing_balance, due_date } ] }

GET /v1/statements/{id}/pdf
→ 302 <pre-signed S3/CloudFront URL>      # short-lived, scoped to this user
```

## Payments

```
POST /v1/accounts/{id}/payments
Idempotency-Key: <uuid>
{ "amount": 25000, "source": "bank_account_ref", "currency": "USD" }
→ 201 { payment_id, status: "posted", new_balance: 120000 }
→ 422 { error: "amount_exceeds_balance" }
```

Delegates to the ledger's `transfer`; idempotent, so a retried payment never
double-pays.

## Disputes

```
POST /v1/disputes
Idempotency-Key: <uuid>
{ "txn_id": "...", "reason": "fraud", "amount": 8999 }
→ 201 { dispute_id, status: "opened", sla_due_at }

GET  /v1/disputes/{id}       → 200 { status, provisional_credit, resolution }
POST /v1/disputes/{id}/evidence  { docs: [ s3_ref ] }  → 202
```

## Admin

```
GET   /v1/admin/accounts/{id}                → 200 { … full account view … }
POST  /v1/admin/accounts/{id}/freeze         { reason }  → 200
POST  /v1/admin/accounts/{id}/adjustments    { amount, reason }  → 201
```

Admin actions require elevated scope, are **always** audited, and sensitive ones
require a second approver (four-eyes) — see
[detailed design](06-detailed-design.md#65-adminsecurity-controls).

## Notifications (preferences)

```
GET  /v1/notifications/preferences
PUT  /v1/notifications/preferences  { email: true, sms: false, push: true }
```

## Why these choices

- **`202 + poll/push` for onboarding and evidence** — these are long-running;
  blocking a request thread on a credit bureau is fragile and doesn't scale.
- **Idempotency mandatory on payments/disputes** — a timeout on a money or
  regulated action is ambiguous; the safe client behavior (retry) must be a
  no-op.
- **PAN never in any response** — only `last4`/token; card data stays in the PCI
  zone to keep audit scope small.
- **Pre-signed URLs for statements** instead of proxying bytes through the
  service — offloads large downloads to S3/CloudFront and keeps access scoped
  and time-limited.
