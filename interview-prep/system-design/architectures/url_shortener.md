# Architecture: URL Shortener (bit.ly-like)

**Scale target:** 100M URLs created/day, 10B redirects/day (100:1 read/write ratio)

---

## Problem

Design a service that maps short codes (e.g., `short.ly/abc123`) to long URLs, and redirects users at high speed. Support custom aliases, expiry, and click analytics.

---

## Architecture Diagram

```
                              ┌──────────────┐
                              │  DNS + CDN   │   ← CDN caches redirect responses at the edge
                              └──────┬───────┘
                                     │
                              ┌──────▼───────┐
                              │ Load Balancer │
                              └──────┬───────┘
                                     │
                              ┌──────▼───────┐
                              │  API Gateway │   ← rate limiting per IP/user
                              └──┬───────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
      ┌───────▼──────┐  ┌────────▼───────┐  ┌──────▼──────────┐
      │ Shorten API  │  │  Redirect API  │  │ Analytics API   │
      │ POST /shorten│  │  GET /{code}   │  │ GET /{code}/stats│
      └───────┬──────┘  └────────┬───────┘  └──────┬──────────┘
              │                  │                  │
      ┌───────▼──────┐  ┌────────▼───────┐  ┌──────▼──────────┐
      │  ID Generator │  │  Redis Cache  │  │ ClickHouse /    │
      │  (Snowflake   │  │  code → URL   │  │ Kafka stream    │
      │   or ULID)    │  │  (TTL = expiry│  │ (click events)  │
      └───────┬──────┘  └────────┬───────┘  └─────────────────┘
              │           cache miss │
              │                  ▼
              │         ┌────────────────┐
              └────────►│  PostgreSQL    │
                        │  urls table    │
                        │  (code, url,   │
                        │   expiry,      │
                        │   user_id)     │
                        └────────────────┘
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| DNS + CDN | DNS, CDN | `building_blocks/dns.md`, `building_blocks/cdn.md` |
| Load Balancer | Load Balancers | `building_blocks/load_balancers.md` |
| API Gateway + Rate Limiter | API Gateway, Rate Limiter | `building_blocks/api_gateway.md`, `building_blocks/rate_limiter.md` |
| Snowflake / ULID ID | Unique ID Generation | `patterns/unique_id_generation.md` |
| Redis Cache | Caches | `building_blocks/caches.md` |
| PostgreSQL | Relational Databases | `building_blocks/relational_databases.md` |
| Indexes on `code` column | Indexes | `concepts/indexes.md` |
| Read replicas for redirect reads | Scaling Reads, Replication | `patterns/scaling_reads.md`, `concepts/replication.md` |
| ClickHouse / Kafka for analytics | Time-Series Data | `patterns/time_series_data.md` |

---

## Key Decisions

### 1. Short code generation
Two approaches:

**Option A — Hash-based:**  
`MD5(long_url)` → take first 6–8 chars → store in DB with collision check.  
Problem: collisions require retry logic; same URL always maps to the same code.

**Option B — ID-based (preferred):**  
Generate a unique numeric ID (Snowflake or ULID), encode it in Base62.  
```
ID: 1234567  →  Base62  →  "B9s3a"
```
No collisions, sortable, no coordination needed with Snowflake.  
→ See `patterns/unique_id_generation.md`

### 2. Redis as the redirect cache
The redirect path (`GET /{code}`) must be sub-millisecond. Cache every active short URL:
```
SET url:{code} "https://long-url-here.com" EX {ttl_seconds}
```
Cache hit rate will be very high — most redirects go to recently created or popular URLs.  
On expiry or cache miss, fall back to PostgreSQL.  
→ See `building_blocks/caches.md`

### 3. CDN for redirect caching
For public (non-personalized) URLs, the CDN can cache the `301/302` redirect response itself.  
A `301 Permanent` redirect lets browsers cache it forever — great for throughput, bad if you need to change the target.  
Use `302 Temporary` if analytics or URL editing matters; the CDN uses `Cache-Control` headers to hold it for minutes/hours.

### 4. PostgreSQL schema + indexes
```sql
CREATE TABLE urls (
  code       VARCHAR(10) PRIMARY KEY,   -- B-tree index by default
  long_url   TEXT NOT NULL,
  user_id    BIGINT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  expires_at TIMESTAMPTZ
);
CREATE INDEX idx_user_urls ON urls (user_id, created_at DESC);
```
Primary key on `code` is the hot path — O(log N) B-tree lookup.  
→ See `concepts/indexes.md`

### 5. Analytics via async Kafka stream
Never write click events synchronously in the redirect path — that would double latency.  
On each redirect: fire-and-forget to Kafka `click-events` topic.  
A consumer aggregates into ClickHouse (columnar store) for time-series analytics: clicks/hour, referrers, geographies.  
→ See `patterns/time_series_data.md`

### 6. Expiry handling
Set `expires_at` in the DB. Redis TTL is set to match. Two-level expiry:
- Redis auto-evicts after TTL.
- Redirect service checks `expires_at` on DB reads and returns 410 Gone if expired.
- Background cleanup job (cron) hard-deletes rows where `expires_at < NOW() - 30 days`.

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| 10B redirects/day (115K/sec peak) | Redis cache absorbs >99% of reads |
| Cache miss → DB read | Read replicas for PostgreSQL |
| Shorten write throughput | Single master is fine at this scale; shard by `user_id` range if needed |
| Custom alias collisions | Check Redis + DB before confirming; optimistic locking |
| Analytics write volume | Async Kafka → ClickHouse; never in redirect path |

---

## Interview Tips

- Start with the read/write ratio: 100:1 means design around reads.
- ID-based code generation is cleaner than hashing — explain why (no collisions, shorter codes, sortable).
- Discuss `301 vs 302` redirect — interviewers love this trade-off.
- The analytics pipeline is a bonus — mention it shows you think beyond the happy path.
