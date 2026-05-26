# Prediction Caching

Cache model outputs to avoid redundant inference. Reduces latency and cost for repeated or similar requests.

---

## Why It Matters

ML inference is expensive:
- A large LLM call costs $0.01–0.10 per request.
- A complex ranking model may take 50–200ms.
- Under load, inference can become the bottleneck.

Many predictions are identical or near-identical — caching reuses prior work.

---

## Exact Cache

Store the result for an exact input key.

```
cache_key = hash(input_features)
if cache_key in cache:
    return cache[cache_key]
else:
    prediction = model.predict(input)
    cache[cache_key] = prediction
    return prediction
```

- Works when the same exact input repeats.
- High hit rate for: search queries (many users search the same thing), batch scoring, product recommendations with shared user segments.
- Low hit rate for: highly personalized predictions with unique feature combinations.

---

## Semantic Cache (Approximate Cache)

For LLMs and embedding-based systems: if a new query is semantically similar to a cached query, return the cached answer.

```
embed(new_query) → ANN search in cache → if similarity > threshold → return cached response
```

- Handles paraphrases and near-duplicate queries.
- Hit rate much higher than exact matching for text inputs.
- Risk: threshold too low → return wrong answer for a superficially similar but semantically different question.

Tools: GPTCache, Momento Semantic Cache.

---

## Offline Pre-Computation (Batch Cache)

For predictable requests, pre-compute predictions in a batch job and store them.

```
[Nightly job] → score all active users × top-1000 items → write to Redis
[Serving time] → read pre-computed prediction (no model call)
```

- Zero inference latency at serving time.
- Only works if you can enumerate inputs in advance.
- Predictions are stale between runs.
- Good for: homepage recommendations, email ranking, daily dashboards.

---

## What to Cache

| Good to cache | Not good to cache |
|---|---|
| Popular search queries | Highly personalized, unique inputs |
| Product/item scores (stable) | Real-time fraud detection (must be fresh) |
| Embedding lookups (slow to recompute) | Predictions with short TTL |
| LLM responses to FAQ-style questions | Stateful conversations |

---

## TTL Strategy

Cache freshness must match acceptable staleness:
- Product price predictions: TTL = 1 hour (prices change).
- User preference embeddings: TTL = 24 hours (preferences stable).
- Search result ranking: TTL = 15 minutes (content changes slowly).
- Fraud score: TTL = 0 (must always be fresh).

---

## Cache Invalidation for ML

- **Event-driven**: invalidate when the underlying data changes (product updated → evict product recommendation cache).
- **TTL-based**: let the cache expire on a schedule.
- **Model change**: when a new model is deployed, flush the entire cache (old predictions are from the old model).

---

## Trade-offs

| Exact cache | Simple, zero false positives | Low hit rate for unique inputs |
| Semantic cache | High hit rate for text | Risk of false positives; adds lookup latency |
| Batch pre-computation | Zero serving latency | Stale; can't handle all inputs |
| No caching | Always fresh | High inference cost, higher latency |
