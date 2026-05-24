# Circuit Breaker & Bulkhead

Patterns for building **resilient** distributed systems. Prevent one failing service from taking down everything else.

---

## The Problem: Cascading Failures

Service A calls Service B. Service B gets slow/overloaded. Service A's requests pile up waiting for B. Service A's thread pool fills up. Service A becomes slow. Service C, which calls A, now fails too. The whole system collapses.

---

## Circuit Breaker

Like an electrical circuit breaker: automatically stops sending requests to a failing service.

### States

```
CLOSED → (too many failures) → OPEN → (timeout elapsed) → HALF-OPEN → (success) → CLOSED
                                                                      → (failure)  → OPEN
```

- **CLOSED**: normal operation. Requests flow through. Failures are counted.
- **OPEN**: failures exceeded threshold. All requests **fail immediately** without hitting the downstream service. Saves resources.
- **HALF-OPEN**: after a timeout, allow a small number of test requests through. If they succeed → close the breaker. If they fail → reopen.

### Configuration knobs
- Failure threshold (e.g., 50% of last 20 requests failed)
- Wait duration in OPEN state (e.g., 30 seconds)
- Number of test requests in HALF-OPEN

### What to do when OPEN
- Return a cached/stale response
- Return a default/fallback value
- Return an error immediately (fail fast)

Libraries: **Resilience4j** (Java), **Polly** (.NET), **Hystrix** (deprecated but concepts still relevant).

---

## Bulkhead

Isolate components so a failure in one doesn't exhaust shared resources.

Named after ship bulkheads — watertight compartments that prevent the whole ship from sinking if one section floods.

### Thread Pool Isolation
Give each downstream dependency its own thread pool. If Service B is slow, it can only exhaust its own thread pool, not the shared one.

```
[Service A]
  ├── Thread pool for Service B (10 threads max)
  ├── Thread pool for Service C (10 threads max)
  └── Thread pool for Service D (10 threads max)
```

If Service B hangs, it fills its 10 threads. Requests to C and D still work.

### Semaphore Isolation
Limit concurrent calls to a dependency via a semaphore. Lighter weight than thread pools, but doesn't isolate thread resources.

### Rate Limiting per Caller
Limit how many requests each upstream client can make, preventing one noisy caller from consuming all capacity.

---

## Timeout

Always set timeouts on outbound calls. Without a timeout, a slow service causes requests to hang forever, filling up your thread pool.

- **Connection timeout**: how long to wait to establish a connection (~1–5s).
- **Read timeout**: how long to wait for a response after connecting (~5–30s, depends on SLA).

---

## Retry with Backoff

Retry transient failures, but don't retry blindly:
- Use **exponential backoff** (1s, 2s, 4s, 8s…) to avoid thundering herd.
- Add **jitter** (randomness) to prevent all clients retrying in sync.
- Set a **max retry count**.
- Don't retry non-idempotent operations (e.g., charging a card) without idempotency keys.

---

## Trade-offs

| Pattern | Benefit | Cost |
|---|---|---|
| Circuit breaker | Fast failure; protects downstream | Adds state; needs tuning |
| Bulkhead | Fault isolation | More resource allocation overhead |
| Timeout | Prevents indefinite hangs | May cut off slow-but-valid requests |
| Retry + backoff | Handles transient failures | Can amplify load on recovering services |

---

## These Work Together

A robust service call uses all four:
1. **Timeout**: don't wait forever.
2. **Retry**: handle transient failures.
3. **Circuit breaker**: stop retrying a dead service.
4. **Bulkhead**: isolate failures from spreading.
