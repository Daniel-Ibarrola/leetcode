# Feature Store

A centralized system for storing, computing, sharing, and serving ML features — consistently between training and serving.

---

## The Problem It Solves

Without a feature store:
- Team A computes "user purchase count last 30 days" in Python. Team B computes it differently in SQL. Models trained on one break when served with the other.
- Features are recomputed from scratch for every model.
- Training uses historical data; serving uses live data — computed differently → **train/serve skew**.

---

## Two Stores in One

### Offline Store
- Historical feature values for training.
- Backed by a data warehouse or data lake (S3 + Parquet, BigQuery, Hive).
- Used for: point-in-time correct feature retrieval for training datasets.

### Online Store
- Latest feature values for low-latency inference.
- Backed by a key-value store (Redis, DynamoDB, Cassandra).
- Used for: serving features at request time (< 10ms lookups).

The same feature definition runs in both stores — guaranteeing consistency.

---

## Point-in-Time Correctness

When building training data, you must fetch the feature values that were available **at the time of the label**, not the current values.

```
Label: user churned on 2024-03-15
Feature: "login_count_last_30_days" as of 2024-03-15 → correct
Feature: "login_count_last_30_days" as of today → data leakage
```

This is one of the hardest problems in ML data pipelines. Feature stores handle it.

---

## Key Capabilities

| Capability | Description |
|---|---|
| Feature registry | Central catalog: what features exist, who owns them, how they're computed |
| Backfilling | Compute historical feature values for training |
| Streaming ingestion | Update online store in near-real-time from event streams |
| Batch ingestion | Bulk-load features from scheduled pipelines |
| Feature sharing | Reuse features across teams and models |

---

## Tools

- **Feast** — open source, widely used
- **Tecton** — managed, production-grade, supports streaming
- **Hopsworks** — open source, full-featured
- **Vertex AI Feature Store** (GCP), **SageMaker Feature Store** (AWS) — managed cloud options

---

## Trade-offs

| Pro | Con |
|---|---|
| Eliminates train/serve skew | Significant infrastructure investment |
| Feature reuse across teams | Adds latency to pipeline if not tuned |
| Point-in-time correct training data | Complexity of keeping offline/online in sync |
| Single source of truth | Overkill for small teams / few models |

---

## When You Need One

- Multiple models sharing the same features.
- Features computed in both batch and real-time.
- Train/serve skew is causing model degradation.
- Team is wasting time rebuilding the same features.

For a single model with simple features, a feature store is likely overkill.
