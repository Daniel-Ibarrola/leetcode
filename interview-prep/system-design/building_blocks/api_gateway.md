# API Gateway

## What is it?
A single entry point that sits between clients and your backend services. Instead of clients calling each microservice directly, all requests go through the gateway, which handles cross-cutting concerns: routing, auth, rate limiting, logging. Examples: AWS API Gateway, Kong, NGINX, Apigee.

## What it does
- **Routing** — forwards requests to the right backend service based on path/method
- **Authentication & Authorization** — validates tokens (JWT, OAuth) before requests reach services
- **Rate limiting** — throttles clients to prevent abuse
- **SSL termination** — handles HTTPS so backends speak plain HTTP
- **Request/response transformation** — reshapes payloads (e.g., aggregates responses from multiple services)
- **Caching** — can cache responses at the edge
- **Logging & monitoring** — central place to capture all traffic metrics

## How it fits in an architecture

```
Client → API Gateway → Service A
                     → Service B
                     → Service C
```

Without a gateway, clients need to know about every service and handle auth themselves — messy and insecure.

## Trade-offs

| Pro | Con |
|-----|-----|
| Single place to enforce auth, rate limits, and logging | Single point of failure (must be highly available) |
| Hides internal service topology from clients | Adds latency (one extra network hop) |
| Decouples client interface from backend structure | Can become a bottleneck if not scaled properly |
| Simplifies client code | Risk of putting too much business logic in the gateway |

## Gateway vs Load Balancer
- **Load balancer** — distributes traffic across identical instances of one service (L4/L7)
- **API Gateway** — routes to *different* services, enforces policy, transforms requests

They're often used together: gateway routes to service A, load balancer distributes across service A's instances.

## When to use
- Microservices architecture with many backend services
- Public APIs that need auth and rate limiting
- When you want a single place to manage cross-cutting concerns

## When NOT to use
- Simple monolith with one backend — overkill, just adds complexity
- Internal service-to-service calls (use a service mesh instead)
