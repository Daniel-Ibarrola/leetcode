# Load Balancers

## What is it?
A load balancer sits in front of your servers and distributes incoming traffic across them. Think of it as a traffic cop: requests come in, and it decides which server handles each one.

## Common Algorithms
- **Round Robin** — requests go to each server in turn (1, 2, 3, 1, 2, 3…)
- **Least Connections** — sends to the server with the fewest active requests
- **IP Hash** — same client IP always goes to the same server (useful for sticky sessions)
- **Weighted** — some servers get more traffic (e.g., bigger machines)

## Types
- **L4 (Transport layer)** — routes based on IP/TCP, fast but dumb
- **L7 (Application layer)** — routes based on HTTP content (URL, headers, cookies), smarter but slightly slower

## Trade-offs

| Pro | Con |
|-----|-----|
| Horizontal scalability — add more servers easily | Single point of failure (unless you have redundant LBs) |
| Hides server failures from clients | Adds a network hop (small latency overhead) |
| Enables zero-downtime deploys | Stateful sessions need special handling (sticky sessions or external session store) |
| Health checks remove bad servers automatically | L7 LBs are more expensive to run |

## When to use
Use whenever you have more than one server handling the same workload. Almost always needed in production systems.

## Key terms
- **Health check** — LB pings servers periodically; stops routing to unhealthy ones
- **Sticky session** — same user always hits the same server (avoids session mismatch, but reduces flexibility)
- **SSL termination** — LB handles HTTPS, forwards plain HTTP to backend (offloads TLS work from servers)
