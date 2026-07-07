# System Design: Online Banking Platform

An online banking / credit-card platform: customers apply for a card, log in to
view accounts, statements and transactions, make payments, and dispute charges;
the system notifies them of events and keeps a tamper-evident audit trail. This
directory contains the full design.

Problem statement: [../online_banking_platform.md](../online_banking_platform.md).

## Contents

1. [Requirements](01-requirements.md)
2. [Estimation](02-estimation.md) — traffic and storage sizing
3. [Storage Schema](03-storage-schema.md) — core tables per service
4. [High-Level Design](04-high-level-design.md) — architecture diagram + data flow
5. [API Design](05-api-design.md) — core endpoints
6. [Detailed Design](06-detailed-design.md) — application workflow, disputes,
   audit trail, security/PCI, peak handling

## TL;DR of the design

- **Microservices split by bounded context**, not one monolith. Onboarding,
  identity, accounts, statements, payments, disputes, notifications and audit
  have very different consistency, scaling and compliance profiles, so each is
  its own service with its own datastore. They communicate synchronously for
  reads and via an **event bus** (Kinesis/SNS) for everything asynchronous.
- **Money lives in the [Account Balance Service](../account_balance_service/)** —
  an ACID, double-entry, sharded ledger. This platform *wraps* that service; it
  does not re-implement balances. A "payment" here is a `transfer` there.
- **Onboarding is a long-running async workflow** (identity → credit check →
  decision → card issuance) orchestrated by a state machine (Step Functions),
  because its steps call slow third parties (KYC, credit bureaus) and must be
  resumable and auditable.
- **Disputes are a state machine** with regulated SLAs (provisional credit,
  chargeback, resolution), each transition audited.
- **Security is the spine, not a layer:** MFA auth, encryption everywhere (KMS),
  PAN tokenization to shrink PCI-DSS scope, network segmentation, and a
  **hash-chained, WORM audit log** for tamper-evidence.
- **99.99% via multi-AZ + multi-region** managed services, stateless compute,
  and graceful degradation (a down notification pipeline never blocks a payment).
- **Peak traffic** (statement close, payment due dates) is absorbed by
  autoscaling stateless services, queue-buffered writes, staggered billing
  cycles, and read replicas + cache for the read-heavy dashboard.

See each file for the reasoning and tradeoffs.
