# Distributed Locking

Coordinate exclusive access to a shared resource across multiple processes or machines. Prevents race conditions when a single DB transaction isn't an option.

---

## When You Need It

- Only one worker should process a job at a time (deduplication).
- Atomic inventory decrement across services.
- Leader election: elect one node as the primary.
- Cron job that should only run on one server.
- Generating a unique resource (e.g., a username).

---

## Approach 1: Redis (SETNX + Expiry)

Atomic `SET key value NX PX ttl_ms` — sets the key only if it doesn't exist, with a TTL.

```
SET lock:resource_id <unique_token> NX PX 30000
```

- If the command returns OK → you have the lock.
- If it returns nil → someone else holds it.
- To release: check the token matches (you own it), then delete it. Use a Lua script for atomicity.
- **TTL is critical**: prevents a crashed holder from keeping the lock forever.

### Risk: Clock drift / GC pauses
If the lock holder pauses (GC, network lag) longer than the TTL, the lock expires. Another node acquires it. Both nodes now think they hold the lock.

### Redlock (Multi-node Redis)
Redis's algorithm for stronger guarantees: acquire the lock on N/2+1 of N Redis nodes independently. Protects against single Redis node failure.
- Controversial — some argue it still has edge cases with clock drift.
- Use if you need stronger guarantees; otherwise single-node Redis is fine for most use cases.

---

## Approach 2: Database-Based Lock

```sql
INSERT INTO locks (resource_id, holder, expires_at)
VALUES ('my_resource', 'worker_1', NOW() + INTERVAL '30 seconds')
ON CONFLICT (resource_id) DO NOTHING;
```

Returns 1 row inserted = lock acquired; 0 = already locked.

Or use `SELECT FOR UPDATE` to lock a row while working on it.

- Durable (survives Redis restart)
- Slower than Redis
- Good when you're already in a DB transaction

---

## Approach 3: Zookeeper / etcd

Purpose-built distributed coordination systems. Use ephemeral nodes (Zookeeper) or leases (etcd) that automatically expire when the holder disconnects.

- Strongest consistency guarantees
- More complex to operate
- Used for: leader election, service discovery, config management
- etcd is the backing store for Kubernetes

---

## Comparison

| Approach | Speed | Durability | Complexity | Use Case |
|---|---|---|---|---|
| Redis SETNX | Fastest | Low (in-memory) | Low | Short-lived locks, rate limiting |
| DB row lock | Medium | High | Low | Already in DB transaction |
| Zookeeper/etcd | Medium | High | High | Leader election, critical coordination |

---

## Common Pitfalls

- **No TTL**: a crashed holder keeps the lock forever. Always set an expiry.
- **TTL too short**: lock expires while the holder is still working. Use a watchdog thread to refresh the TTL periodically.
- **Not validating ownership on release**: deleting a lock you don't own. Always check the token before deleting.
- **Using locks for high-throughput paths**: locks are serializing — they destroy throughput. Design to avoid them where possible (optimistic concurrency, CAS operations).

---

## Optimistic Locking (Alternative)

Instead of blocking, let writes proceed and check for conflicts at commit time using a **version number**:

```sql
UPDATE items SET stock = stock - 1, version = version + 1
WHERE id = 1 AND version = :expected_version
```

If 0 rows updated → conflict, retry. Better throughput than locks when conflicts are rare.
