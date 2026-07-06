# 5. API Design

REST over HTTPS, JSON bodies. Core endpoints only. All amounts are **integer minor
units** (cents). All mutating endpoints require an `Idempotency-Key` header.

## Conventions

- Auth: bearer token, validated at API Gateway.
- Money: `{ "amount": 1050, "currency": "USD" }` = \$10.50.
- Mutations carry `Idempotency-Key: <uuid>`; replaying the same key returns the
  original result without re-applying it.
- Optimistic concurrency: reads return a `version`; a client may pass
  `If-Match: <version>` to make a write conditional.

## Operation types (what credit / debit / transfer mean)

The three mutating operations are the **same primitive** — move funds between two
accounts — differing only in *who the counterparty is*:

| Endpoint | Business intent | Counterparty | Crosses the system boundary? |
|----------|-----------------|--------------|------------------------------|
| `POST …/credit` | **Deposit** — money in | a **system** settlement account | Yes — from an external rail |
| `POST …/debit` | **Withdrawal** — money out | a **system** settlement account | Yes — to an external rail |
| `POST /transfers` | Internal move between customers | another **user** account | No — stays inside the ledger |

- **Transfer** = money moves between two accounts **inside** the system; total money
  in the system is unchanged.
- **Credit / debit** = money **enters or leaves** the system; the counterparty is an
  internal system account modeling the outside world (deposits/withdrawals).

> ⚠️ "Credit/debit" here is the **API operation** (deposit/withdrawal). Don't confuse
> it with the **ledger direction** (the +/− on each leg): *every* transaction — even a
> deposit — is two-legged with one debit and one credit leg. See
> [storage schema](03-storage-schema.md#operation-types-vs-ledger-directions-avoid-the-naming-trap).
>
> The endpoints are kept separate (rather than one `move` call) because
> deposits/withdrawals touch external rails and may be `pending` until confirmed,
> whereas internal transfers can be a single synchronous ACID commit.

## Endpoints

### Read balance

```
GET /v1/accounts/{account_id}/balance
→ 200 { "account_id": "...", "balance": 42050, "currency": "USD", "version": 87 }
```

Strongly consistent (reads the writer / write-through cache).

### Credit

```
POST /v1/accounts/{account_id}/credit
Idempotency-Key: <uuid>
{ "amount": 5000, "currency": "USD", "reference": "payroll-2026-07" }
→ 201 { "transaction_id": "...", "balance": 47050, "status": "posted" }
```

### Debit

```
POST /v1/accounts/{account_id}/debit
Idempotency-Key: <uuid>
{ "amount": 2000, "currency": "USD", "reference": "atm-withdrawal" }
→ 201 { "transaction_id": "...", "balance": 45050, "status": "posted" }
→ 422 { "error": "insufficient_funds", "balance": 45050 }
```

### Transfer (atomic)

```
POST /v1/transfers
Idempotency-Key: <uuid>
{ "from_account_id": "A", "to_account_id": "B", "amount": 10000, "currency": "USD" }
→ 201 { "transaction_id": "...", "status": "posted",
        "from_balance": 35050, "to_balance": 60000 }
→ 422 { "error": "insufficient_funds" }
```

Both legs commit or neither does.

### Transaction history

```
GET /v1/accounts/{account_id}/transactions?limit=50&cursor=<opaque>
→ 200 {
    "entries": [
      { "transaction_id": "...", "direction": "debit", "amount": 2000,
        "balance_after": 45050, "created_at": "2026-07-06T12:00:00Z" }
    ],
    "next_cursor": "..."   // keyset pagination on (account_id, created_at)
  }
```

Keyset (cursor) pagination, not `OFFSET` — stable and O(1) per page over a table
that only grows.

## Status codes / error contract

| Code | Meaning |
|------|---------|
| `200` | Read OK |
| `201` | Mutation applied |
| `409` | `version` conflict (`If-Match` failed) — client should re-read and retry |
| `422` | Business rule rejected (insufficient funds, frozen account) |
| `429` | Rate limited |
| `503` | Writer unavailable (failover in progress) — retry with same idempotency key |

## Why these choices

- **Idempotency keys are mandatory on writes**, not optional. In a money system a
  network timeout on a debit is ambiguous; without dedupe the safe client behavior
  (retry) would double-charge. The key makes retries a no-op.
- **Separate `/credit` and `/debit` from `/transfers`** — a transfer has a
  cross-account invariant (two legs sum to zero) that single-account ops don't; the
  API mirrors the transactional boundary.
- **`version` / `If-Match`** gives clients optimistic concurrency without exposing
  DB locks, so a "read-modify-write" from the client (e.g. "debit only if balance
  unchanged") is expressible and safe.
