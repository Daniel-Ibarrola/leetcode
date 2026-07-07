# 3. Storage Schema

Core tables only, grouped by owning service — each microservice owns its data
and no other service reads its tables directly (they call its API or consume its
events). Balances/ledger tables live in the
[Account Balance Service](../account_balance_service/03-storage-schema.md) and
are **not** duplicated here.

## Identity service — `users`, `mfa_factors`, `sessions`

| Table | Column | Type | Notes |
|-------|--------|------|-------|
| `users` | `user_id` | UUID | PK. |
| | `email` / `phone` | VARCHAR | Contact + MFA delivery; encrypted. |
| | `password_hash` | VARCHAR | Argon2/bcrypt; never plaintext. |
| | `status` | ENUM | `active`, `locked`, `closed`. |
| `mfa_factors` | `factor_id` | UUID | PK. |
| | `user_id` | UUID | FK. |
| | `type` | ENUM | `totp`, `sms`, `push`. |
| | `secret_ref` | VARCHAR | KMS-encrypted / vault ref, not the raw secret. |
| `sessions` | `session_id` | UUID | PK. Stored in **DynamoDB/Redis** with TTL, not Aurora. |
| | `user_id`, `expires_at`, `mfa_passed` | | Short-lived; TTL auto-evicts. |

## Onboarding service — `applications`

One row per credit-card application; drives the approval workflow.

| Column | Type | Notes |
|--------|------|-------|
| `application_id` | UUID | PK. |
| `applicant` | JSONB | Name, DOB, SSN **tokenized**, address, income. Encrypted. |
| `status` | ENUM | `submitted`→`identity_verified`→`credit_checked`→`approved`/`rejected`→`card_issued`. |
| `kyc_result` | JSONB | Vendor decision + reference id. |
| `credit_result` | JSONB | Bureau score band + reference id (not the raw report). |
| `decision_reason` | TEXT | For adverse-action notices (regulatory). |
| `account_id` | UUID | Set once approved and the account is opened. |
| `created_at` / `updated_at` | TIMESTAMPTZ | |

## Account service — `accounts`, `cards`

Account *product* metadata; **balances live in the ledger service**.

| Table | Column | Type | Notes |
|-------|--------|------|-------|
| `accounts` | `account_id` | UUID | PK. Same id used as the ledger account. |
| | `user_id` | UUID | Owner. |
| | `credit_limit` | BIGINT | Cents. |
| | `apr_bps` | INT | Interest rate, basis points. |
| | `cycle_day` | SMALLINT | Statement close day (1–28) — **staggered** to spread load. |
| | `status` | ENUM | `active`, `frozen`, `closed`, `delinquent`. |
| `cards` | `card_id` | UUID | PK. |
| | `account_id` | UUID | FK. |
| | `pan_token` | VARCHAR | **Token**, never the real PAN. Vault resolves it in PCI zone. |
| | `last4`, `exp`, `network` | | Safe-to-display fragments. |
| | `status` | ENUM | `active`, `blocked`, `replaced`. |

## Transaction history service — `transactions`

Read-optimized copy of settled postings (projected from ledger events + card
network settlement). Sharded by `account_id`, keyset-paginated.

| Column | Type | Notes |
|--------|------|-------|
| `txn_id` | UUID | PK. |
| `account_id` | UUID | Shard key. |
| `direction` | ENUM | `debit` (purchase) / `credit` (payment/refund). |
| `amount` | BIGINT | Cents. |
| `merchant` | VARCHAR | Display name. |
| `mcc` / `category` | VARCHAR | Merchant category. |
| `status` | ENUM | `pending`, `posted`, `disputed`, `reversed`. |
| `posted_at` | TIMESTAMPTZ | |

Index: `(account_id, posted_at DESC)` for history pagination.

## Statement service — `statements`

| Column | Type | Notes |
|--------|------|-------|
| `statement_id` | UUID | PK. |
| `account_id` | UUID | FK. |
| `period_start` / `period_end` | DATE | Billing cycle. |
| `opening_balance` / `closing_balance` | BIGINT | Cents. |
| `min_due` / `due_date` | BIGINT / DATE | Drives payment-due notifications. |
| `pdf_s3_key` | VARCHAR | Rendered PDF in S3. |
| `status` | ENUM | `generated`, `delivered`. |

## Dispute service — `disputes`

| Column | Type | Notes |
|--------|------|-------|
| `dispute_id` | UUID | PK. |
| `txn_id` / `account_id` | UUID | The charge under dispute. |
| `reason` | ENUM | `fraud`, `not_received`, `duplicate`, `incorrect_amount`, … |
| `status` | ENUM | `opened`→`provisional_credit`→`under_review`→`chargeback`→`resolved_customer`/`resolved_merchant`. |
| `amount` | BIGINT | Disputed amount, cents. |
| `sla_due_at` | TIMESTAMPTZ | Regulated deadline (e.g. Reg E/Z timers). |
| `evidence` | JSONB | Customer + merchant docs (S3 refs). |

## Notification service — `notifications`

| Column | Type | Notes |
|--------|------|-------|
| `notification_id` | UUID | PK. |
| `user_id` | UUID | Recipient. |
| `channel` | ENUM | `email`, `sms`, `push`. |
| `template` / `payload` | VARCHAR/JSONB | What to render. |
| `status` | ENUM | `queued`, `sent`, `failed`, `suppressed`. |
| `dedup_key` | VARCHAR | Prevents duplicate sends on retries. |

## Audit service — `audit_log`

Append-only, hash-chained. **Never updated or deleted.**

| Column | Type | Notes |
|--------|------|-------|
| `seq` | BIGINT | Monotonic sequence (per partition). |
| `actor` | VARCHAR | User/admin/service id. |
| `action` | VARCHAR | e.g. `payment.created`, `account.frozen`. |
| `target` | VARCHAR | Entity acted on. |
| `before_hash` / `after_hash` | CHAR(64) | Hash of state, for change proof. |
| `prev_hash` | CHAR(64) | Hash of the previous record → **chain**. |
| `record_hash` | CHAR(64) | `H(this record ‖ prev_hash)`. Tamper-evident. |
| `created_at` | TIMESTAMPTZ | |

Streamed to **S3 Object Lock (WORM)**; the chain makes any retro-edit detectable
(see [detailed design](06-detailed-design.md#64-tamper-evident-audit-trail)).

## Cross-cutting notes

- **PII columns are encrypted** (KMS-backed, field or envelope encryption); SSN
  and PAN are **tokenized** so most services never hold the raw value.
- **No cross-service foreign keys** — services reference each other by id and
  reconcile via events; each can be scaled and deployed independently.
