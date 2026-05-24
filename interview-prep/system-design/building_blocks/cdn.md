# CDN (Content Delivery Network)

## What is it?
A CDN is a globally distributed network of servers (called "edge nodes" or "Points of Presence") that cache and serve content close to the user's physical location. Instead of every user hitting your origin server in, say, Virginia, a user in Tokyo gets content from a nearby edge node in Tokyo. Examples: Cloudflare, AWS CloudFront, Akamai.

## What gets cached on a CDN?
- Static assets: images, CSS, JavaScript, fonts, videos
- HTML pages (if they don't change per user)
- API responses (if cacheable)
- Software downloads

## How it works
1. User requests `example.com/logo.png`
2. DNS resolves to the nearest CDN edge node
3. If the edge has the file cached → serves it immediately (cache hit)
4. If not (cache miss) → edge fetches from origin, caches it, serves it
5. Future requests for the same file hit the cache

## Key concepts
- **Cache-Control / TTL** — tells the CDN how long to cache a file before re-fetching
- **Cache invalidation** — force the CDN to fetch fresh content before TTL expires (usually done on deploy)
- **Edge computing** — some CDNs (Cloudflare Workers) let you run code at the edge, not just serve files

## Trade-offs

| Pro | Con |
|-----|-----|
| Much lower latency for global users | Stale content if cache isn't invalidated properly |
| Offloads traffic from origin servers | Costs money (charged per GB transferred) |
| Built-in DDoS mitigation at edge | Dynamic, personalized content can't be cached |
| High availability — edge nodes are redundant | Cache invalidation adds deploy complexity |

## When to use
- Any app with global users and static/semi-static content
- Video streaming, image-heavy sites
- Protecting origin from traffic spikes
- Reducing server bandwidth costs

## When NOT to use
- Purely dynamic, user-specific content with no caching opportunity
- Very small-scale internal apps with localized users
