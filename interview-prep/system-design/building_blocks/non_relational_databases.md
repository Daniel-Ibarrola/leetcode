# Non-Relational Databases (NoSQL)

## What is it?
Databases that don't use the traditional table/row/column model. They trade some SQL guarantees (like strong consistency and complex joins) for flexibility, speed, or scale. Examples: MongoDB, Cassandra, DynamoDB, Redis.

## Types

### Key-Value
- Data stored as key → value pairs (like a giant hash map)
- Extremely fast reads/writes
- Examples: Redis, DynamoDB
- Use for: sessions, caches, leaderboards, counters

### Document
- Data stored as JSON-like documents (flexible schema)
- Good for nested/variable-shaped data
- Examples: MongoDB, Firestore
- Use for: user profiles, content, catalogs

### Wide-Column
- Rows can have different columns; optimized for large-scale writes and time-series
- Examples: Cassandra, HBase
- Use for: event logs, IoT data, time-series, write-heavy workloads

### Graph
- Data stored as nodes and edges (relationships are first-class)
- Examples: Neo4j
- Use for: social networks, recommendation engines, fraud detection

## Consistency model: BASE (vs ACID)
- **Basically Available** — system responds even if data might not be consistent
- **Soft state** — state can change over time even without input
- **Eventually consistent** — all replicas will converge to the same value, but not immediately

## Trade-offs

| Pro | Con |
|-----|-----|
| Scales horizontally with ease | Weak or eventual consistency (no ACID by default) |
| Flexible schema — easy to evolve data shape | No joins; application must handle relationships |
| Very high write throughput | Querying is limited compared to SQL |
| Built for distributed environments | Less mature tooling; steeper operational learning curve |

## When to use
- Massive scale (millions of writes/sec), where SQL becomes a bottleneck
- Flexible/evolving schemas (e.g., different attributes per user)
- Specific access patterns that map cleanly to a NoSQL model (e.g., time-series)

## When NOT to use
- Complex queries with many joins
- Transactions requiring ACID guarantees (banking, orders)
- Small-to-medium scale where SQL works fine
