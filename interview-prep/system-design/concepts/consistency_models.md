# Consistency Models

Defines what a client can expect to read after a write in a distributed system. Arranged from strongest to weakest.

## The Spectrum

```
Strong ←————————————————————————→ Weak
Linearizable > Sequential > Causal > Eventual
```

---

## Linearizability (Strong Consistency)

- Once a write completes, all subsequent reads see that write.
- Operations appear to execute instantaneously at some point in real time.
- **Feels like a single machine.**
- Cost: high latency, lower availability.
- Examples: etcd, Zookeeper, Google Spanner.

---

## Sequential Consistency

- All nodes see operations in the same order, but that order may lag real time.
- Weaker than linearizable: a read might return an old value even after a write completes, as long as the global order is consistent.

---

## Causal Consistency

- Operations that are causally related are seen in the correct order.
- Unrelated operations can be seen in any order.
- Example: if you post a comment in reply to another, anyone who sees your reply also sees the original post.
- Used by: MongoDB (causal sessions), some distributed caches.

---

## Eventual Consistency

- If no new updates are made, all replicas will eventually converge to the same value.
- No guarantee on *when* — could be milliseconds or seconds.
- Very available, very scalable.
- Examples: DNS, DynamoDB (default), Cassandra (tunable), S3.

---

## Read-Your-Writes

A session-level guarantee: after you write something, you will always read your own write back.
- Not global consistency — other clients may still see the old value.
- Useful for user-facing apps (e.g., "I just updated my profile, I should see it").

---

## Monotonic Reads

Once you read a value, you'll never read an older value in subsequent reads.
- Prevents confusing time-travel reads across replicas.

---

## Trade-offs

| Model | Consistency | Latency | Availability | Use When |
|---|---|---|---|---|
| Linearizable | Strongest | Highest | Lowest | Financial txns, leader election |
| Sequential | Strong | High | Low | Distributed locks |
| Causal | Medium | Medium | Medium | Social apps, collaborative editing |
| Eventual | Weakest | Lowest | Highest | DNS, caches, shopping carts |

---

## Conflict Resolution (for Eventual Consistency)

When replicas diverge, you need a way to merge:
- **Last Write Wins (LWW)**: keep the write with the latest timestamp. Simple, but can lose data.
- **Vector clocks**: track causal history to detect conflicts explicitly.
- **CRDTs** (Conflict-free Replicated Data Types): data structures that always merge correctly (e.g., counters, sets).
