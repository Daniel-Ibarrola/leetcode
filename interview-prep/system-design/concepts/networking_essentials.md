# Networking Essentials

Core networking concepts that come up in system design interviews.

---

## Protocols at a Glance

| Protocol | Layer | Use Case |
|---|---|---|
| TCP | Transport | Reliable, ordered delivery. HTTP, databases. |
| UDP | Transport | Fast, no guarantee. Video streaming, DNS, gaming. |
| HTTP/1.1 | Application | Request/response. One request per connection (with keep-alive). |
| HTTP/2 | Application | Multiplexed streams over one connection. Faster for many small requests. |
| HTTP/3 | Application | Uses QUIC (UDP-based). Lower latency, better on lossy networks. |
| WebSocket | Application | Full-duplex persistent connection. Real-time apps (chat, live feeds). |
| gRPC | Application | Binary protocol over HTTP/2. Efficient for service-to-service calls. |

---

## TCP vs UDP

| | TCP | UDP |
|---|---|---|
| Delivery guarantee | Yes (retransmits lost packets) | No |
| Ordering | Yes | No |
| Latency | Higher (handshake + ACKs) | Lower |
| Use case | APIs, file transfer, DB | Video calls, DNS, live streaming |

---

## HTTP Methods

| Method | Idempotent | Safe | Use |
|---|---|---|---|
| GET | Yes | Yes | Read data |
| POST | No | No | Create resource |
| PUT | Yes | No | Replace resource |
| PATCH | No | No | Partial update |
| DELETE | Yes | No | Delete resource |

**Idempotent**: calling it N times = calling it once. **Safe**: no side effects.

---

## Status Codes to Know

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content (success, no body) |
| 301/302 | Redirect (permanent/temporary) |
| 400 | Bad Request (client error) |
| 401 | Unauthorized (not authenticated) |
| 403 | Forbidden (authenticated but no permission) |
| 404 | Not Found |
| 429 | Too Many Requests (rate limited) |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## DNS (Domain Name System)

Translates domain names → IP addresses.

Resolution order: browser cache → OS cache → recursive resolver → root → TLD → authoritative NS.

**Record types:**
- `A` — domain → IPv4
- `AAAA` — domain → IPv6
- `CNAME` — alias to another domain
- `MX` — mail server
- `TXT` — arbitrary text (used for verification, SPF)

**TTL**: how long a DNS record can be cached. Low TTL = faster failover, more DNS traffic.

---

## Latency Numbers (Rough Order of Magnitude)

| Operation | ~Latency |
|---|---|
| L1 cache hit | 1 ns |
| L2 cache hit | 4 ns |
| RAM access | 100 ns |
| SSD random read | 100 µs |
| Same-datacenter network round trip | 0.5 ms |
| Cross-region (US East ↔ US West) | 40 ms |
| Cross-continent (US ↔ Europe) | 80 ms |

---

## Long Polling vs WebSockets vs SSE

| | Long Polling | WebSocket | SSE |
|---|---|---|---|
| Direction | Client pulls | Bidirectional | Server pushes only |
| Connection | New request per poll | Persistent | Persistent |
| Overhead | High (HTTP headers each time) | Low | Low |
| Use case | Simple notifications | Chat, gaming, collaboration | Live feeds, dashboards |

---

## Key Trade-offs

- **TCP reliability costs latency** — use UDP when you can tolerate loss (video, gaming).
- **HTTP/2 multiplexing** solves HTTP/1.1's head-of-line blocking within a connection.
- **WebSockets** are great for real-time but require sticky sessions or a message broker if you scale horizontally.
- **gRPC** is faster than REST for internal microservice calls but requires a schema (protobuf) and is harder to debug.
