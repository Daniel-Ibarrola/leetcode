# 3. Storage Schema

Core tables only. The design is a **double-entry ledger**: the `ledger_entries`
table is the immutable source of truth, and `accounts.balance` is a cached
running total maintained transactionally alongside it.

## `accounts`

The current state of each account. One row per account. Mutable.

| Column | Type | Notes |
|--------|------|-------|
| `account_id` | UUID | PK. Also the shard key. |
| `owner_id` | UUID | User who owns the account. |
| `currency` | CHAR(3) | ISO 4217. Single currency per account. |
| `balance` | BIGINT | **Minor units (cents).** Cached materialization of the ledger. |
| `status` | ENUM | `active`, `frozen`, `closed`. |
| `version` | BIGINT | Optimistic-lock / row version, bumped on every mutation. |
| `created_at` / `updated_at` | TIMESTAMPTZ | |

- Balance is `BIGINT`, never float — exact cents.
- `version` supports optimistic concurrency and lets clients detect lost updates.

## `transactions`

One row per logical operation (a credit, a debit, or a transfer). The unit of
atomicity. Groups the ledger legs together.

| Column | Type | Notes |
|--------|------|-------|
| `transaction_id` | UUID | PK. |
| `type` | ENUM | `credit`, `debit`, `transfer`. |
| `status` | ENUM | `pending`, `posted`, `failed`, `reversed`. |
| `idempotency_key` | VARCHAR | **Unique.** Dedupes client retries. |
| `created_at` | TIMESTAMPTZ | |
| `metadata` | JSONB | Free-form (description, source, reference id). |

- `UNIQUE(idempotency_key)` is the linchpin of safe retries (see detailed design).

## `ledger_entries`

The immutable, append-only record of truth. **Never updated or deleted** — a
correction is a new compensating entry. Every balance change lives here.

| Column | Type | Notes |
|--------|------|-------|
| `entry_id` | UUID | PK. |
| `transaction_id` | UUID | FK → `transactions`. |
| `account_id` | UUID | FK → `accounts`. Shard key. |
| `direction` | ENUM | `debit` or `credit`. |
| `amount` | BIGINT | Minor units, always **positive**; `direction` carries the sign. |
| `balance_after` | BIGINT | Account balance immediately after this entry — snapshot for audit & history. |
| `created_at` | TIMESTAMPTZ | |

Indexes:

- `(account_id, created_at DESC)` — powers paginated transaction history.
- `(transaction_id)` — fetch both legs of a transfer.

### Double-entry invariant

For any committed transaction, the signed sum of its legs is zero:

```
credit(B, 100) + debit(A, 100)  →  (+100) + (−100) = 0
```

Summing all `ledger_entries` for an account reproduces `accounts.balance`. This is
the reconciliation check: **derived total must equal the cached balance**, always.

## `idempotency_keys` (or DynamoDB table)

| Column | Type | Notes |
|--------|------|-------|
| `key` | VARCHAR | PK. |
| `transaction_id` | UUID | The result to replay on a duplicate request. |
| `response` | JSONB | Cached response body. |
| `expires_at` | TIMESTAMPTZ | TTL (24–48 h). |

## Why cache the balance instead of always summing the ledger?

| Option | Read cost | Tradeoff |
|--------|-----------|----------|
| **Materialized `balance` column (chosen)** | O(1) single row read | Must update it in the same txn as the ledger; risk of drift → mitigated by reconciliation. |
| Sum ledger on every read | O(n) over account history | Correct by construction but gets slower forever; unacceptable at 20k QPS. |
| Snapshot + replay recent entries | O(k) | Middle ground; more moving parts. Overkill here. |

We choose the materialized column for O(1) strongly-consistent reads, and treat the
ledger as the authority that a nightly job reconciles against.
