# Relational Databases (SQL)

## What is it?
A database that stores data in tables with rows and columns. Relationships between tables are defined via foreign keys. You query it with SQL. Examples: PostgreSQL, MySQL, SQLite.

## Core properties: ACID
- **Atomicity** — a transaction either fully succeeds or fully fails (no partial writes)
- **Consistency** — data always satisfies defined rules/constraints
- **Isolation** — concurrent transactions don't interfere with each other
- **Durability** — committed data survives crashes

## Scaling patterns
- **Vertical scaling** — bigger machine (more CPU/RAM). Simple but has a ceiling.
- **Read replicas** — primary handles writes, replicas handle reads. Good for read-heavy workloads.
- **Sharding** — split data across multiple DB instances by a shard key (e.g., user_id % N). Hard to do right.
- **Connection pooling** — reuse DB connections instead of opening a new one per request (PgBouncer, etc.)

## Indexes
- Speed up reads dramatically by avoiding full table scans
- Slow down writes (index must be updated on every write)
- Use on columns you frequently filter/join/sort on

## Trade-offs

| Pro | Con |
|-----|-----|
| Strong consistency and ACID guarantees | Harder to scale horizontally than NoSQL |
| Powerful joins and complex queries | Schema changes can be painful on large tables |
| Mature tooling, widely understood | Vertical scaling is expensive |
| Great for structured, relational data | Can become a bottleneck under very high write loads |

## When to use
- Financial data, orders, user accounts — anything where correctness is critical
- Complex queries with joins across multiple entities
- When your data has a clear, stable schema

## When NOT to use
- Massive write throughput at scale (consider NoSQL or time-series DBs)
- Unstructured or highly variable data shapes
- Global low-latency reads (consider caching or distributed stores)
