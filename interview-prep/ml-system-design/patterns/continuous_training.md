# Continuous Training & Retraining Triggers

Models degrade over time as the world changes. Continuous training keeps models fresh by automating the retrain → evaluate → deploy cycle.

---

## Why Retrain?

- New data reveals patterns the model hasn't seen.
- Data drift: input distribution has shifted.
- Concept drift: the relationship between inputs and labels has changed.
- Business change: new products, features, user segments.

---

## Retraining Triggers

### Scheduled
Retrain on a fixed cadence (daily, weekly, monthly).
- Predictable, easy to operate.
- May retrain unnecessarily, or not quickly enough when drift happens.
- Good starting point for most systems.

### Performance-Based
Retrain when model metrics drop below a threshold.
- Requires labeled feedback (can be delayed — e.g., fraud confirmed 3 days later).
- More reactive than scheduled, but labels must be available.

### Drift-Based
Retrain when a drift detector signals significant distribution shift in inputs or predictions.
- Doesn't require labels — reacts to feature distribution changes.
- Risk of false alarms triggering unnecessary retraining.

### Data Volume-Based
Retrain when N new labeled examples have accumulated.
- Ensures the model always benefits from a meaningful data increment.
- Predictable cost per training run.

---

## Automated Retraining Pipeline

```
[Trigger fires]
    → Pull fresh training data
    → Run training pipeline
    → Evaluate vs production model
    → If better: register + deploy to staging
    → Automated tests pass → promote to production
    → If worse: alert, investigate
```

The "if better" gate is critical — automated retraining without quality gates can silently deploy degraded models.

---

## Evaluation Gate

Before any automated deployment, the new model must beat the current production model on:
- Held-out test set (static, doesn't change between runs)
- Recent data slice (last N days — validates on current distribution)
- Business metric proxy (CTR, conversion, precision@k)

---

## Continual / Online Learning

Some systems update the model incrementally as each new data point arrives.
- Very low latency to new patterns.
- Risk of catastrophic forgetting (model overwrites old knowledge).
- Risk of poisoning (adversarial inputs rapidly degrade the model).
- Used in: ads CTR models, fraud detection, some recommendation systems.
- Requires careful safeguards: learning rate clipping, anomaly detection on updates, shadow comparison.

---

## Data Strategy for Retraining

| Strategy | Description | When to Use |
|---|---|---|
| Full retrain | Use all historical data | Label distribution is stable |
| Rolling window | Use only the last N days/weeks | Concept drift — old data misleads |
| Weighted recent | All data, but recent examples weighted higher | Gradual drift |
| Fine-tuning | Start from current model, train on new data only | Stable base, incremental updates |

---

## Trade-offs

| Frequent retraining | Fresh model | Higher compute cost, more deployment risk |
| Infrequent retraining | Stable, cheaper | Slower adaptation to drift |
| Full retrain | Stable | Expensive; old data may be redundant |
| Rolling window | Fast adaptation | Loses long-term signal |
| Automated deployment | Fast | Risk of bad model auto-deploying |
| Manual gate | Safe | Slow at high retrain frequency |
