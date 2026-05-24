# Caching

Store copies of data in a fast-access layer so future requests skip the slow source (DB, API, computation).

## How It Works

1. Request comes in → check cache first
2. **Cache hit**: return cached data (fast)
3. **Cache miss**: fetch from source, store in cache, return data

## Cache Placement

| Location | Example | Latency |
|---|---|---|
| Client-side | Browser cache | ~0ms (local) |
| CDN | CloudFront edge node | ~10ms |
| Application-level | Redis / Memcached | ~1ms |
| Database query cache | MySQL query cache | ~5ms |

## Eviction Policies

- **LRU** (Least Recently Used) — evict the item not accessed for the longest time. Most common.
- **LFU** (Least Frequently Used) — evict the item accessed least often.
- **TTL** (Time To Live) — evict after a fixed time window regardless of usage.

## Invalidation Strategies

| Strategy | How | When to Use |
|---|---|---|
| Write-through | Write to cache AND DB simultaneously | Strong consistency needed |
| Write-back | Write to cache only; flush to DB later | High write throughput, tolerate some data loss |
| Write-around | Write directly to DB, skip cache | Data written once, rarely re-read |
| Cache-aside | App checks cache; on miss, loads from DB | Most common general pattern |

## Trade-offs

| Pro | Con |
|---|---|
| Dramatically reduces latency | Stale data risk |
| Reduces DB load | Cache invalidation is hard |
| Can absorb traffic spikes | Adds infrastructure complexity |
| Cheap reads at scale | Cold start / cache warm-up problem |

## Common Pitfalls

- **Cache stampede**: many requests miss simultaneously and all hit the DB. Fix: mutex lock or probabilistic early expiration.
- **Thundering herd**: same as stampede but after a cache restart.
- **Hot keys**: one cache key gets disproportionate traffic. Fix: replicate or shard the key.

## Quick Rules of Thumb

- Cache data that is **read frequently, written rarely**.
- TTL should reflect how stale you can tolerate, not how long you want to keep data.
- Always plan for the cold-start case.
