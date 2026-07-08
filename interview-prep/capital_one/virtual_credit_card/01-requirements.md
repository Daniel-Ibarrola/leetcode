# 1. Requirements

## Problem

Design a system that issues and manages **virtual credit cards** for customers:
generate card credentials on demand, let customers control how each card can be
used, and route every charge made on a virtual card back to the customer's
underlying account.

## Functional

- **Generate a virtual card** — a unique PAN, expiry date, and CVV, issued
  on demand and linked to the customer's underlying physical card/account.
- **Per-card controls** — spending limits, merchant-category restrictions,
  and a custom expiry date, set at creation or updated later.
- **One-time-use and recurring-use cards** — a one-time card auto-retires
  after its first authorization; a recurring card stays usable until expiry
  or cancellation.
- **Lifecycle actions** — freeze, unfreeze, and permanently cancel a card.
- **Route and settle charges** — every authorization and settlement on a
  virtual card resolves against the linked account's real balance/credit line.

## Non-functional

- **Card standards** — PAN passes the Luhn check and conforms to the issuing
  network's (Visa/Mastercard) BIN and format rules.
- **PCI-DSS** for storage and transmission of card credentials (PAN, CVV,
  expiry).
- **Sub-second issuance** — card creation is a synchronous, customer-facing
  call; no async workflow on the happy path.
- **Scale** — tens of millions of active virtual cards, with heavy churn from
  one-time-use cards.
- **Full audit log** — every action on a card (creation, update, freeze,
  cancel, authorization) is recorded.

## Assumptions / scope decisions

| # | Assumption | Why it matters |
|---|------------|-----------------|
| 1 | Balances, credit lines, and settlement are owned by the existing **[Account Balance Service](../account_balance_service/)** (ACID double-entry ledger). This system issues card *credentials and rules*; it calls the ledger to check/debit, it doesn't reimplement money. | Keeps this design about card issuance and the authorization decision, not a second ledger. |
| 2 | We sit behind an existing **card-network/processor integration** (e.g. a BIN sponsor or Visa/Mastercard direct connection) that speaks the network's wire protocol (ISO 8583) and calls **our** decision endpoint for each authorization. | Bounds scope to the issuer side: receive a normalized auth request, return approve/decline. We don't build the network switch. |
| 3 | **Raw PAN and CVV never touch general application services.** They are generated and stored only inside an isolated, PCI-scoped **token vault** (HSM-backed); every other service holds a token reference + `last4`. | Shrinks PCI-DSS audit scope to one small, hardened component instead of the whole system. |
| 4 | Money is **integer minor units (cents)**, never float. | Same discipline as the ledger; avoids rounding bugs. |
| 5 | "Millions of active virtual cards per customer cohort" is read as **tens of millions of cards system-wide**, with individual customers able to hold many at once — one-time-use cards are created and retired constantly. | Drives the estimation in [02](02-estimation.md): churn, not just standing count, dominates storage growth. |
| 6 | Consistency needs differ by action: **freeze/cancel must be immediately visible to the authorization path** (a frozen card must not authorize the next transaction); card creation/listing can tolerate ordinary read-replica lag. | Lets the hot authorization path use a strongly-consistent, low-latency cache rather than a general read replica. |
| 7 | **Fraud scoring is a separate, existing system** ([fraud_detection.md](../fraud_detection.md)) that the authorization path calls as one more check, not something this design re-implements. | Keeps this design focused on card rules (limits, restrictions, status), not behavioral fraud modeling. |

## Out of scope

Physical card issuance/fulfillment, the underlying ledger's internals (see
[Account Balance Service](../account_balance_service/)), card-network switch /
ISO 8583 wire details, fraud/ML scoring internals (see
[fraud_detection.md](../fraud_detection.md)), and rewards/points.
