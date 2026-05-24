# Multi-Step Processes

When a workflow requires multiple sequential (or parallel) steps — each potentially involving different services — you need a coordination strategy.

Examples: e-commerce checkout (validate cart → charge payment → reserve inventory → send confirmation), user onboarding, data pipelines.

---

## The Core Problem

Steps span multiple services. If step 3 fails after steps 1 and 2 succeeded, you have partial state. You need a way to either:
- **Roll back** the previous steps (compensating transactions), or
- **Retry forward** until the whole workflow completes.

---

## Approach 1: Choreography (Event-Driven)

Each service does its step and publishes an event. The next service listens for that event and triggers its step.

```
OrderService → [OrderCreated] → PaymentService
PaymentService → [PaymentCharged] → InventoryService
InventoryService → [InventoryReserved] → NotificationService
```

- No central coordinator
- Loosely coupled; easy to add steps by subscribing a new service
- Hard to see the whole workflow at a glance
- Debugging failures across services is complex
- Good for: simple linear flows, high decoupling requirements

---

## Approach 2: Orchestration (Saga / Workflow Engine)

A central orchestrator tells each service what to do and tracks state.

```
WorkflowEngine:
  1. Call PaymentService.charge()
  2. If success → call InventoryService.reserve()
  3. If success → call NotificationService.send()
  4. If step 2 fails → call PaymentService.refund()  ← compensating transaction
```

- Single source of truth for workflow state
- Easier to monitor, debug, and retry
- Central orchestrator can become a bottleneck or single point of failure
- Good for: complex flows, compensation logic, long-running processes

Tools: AWS Step Functions, Temporal, Conductor, Airflow (data pipelines).

---

## Saga Pattern

A saga is a sequence of local transactions, each publishing an event that triggers the next. If a step fails, **compensating transactions** undo previous steps.

| Step | Action | Compensation |
|---|---|---|
| 1 | Charge payment | Refund payment |
| 2 | Reserve inventory | Release inventory |
| 3 | Send email | (none — can't unsend) |

Key insight: compensating transactions must be **idempotent** and always succeed.

---

## Handling Failures

### Retry with exponential backoff
For transient failures (network blip). Always set a max retry count.

### Dead-letter queue (DLQ)
Jobs that exhaust retries go here for manual investigation.

### Idempotency keys
If a step is retried, it shouldn't create duplicate side effects. Pass a unique key per workflow step; downstream services deduplicate by key.

### Outbox Pattern
Before publishing an event, write it to an "outbox" table in the same DB transaction as the state change. A separate process reliably publishes outbox events. Prevents the "wrote to DB but failed to publish event" split-brain problem.

---

## Trade-offs

| Approach | Visibility | Coupling | Failure Handling | Complexity |
|---|---|---|---|---|
| Choreography | Low (distributed) | Low | Hard to trace | Low |
| Orchestration | High (central) | Higher | Easy to trace | Medium-High |

---

## Decision Guide

- Simple 2–3 step flow with independent services? → Choreography.
- Complex branching logic, compensation required, or you need observability? → Orchestration.
- Long-running (minutes to days)? → Dedicated workflow engine (Temporal, Step Functions).
- All steps in one codebase? → Just use a DB transaction.
