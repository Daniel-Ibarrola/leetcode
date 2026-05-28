# Architecture: Metrics & Monitoring Dashboard (Datadog/Prometheus-like)

**Scale target:** 1M services emitting metrics, 500K data points/sec ingestion, 1-second resolution, 13-month retention

---

## Problem

Design a system that ingests high-volume time-series metrics from distributed services, stores them efficiently, and serves real-time dashboards and alerts.

---

## Architecture Diagram

```
                    ┌──────────────────────────────────────────────┐
                    │                  INGESTION                   │
                    └──────────────────────────────────────────────┘

Services / Agents
  (CPU, memory, latency, error rates)
        │
        │ push (UDP/HTTP) or pull (Prometheus scrape)
        ▼
  Load Balancer
        │
        ▼
  Ingestion Service  ──────────────────────► Kafka
  (validate, tag,                     topic: raw-metrics
   batch)                                      │
                                     ┌─────────┘
                                     │
                    ┌────────────────▼─────────────────────┐
                    │          STORAGE LAYER               │
                    └──────────────────────────────────────┘

                         Kafka Consumer Workers
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
         Hot Storage      Warm Storage    Cold Storage
         (ClickHouse      (ClickHouse     (S3 + Parquet
          in-memory        on-disk,        columnar,
          1-hour window)   7-day window)   13-month)
                                │
                         Downsampling Worker
                         (1s → 1m → 1h rollups
                          using materialized views)

                    ┌──────────────────────────────────────────────┐
                    │               QUERY LAYER                    │
                    └──────────────────────────────────────────────┘

User Dashboard / Alerting Engine
        │
        ▼
  Query Service
        │
        ├──► Redis Cache (pre-computed queries, popular dashboards)
        │
        ├──► ClickHouse (recent data, aggregations)
        │
        └──► S3 (historical data via Presto/Athena)

                    ┌──────────────────────────────────────────────┐
                    │               ALERTING                       │
                    └──────────────────────────────────────────────┘

  Kafka (raw-metrics) ──► Alert Evaluation Service
                                  │
                          evaluate rules against sliding windows
                                  │
                          if threshold breached:
                          Kafka (alert-events topic)
                                  │
                          ├──► PagerDuty / Slack
                          └──► Alert History DB
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| Load Balancer (ingestion) | Load Balancers | `building_blocks/load_balancers.md` |
| Kafka (metrics stream) | Pub/Sub | `building_blocks/pub_sub.md` |
| ClickHouse (columnar store) | Time-Series Data | `patterns/time_series_data.md` |
| Downsampling / rollups | Time-Series Data | `patterns/time_series_data.md` |
| S3 (cold storage) | Blob Storage | `building_blocks/blob_storage.md` |
| Redis (query cache) | Caches | `building_blocks/caches.md` |
| Sharding metrics by service_id | Sharding | `concepts/sharding.md` |
| Scaling write throughput | Scaling Writes | `patterns/scaling_writes.md` |
| Time-based partitioning | Indexes | `concepts/indexes.md` |
| Replication for ClickHouse | Replication | `concepts/replication.md` |
| CAP trade-off (availability over consistency) | CAP Theorem | `concepts/cap_theorem.md` |

---

## Key Decisions

### 1. Append-only writes — the fundamental property of metrics
Metrics are never updated, only appended. This unlocks:
- No write-write conflicts → no locking needed
- Columnar compression (ClickHouse stores columns together → 10x+ compression for repeated values)
- Time-based partitioning: each partition is a time range, old partitions are read-only  
→ See `patterns/time_series_data.md`

### 2. Kafka as the ingestion buffer
Services emit metrics at 500K points/sec. Kafka absorbs spikes and decouples:
- Ingestion rate from storage rate
- Multiple consumers: hot storage writer, alert evaluator, analytics pipeline

If ClickHouse is slow, Kafka buffers the backlog without dropping data.

### 3. Tiered storage with downsampling
Storing 1-second resolution for 13 months is prohibitively expensive.  
Downsampling workers create aggregated rollups:
```
raw (1s)  →  kept for 24 hours
1m rollup →  kept for 7 days
1h rollup →  kept for 13 months
```
Rollups are stored as materialized views in ClickHouse or pre-computed to S3.  
Dashboard queries automatically hit the right tier based on the time range selected.

### 4. Columnar storage (ClickHouse) over row storage
Metrics queries are: "give me CPU usage for service X over the last 6 hours, aggregated by minute."  
This is a column scan, not a row lookup. ClickHouse stores all timestamps together, all values together:
- Column scan reads only the relevant columns (timestamp, value)
- 100x faster than row-oriented PostgreSQL for this access pattern  
→ See `patterns/time_series_data.md`

### 5. Time-based partitioning + sharding
Partition by time in ClickHouse: each partition = one day or one week.  
Shard by `(service_id, metric_name)` hash across ClickHouse nodes.  
Queries for a single service touch one shard; range queries over all services scatter across all shards.  
→ See `concepts/sharding.md`

### 6. Redis cache for dashboard queries
Popular dashboards repeat the same queries every few seconds.  
Pre-compute and cache results with a short TTL (10–30 seconds):
```
cache:query:{hash_of_query_params} → aggregated result
```
A 10-second stale dashboard is acceptable for monitoring; it removes 95% of DB query load.

### 7. AP over CP for metric ingestion
During a network partition, prioritize **availability**: keep accepting metrics, accept that some may be slightly out of order or briefly duplicated.  
Strong consistency would require coordination across ClickHouse nodes, adding latency to every write.  
Duplicate data points are handled by deduplication at query time or during compaction.  
→ See `concepts/cap_theorem.md`

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| 500K writes/sec to storage | Kafka batching; ClickHouse bulk insert (not row-by-row) |
| Long-range queries (13 months) | S3 + Parquet; Presto/Athena for ad-hoc; pre-aggregated rollups for dashboards |
| Hot metrics (frequently queried) | Redis cache in front of query service |
| Alert evaluation lag | Dedicated Kafka consumer group; in-memory sliding window evaluation |
| Storage cost | Aggressive compression (columnar + LZ4/ZSTD); downsampling old data |

---

## Interview Tips

- Key insight: metrics are **append-only** — design the whole system around that property.
- Justify ClickHouse over PostgreSQL: columnar is 100x faster for aggregation queries.
- Mention the tiered storage model — hot/warm/cold with downsampling is a real pattern used by Datadog, Prometheus+Thanos, etc.
- Alert evaluation is a separate read path — never block ingestion on it.
- Discuss cardinality: too many unique tag combinations (high-cardinality labels) can explode storage — a real operational challenge.
