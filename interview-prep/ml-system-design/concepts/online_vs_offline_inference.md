# Online vs Offline Inference

How and when predictions are generated. This is one of the first design decisions in any ML system.

---

## Offline Inference (Batch Prediction)

Run the model on a large dataset periodically. Store predictions in a DB. Serve from the DB at request time.

```
[Scheduled Job] → load model → run on all users → write predictions to DB
[User request]  → read prediction from DB (no model involved)
```

**Characteristics:**
- No latency from the model at serve time — it's just a DB read.
- Predictions may be stale (computed hours ago).
- Can use large, slow models — latency doesn't matter.
- Only practical if you can enumerate all inputs in advance.

**Good for:** recommendation emails, churn scores, weekly reports, pre-ranking candidates before real-time reranking.

---

## Online Inference (Real-Time Prediction)

Run the model on each request, in the request path.

```
[User request] → feature lookup → model inference → return prediction
```

**Characteristics:**
- Fresh prediction every time.
- Model latency is in the critical path — must be fast (< 100ms for user-facing).
- Can react to real-time context (current page, time of day, live inventory).
- Requires a model serving infrastructure.

**Good for:** fraud detection, search ranking, ad CTR prediction, chatbots, recommendations requiring real-time context.

---

## Near-Real-Time (Asynchronous)

Hybrid: predictions are triggered by events but computed asynchronously, not in the request path.

```
[Event: user viewed product] → queue → model computes prediction → stored
[Next request] → read pre-computed (but recent) prediction
```

Decouples freshness from request latency.

---

## Comparison

| | Offline | Online | Near-Real-Time |
|---|---|---|---|
| Prediction freshness | Hours/days old | Real-time | Minutes old |
| Serving latency | ~1ms (DB read) | Model latency | ~1ms (DB read) |
| Model size constraint | None | Must be fast | None |
| Can use request context | No | Yes | Partially |
| Complexity | Low | Medium | Medium |

---

## Decision Guide

1. **Must react to real-time context?** (current basket, live session) → Online
2. **Can you enumerate all inputs in advance?** (all users, all products) → consider Offline
3. **Model is too slow for real-time?** (large transformer) → Offline or Near-Real-Time
4. **Latency SLA < 100ms?** → Online with a small/optimized model, or Offline pre-compute
5. **High QPS with variable load?** → Offline + cache absorbs spikes; Online requires autoscaling

---

## Hybrid Pattern

Many systems combine both:
- **Offline**: pre-rank thousands of candidates per user.
- **Online**: re-rank the top-N candidates in real time using fresh context.

This constrains the online model's work to a manageable candidate set.
