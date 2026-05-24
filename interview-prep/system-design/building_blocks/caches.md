# Caches

## What is it?
A cache stores copies of frequently-accessed data in fast memory (RAM) so you don't have to hit a slower source (database, API, disk) every time. The classic trade-off: speed vs. freshness.

## Where caches live
- **Client-side** — browser cache, mobile app cache
- **CDN** — caches static assets geographically close to users
- **Application cache** — in-process (e.g., a Python dict), fast but not shared across servers
- **Distributed cache** — shared across servers (Redis, Memcached), the most common production pattern

## Eviction Policies (what to remove when full)
- **LRU (Least Recently Used)** — evicts the item not accessed for the longest time (most common)
- **LFU (Least Frequently Used)** — evicts the item accessed fewest times
- **TTL (Time To Live)** — items expire after a set duration regardless of usage

## Cache Invalidation Strategies
- **Write-through** — write to cache AND DB at the same time (consistent, but slower writes)
- **Write-back (write-behind)** — write to cache only, sync to DB asynchronously (fast writes, risk of data loss)
- **Cache-aside (lazy loading)** — app checks cache first; on miss, loads from DB and populates cache (most common)

## Trade-offs

| Pro | Con |
|-----|-----|
| Dramatically reduces DB load | Stale data — cache may not reflect latest DB state |
| Very low read latency (microseconds vs. milliseconds) | Cache invalidation is hard to get right |
| Absorbs traffic spikes | Extra infrastructure to manage |
| Can serve as a rate-limiter or session store | Cold start — empty cache after restart |

## Common pitfalls
- **Cache stampede (thundering herd)** — cache expires, many requests hit DB simultaneously; mitigate with locks or probabilistic early expiration
- **Cache penetration** — requests for non-existent keys always miss; mitigate with bloom filters or caching null results
- **Cache avalanche** — many keys expire at once; mitigate by staggering TTLs

## When to use
- Repeated reads of the same data (user profiles, config, product catalog)
- Expensive computation results
- Session storage

## When NOT to use
- Data that changes very frequently — by the time a cached value is read, it's likely stale
- Data that must always be strongly consistent (e.g., account balances, inventory counts)
- Unique or low-repetition queries — if every request is different, the cache hit rate will be near zero and you're just burning memory
- Write-heavy workloads — caches shine on reads; if writes dominate, the overhead of keeping the cache in sync outweighs the benefit
- Small datasets that already fit in DB memory — the DB buffer pool effectively caches them anyway
