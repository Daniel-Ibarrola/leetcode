# Data & Model Drift

Models degrade over time because the world changes. Drift is the umbrella term for this degradation.

---

## Types of Drift

### Data Drift (Feature Drift / Covariate Shift)
The distribution of input features changes, but the relationship between features and labels stays the same.

Example: user age distribution shifts as your product grows. Model still "works" but predictions become less calibrated.

### Concept Drift
The relationship between inputs and labels changes.

Example: "free shipping" used to predict high conversion. Now everyone offers it — it no longer predicts anything.

This is the hardest to handle because the label definition itself has changed.

### Label Drift
The distribution of labels (targets) changes.

Example: fraud rate increases from 0.1% to 1%. A model trained on the old distribution now misclassifies more fraud as legitimate.

### Prediction Drift
Model output distribution shifts — model starts predicting more positives, or scores cluster near 0/1.

A useful proxy metric when ground-truth labels aren't available immediately.

---

## Detecting Drift

### Statistical Tests
Compare current feature distribution against the training baseline:
- **KS test** (Kolmogorov-Smirnov) — for continuous features
- **Chi-squared test** — for categorical features
- **PSI** (Population Stability Index) — common in finance/credit models; PSI > 0.2 = significant drift

### Monitoring Metrics
- Feature mean, std, nulls, out-of-range values — compare to training baseline.
- Prediction score distribution — watch for shifts.
- Business KPIs — click-through rate, conversion, accuracy (if labels available).

### Label Feedback Loop
If ground truth arrives with a delay (e.g., fraud confirmed 3 days after transaction), measure model accuracy on the labeled subset continuously.

---

## Responding to Drift

| Drift Severity | Response |
|---|---|
| Minor (PSI 0.1–0.2) | Alert, investigate, monitor more closely |
| Moderate (PSI > 0.2) | Retrain on recent data |
| Severe (PSI > 0.25, accuracy tanking) | Emergency retrain + rollback to rule-based fallback |
| Concept drift confirmed | Rethink features and model design, not just retrain |

---

## Retraining Strategies

| Strategy | How | When |
|---|---|---|
| Scheduled retraining | Retrain every N days regardless | Drift is predictable and gradual |
| Triggered retraining | Retrain when drift metric exceeds threshold | Drift is unpredictable |
| Continuous learning | Model updates incrementally as new data arrives | High data velocity, stateless models |
| Rolling window | Train on only the most recent N days | Concept drift — old data is misleading |

---

## Trade-offs

| Aggressive retraining | Catches drift faster | More compute cost, more deployment risk |
| Conservative retraining | Stable, lower cost | Slower to adapt to drift |
| Rolling window training | Adapts to concept drift | May lose useful historical signal |
| Full history training | Stable, high data volume | Slow to adapt when distribution shifts |

---

## Monitoring Stack

```
[Serving logs] → [Feature stats aggregator] → [Drift detector] → [Alert / trigger retrain]
```

Tools: Evidently AI, WhyLogs, Arize, Fiddler, SageMaker Model Monitor, Vertex Model Monitoring.
