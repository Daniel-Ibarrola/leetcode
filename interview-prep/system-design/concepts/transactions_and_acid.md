# Transactions & ACID

A **transaction** is a sequence of DB operations treated as a single unit. Either all succeed or all are rolled back.

---

## ACID Properties

### Atomicity
All operations in a transaction succeed, or none of them do. No partial updates.
- Example: transfer $100 from A to B → debit A AND credit B. If the credit fails, the debit is rolled back.

### Consistency
A transaction brings the DB from one valid state to another. All constraints, rules, and invariants are enforced.
- Example: a foreign key constraint is never violated mid-transaction.

### Isolation
Concurrent transactions don't interfere with each other. Each transaction behaves as if it's running alone.
- This is the expensive one. See isolation levels below.

### Durability
Once a transaction commits, it stays committed — even if the server crashes immediately after.
- Achieved via write-ahead log (WAL): changes are written to disk before the commit is acknowledged.

---

## Isolation Levels

Weaker isolation = better performance. Stronger isolation = fewer anomalies.

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|---|---|---|---|
| Read Uncommitted | Possible | Possible | Possible |
| Read Committed | No | Possible | Possible |
| Repeatable Read | No | No | Possible |
| Serializable | No | No | No |

**Anomalies explained:**
- **Dirty read**: read data written by a transaction that hasn't committed yet.
- **Non-repeatable read**: read the same row twice in a transaction; get different values (another transaction committed a change in between).
- **Phantom read**: re-run a range query; get different rows (another transaction inserted/deleted rows).

Most databases default to **Read Committed**. Postgres uses MVCC to implement Repeatable Read efficiently.

---

## Serializable Isolation

All transactions appear to execute in some serial (one-at-a-time) order. Strongest guarantee, highest cost.

Implementations:
- **Two-Phase Locking (2PL)**: acquire all locks before releasing any. Simple but slow (lots of lock contention).
- **Serializable Snapshot Isolation (SSI)**: optimistic — detects conflicts at commit time. Used by Postgres.

---

## Common Concurrency Issues

### Lost Update
Two transactions read-modify-write the same value. One overwrites the other's change.
Fix: `SELECT FOR UPDATE`, optimistic locking with version numbers.

### Write Skew
Two transactions read overlapping data, make decisions based on it, then write non-overlapping data. Each write is "valid" individually but together they violate an invariant.
Classic example: two doctors both see "2 doctors on call," both decide to go off-call. Now 0 doctors on call.
Fix: Serializable isolation.

---

## Distributed Transactions

Transactions across multiple services or DB shards are hard.

### Two-Phase Commit (2PC)
1. **Prepare phase**: coordinator asks all participants "can you commit?" Each participant votes yes/no.
2. **Commit phase**: if all vote yes, coordinator sends commit. Otherwise, sends rollback.

- Provides atomicity across distributed nodes.
- Slow (2 round trips), blocking (participants hold locks while waiting).
- Coordinator failure → participants can be stuck.

### Saga Pattern (Alternative)
Break the transaction into local transactions with compensating actions. See `multi_step_processes.md`.

---

## Trade-offs

| Stronger Isolation | More serializable → fewer anomalies → slower, more contention |
| Weaker Isolation | Faster, higher throughput → risk of anomalies |
| Distributed Txn (2PC) | Atomicity across nodes → latency, blocking, coordinator SPOF |
| Saga | Scalable, no locking → complex, only eventual consistency |

---

## Quick Rules of Thumb

- Use transactions for any multi-step operation where partial failure is unacceptable.
- Default to **Read Committed** (most DB defaults) unless you have a specific reason for stronger isolation.
- Avoid long-running transactions — they hold locks and block other operations.
- For cross-service operations, design with sagas; avoid 2PC.
