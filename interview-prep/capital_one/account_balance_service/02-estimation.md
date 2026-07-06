# 2. Estimation

Back-of-the-envelope sizing to justify the storage and compute choices. Round
numbers; the goal is order of magnitude, not precision.

## Assumptions

| Quantity | Value |
|----------|-------|
| Accounts | 100 M |
| Write transactions (credit/debit/transfer) — average | 2,000 TPS |
| Write transactions — peak | 5,000 TPS |
| Balance/history reads | 20,000 QPS (reads ≫ writes) |
| Ledger entries per transaction | 2 (double-entry: one debit leg, one credit leg) |
| Retention in hot OLTP store | 90 days; older data archived to the data lake |

## Throughput

- Writes: `2,000 txn/s → 4,000 ledger rows/s` average, `10,000 rows/s` at peak.
- Reads: `20,000 QPS`, dominated by balance lookups (a single indexed row read).

Read:write ≈ 10:1, so the read path is what we scale out horizontally (replicas /
cache), while the write path is what we shard.

## Storage

### Accounts table (small)

Row ≈ 100 bytes (ids, balance, currency, version, timestamps).

```
100 M accounts × 100 B ≈ 10 GB
```

Fits comfortably in RAM on a single instance — the accounts table is never the
bottleneck. The pressure is entirely on the ledger.

### Ledger table (dominant)

Row ≈ 200 bytes (entry_id, transaction_id, account_id, amount, type,
balance_after, created_at, small metadata).

```
Per day:   2,000 txn/s × 2 legs × 86,400 s        = 345.6 M rows/day
           345.6 M × 200 B                        ≈ 69 GB/day (raw)
With indexes (~1.8×)                               ≈ 125 GB/day
Per year (raw)                                     ≈ 25 TB/year
Per year (with indexes)                            ≈ 45 TB/year
```

- **Hot store (90-day retention):** `~125 GB/day × 90 ≈ 11 TB`. Comfortable for a
  single Aurora volume (128 TB max), and small enough that per-shard subsets stay
  in the hundreds of GB.
- **Archive (S3 data lake):** grows `~25 TB/year` raw, but Parquet + compression
  cuts that to `~5–8 TB/year`. S3 is effectively unbounded and cheap, so multi-year
  audit retention is a non-issue.

### Idempotency keys (short-lived)

One row per write request, TTL'd after 24–48 h.

```
345.6 M txn/day... but keyed per request (~1 per txn) × ~120 B ≈ 40 GB/day
Kept 48 h ≈ 80 GB, then expired.
```

Store in DynamoDB with a TTL attribute (auto-eviction) or a partitioned Aurora
table pruned by a scheduled job.

## Takeaways

1. **Accounts are tiny (10 GB); the ledger is everything (~25 TB/yr).** This is
   why we keep only a rolling window hot and stream the rest to S3.
2. **Writes are the scaling problem, not storage capacity.** 5,000 TPS of *ACID*
   writes across 100 M accounts is what pushes us to shard by `account_id`.
3. **Reads dominate volume (10:1)** and can be absorbed by replicas + a cache,
   because most reads are single-account balance/history lookups.
