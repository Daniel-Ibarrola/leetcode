# Data Flywheel & Feedback Loops

A data flywheel is a self-reinforcing cycle: better model → better user experience → more users → more data → better model. Understanding feedback loops — both virtuous and vicious — is essential for ML system design.

---

## The Virtuous Cycle

```
More users
    → More interactions (clicks, purchases, ratings)
    → More labeled training data
    → Better model
    → Better recommendations / predictions
    → Better user experience
    → More users  ← loop
```

This is how companies like Netflix, Spotify, and Google compound their ML advantage over time. The data moat widens with scale.

---

## Feedback Collection Patterns

### Explicit Feedback
User directly expresses preference.
- Star ratings, thumbs up/down, explicit "not interested."
- High signal, low volume — users rarely give explicit feedback.

### Implicit Feedback
Inferred from user behavior.
- Clicks, dwell time, purchases, shares, scrolls past.
- High volume, noisy — a click doesn't always mean satisfaction.
- Most practical source for large-scale recommendation systems.

### Delayed Labels
Ground truth arrives after the prediction.
- Fraud: confirmed days/weeks after the transaction.
- Churn: confirmed weeks after the prediction.
- Conversion: confirmed hours after the recommendation.
- Must design pipelines to join predictions with labels when they arrive.

---

## Label Joining Pipeline

```
[Prediction served] → log (request_id, user_id, item_id, timestamp, prediction)
[User action occurs] → log (request_id, action, timestamp)
[Label joiner job] → join on request_id within time window → labeled training example
```

The time window for joining must match the label delay (e.g., join up to 7 days later for fraud).

---

## Negative Feedback & Closed-Loop Problems

### Exposure Bias
The model only learns from items it recommended. Items never shown never get feedback → model doesn't know if they'd be liked.

Fix: **exploration** — occasionally surface non-top recommendations to gather signal on unexplored items (epsilon-greedy, Thompson sampling).

### Popularity Bias
Popular items get more clicks → more training signal → model recommends them more → they get even more popular. Niche items starve.

Fix: **debias training data** by weighting items by inverse popularity, or explicitly evaluate coverage metrics.

### Feedback Delay Skew
Model trained on recent data is evaluated on past predictions but deployed on future inputs. If user behavior changes seasonally, the training window matters.

### Self-Fulfilling Prophecy
A model that ranks item A first → everyone clicks A → model thinks A is great → ranks A first. The model has no counterfactual: what if B had been shown instead?

Fix: holdback experiments (don't show recommendations to a holdback group), counterfactual evaluation.

---

## Designing the Feedback Loop

| Decision | Option A | Option B |
|---|---|---|
| Feedback signal | Implicit (clicks) → high volume, noisy | Explicit (ratings) → low volume, clean |
| Label delay | Short delay → label sooner, less complete | Long delay → more complete, slower training |
| Exploration | No exploration → pure exploitation, exposure bias | Exploration → better coverage, lower short-term metric |
| Training cadence | Frequent retraining → adapts to new behavior | Infrequent → stable, cheaper |

---

## Monitoring Feedback Loops

Watch for:
- **Declining diversity**: recommendation coverage shrinks over time → popularity bias.
- **Metric inflation without business value**: clicks go up but engagement goes down (clickbait loop).
- **Label rate drift**: if users click less (behavior shift), your positive label rate changes.

---

## Interview Application

When asked to design a recommendation or ranking system, always address:
1. How do you collect feedback?
2. How do you join predictions with delayed labels?
3. How do you handle exploration vs. exploitation?
4. What prevents the model from collapsing to recommending only popular items?
