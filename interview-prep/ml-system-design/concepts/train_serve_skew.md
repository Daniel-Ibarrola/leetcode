# Train/Serve Skew

When the features (or data distribution) seen during training differ from what the model receives at serving time. One of the most common causes of model underperformance in production.

---

## Why It Happens

### Feature Computation Mismatch
Training uses a Python script to compute features. Serving uses a Java service. Small differences in logic (rounding, null handling, timezone) cause feature values to diverge.

### Stale Features at Serving Time
Training uses up-to-date historical data. Serving reads from a cache that's 6 hours old.

### Missing Features
A feature is available at training time but unavailable or null at serving time (e.g., derived from a system that doesn't exist in prod yet).

### Data Leakage (Reverse Skew)
Training accidentally uses information from the future (label or target leaked into features). Model looks great offline, performs poorly online.

### Schema Change
A feature value that was `int` in training is now `float` at serving time, or a categorical value has new unseen categories.

---

## Consequences

- Model performs well in offline evaluation but poorly in production.
- Debugging is hard — the model itself isn't broken, the inputs are.
- Degrades silently: metrics drift slowly rather than crashing loudly.

---

## How to Detect It

### Log Training and Serving Features
Log feature values at serving time. Compare distributions to training data:
- Mean, std, percentiles
- Missing value rate
- Category distribution

### Training-Serving Feature Comparison
Before deploying, run the model on a sample of live traffic using the serving feature pipeline. Compare predictions to offline eval — if they diverge significantly, there's skew.

### Shadow Mode
Run the new model on live traffic without serving its predictions. Compare features and outputs against the current model.

---

## How to Prevent It

| Technique | How It Helps |
|---|---|
| **Feature Store** | Single feature computation logic, shared between training and serving |
| **Point-in-time correct training data** | Training features reflect what was available at prediction time |
| **Schema validation** | Enforce types, ranges, allowed values at serving time |
| **Integration tests** | Test the full serving pipeline end-to-end before deployment |
| **Feature logging** | Log served features; replay them in training |

---

## The Root Cause Pattern

Skew almost always comes down to: **two different code paths computing the same thing**.

The fix is always the same: **one code path**. The feature store enforces this by design.

---

## Quick Checks Before Deployment

- Does the serving pipeline use the same feature logic as training?
- Are all features available at serving time? What happens if one is null?
- Does the training dataset use point-in-time correct feature values?
- Have you compared feature distributions: training vs. a live sample?
