# Training Pipeline Design

The end-to-end process of going from raw data to a registered, evaluated model artifact. Getting this right makes ML reproducible, debuggable, and automatable.

---

## Pipeline Stages

```
[Raw Data]
    → [Data Validation]
    → [Feature Engineering]
    → [Data Splitting]
    → [Model Training]
    → [Evaluation]
    → [Model Registration]
    → [Deployment Gate]
```

Each stage is an independent, retryable step with defined inputs and outputs.

---

## Stage Breakdown

### 1. Data Ingestion
Pull data from sources: data warehouse, data lake, feature store.
- Always record what data was used (version, row count, date range).
- Never modify source data — copy to a pipeline-specific location.

### 2. Data Validation
Catch bad data before it corrupts training.
- Schema checks: expected columns, types.
- Statistical checks: null rates, outliers, value ranges match expected distribution.
- Fail fast: a pipeline that silently trains on bad data is worse than one that crashes.
- Tools: Great Expectations, TFX Data Validation, Pandera.

### 3. Feature Engineering
Transform raw data into model-ready features.
- Apply the **same transformations** that serving will apply (prevent train/serve skew).
- Fit transformers (scalers, encoders) on train set only; apply to val/test.

### 4. Data Splitting
Separate into train, validation, and test sets.
- **Temporal data**: always split by time. Never shuffle time-series data — you'll leak future into past.
- **Random split**: fine for i.i.d. data.
- Hold the test set out entirely until final evaluation.

### 5. Training
Run the training loop. Log everything to an experiment tracker.
- Hyperparameters, metrics per epoch, final metrics.
- Save checkpoints; resume from checkpoint if interrupted.

### 6. Evaluation
Measure model quality on held-out data.
- Use metrics appropriate to the problem (accuracy, AUC-ROC, F1, NDCG…).
- Compare against: baseline, current production model, minimum acceptable threshold.
- **Slice-based evaluation**: evaluate on subgroups (demographics, categories) to catch performance disparities.

### 7. Model Registration
If metrics pass thresholds, register the model artifact in the model registry with full metadata.
- Link to the training run, dataset version, git commit.

### 8. Deployment Gate
Human or automated check before going to production:
- Does it pass A/B test? Shadow mode? Canary?
- Are there fairness/bias concerns?

---

## Key Principles

- **Reproducibility**: same inputs always produce same output. Pin random seeds, library versions, data versions.
- **Fail fast**: validate data and inputs early; don't waste GPU hours on bad data.
- **Idempotent steps**: re-running any step produces the same result.
- **Artifact handoff**: each step consumes and produces versioned artifacts — no shared mutable state.

---

## Trade-offs

| Monolithic script | Simple to start | Hard to debug, retry, or parallelize |
| DAG-based pipeline | Retryable, parallelizable, observable | More upfront infrastructure |
| Fully automated pipeline | Faster iteration | Risk of deploying bad models automatically |
| Manual deployment gate | Safer | Slower, doesn't scale to frequent retraining |
