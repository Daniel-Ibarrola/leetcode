# 5. API Design

REST over HTTPS, JSON bodies. Core endpoints only. Amounts are **integer minor
units** (cents). All mutations require an `Idempotency-Key` header.

## Conventions

- **Auth:** bearer JWT, validated at API Gateway; card-level actions require
  the caller to own the underlying account.
- **Money:** `{ "amount": 5000, "currency": "USD" }` = \$50.00.
- **Idempotency:** replaying a key returns the original result without
  re-issuing or re-authorizing.
- **Errors:** `422` business rule (limit exceeded, restricted merchant),
  `409` conflict (e.g. cancel an already-cancelled card), `429` rate limited,
  `401/403` auth.

## Cards (customer-facing)

```
POST /v1/cards
Idempotency-Key: <uuid>
{ "account_id": "...", "usage_type": "one_time" | "recurring",
  "spending_limit": 20000, "merchant_restriction": { "mcc_allow": ["5411"] },
  "expiry_override": "2027-01-31" }
→ 201 { card_id, pan, cvv, expiry, last4, network, status: "active" }
```

`pan`/`cvv` are returned **once**, fetched directly from the token vault for
this response only — never logged, never persisted outside the vault, and
never returned again by any other endpoint.

```
GET /v1/cards/{card_id}
→ 200 { card_id, last4, expiry, network, usage_type, status, spending_limit,
        merchant_restriction }        # never the PAN/CVV again

PATCH /v1/cards/{card_id}
{ "spending_limit": 10000, "merchant_restriction": { "mcc_deny": ["7995"] } }
→ 200 { card_id, ...updated fields }

POST /v1/cards/{card_id}/freeze     → 200 { status: "frozen" }
POST /v1/cards/{card_id}/unfreeze   → 200 { status: "active" }
DELETE /v1/cards/{card_id}          → 200 { status: "cancelled" }   # permanent
```

Freeze/unfreeze/cancel are synchronous and immediately reflected in the
authorization path's cache (see
[06](06-detailed-design.md#62-freeze-unfreeze-cancel-cache-consistency)).

```
GET /v1/cards/{card_id}/transactions?limit=50&cursor=<opaque>
→ 200 { entries: [ { authorization_id, merchant, amount, decision,
                     decline_reason, requested_at } ], next_cursor }
```

Keyset (cursor) pagination on `(card_id, requested_at)`.

## Authorization (internal, called by the card network/processor)

```
POST /internal/v1/authorizations
{ "pan_token": "...", "amount": 4599, "merchant_id": "...", "mcc": "5812" }
→ 200 { decision: "approved" | "declined", decline_reason?, authorization_id }
```

Not customer-facing — reached only via the processor's dedicated,
low-latency ingress (PrivateLink/Direct Connect), not the public API Gateway.
Must respond within the processor's authorization timeout budget; see
[04](04-high-level-design.md#authorize-a-charge-sync-tight-sla).

## Why these choices

- **PAN/CVV appear in exactly one response, exactly once** — the issuance
  response — and nowhere else. Every other endpoint deals only in
  `last4`/token, keeping card data out of logs, caches, and general storage.
- **Idempotency mandatory on issuance** — a client retry after a timeout must
  never mint two live cards against the same account.
- **The authorization endpoint is a distinct, internal API**, not a variant of
  the public one — different network path, different latency contract,
  different caller (a processor, not a browser/app).
- **Freeze/unfreeze/cancel return synchronously** with the new status — the
  customer-visible guarantee ("I froze it, it's frozen") has to be true the
  instant the call returns, not eventually.
