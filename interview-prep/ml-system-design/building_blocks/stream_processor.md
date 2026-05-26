# Stream Processor

Computes features and aggregations continuously over event streams, enabling near-real-time ML features.

---

## Why It's Needed for ML

Many powerful features are time-windowed aggregates:
- "Number of failed login attempts in the last 5 minutes" (fraud detection)
- "Average click-through rate of a user in the last hour" (ads ranking)
- "Total spend by a user in the last 24 hours" (recommendation)

Computing these in batch (hourly/daily jobs) introduces too much lag. Stream processing computes them continuously as events arrive.

---

## Core Concepts

### Event Stream
An ordered, continuous sequence of events. Each event has a timestamp and payload.
Source: Kafka topic, Kinesis stream, Pub/Sub.

### Window Types

| Window | Description | Example |
|---|---|---|
| **Tumbling** | Fixed, non-overlapping intervals | Clicks per minute (resets every minute) |
| **Sliding** | Fixed size, moves forward | Clicks in the last 60 minutes, updated every 10 min |
| **Session** | Groups events by inactivity gap | All events in a user session |

### Watermarks
Events arrive out of order (network delays). A watermark tells the processor "all events up to time T have arrived — process the window."

### Stateful vs Stateless Processing
- **Stateless**: transform each event independently (filter, enrich, reformat)
- **Stateful**: maintain state across events (running counts, sums, joins across streams)

---

## Tools

| Tool | Notes |
|---|---|
| **Apache Flink** | Most powerful for stateful streaming; production ML feature pipelines |
| **Apache Spark Streaming** | Micro-batch; easier if team knows Spark |
| **Kafka Streams** | Lightweight, runs inside Kafka ecosystem; good for simpler use cases |
| **Google Dataflow** (GCP) | Managed Flink/Beam |
| **Amazon Kinesis Data Analytics** | Managed Flink on AWS |
| **Materialize** | SQL-native streaming; good for simpler aggregations |

---

## ML Feature Computation Pattern

```
[Events] → Kafka → [Stream Processor] → [Online Feature Store (Redis)]
                                                    ↓
                                           Model reads at serve time
```

1. User/system events flow into Kafka.
2. Stream processor computes windowed aggregates continuously.
3. Results written to the online feature store.
4. Model serving reads features from the online store (low latency).

---

## Lambda vs Kappa Architecture

### Lambda
- **Batch layer**: processes all historical data overnight for accuracy.
- **Speed layer**: stream processor handles recent data for low latency.
- **Serving layer**: merges both.
- Complex: two code paths to maintain.

### Kappa
- **Streaming only**: everything goes through the stream processor.
- Reprocess historical data by replaying the event log.
- Simpler: one code path.
- Preferred for new systems where the event log is complete.

---

## Trade-offs

| Pro | Con |
|---|---|
| Near-real-time features | Complex to build and operate |
| Handles late-arriving events (watermarks) | Stateful processors need careful fault tolerance |
| Enables features impossible in batch | Debugging streaming bugs is harder than batch |
| Replayable (if backed by Kafka) | Higher infrastructure cost than pure batch |
