# Pub/Sub (Publish-Subscribe)

## What is it?
A messaging pattern where publishers send messages to a topic, and all subscribers to that topic receive a copy. Unlike a message queue (one-to-one), Pub/Sub is one-to-many broadcast. Examples: Google Pub/Sub, Apache Kafka, AWS SNS, Redis Pub/Sub.

## How it works
1. Publisher sends a message to a **topic**
2. The Pub/Sub system fans the message out
3. Every **subscriber** to that topic receives a copy of the message
4. Subscribers process independently — one slow subscriber doesn't block others

## Key concepts
- **Topic** — a named channel for a category of events (e.g., `user.signup`, `order.placed`)
- **Publisher** — service that emits events
- **Subscriber** — service that listens to a topic and reacts to events
- **Consumer group** (Kafka) — multiple instances share a topic's messages; each message goes to only one instance in the group (useful for scaling consumers while still broadcasting to other groups)
- **Retention** — Kafka retains messages for a configurable time, so subscribers can replay history

## Pub/Sub vs Message Queue

| | Message Queue | Pub/Sub |
|---|---|---|
| Delivery | One consumer gets each message | All subscribers get each message |
| Use case | Work distribution | Event broadcasting |
| Examples | RabbitMQ, SQS | Kafka, SNS, Google Pub/Sub |

Note: Kafka blurs this line — it supports both patterns depending on how consumer groups are configured.

## Trade-offs

| Pro | Con |
|-----|-----|
| Decouples services — publishers don't know about subscribers | Harder to guarantee ordering across topics |
| Easy to add new subscribers without changing publisher | At-least-once delivery requires idempotent consumers |
| Scales fan-out naturally | More complex than direct API calls |
| Event replay possible (Kafka) | Message filtering/routing can get complicated |

## When to use
- Event-driven architectures where multiple services react to the same event
- Audit logs, analytics pipelines, real-time notifications
- Microservices communication where you want loose coupling
- When you need to fan out one event to many downstream consumers (e.g., "order placed" → notify inventory, billing, email service)
