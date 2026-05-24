# Managing Long-Running Tasks

A task that takes more than a few seconds (video transcoding, report generation, ML inference, data exports) can't be handled synchronously in an HTTP request. The connection would time out and the client would be left hanging.

## Core Pattern: Async Job Queue

1. Client submits a request → API immediately returns a **job ID**.
2. Job is placed on a queue (SQS, Celery, BullMQ, Kafka).
3. Worker picks up the job and processes it.
4. Worker writes the result to storage or DB and marks job as complete.
5. Client polls for status, or gets notified via webhook / push notification.

---

## Components

| Component | Role |
|---|---|
| API layer | Accepts request, enqueues job, returns job ID |
| Queue | Buffers jobs; decouples producers from workers |
| Workers | Execute the job; stateless and horizontally scalable |
| Job store | Tracks job status (pending, running, done, failed) |
| Result store | Holds output (S3, DB, cache) |
| Notification | Tells client when done (webhook, SSE, polling) |

---

## Status Polling

Client hits `GET /jobs/{id}` periodically:
```
{ "id": "abc123", "status": "running", "progress": 42 }
```
Simple, no persistent connection needed. Add exponential backoff to avoid hammering the API.

---

## Webhook / Push Notification

When job completes, system calls a URL the client provided, or pushes via WebSocket/SSE.
- Better UX (no polling delay)
- Client must expose a callback URL (works for server-to-server, harder for browser clients)

---

## Retries and Idempotency

- Workers will crash. Jobs must be **retried safely** → make workers idempotent (running a job twice produces the same result).
- Use a **dead-letter queue (DLQ)** for jobs that fail repeatedly — investigate separately.
- Record which jobs have already been processed to avoid double-processing.

---

## Progress Reporting

For jobs with stages, write intermediate progress to the job store. Client polls and shows a progress bar.
- Keep updates lightweight (just a percentage or stage name)
- Don't write progress on every loop iteration — throttle to every N% or every N seconds

---

## Trade-offs

| Decision | Pro | Con |
|---|---|---|
| Async queue | Decouples, scales, absorbs spikes | Client needs to poll or be notified |
| Polling for status | Simple, stateless | Wastes requests; adds latency to notification |
| Webhook callback | Instant notification | Client must handle incoming requests |
| Multiple workers | Parallel throughput | Need idempotent job design |
| DLQ for failures | Prevents silent data loss | Ops overhead to monitor and reprocess |

---

## Common Pitfalls

- **Timeout on the enqueue call**: if the queue is slow, the initial API call may time out. Use fire-and-forget with a fast queue.
- **No idempotency**: a retry causes a duplicate side effect (e.g., double charge, double email).
- **Lost jobs**: if a worker crashes mid-job and the message was already ACKed, the job is gone. Don't ACK until the work is done.
- **No visibility**: without a job status store, clients have no way to check progress or debug failures.
