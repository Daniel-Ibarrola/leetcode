# 1. Requirements

## Functional

- **Read balance** — return the current balance for a given account.
- **Credit / debit** — change an account's balance by a given amount.
- **Transfer** — move funds atomically between two accounts (debit A, credit B).
- **Transaction history** — expose an ordered, paginated history per account.
- **Concurrency** — multiple clients may operate on the same account at once.

## Non-functional

- **Reliability** — balance data must never be lost or corrupted.
- **Strong consistency** — a read after a write reflects the latest balance
  (read-your-writes, no stale reads for balance).
- **Atomicity** — the debit and credit of a transfer both commit or both roll back;
  no partial state is ever visible.
- **Scale** — millions of accounts, thousands of transactions per second.
- **Auditability** — every mutation is durably logged for audit and reconciliation.

## Assumptions / scope decisions

These are stated up front because they drive the whole design:

| # | Assumption | Why it matters |
|---|------------|----------------|
| 1 | Money is stored as an **integer of minor units** (cents), never a float. | Floats lose precision; regulators require exact arithmetic. |
| 2 | An account has a **single currency**. Cross-currency transfer is out of scope (would need FX + a two-legged transfer). | Keeps the balance a single scalar. |
| 3 | **Overdraft is not allowed** by default (debit fails if it would go negative). Configurable per account type. | Defines the core business rule enforced in the write path. |
| 4 | Consistency beats availability for the write path (CP in CAP). | A wallet that shows the wrong balance is worse than one that's briefly unavailable. |
| 5 | Balance reads must be strongly consistent; **history reads may tolerate slight staleness**. | Lets us serve history from read replicas / the data lake. |

## Out of scope

Authentication/authorization, KYC/onboarding, interest accrual, statements,
notifications, and dispute workflows — these belong to the surrounding
[online banking platform](../online_banking_platform.md).
