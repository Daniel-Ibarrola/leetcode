# Architecture: Ride-Sharing Platform (Uber-like)

**Scale target:** 10M daily rides, 500K concurrent active trips, real-time location updates every 4 seconds

---

## Problem

Design a system that matches riders with nearby drivers in real time, tracks trips, and handles the end-to-end lifecycle of a ride (request → match → en route → drop-off → payment).

---

## Architecture Diagram

```
                     ┌──────────────────────────────────────┐
                     │         LOCATION TRACKING            │
                     └──────────────────────────────────────┘

Driver App ──► WebSocket ──► Location Service ──► Redis GeoHash
                                                  geo:drivers
                                                  (driver_id → lat/lng)

                     ┌──────────────────────────────────────┐
                     │        RIDE REQUEST FLOW             │
                     └──────────────────────────────────────┘

Rider App
    │
    ▼
API Gateway (auth, rate limit)
    │
    ▼
Ride Request Service
    │
    ├──► Redis GeoHash → find nearby drivers (GEORADIUS query)
    │
    ├──► Matching Service → rank candidates, send offer to driver
    │       │
    │       ▼
    │    Message Queue (driver offer topic)
    │       │
    │   Driver App ◄── WebSocket push (offer notification)
    │       │
    │   Driver accepts → Ride confirmed
    │
    └──► Trip DB (PostgreSQL) → INSERT trip (status=REQUESTED)

                     ┌──────────────────────────────────────┐
                     │          ACTIVE TRIP FLOW            │
                     └──────────────────────────────────────┘

Driver App ──► Location Service ──► Kafka (trip-location topic)
                                          │
                               ┌──────────▼───────────┐
                               │  Trip Tracking Worker │
                               │  (update ETA,         │
                               │   route deviation)    │
                               └──────────┬───────────┘
                                          │
                               Rider App ◄── SSE / WebSocket
                               (real-time driver location on map)

                     ┌──────────────────────────────────────┐
                     │         TRIP COMPLETION              │
                     └──────────────────────────────────────┘

Driver marks trip complete
    │
    ▼
Trip Service → UPDATE trips SET status=COMPLETED
    │
    ▼
Kafka (trip-completed topic)
    ├──► Payment Service (charge rider, pay driver)
    ├──► Notification Service (receipt email/push)
    └──► Analytics Pipeline
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| API Gateway | API Gateway | `building_blocks/api_gateway.md` |
| Rate limiting (prevent request flooding) | Rate Limiter | `building_blocks/rate_limiter.md` |
| Redis GeoHash (driver locations) | Caches | `building_blocks/caches.md` |
| WebSocket / SSE (real-time location) | Real-Time Updates | `patterns/real_time_updates.md` |
| Kafka (trip events) | Pub/Sub | `building_blocks/pub_sub.md` |
| Message Queue (driver offers) | Message Queues | `building_blocks/message_queues.md` |
| Distributed lock (prevent double-match) | Distributed Locking | `patterns/distributed_locking.md` |
| PostgreSQL (trips) | Relational Databases | `building_blocks/relational_databases.md` |
| Trip lifecycle (multi-step) | Multi-Step Processes | `patterns/multi_step_processes.md` |
| Payment + notification (long-running) | Long-Running Tasks | `patterns/long_running_tasks.md` |
| Circuit breaker (payment service) | Circuit Breaker & Bulkhead | `patterns/circuit_breaker_and_bulkhead.md` |
| CAP trade-off (location vs. accuracy) | CAP Theorem | `concepts/cap_theorem.md` |

---

## Key Decisions

### 1. Redis GeoHash for driver location
Driver apps send location every 4 seconds → Location Service writes to Redis:
```
GEOADD drivers:nyc <lng> <lat> <driver_id>
GEORADIUS drivers:nyc <rider_lng> <rider_lat> 2 km ASC COUNT 10
```
Redis in-memory GeoHash queries are O(N+log(M)) — fast enough for real-time matching.  
Location is **eventually consistent** by design: a 4-second-stale position is acceptable.

### 2. Distributed lock during driver matching
When the matching service selects a driver, it acquires a Redis lock on that driver_id before sending the offer.  
This prevents two riders from being offered the same driver simultaneously.
```
SETNX lock:driver:{driver_id}  (expires in 30 seconds)
```
→ See `patterns/distributed_locking.md`

### 3. WebSocket for driver app, SSE for rider app
- **Driver app**: bidirectional — must receive offers and send location → **WebSocket**
- **Rider app**: receives-only (driver's position on map) → **SSE** is simpler and sufficient
- WebSocket connections are held by a dedicated gateway; route messages via Kafka to decouple stateful connections from business logic  
→ See `patterns/real_time_updates.md`

### 4. Trip as a multi-step saga
A trip progresses through states: `REQUESTED → MATCHED → DRIVER_EN_ROUTE → IN_TRIP → COMPLETED → PAID`.  
Each state transition is an event on Kafka. Downstream services (payment, analytics) consume events independently.  
If payment fails: retry with exponential backoff; compensating transaction refunds if needed.  
→ See `patterns/multi_step_processes.md`

### 5. PostgreSQL for trip records
Trips require ACID: payment charge must match trip record atomically.  
Rider/driver history queries need joins (trips ↔ users ↔ routes).  
Shard by `city_id` or `rider_id` once single-node capacity is exceeded.  
→ See `concepts/transactions_and_acid.md`

### 6. Circuit breaker around payment service
Payment is a third-party call (Stripe/Braintree). Wrap it with a circuit breaker:
- If the payment service returns errors > threshold, open the circuit.
- Queue the charge for retry rather than blocking the trip-completion flow.  
→ See `patterns/circuit_breaker_and_bulkhead.md`

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| WebSocket connections (500K concurrent) | Stateless WS gateway + Kafka for fan-out; scale horizontally |
| Location update write volume | Redis cluster; batch writes; reduce frequency for idle drivers |
| Matching latency | Pre-filter by geohash cell; limit candidate set before ranking |
| Hot cities (NYC rush hour) | Regional sharding; city-level Redis clusters |
| Payment service downtime | Circuit breaker + async retry queue |

---

## Interview Tips

- Key insight: location data is **write-heavy, read-fast, and stale-tolerant** → Redis GeoHash, not a SQL table.
- Discuss the matching algorithm briefly: proximity, driver rating, estimated arrival time.
- The distributed lock is the hardest correctness problem — the interviewer will likely probe it.
- Surge pricing: a separate service that reads trip demand/supply ratio and publishes a multiplier — hangs off the same Kafka topics.
