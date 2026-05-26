# Data Versioning & Lineage

Tracking what data produced which model, and being able to reproduce any past result exactly.

---

## The Problem

A model's behavior is determined by three things: **code + data + config**. Most teams version code (git) and config (git or registry). Data is often not versioned — it just mutates.

Without versioned data:
- You can't reproduce a training run from 3 months ago.
- You don't know if a model performance change was caused by a code change or a data change.
- A bug in the pipeline corrupts data with no rollback path.
- Regulatory audits ("what data was used to make this decision?") have no answer.

---

## Data Versioning

### Snapshot Versioning
Take a copy of the dataset at each training run. Store as a versioned artifact (e.g., `s3://data/v42/train.parquet`).
- Perfectly reproducible.
- High storage cost — N copies of large datasets.

### Pointer Versioning (DVC-style)
Store the data once; version the pointer (a hash or manifest file in git).
- Storage-efficient.
- Reproducible if underlying storage is immutable.
- Tools: **DVC** (Data Version Control), **Delta Lake**, **Iceberg**.

### Delta Tables (Lake Format)
Data lake formats (Delta Lake, Apache Iceberg, Apache Hudi) provide:
- **ACID transactions** on data lake files.
- **Time travel**: query data as it was at any past timestamp.
- **Schema evolution**: track schema changes over time.
- Efficiently version without copying everything.

---

## Lineage

Lineage tracks the full provenance of a model or dataset:

```
Raw events (S3) 
  → ETL job v3.2 (git commit abc123) 
  → processed dataset v18 (2024-03-10)
  → training run #441 (hyperparams: lr=0.001)
  → model v7 (accuracy: 0.89)
  → deployed to production 2024-03-12
```

This chain lets you answer:
- "Was this model trained on data that included the bug we fixed?"
- "Which models are affected if we retrain with corrected data?"
- "What was the input to this prediction?" (regulatory requirement)

---

## Tools

| Tool | Focus |
|---|---|
| **DVC** | Data version control, pipeline tracking |
| **Delta Lake** | ACID + time travel on data lake |
| **Apache Iceberg** | Same as Delta Lake, more open |
| **MLflow** | Experiment + artifact lineage within ML runs |
| **DataHub / OpenMetadata / Amundsen** | Enterprise data catalog + lineage |
| **dbt** | SQL transformation lineage |

---

## Minimum Viable Practice

Even without a dedicated tool:
1. Store training datasets as immutable, named snapshots (never overwrite).
2. Log the dataset version (file path + hash) with every training run.
3. Record the git commit of training code.
4. Store this in your experiment tracker or a simple DB.

This gives you reproducibility and basic lineage without a heavy tool.

---

## Trade-offs

| Full versioning + lineage | Reproducible, auditable, debuggable | Storage cost, pipeline complexity |
| No versioning | Simple | Can't reproduce, can't debug data issues |
| Time-travel formats (Delta/Iceberg) | Efficient, queryable history | Requires adopting a new table format |
