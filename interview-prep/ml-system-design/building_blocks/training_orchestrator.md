# Training Orchestrator

Schedules, manages, and monitors ML training jobs — from data ingestion through model registration.

---

## What It Does

- Defines the training pipeline as a **DAG** (directed acyclic graph) of steps.
- Schedules runs (triggered, scheduled, or on-demand).
- Allocates compute (CPUs, GPUs, distributed nodes).
- Handles retries on step failure.
- Passes artifacts between steps.
- Provides visibility: what's running, what failed, how long it took.

---

## Typical Pipeline DAG

```
[Ingest Data] → [Validate Data] → [Compute Features] → [Train Model]
                                                             ↓
                                              [Evaluate Model] → [Register if metrics pass]
```

Each box is a step. Steps are independent units that can be retried or run in parallel.

---

## Tools

| Tool | Type | Best For |
|---|---|---|
| **Apache Airflow** | Open source, general | Data + ML pipelines, mature ecosystem |
| **Kubeflow Pipelines** | Kubernetes-native | ML-specific, cloud-native |
| **Metaflow** (Netflix) | Open source | Data scientist-friendly, local-to-cloud |
| **Prefect** | Managed/open source | Modern Airflow alternative, Python-first |
| **Dagster** | Open source | Data-aware orchestration, strong observability |
| **SageMaker Pipelines** (AWS) | Managed | AWS-native ML pipelines |
| **Vertex AI Pipelines** (GCP) | Managed | GCP-native |

---

## Step Isolation

Each step runs in its own container/environment:
- Reproducible (no hidden dependencies between steps)
- Independently scalable (training step gets GPUs, validation step doesn't)
- Independently retryable (fail in validation → rerun just validation)

---

## Triggering Runs

| Trigger | When to Use |
|---|---|
| Scheduled (cron) | Regular retraining (weekly, daily) |
| Data arrival | New data lands in S3/GCS → trigger training |
| Drift detected | Monitoring detects model/data drift → retrain |
| Manual | Ad-hoc experiments, debugging |
| CI/CD | Code change to model → trigger pipeline |

---

## Trade-offs

| Pro | Con |
|---|---|
| Reproducible, auditable runs | Overhead of containerizing each step |
| Handles failures and retries | Learning curve for DAG framework |
| Scales compute per step | Infrastructure cost to run orchestrator itself |
| Clear dependency graph | Debugging distributed pipelines is complex |

---

## Relationship to Other Components

```
Orchestrator triggers →
  Feature Store (fetch training data)
  Experiment Tracker (log metrics)
  Model Registry (register result)
```

The orchestrator is the glue that connects all other ML building blocks.
