# 2. Estimation

Back-of-the-envelope sizing to justify storage and compute choices. Order of
magnitude, not precision.

## Assumptions

| Quantity | Value |
|----------|-------|
| Cardholders / accounts | 50 M |
| Concurrent users at peak | ~2 M |
| Card transactions posted per cardholder/day | 3 → **150 M postings/day** |
| Payments (toward balance) | ~60 M/month, **clustered around due dates** |
| Statements generated | 50 M/month (billing cycles staggered → ~1.7 M/day) |
| New applications | ~5 M/year |
| Disputes | ~0.1% of postings → ~150 K/day |
| Notifications | 3–5 per user/month → ~200 M/month |
| Audit events (reads + writes + admin) | ~500 M/day |

## Throughput

- **Postings ingest:** `150 M/day ÷ 86,400 ≈ 1,700/s` average, **~7,000/s at
  peak** (4×). These are appended to transaction history (write-heavy but not
  contended — different accounts).
- **Payments:** low average, but **spiky** — if half of a month's payments land
  in a 3-day window around common due dates, that window sees a few thousand
  writes/sec at peak. Each is one ledger `transfer`.
- **API reads (dashboard/history/statements):** the dominant load. At 2 M
  concurrent users doing a few requests each per session → **tens of thousands
  of QPS**, peaking higher at statement close.

Read:write is heavily read-skewed → scale reads with **replicas + cache + CDN**;
writes are absorbed by the ledger's sharding and by **queue buffering** for
non-urgent work.

## Storage

### Accounts + card metadata (small)

Row ≈ 2 KB (ids, tokenized card ref, limits, status, cycle config).

```
50 M × 2 KB ≈ 100 GB   → fits one Aurora cluster comfortably
```

### Transaction history (dominant OLTP growth)

Row ≈ 400 B (txn id, account id, merchant, amount, category, timestamps).

```
Per day:  150 M × 400 B          ≈ 60 GB/day (raw)
+ indexes (~1.8×)                ≈ 110 GB/day
Per year (raw)                   ≈ 22 TB/year
Per year (indexed)               ≈ 40 TB/year
```

Keep **12–24 months hot** (Aurora, sharded by account/customer), stream older
rows to the **S3 data lake** (Parquet, ~4× compression) for cheap long-term
history and regulatory retention (7 years).

### Statements (S3, large but cheap)

PDF ≈ 60 KB each.

```
50 M/month × 60 KB ≈ 3 TB/month ≈ 36 TB/year
```

Store in **S3**, lifecycle to Glacier after ~1 year, retain 7 years for
compliance. We store rendered PDFs *plus* the structured data used to render
them, so a statement can be re-generated/verified.

### Audit log (high volume, WORM)

Row ≈ 300 B (actor, action, target, before/after hash, prev-hash, timestamp).

```
500 M/day × 300 B ≈ 150 GB/day ≈ 55 TB/year
```

Hash-chained and streamed to **S3 with Object Lock (WORM)**; a rolling window
stays queryable in DynamoDB/OpenSearch. See
[detailed design](06-detailed-design.md#64-tamper-evident-audit-trail).

### Applications & disputes (small)

```
Applications: 5 M/yr × 5 KB   ≈ 25 GB/year
Disputes:     150 K/day × 2 KB ≈ 300 MB/day ≈ 110 GB/year
```

Both fit easily in Aurora; disputes are long-lived (regulated retention) but
low-volume.

## Takeaways

1. **Transaction history and the audit log dominate growth** (~40 TB/yr and
   ~55 TB/yr). Both follow the same pattern: small hot window in a fast store,
   everything else streamed to cheap, durable, compliant S3.
2. **Accounts, applications, disputes are tiny** — their challenge is
   correctness/workflow, not volume.
3. **The system is read-dominated and bursty**, so the money is spent on read
   scaling (replicas, cache, CDN) and on absorbing peaks (autoscaling + queues),
   not on raw write capacity.
