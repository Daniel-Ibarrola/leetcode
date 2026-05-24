# Scaling Reads

When your system gets more read traffic than a single DB can handle, you need to distribute that load.

## Strategies

### 1. Read Replicas
Add read-only copies of the primary DB. Reads go to replicas; writes go to primary.
- Easy to set up with most managed DBs (RDS, Cloud SQL)
- Replicas may lag behind primary by milliseconds → stale reads possible
- Good for: analytics queries, dashboards, reporting

### 2. Caching Layer
Store hot results in Redis / Memcached in front of the DB.
- Dramatically reduces DB load for repeated queries
- Risk: stale data, cache invalidation complexity
- Good for: read-heavy, rarely-changing data (product catalog, user profiles)

### 3. CDN for Static Content
Serve images, JS, CSS, and even API responses from edge nodes geographically close to users.
- Near-zero latency for cached content
- Only works for content that can be cached (not personalized, not transactional)

### 4. CQRS (Command Query Responsibility Segregation)
Separate the read model from the write model entirely. Writes update the write store; a separate read store (optimized for queries) is updated asynchronously.
- Read store can be denormalized, pre-aggregated, tuned for specific queries
- Added complexity: two data stores, eventual consistency between them
- Good for: high read volume with complex query patterns

### 5. Sharding / Partitioning
Split data across nodes so each node handles a subset of reads.
- Scales both reads and storage
- Cross-shard queries are expensive
- Adds operational complexity

## Trade-offs

| Strategy | Consistency Risk | Complexity | Best For |
|---|---|---|---|
| Read replicas | Replication lag | Low | General read scale-out |
| Caching | Stale data | Medium | Hot, rarely-changing data |
| CDN | High (long TTLs) | Low | Static / semi-static content |
| CQRS | Eventual (by design) | High | Complex query patterns |
| Sharding | Low (if designed well) | High | Very large datasets |

## Decision Guide

1. Is data mostly static? → CDN or cache first.
2. Is the bottleneck repetitive DB queries? → Add a cache.
3. Do you need near-real-time but can tolerate slight lag? → Read replicas.
4. Do reads and writes have very different shapes? → Consider CQRS.
5. Is one node simply out of disk / RAM? → Shard.
