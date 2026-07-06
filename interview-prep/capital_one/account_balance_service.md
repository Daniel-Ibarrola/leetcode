# System Design: Account Balance Service

## Problem

Design a backend service that stores and updates user account balances, similar to a wallet or bank ledger.

## Requirements

**Functional:**
- Read the current balance for a given account
- Credit or debit an account by a given amount
- Transfer funds atomically between two accounts
- Expose a transaction history for each account
- Support concurrent operations from multiple clients on the same account

**Non-functional:**
- Highly reliable — balance data must never be lost or corrupted
- Strongly consistent — a read after a write must reflect the latest balance
- Atomic transactions — a debit and credit in a transfer must both succeed or both fail (no partial updates)
- Support millions of accounts and thousands of transactions per second
- Every balance mutation must be durably logged for auditing and reconciliation

## Design

Full design in [`account_balance_service/`](account_balance_service/README.md):
requirements, estimation, storage schema, high-level + detailed diagrams, and API.
