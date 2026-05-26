# Batch vs Real-Time Feature Computation

How and when features are computed determines freshness, latency, and cost. Most production ML systems use a combination.

---

## Batch Features

Computed on a schedule over historical data. Results stored in a DB or feature store for fast lookup at serving time.

```
[Scheduled job] → query data warehouse → compute features → write to feature store (offline + online)
[Serving time] → read features from online store (fast lookup)
```

**Characteristics:**
- Computed hours or days before serving.
- Can be expensive to compute (complex aggregations, large datasets) — run offline.
- No latency at serving time: just a DB read.
- Stale by design — freshness = how often the job runs.

**Examples:**
- User's total purchase count (last 30 days)
- Seller average rating
- Item popularity score
- User preference embeddings

---

## Real-Time (On-Request) Features

Computed at serving time, using the current request as input.

```
[Request arrives] → compute features on the fly → model inference → response
```

**Characteristics:**
- Always fresh — uses current context.
- Adds latency to the serving path.
- Limited in complexity — must complete in < 10–50ms.
- Can use information only available at request time.

**Examples:**
- Time of day, day of week
- Query text (user just typed this)
- Current page context
- Device type, location

---

## Near-Real-Time (Streaming) Features

Computed continuously from an event stream. Results written to the online feature store as events arrive.

```
[Events → Kafka] → [Stream Processor (Flink)] → [Online Feature Store (Redis)]
[Serving time] → read from online store (milliseconds)
```

**Characteristics:**
- Fresh within seconds/minutes of events occurring.
- More complex to build and operate than batch.
- Needed when batch freshness is insufficient.

**Examples:**
- Failed login attempts in the last 5 minutes (fraud)
- Number of items a user viewed in the current session
- Real-time inventory count

---

## Summary

| | Batch | Real-Time | Streaming |
|---|---|---|---|
| Freshness | Hours/days | Instant | Seconds/minutes |
| Serving latency | ~1ms (lookup) | Adds to latency | ~1ms (lookup) |
| Compute cost | Run once, amortized | Per-request | Continuous |
| Complexity | Low | Low | High |
| Use for | Historical patterns | Request context | Recent behavior |

---

## The Typical Production System

Most systems use all three layers:

```
Request → [Real-time features: query, context, time]
        + [Streaming features: recent activity, live counts]
        + [Batch features: historical aggregations, embeddings]
        → Concatenate → Model → Prediction
```

The feature store (offline + online stores) is the infrastructure that makes this composable.

---

## Decision Guide

| Question | Answer |
|---|---|
| Is the feature available at request time only? | Real-time |
| Is freshness within hours acceptable? | Batch |
| Is freshness within minutes required? | Streaming |
| Is the computation expensive (hours to run)? | Batch |
| Does it need request-level context? | Real-time |
