# CAP Theorem

A distributed system can guarantee at most **2 of 3** properties simultaneously:

| Property | Meaning |
|---|---|
| **C**onsistency | Every read returns the most recent write (or an error) |
| **A**vailability | Every request gets a (non-error) response, but it may not be the latest data |
| **P**artition Tolerance | The system keeps working even if nodes can't communicate |

## The Catch

**Network partitions always happen** in distributed systems (cables fail, nodes crash, etc.). So P is not optional — you must tolerate partitions.

This means the real choice is: **CP vs AP** during a partition.

## CP vs AP

### CP (Consistency + Partition Tolerance)
- If a partition occurs, the system returns an error rather than stale data.
- Prioritizes correctness over uptime.
- Examples: HBase, Zookeeper, etcd, traditional RDBMS with synchronous replication.

### AP (Availability + Partition Tolerance)
- If a partition occurs, the system returns the best data it has (possibly stale).
- Prioritizes uptime over correctness.
- Examples: Cassandra, DynamoDB, CouchDB, DNS.

## Real-World Framing

CAP is a theoretical model. In practice, think in terms of:
- **What happens during a network partition?** Do we serve stale data or return an error?
- **How eventual is eventual consistency?** Milliseconds vs minutes matters.

## Trade-offs

| CP | AP |
|---|---|
| Safer for financial data, inventory | Better for social feeds, DNS, analytics |
| May reject writes during partition | Always responsive, may return stale data |
| Easier to reason about correctness | Requires conflict resolution logic |

## PACELC Extension

CAP only covers partition scenarios. **PACELC** extends it:
- **If Partition** → choose C or A (same as CAP)
- **Else (normal operation)** → choose Latency or Consistency

This captures the everyday trade-off: even without partitions, you often trade consistency for lower latency (e.g., reading from a local replica).
