# System Design: Account Balance Service

A backend service that stores and updates user account balances, similar to a
wallet or bank ledger. This directory contains the full design.

## Contents

1. [Requirements](01-requirements.md)
2. [Estimation](02-estimation.md) — traffic and storage sizing
3. [Storage Schema](03-storage-schema.md) — core tables and columns
4. [High-Level Design](04-high-level-design.md) — architecture diagram + data flow
5. [API Design](05-api-design.md) — core endpoints
6. [Detailed Design](06-detailed-design.md) — write path, concurrency, sharding, audit
7. [Idempotency Keys — Deep Dive](07-idempotency.md) — why they exist and the two-layer enforcement

## TL;DR of the design

- **Source of truth is a relational, ACID database (Amazon Aurora PostgreSQL).**
  The problem is defined by strong consistency and atomic multi-row transfers —
  exactly what a SQL engine with real transactions gives us for free. We pay for
  this with harder horizontal write scaling, which we address by sharding on
  `account_id`.
- **Double-entry, append-only ledger** is the durable record of truth. The
  `balance` column on the account is a *cached materialization* of the ledger,
  updated inside the same transaction that appends ledger rows.
- **Concurrency** is handled with row-level locks (`SELECT … FOR UPDATE`),
  acquired in a deterministic order for transfers to avoid deadlocks.
- **Every request is idempotent** via a client-supplied idempotency key, so retries
  after a timeout never double-charge.
- **Auditing/reconciliation** is served by streaming the ledger (change data
  capture) to an S3 data lake, keeping the hot OLTP database small.

See each file for the reasoning and tradeoffs.
