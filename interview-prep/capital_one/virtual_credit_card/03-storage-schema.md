# 3. Storage Schema

Core tables only, grouped by owning service — each service owns its data and
no other service reads its tables directly (they call its API or consume its
events). Balances/ledger tables live in the
[Account Balance Service](../account_balance_service/03-storage-schema.md) and
are **not** duplicated here.

## Card management service — `virtual_cards`, `card_limits`

| Table | Column | Type | Notes |
|-------|--------|------|-------|
| `virtual_cards` | `card_id` | UUID | PK. |
| | `customer_id` | UUID | Owner. |
| | `account_id` | UUID | FK → underlying account/ledger account. |
| | `pan_token` | VARCHAR | **Token**, never the real PAN. Vault resolves it in the PCI zone. |
| | `last4` / `expiry` / `network` | | Safe-to-display fragments. |
| | `usage_type` | ENUM | `one_time`, `recurring`. |
| | `status` | ENUM | `active`, `frozen`, `cancelled`, `expired`, `burned` (one-time card consumed). |
| | `created_at` / `cancelled_at` | TIMESTAMPTZ | |
| `card_limits` | `card_id` | UUID | PK / FK. |
| | `spending_limit` | BIGINT | Cents. Total cap over the card's life or a rolling period. |
| | `per_transaction_limit` | BIGINT | Cents. |
| | `merchant_restriction` | JSONB | MCC allow/deny list. |
| | `velocity_limit` | SMALLINT | Max authorizations per day, optional. |
| | `expiry_override` | DATE | Customer-set expiry, if earlier than the network max. |

`virtual_cards` and `card_limits` share a PK — a 1:1 split purely so hot
authorization reads (`card_limits`, tiny row) aren't competing with the wider
metadata row.

## Token vault (PCI zone) — `card_credentials`

Physically and logically isolated from every other datastore in the system —
separate VPC, separate IAM boundary, accessed only through the vault's own
API (never a direct DB connection from another service).

| Column | Type | Notes |
|--------|------|-------|
| `token_id` | UUID | PK. Referenced as `pan_token` elsewhere. |
| `encrypted_pan` | BYTEA | Envelope-encrypted; decryptable only inside the vault. |
| `encrypted_cvv` | BYTEA | Same. |
| `network_bin` | VARCHAR | BIN range used to generate a network-valid PAN. |
| `kms_key_id` | VARCHAR | Data-encryption-key reference (KMS/CloudHSM). |
| `created_at` | TIMESTAMPTZ | |

## Authorization service — `authorizations`

Append-mostly log of every authorization attempt (approved or declined),
sharded by `card_id`. This is the record the card management service reads to
answer "recent transactions."

| Column | Type | Notes |
|--------|------|-------|
| `authorization_id` | UUID | PK. |
| `card_id` | UUID | Shard key. |
| `account_id` | UUID | FK → ledger account. |
| `amount` | BIGINT | Cents. |
| `merchant_id` / `mcc` | VARCHAR | |
| `decision` | ENUM | `approved`, `declined`. |
| `decline_reason` | VARCHAR | `frozen`, `limit_exceeded`, `merchant_restricted`, `expired`, `fraud_hold`, … |
| `requested_at` | TIMESTAMPTZ | |

Index: `(card_id, requested_at DESC)` for history pagination.

## Audit service — `audit_log`

Append-only, hash-chained — same tamper-evident pattern used by the
[online banking platform](../online_banking_platform/03-storage-schema.md#audit-service--audit_log).
**Never updated or deleted.**

| Column | Type | Notes |
|--------|------|-------|
| `seq` | BIGINT | Monotonic sequence (per partition). |
| `actor` | VARCHAR | Customer/admin/service id. |
| `action` | VARCHAR | e.g. `card.created`, `card.frozen`, `authorization.declined`. |
| `target` | VARCHAR | `card_id` acted on. |
| `prev_hash` / `record_hash` | CHAR(64) | Hash chain — see [06](06-detailed-design.md#65-audit-trail). |
| `created_at` | TIMESTAMPTZ | |

## Cross-cutting notes

- **No cross-service foreign keys** — services reference each other by id and
  reconcile via events.
- **The vault is the only place PAN/CVV exist in cleartext (decrypted).**
  Every other table stores a token and a `last4` fragment; this is the whole
  point of the PCI-scope-reduction decision (see [06](06-detailed-design.md#63-pci-dss-scope-reduction)).
- `virtual_cards.account_id` and `authorizations.account_id` are references
  into the [Account Balance Service](../account_balance_service/03-storage-schema.md);
  this system never stores a balance.
