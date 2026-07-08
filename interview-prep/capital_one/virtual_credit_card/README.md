# System Design: Virtual Credit Card Product

Issue and manage virtual credit cards: generate card credentials on demand,
let customers set per-card limits and restrictions, support one-time and
recurring cards, and route every charge back to the customer's underlying
account. This directory contains the full design.

## Contents

1. [Requirements](01-requirements.md)
2. [Estimation](02-estimation.md) — throughput and storage sizing
3. [Storage Schema](03-storage-schema.md) — core tables per service
4. [High-Level Design](04-high-level-design.md) — AWS architecture diagram + data flow
5. [API Design](05-api-design.md) — core endpoints
6. [Detailed Design](06-detailed-design.md) — issuance, cache consistency,
   PCI scope reduction, authorization hot path, audit trail, failure handling

## TL;DR of the design

- **Card Management and Authorization are split into separate services**,
  even though they share the same card data — issuance is low-volume with a
  sub-second budget, authorization is thousands of requests/second with a
  sub-second-*of*-a-second budget. Coupling them would force one path to
  inherit the other's constraints.
- **Money is delegated to the existing [Account Balance Service](../account_balance_service/)**
  (ACID double-entry ledger) and risk scoring to the existing
  [fraud detection system](../fraud_detection.md) — this design owns card
  *rules* (limits, restrictions, status), not money or fraud modeling.
- **Raw PAN/CVV live only inside an isolated token vault** (HSM/KMS-backed);
  every other service holds a token + `last4`. The authorization hot path is
  built to avoid calling the vault at all in the common case, which is what
  keeps PCI-DSS audit scope small.
- **Freeze/unfreeze/cancel write through to the authorization cache
  synchronously** — a customer-visible "frozen" has to be true for the very
  next transaction, not eventually.
- **One-time-use cards burn atomically with their approving authorization**,
  the same idempotency discipline the ledger uses, applied at the card level.
- **Fail-open vs. fail-closed is decided per dependency**: the ledger fails
  closed (can't approve a debit you can't perform), the fraud engine fails
  open (blocking commerce on a scoring blip is worse than temporarily
  accepting extra risk).
- **Audit reuses the hash-chained, WORM log** from the
  [online banking platform](../online_banking_platform/) rather than a new
  mechanism — the "log every action" requirement is the same shape.

See each file for the reasoning and tradeoffs.
