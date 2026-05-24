# Real-Time Updates

Getting data to clients as soon as it changes, without them having to ask.

## Approaches

### 1. Short Polling
Client sends a request on a timer (e.g., every 5 seconds): "Any updates?"
- Simplest to implement
- Wasteful: most responses are empty
- High load on server at scale
- Good for: low-frequency updates, simple dashboards

### 2. Long Polling
Client sends a request; server holds it open until there's something to send (or it times out). Client immediately reconnects after receiving a response.
- Better than short polling: fewer empty responses
- Still HTTP overhead per "message"
- Connection management complexity on server
- Good for: moderate-frequency updates, simpler infra requirements

### 3. Server-Sent Events (SSE)
Client opens one HTTP connection; server streams events down it indefinitely.
- Simple: native browser support, standard HTTP
- Server → client only (unidirectional)
- Works over HTTP/2 (many streams per connection)
- Good for: live feeds, notifications, dashboards

### 4. WebSockets
Full-duplex persistent TCP connection. Both sides can send at any time.
- Lowest latency, most flexible
- Requires sticky sessions or a pub/sub broker when scaling horizontally
- More complex connection lifecycle
- Good for: chat, multiplayer games, collaborative editing, trading UIs

### 5. Pub/Sub + Push
Backend publishes events to a broker (Redis Pub/Sub, Kafka, Pusher). A gateway layer pushes to connected clients.
- Decouples event producers from clients
- Scales to many connections
- Adds broker as a component to manage
- Used by: Firebase Realtime DB, Pusher, Ably

## Comparison

| | Short Poll | Long Poll | SSE | WebSocket |
|---|---|---|---|---|
| Direction | Client pulls | Client pulls | Server pushes | Bidirectional |
| Connection | New each time | Held open | Persistent | Persistent |
| Overhead | High | Medium | Low | Low |
| Browser support | Always | Always | Native | Native |
| Complexity | Very low | Low | Low | Medium |
| Use case | Simple status | Notifications | Feeds, alerts | Chat, gaming |

## Scaling Considerations

- WebSockets maintain stateful connections → you need a way to route messages to the right server instance.
- Solution: all instances subscribe to a shared pub/sub channel (Redis, Kafka). When a message arrives, the right server pushes it to the connected client.
- SSE is easier to scale because it is one-directional; load balancers handle it like any HTTP connection.

## Decision Guide

1. Server → client only? → SSE (simple, scalable)
2. Need bidirectional? → WebSocket
3. Very simple, low frequency? → Long polling is fine
4. Real-time collaborative? → WebSocket + pub/sub broker
