# 1. Requirements

## Problem

Design an online banking platform with scope similar to a credit card application system.

## Functional

- **Apply for a credit card account** — identity verification (KYC), credit
  check, and an approval workflow ending in card issuance or rejection.
- **Authenticated access** — customers log in (with MFA) and view account
  details, statements, and transaction history.
- **Make payments** toward the card balance.
- **Dispute a charge** — open a dispute, track it through a regulated workflow.
- **Notifications** — email / SMS / push for account events (payment due,
  transaction posted, dispute status changed).
- **Administration** — internal staff can view and manage accounts.

## Non-functional

- **Secure authn/authz** with MFA support.
- **Encryption** of PII and financial data at rest and in transit.
- **Regulatory compliance** — PCI-DSS (card data) and SOC 2.
- **High availability** — 99.99% uptime (~52 min downtime/year).
- **Scale** — millions of concurrent users; pronounced peaks around statement
  close and payment due dates.
- **Tamper-evident audit trail** for every user and admin action.

## Assumptions / scope decisions

These are stated up front because they shape the whole design:

| # | Assumption | Why it matters |
|---|------------|----------------|
| 1 | Balances/postings are owned by the existing **[Account Balance Service](../account_balance_service/)** (ACID double-entry ledger). This platform orchestrates *around* it. | We don't re-implement money; a payment is a `transfer`, a posting is a `credit`/`debit`. Keeps this doc about workflows, not ledgers. |
| 2 | The **card authorization switch** (real-time approve/decline at the point of sale) is a separate low-latency system. We **consume** its settled transactions, we don't run the auth path. | Bounds scope to the customer-facing platform, not the payments network. |
| 3 | **Reads dominate** — dashboards, statements, history — far more than writes (payments, disputes, applications). | We scale reads with replicas + cache and CDN; writes are comparatively low-volume. |
| 4 | Money is **integer minor units (cents)**, never float. | Same discipline as the ledger; regulators require exact arithmetic. |
| 5 | We **never store raw PAN** in our services; card numbers are tokenized in an isolated PCI zone / via a token vault. | Shrinks PCI-DSS audit scope to a small blast radius. |
| 6 | Consistency needs differ per domain: **payments = strong** (money), **application/dispute status = read-your-writes within the workflow**, **dashboards/history = slight staleness OK**. | Lets each service pick the cheapest correct storage/consistency. |

## Out of scope

Card network authorization/clearing, fraud detection (see
[fraud_detection.md](../fraud_detection.md)), rewards/points, interest
computation internals, and the physical card fulfilment vendor integration.
