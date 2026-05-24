# Message Queues

## What is it?
A message queue is a buffer that holds messages between a producer (sender) and a consumer (receiver). The producer puts a message in the queue; the consumer picks it up and processes it — asynchronously and independently. Examples: RabbitMQ, Amazon SQS, ActiveMQ.

## How it works
1. Producer sends a message to the queue
2. Queue stores the message (durably, if configured)
3. Consumer polls or receives the message
4. Consumer acknowledges processing; queue removes the message

## Key concepts
- **Producer** — the service that sends messages
- **Consumer** — the service that processes messages
- **Acknowledgment (ack)** — consumer signals successful processing; queue deletes the message
- **Dead Letter Queue (DLQ)** — where failed/unprocessable messages go for inspection
- **At-least-once delivery** — message may be delivered more than once (consumers must be idempotent)
- **At-most-once delivery** — message delivered once but may be lost if consumer crashes
- **Exactly-once** — hardest to achieve; requires special coordination

## Trade-offs

| Pro | Con |
|-----|-----|
| Decouples producer from consumer (they don't need to be up simultaneously) | Adds latency — processing is async, not instant |
| Absorbs traffic spikes (queue acts as a buffer) | Operational complexity (another system to manage) |
| Easy to scale consumers independently | Ordering guarantees are hard (unless you use partitioned queues) |
| Built-in retry and DLQ for failed messages | Debugging async flows is harder than synchronous calls |

## Message Queues vs Pub/Sub
- **Queue**: one message → one consumer (point-to-point)
- **Pub/Sub**: one message → many consumers (broadcast)

## When to use
- Background jobs (sending emails, processing images, generating reports)
- Decoupling microservices so one failure doesn't cascade
- Rate-limiting work (consumers process at their own pace)
- Ensuring work isn't lost if a downstream service is temporarily down
