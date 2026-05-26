# Model A/B Testing & Safe Deployment

Rolling out a new model safely. ML deployments are riskier than regular code deployments — a bad model can cause silent, hard-to-detect harm.

---

## Deployment Strategies

### Shadow Mode
The new model runs alongside the current model but its predictions are **never shown to users**. Both models see the same requests. Results are logged and compared offline.

```
Request → [Production model] → user sees this response
       → [Shadow model]     → prediction logged, never served
```

- Zero risk to users.
- Validates prediction distribution, feature pipeline, latency.
- Can't measure real user impact (users never saw shadow predictions).
- **Use first**, before any live traffic exposure.

### Canary Deployment
Route a small percentage (1–5%) of live traffic to the new model.

```
100 requests → 95 → [Production model]
            →  5 → [New model]
```

- Real user impact measured on a small cohort.
- If metrics degrade, roll back with minimal exposure.
- Gradually increase traffic as confidence grows.

### A/B Test
Randomly assign users to control (current model) or treatment (new model) groups. Run for a fixed period.

```
User group A → [Model v1]  ← control
User group B → [Model v2]  ← treatment
```

- Measures real business impact (CTR, conversion, revenue) with statistical rigor.
- Requires sufficient sample size for statistical significance.
- Takes time — can't accelerate with more traffic if user-level assignment is required.
- The standard way to measure model value.

### Multi-Armed Bandit
Dynamically allocate more traffic to whichever model performs better, in real time.

- Faster than A/B test — less traffic wasted on the worse model.
- Less statistically rigorous — harder to isolate causation.
- Good for fast-moving environments where the "best" model changes.

---

## Rollback Plan

Always have one before deploying. Define:
- What metric triggers a rollback (and at what threshold).
- Who is on-call and how to execute the rollback.
- How long before auto-rollback kicks in if no human intervenes.

---

## Metrics to Monitor Post-Deployment

| Category | Metrics |
|---|---|
| Model health | Prediction distribution, confidence scores, null/error rate |
| System health | Latency (p50, p99), error rate, throughput |
| Business metrics | CTR, conversion, revenue, engagement |
| Fairness | Performance across demographic / segment slices |

---

## Recommended Rollout Sequence

```
1. Shadow mode (no user exposure, validate pipeline)
2. 1% canary (catch major regressions quickly)
3. 10% canary (confirm canary metrics stable)
4. Full A/B test (measure business impact with statistical rigor)
5. Full rollout (if A/B test wins)
```

---

## Trade-offs

| Shadow mode | Zero risk | Can't measure real impact |
| Canary | Low risk, real signal | Small sample may not catch subtle regressions |
| A/B test | Rigorous business measurement | Slow, requires discipline |
| Multi-armed bandit | Fast, adaptive | Weaker statistical guarantees |
| Full rollout immediately | Fast | High risk |
