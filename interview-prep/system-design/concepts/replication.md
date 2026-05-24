# Replication

Keeping copies of data on multiple nodes for fault tolerance, read scaling, and geographic distribution.

---

## Why Replicate?

- **Availability**: if the primary fails, a replica can take over.
- **Read scale**: distribute read traffic across replicas.
- **Latency**: serve reads from a node geographically close to the user.
- **Backup**: replicas can serve as live backups.

---

## Replication Topologies

### Leader-Follower (Primary-Replica)
One node accepts writes (leader). Changes are replicated to followers. Reads can go to any node.

```
[Leader] ← writes
   ↓ replicate
[Follower 1] ← reads
[Follower 2] ← reads
```

- Simple, easy to reason about.
- Followers may lag behind leader → stale reads.
- Write throughput limited to what the leader can handle.
- Used by: Postgres, MySQL, MongoDB (replica sets), Redis.

### Multi-Leader (Multi-Primary)
Multiple nodes accept writes. Each leader replicates to the others.

- Higher write availability (writes succeed if any leader is up).
- **Conflict resolution required**: two leaders can accept conflicting writes for the same record.
- Complex to implement correctly.
- Use case: multi-datacenter writes where cross-DC write latency is unacceptable.

### Leaderless (Dynamo-Style)
No designated leader. Clients write to multiple nodes and read from multiple nodes. Quorums determine success.

```
Write: send to N nodes, require W acknowledgements
Read: query N nodes, require R acknowledgements
If W + R > N → reads see the latest write (quorum overlap)
```

- Highly available: no single leader to fail.
- Tolerates node failures gracefully.
- Eventual consistency; conflict resolution needed.
- Used by: Cassandra, DynamoDB, Riak.

---

## Synchronous vs Asynchronous Replication

### Synchronous
Leader waits for at least one follower to confirm it received the write before acknowledging the client.
- **No data loss** on leader failure (follower has the data).
- **Higher write latency** (must wait for network round trip to follower).
- If the synchronous follower is down, writes block.

### Asynchronous
Leader acknowledges the write immediately; replication happens in the background.
- **Lower write latency**.
- **Replication lag**: followers may be seconds (or more) behind the leader.
- If leader fails before replication, that data is **lost**.

### Semi-Synchronous (Common Compromise)
One follower is synchronous; the rest are async. Guarantees at least one copy of every write without requiring all replicas to confirm.

---

## Replication Lag & Problems

Even with async replication, lag causes issues:

| Problem | What Happens | Fix |
|---|---|---|
| Reading your own write | Write to leader; read from lagging follower → see stale data | Route reads to leader for 1 minute after a write |
| Monotonic reads | Read v2, then v1 from a different replica (time going backward) | Pin user to same replica |
| Consistent prefix reads | See effects before their causes (B before A if replicas process out of order) | Causally consistent reads |

---

## Failover

When the leader fails, a follower must be promoted.

**Automatic failover steps:**
1. Detect leader failure (heartbeat timeout).
2. Elect a new leader (follower with most up-to-date log, or via consensus: Raft, Paxos).
3. Redirect clients to new leader.
4. Old leader re-joins as a follower.

**Risks:**
- Split-brain: two nodes both think they're the leader. Fix: fencing (only one leader can write at a time), quorum-based elections.
- Data loss: newly promoted leader may not have the latest writes if replication was async.

---

## Trade-offs

| Topology | Write Scale | Consistency | Complexity |
|---|---|---|---|
| Leader-Follower | Limited (one leader) | Strong (sync) / Eventual (async) | Low |
| Multi-Leader | High | Hard to guarantee | High |
| Leaderless | High | Tunable via quorum | Medium |

| Sync Replication | No data loss | Higher latency |
| Async Replication | Low latency | Data loss risk, replication lag |
