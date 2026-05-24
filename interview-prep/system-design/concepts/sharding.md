# Sharding

Split a large dataset across multiple databases/nodes so no single machine holds all the data. Each split is a **shard**.

## Why Shard?

A single DB eventually hits limits: disk space, RAM, write throughput. Sharding scales horizontally by distributing data.

## Sharding Strategies

### Range-Based
Split by value range (e.g., user IDs 1–1M on shard A, 1M–2M on shard B).
- Simple to reason about
- Risk: **hot spots** if one range gets most traffic (e.g., newest users)

### Hash-Based
Apply a hash function to the shard key; route to `hash(key) % N`.
- Even distribution
- Adding/removing shards requires **resharding** (moving data)

### Consistent Hashing
A ring-based approach where adding/removing nodes only moves a fraction of keys.
- Standard solution for minimizing resharding cost
- Used by DynamoDB, Cassandra, Redis Cluster

### Directory-Based
A lookup table maps each key to its shard.
- Very flexible (easy to rebalance)
- The directory itself becomes a bottleneck/single point of failure

## Choosing a Shard Key

Good shard keys:
- High cardinality (many distinct values)
- Evenly distributed access patterns
- Rarely updated

Bad shard keys: timestamps (monotonically increasing → range hotspot), low-cardinality fields (e.g., boolean).

## Trade-offs

| Pro | Con |
|---|---|
| Horizontal scalability | Cross-shard queries are complex/slow |
| Fault isolation per shard | Transactions across shards are hard |
| Can tune each shard independently | Rebalancing is operationally painful |
| Parallel write throughput | Joins across shards require application-level logic |

## Cross-Shard Problems

- **Cross-shard joins**: pull data from multiple shards into the app layer and join there.
- **Cross-shard transactions**: use 2-phase commit (slow) or design to avoid them.
- **Global aggregations**: scatter-gather — query all shards, aggregate results.

## Alternatives to Consider First

Before sharding, try: read replicas, vertical scaling, caching, better indexes. Sharding adds significant complexity.
