# Write-Heavy Time-Series Data

Metrics, logs, IoT sensor readings, financial tick data, analytics events. Characterized by: very high write volume, append-only (rarely update old data), queries are time-range based, old data is less valuable.

---

## Why Regular DBs Struggle

- High write volume overwhelms a single node.
- Auto-increment IDs / random inserts fragment B-tree indexes.
- Old data still takes up space even though it's rarely queried.
- Queries like "average CPU usage in the last hour" require full table scans without specialized indexing.

---

## Key Design Principles

### 1. Append-Only Writes
Never update. Only insert. This enables:
- Sequential disk writes (fast)
- No lock contention
- Easy replication

### 2. Time-Based Partitioning
Partition data by time (hourly, daily, monthly tables). Old partitions can be:
- Archived to cheaper storage
- Dropped entirely (instead of deleting rows — instant)
- Tiered: hot (recent) → warm → cold

### 3. Columnar Storage
Time-series DBs store data column-by-column. When you query "avg CPU over time," you only read the CPU column, not entire rows. Massive I/O reduction.

### 4. Compression
Repeated values compress extremely well. Adjacent timestamps and metrics are often similar → delta encoding, run-length encoding.

### 5. Downsampling / Rollups
Aggregate raw data into lower-resolution summaries over time:
```
Raw: 1-second readings  → keep for 7 days
1-min avg              → keep for 30 days
1-hour avg             → keep for 1 year
```
Drastically reduces storage. Old queries run against the rollup, not raw data.

---

## Tools

| Tool | Use Case |
|---|---|
| **InfluxDB** | General metrics, IoT, monitoring |
| **TimescaleDB** | Postgres extension; SQL + time-series optimizations |
| **Prometheus** | Metrics collection + alerting (pull-based) |
| **ClickHouse** | High-throughput analytics, columnar |
| **Apache Cassandra** | Wide-column; good for time-series at massive scale |
| **Elasticsearch** | Logs and events (ELK stack) |
| **S3 + Parquet** | Long-term archival, batch analytics |

---

## Write Path Pattern

```
Sensors / App → Buffer (Kafka) → Batch Writer → Time-series DB
```

- **Buffer with Kafka**: absorbs write spikes; batches small writes into larger flushes.
- **Batch writer**: groups writes by time window and flushes in bulk (much faster than one-by-one).
- Never write individual data points to the DB one at a time.

---

## Query Patterns

- **Range query**: `WHERE time BETWEEN t1 AND t2` — always use time as the leading index/partition key.
- **Aggregation**: pre-compute rollups for common windows rather than aggregating on the fly.
- **Last known value**: store the latest value separately in a cache (Redis) for real-time dashboards.

---

## Trade-offs

| Decision | Pro | Con |
|---|---|---|
| Time partitioning | Fast drops/archives | Range queries crossing partitions need multiple reads |
| Downsampling | Huge storage savings | Lose raw data fidelity |
| Columnar storage | Fast range aggregations | Slow for point lookups by row |
| Kafka buffer | Absorbs spikes | Adds latency, another system to manage |

---

## Interview Tips

- Always mention **time-based partitioning** and **TTL/retention policies**.
- Downsampling is a key differentiator from regular DB design.
- For monitoring systems: Prometheus for collection, InfluxDB or TimescaleDB for storage, Grafana for visualization.
