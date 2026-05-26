# Experiment Tracker

Records every training run — hyperparameters, metrics, artifacts, code version — so you can compare experiments and reproduce results.

---

## What It Tracks

| Category | Examples |
|---|---|
| **Hyperparameters** | learning rate, batch size, epochs, model architecture |
| **Metrics** | train loss, val loss, accuracy, F1, AUC — per epoch |
| **Artifacts** | model weights, plots, confusion matrices |
| **Environment** | Python version, library versions, git commit hash |
| **Dataset** | dataset version, size, split ratios |
| **System** | GPU type, training duration, hardware utilization |

---

## Why It Matters

Without tracking:
- "What settings produced that good model from last month?" → gone.
- Can't reproduce results for a paper, audit, or debugging session.
- Comparing two model versions requires manual notes.

With tracking:
- Full history of every experiment.
- Compare runs side by side (metrics, params).
- Identify which hyperparameter changes actually helped.
- Reproduce any past result exactly.

---

## Core Concepts

### Run
A single training execution. Has a unique ID, timestamps, and all logged data.

### Experiment
A group of related runs (e.g., "all runs for the churn model").

### Artifact
Any file output from a run: model file, dataset, image, CSV.

---

## Tools

- **MLflow** — open source, self-hostable, integrates with most frameworks
- **Weights & Biases (W&B)** — managed, strong visualizations, popular in research/industry
- **Neptune.ai** — managed, good for large teams
- **Comet ML** — managed alternative
- **TensorBoard** — basic, built into TensorFlow/Keras; metrics only, no full experiment management

---

## Minimal Logging Pattern

```python
mlflow.start_run()
mlflow.log_params({"lr": 0.001, "batch_size": 32})
# ... training loop ...
mlflow.log_metric("val_loss", val_loss, step=epoch)
mlflow.log_artifact("model.pkl")
mlflow.end_run()
```

---

## Trade-offs

| Pro | Con |
|---|---|
| Reproducibility | Logging overhead in training code |
| Systematic comparison of runs | Storage costs for many artifacts |
| Debugging degraded models | Adds dependency to training pipeline |
| Audit trail for regulated environments | Overkill for throwaway experiments |

---

## Relationship to Model Registry

Experiment tracker and model registry are complementary:
- **Tracker**: records the journey — every run, every metric.
- **Registry**: records the decision — which model goes to production.

Best practice: when promoting a model, link the registry entry back to the experiment run that produced it.
