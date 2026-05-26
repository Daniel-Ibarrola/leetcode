# Model Registry

A centralized repository for versioning, storing, and managing the lifecycle of trained ML models.

---

## What It Stores

For each model version:
- Serialized model artifact (weights, parameters)
- Metadata: training date, dataset version, hyperparameters, framework
- Performance metrics: accuracy, F1, AUC on eval set
- Lineage: which training run, which data, which code produced it
- Stage: `Staging` → `Production` → `Archived`

---

## Lifecycle Stages

```
[Training Run] → [Registered] → [Staging] → [Production] → [Archived]
                                     ↑ evaluated/tested
```

- **Staging**: deployed to a test/shadow environment. Evaluated before promoting.
- **Production**: actively serving traffic.
- **Archived**: no longer in use, but retained for reproducibility and rollback.

---

## Why It Matters

**Without a registry:**
- "Which model is running in prod?" → dig through deployment scripts.
- "Why did accuracy drop last week?" → no record of what changed.
- Rollback = scrambling to find an old artifact.

**With a registry:**
- Reproducible: every model is traceable to code + data + config.
- Auditable: full history of what ran in prod and when.
- Rollback: promote a previous version in one step.

---

## Integration with CI/CD

```
Train → Evaluate → Register (if metrics pass threshold) → Promote to Staging
→ Integration tests pass → Promote to Production
```

Automate promotion gates: only register a model if eval metrics exceed a minimum threshold. Only promote to prod if staging tests pass.

---

## Tools

- **MLflow Model Registry** — open source, widely used, integrates with MLflow tracking
- **Weights & Biases (W&B) Artifacts** — pairs naturally with W&B experiment tracking
- **SageMaker Model Registry** (AWS) — managed
- **Vertex AI Model Registry** (GCP) — managed
- **Hugging Face Hub** — for NLP/LLM models specifically

---

## Trade-offs

| Pro | Con |
|---|---|
| Reproducibility and auditability | Another system to maintain |
| Safe rollback | Artifact storage costs grow over time |
| Enforces evaluation gates before production | Adds steps to the deployment process |
| Shared visibility across teams | Requires discipline to keep metadata accurate |

---

## Minimum Viable Registry

If you can't adopt a full tool, at minimum track in a DB or spreadsheet:
- Model ID, version, artifact path (S3 key)
- Eval metrics at time of registration
- Deployment date and status
- Link to training run / git commit

This is better than nothing, but doesn't give you lineage or automated lifecycle management.
