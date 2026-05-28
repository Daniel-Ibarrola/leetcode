# Architecture: Social Media Feed (Twitter/X-like)

**Scale target:** 500M users, 100K writes/sec (tweets), 10M reads/sec (feed loads)

---

## Problem

Design a system where users post short messages and see a real-time, ranked feed of posts from accounts they follow.

---

## Architecture Diagram

```
                            ┌─────────────────┐
                            │   DNS + GeoDNS   │   ← routes to nearest region
                            └────────┬────────┘
                                     │
                            ┌────────▼────────┐
                            │      CDN        │   ← serves static assets, media thumbnails
                            └────────┬────────┘
                                     │
                            ┌────────▼────────┐
                            │   Load Balancer  │
                            └────────┬────────┘
                                     │
                            ┌────────▼────────┐
                            │   API Gateway   │   ← auth, rate limiting, routing
                            └──┬──────────┬──┘
                               │          │
              ┌────────────────▼──┐  ┌────▼──────────────────┐
              │   Write Service   │  │     Read Service       │
              │  (post a tweet)   │  │  (load feed / profile) │
              └────────┬──────────┘  └────────┬───────────────┘
                       │                      │
         ┌─────────────▼──────────┐   ┌───────▼──────────────┐
         │     Kafka (Pub/Sub)     │   │   Redis Feed Cache   │
         │  topic: new-posts       │   │  feed:user:{id}      │
         └──┬───────────┬─────────┘   └───────┬──────────────┘
            │           │                     │ (cache miss)
    ┌───────▼───┐  ┌────▼──────────┐  ┌───────▼──────────────┐
    │ Fan-Out   │  │ Notification  │  │   Post Store (DB)    │
    │ Worker    │  │ Service       │  │   Cassandra (sharded)│
    └───────────┘  └───────────────┘  └──────────────────────┘
         │
    writes post_id into
    feed:user:{follower_id} in Redis
    (for regular users, fan-out on write)
    (for celebrities, fan-out on read)
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| DNS + GeoDNS | DNS | `building_blocks/dns.md` |
| CDN | CDN | `building_blocks/cdn.md` |
| Load Balancer | Load Balancers | `building_blocks/load_balancers.md` |
| API Gateway | API Gateway | `building_blocks/api_gateway.md` |
| Rate limiting on post | Rate Limiter | `building_blocks/rate_limiter.md` |
| Kafka | Pub/Sub | `building_blocks/pub_sub.md` |
| Redis Feed Cache | Caches | `building_blocks/caches.md` |
| Post Store (Cassandra) | Non-Relational Databases | `building_blocks/non_relational_databases.md` |
| Fan-out Worker | Feed / Timeline Generation | `patterns/feed_and_timeline.md` |
| Real-time notifications | Real-Time Updates | `patterns/real_time_updates.md` |
| Paginating the feed | Pagination | `patterns/pagination.md` |
| Scaling read traffic | Scaling Reads | `patterns/scaling_reads.md` |
| Sharding post store | Sharding | `concepts/sharding.md` |

---

## Key Decisions

### 1. Hybrid fan-out
Regular users (< ~10K followers): **fan-out on write** — pre-build feed in Redis at post time.  
Celebrity users: **fan-out on read** — merge their posts into the feed at read time.  
→ See `patterns/feed_and_timeline.md`

### 2. Feed storage in Redis sorted sets
```
feed:user:bob → [(post_id, timestamp_score), ...]
```
Store only post IDs; fetch post content separately to avoid data duplication.  
Trim feed to last ~1000 entries — users rarely scroll further.

### 3. Cassandra for the post store
Posts are append-only with high write throughput. Cassandra handles:
- Wide-column model: `(user_id, timestamp) → post_content`
- Tunable consistency: write with `QUORUM`, read with `ONE` (AP system)
- Easy time-based partitioning

### 4. Kafka as the backbone
A single `new-posts` topic decouples the write path from all downstream consumers:
- Fan-out worker
- Search indexer
- Analytics pipeline
- Notification service  
→ Each is an independent consumer group; adding a new consumer requires no change to the write service.

### 5. Cursor-based pagination on the feed
Never use `OFFSET` on a feed at scale — results shift as new posts arrive.  
Use the last-seen post's timestamp/score as the cursor.  
→ See `patterns/pagination.md`

### 6. CAP trade-off
This is an **AP system**. A follower may see a slightly stale feed if a fan-out worker is lagging — acceptable.  
Strong consistency would require locking across millions of feed writes.  
→ See `concepts/cap_theorem.md`

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| Write amplification for celebrities | Hybrid fan-out (fan-out on read for high-follower accounts) |
| Feed read latency | Pre-built Redis feed; CDN for media |
| Post DB throughput | Cassandra sharded by user_id with consistent hashing |
| Hot partitions (trending topics) | Scatter writes across multiple shards; aggregate at read |
| Fan-out worker lag | Scale consumer group horizontally; increase Kafka partitions |

---

## Interview Tips

- Start with: "What's the read/write ratio and what's the follower distribution?"
- Justify Cassandra over MySQL: high write throughput, no complex joins, time-ordered queries fit wide-column model.
- Discuss feed staleness vs. consistency trade-off explicitly.
- Mention that search indexing (for tweet search) hangs off the same Kafka topic.
