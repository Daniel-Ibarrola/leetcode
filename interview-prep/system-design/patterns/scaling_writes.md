# Scaling Writes

Write-heavy systems hit limits differently than read-heavy ones: you can't just add replicas. The primary DB is the bottleneck.

## Strategies

### 1. Write-Ahead Log (WAL) / Buffering
Buffer writes in memory or a fast append-only log before flushing to durable storage.
- High throughput, low latency writes
- Risk of data loss if buffer isn't persisted before crash
- Used internally by most DBs (Postgres WAL, Kafka log)

### 2. Async Writes via Queue
Put writes onto a message queue (Kafka, SQS). Workers drain the queue and write to the DB.
- Decouples producers from DB throughput
- Absorbs traffic spikes
- Writes are not immediately visible → eventual consistency
- Good for: event ingestion, audit logs, activity feeds

### 3. Sharding
Split the write load across multiple DB primaries, each owning a partition of the data.
- True horizontal write scale
- Cross-shard transactions are hard
- Choose a shard key that distributes writes evenly (avoid hotspots)

### 4. Denormalization / Pre-computation
Write aggregated/derived data at write time so reads are cheap.
- Moves work to write path, keeps reads fast
- Duplicates data; updates require updating multiple places
- Good for: counters, leaderboards, dashboards

### 5. Event Sourcing
Instead of updating a record, append an event to an immutable log. State is derived by replaying events.
- Perfect audit trail
- Naturally scales writes (append-only)
- Complex to query current state; requires projection/read models
- Good for: financial transactions, order management

### 6. Batching
Accumulate writes and flush in bulk instead of one-by-one.
- Much higher throughput per second
- Increases latency for individual writes
- Used by: time-series DBs, analytics pipelines

## Trade-offs

| Strategy | Consistency | Latency | Complexity | Best For |
|---|---|---|---|---|
| Queue + async workers | Eventual | High (for caller) | Medium | Spike absorption, decoupling |
| Sharding | Strong per shard | Low | High | Large scale, high write throughput |
| Denormalization | Must manage manually | Low | Medium | Read-optimized systems |
| Event sourcing | Strong (append-only) | Low | Very high | Audit, financial, CQRS |
| Batching | Strong (on flush) | High | Low | Analytics, bulk ingest |

## Common Pitfalls

- **Write hotspots**: monotonically increasing keys (timestamps, auto-increment IDs) funnel all writes to one shard. Use UUIDs or hash-based IDs.
- **Synchronous writes to slow stores**: if your write path blocks on a slow DB, the entire system slows down. Use async or buffering.
- **Over-normalizing**: forces multi-table writes per logical operation; consider denormalizing critical paths.
