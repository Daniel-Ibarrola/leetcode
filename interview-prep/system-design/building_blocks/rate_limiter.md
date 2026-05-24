# Rate Limiter

## What is it?
A mechanism that controls how many requests a client can make in a given time window. Protects your services from abuse, DoS attacks, and runaway clients. Can live in the API Gateway, a middleware layer, or as a standalone service.

## Common Algorithms

### Token Bucket
- A bucket holds up to N tokens; tokens are added at a fixed rate
- Each request consumes one token; if the bucket is empty, the request is rejected
- Allows short bursts (use up accumulated tokens), then throttles to the refill rate
- **Most common in practice** (used by AWS, Stripe)

### Leaky Bucket
- Requests enter a queue (the "bucket"); they leak out at a fixed rate
- Smooths out bursts — output rate is always constant
- Good for protecting downstream services from spikes

### Fixed Window Counter
- Divide time into fixed windows (e.g., each minute); count requests per window
- Simple to implement, but has an edge case: a client can send 2× the limit by hitting the boundary (last second of window + first second of next)

### Sliding Window Log
- Keep a log of request timestamps; count how many fall within the last N seconds
- Accurate but memory-intensive (stores every timestamp)

### Sliding Window Counter
- Hybrid: use two fixed windows and interpolate based on position in the current window
- Good balance of accuracy and memory efficiency

## Where to store the counters
- **In-memory (per node)** — fast but not shared; each server has its own count, so the limit isn't enforced globally
- **Redis** — distributed, shared across all servers; use atomic `INCR` + `EXPIRE`; the standard approach for global rate limiting

## Trade-offs

| Pro | Con |
|-----|-----|
| Protects services from overload and abuse | Adds latency (especially with a Redis round-trip per request) |
| Fairness — prevents one client from hogging resources | Hard to set the right limits (too tight = frustrating; too loose = useless) |
| Can be tiered (free vs. paid limits) | Distributed rate limiting requires coordination (Redis becomes a bottleneck at extreme scale) |

## Rate limiting headers (good practice)
Return these so clients can self-throttle:
- `X-RateLimit-Limit` — max requests allowed
- `X-RateLimit-Remaining` — requests left in current window
- `X-RateLimit-Reset` — timestamp when the window resets
- `429 Too Many Requests` — status code when limit is exceeded

## When to use
- Public APIs exposed to external clients
- Login endpoints (prevent brute force)
- Any endpoint that's expensive to compute or touches a downstream service
- Enforcing per-user or per-tier quotas

## When NOT to use
- Pure internal service-to-service traffic where you control both sides
- When circuit breakers already protect the downstream (though both can coexist)
