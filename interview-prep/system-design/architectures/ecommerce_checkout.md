# Architecture: E-commerce Checkout & Order Management

**Scale target:** 50K orders/sec during peak (Black Friday), global users, inventory across 10M SKUs

---

## Problem

Design the checkout and order management system for a large e-commerce platform. A user adds items to a cart, places an order, inventory is reserved, payment is charged, and fulfillment begins.

---

## Architecture Diagram

```
                         ┌───────────────────────────────────────┐
                         │          CHECKOUT FLOW                │
                         └───────────────────────────────────────┘

User
 │
 ▼
API Gateway (auth, rate limit)
 │
 ├──► Cart Service ──────────────────────► Redis (cart:{user_id})
 │                                         (TTL = 30 days)
 │
 ├──► Inventory Service (check stock) ──► Redis (inventory:{sku_id} = count)
 │       │                               (write-through to DB)
 │       │ if in stock: reserve
 │       ▼
 │    Distributed Lock (Redis SETNX)     ← prevents overselling
 │    lock:sku:{sku_id}
 │
 └──► Checkout Service ──────────────────► PostgreSQL: INSERT order (status=PENDING)
          │                                             INSERT order_items
          │
          ▼
     Kafka (order-created topic)
          │
          ├──► Payment Worker ──────────► Payment Gateway (Stripe)
          │         │                          │
          │         │ success                  │ failure
          │         ▼                          ▼
          │    UPDATE order status=PAID    retry / DLQ
          │         │
          │         ▼
          │    Kafka (payment-confirmed topic)
          │
          ├──► Fulfillment Service ──────► Warehouse System (3PL API)
          │
          ├──► Notification Service ──────► Email / Push (order confirmation)
          │
          └──► Inventory Service ──────────► Decrement DB inventory permanently

                         ┌───────────────────────────────────────┐
                         │         ORDER STATUS POLLING          │
                         └───────────────────────────────────────┘

User polls: GET /orders/{id}/status
    │
    ▼
Order Service ──► Redis (order-status:{id}) ──► return status
                       │ (cache miss)
                       ▼
                  PostgreSQL (read replica)
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| API Gateway + Rate Limiter | API Gateway, Rate Limiter | `building_blocks/api_gateway.md`, `building_blocks/rate_limiter.md` |
| Redis (cart, inventory) | Caches | `building_blocks/caches.md` |
| Distributed lock (prevent overselling) | Distributed Locking | `patterns/distributed_locking.md` |
| PostgreSQL (orders) | Relational Databases | `building_blocks/relational_databases.md` |
| ACID transactions | Transactions & ACID | `concepts/transactions_and_acid.md` |
| Kafka (order events) | Pub/Sub | `building_blocks/pub_sub.md` |
| Message Queue (payment jobs) | Message Queues | `building_blocks/message_queues.md` |
| Saga pattern (multi-step) | Multi-Step Processes | `patterns/multi_step_processes.md` |
| Payment as long-running task | Long-Running Tasks | `patterns/long_running_tasks.md` |
| Circuit breaker (payment GW) | Circuit Breaker & Bulkhead | `patterns/circuit_breaker_and_bulkhead.md` |
| Order status polling | Long-Running Tasks | `patterns/long_running_tasks.md` |
| Read replicas for order queries | Scaling Reads, Replication | `patterns/scaling_reads.md`, `concepts/replication.md` |

---

## Key Decisions

### 1. Distributed lock to prevent overselling
The critical race condition: two users simultaneously checking stock for the last unit.

```
SETNX lock:sku:{sku_id}  (expire: 500ms)
  → check inventory
  → decrement if available
  → release lock
```
Redis SETNX ensures only one reservation proceeds at a time.  
Alternative: optimistic locking with a version number in the DB (`UPDATE inventory SET count = count - 1 WHERE sku_id = ? AND count > 0`).  
→ See `patterns/distributed_locking.md`

### 2. Checkout as a Saga (choreography)
The checkout spans multiple services — payment, inventory, fulfillment — each independently owned.  
Use **choreography-based Saga**: each service listens for an event and publishes the next:
```
order-created → payment-worker → payment-confirmed → fulfillment-service → order-shipped
```
Each step has a **compensating transaction** on failure:
- Payment fails → release inventory reservation → cancel order
- Fulfillment fails → initiate refund

→ See `patterns/multi_step_processes.md`

### 3. Outbox pattern for reliable event publishing
To avoid losing the Kafka message if the server crashes after DB write but before publish:
```sql
BEGIN;
INSERT INTO orders ...;
INSERT INTO outbox (event_type, payload) VALUES ('order-created', {...});
COMMIT;
-- Background process reads outbox and publishes to Kafka, then deletes
```
This makes the DB write and event publish atomic.

### 4. Redis for cart and inventory cache
- **Cart**: `HSET cart:{user_id} {sku_id} {qty}` — expires after 30 days of inactivity.
- **Inventory**: write-through cache; increment/decrement in Redis and DB together.  
  Redis handles peak read load; DB is the source of truth.

### 5. ACID for the order record
The order INSERT must be atomic: order + line items together, or neither.  
PostgreSQL transaction ensures this. No distributed transaction needed here — everything is within one DB.  
For cross-service consistency, Saga + compensating transactions replace 2PC.  
→ See `concepts/transactions_and_acid.md`

### 6. Status polling for the user
After placing an order, the user polls `GET /orders/{id}/status`.  
Status is cached in Redis (updated by each Saga step).  
Cache TTL is short (~5 seconds) to reflect rapid state transitions during checkout.  
→ See `patterns/long_running_tasks.md`

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| Inventory lock contention (hot SKUs) | Shard inventory lock by SKU; pre-allocate inventory "buckets" for flash sales |
| Order write throughput | Shard PostgreSQL by `user_id` hash; use write-ahead log batching |
| Payment worker failures | Dead-letter queue; idempotent retries using `order_id` as idempotency key |
| Black Friday peak (50K orders/sec) | Queue checkout requests; smooth traffic via rate limiting at API Gateway |
| Fulfillment 3PL API slowness | Circuit breaker; async fulfillment via queue; don't block order confirmation on it |

---

## Interview Tips

- The overselling problem is the core challenge — explain optimistic vs. pessimistic locking.
- Saga vs. 2PC: always argue for Saga in microservices — 2PC has availability and latency costs.
- Mention idempotency keys on payment: retrying a charge must not double-charge.
- Flash sale variant: pre-allocate inventory to regional "buckets" to reduce lock contention.
