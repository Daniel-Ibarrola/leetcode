# 2. Estimation

Back-of-the-envelope sizing to justify storage and compute choices. Order of
magnitude, not precision.

## Assumptions

| Quantity | Value |
|----------|-------|
| Customers using virtual cards | 20 M |
| Active virtual cards (standing, at any moment) | 40 M (avg 2/customer, heavily skewed) |
| New cards issued/day (mostly **one-time-use**, dominates churn) | ~5.2 M/day |
| Lifecycle actions/day (freeze, unfreeze, cancel) | ~1 M/day |
| Authorizations/day (across recurring + one-time cards) | ~30 M/day |
| Audit events/day (creation + lifecycle + auths + declines) | ~40 M/day |

## Throughput

- **Issuance:** `5.2 M ÷ 86,400 ≈ 60/s` average, **~300/s at peak** (5×, e.g.
  checkout-flow bursts). Must stay **sub-second at p99** — this is a
  synchronous, customer-facing call, not a workflow.
- **Authorization:** `30 M ÷ 86,400 ≈ 350/s` average, **~3,500/s at peak**
  (10×, holiday/lunch-hour spikes). This is the tightest SLA in the system —
  the issuer's decision has to fit inside the card network's authorization
  timeout budget, in the same latency class as
  [the fraud engine's 150 ms p99](../fraud_detection.md).
- **Audit ingestion:** ~40 M/day ≈ 460/s average, bursting with authorization
  peaks.

Authorization is the throughput- and latency-sensitive path; issuance and
lifecycle actions are comparatively low-volume and latency-tolerant by
comparison (sub-second, not sub-100ms).

## Storage

### Card metadata (`virtual_cards`)

Row ≈ 400 B (card id, customer id, account id, PAN token ref, last4, expiry,
network, usage type, status, timestamps).

```
Standing active cards:  40 M × 400 B                  ≈ 16 GB   (trivial)
Cumulative issuance:     5.2 M/day × 400 B × 365       ≈ 760 GB/year (raw)
                         + indexes (~1.5×)             ≈ 1.1 TB/year
```

The standing count is tiny — the churn from one-time-use cards is what
accumulates. Keep active + recently-retired cards (e.g. 90 days) in the hot
store; archive older burned/expired/cancelled cards to the S3 data lake,
retained per the audit requirement (typically 7 years).

### Token vault (PCI zone)

Row ≈ 200 B (token id, encrypted PAN, encrypted CVV, KMS key ref). Same
cardinality as issuance, smaller row.

```
5.2 M/day × 200 B × 365 ≈ 380 GB/year (raw)
```

Small in absolute terms, but this is the highest-sensitivity data in the
system — isolated store, HSM/KMS-backed, tightest access controls (see
[04](04-high-level-design.md) and [06](06-detailed-design.md#63-pci-dss-scope-reduction)).

### Card limits/rules (`card_limits`)

Standing-count only — rules live and die with the card.

```
40 M × 300 B ≈ 12 GB   (trivial)
```

### Authorizations (`authorizations`)

Row ≈ 400 B (auth id, card id, account id, amount, merchant, MCC, decision,
timestamp).

```
Per day:  30 M × 400 B            ≈ 12 GB/day (raw)
+ indexes (~1.8×)                 ≈ 22 GB/day
Per year (raw)                    ≈ 4.4 TB/year
Per year (indexed)                ≈ 8 TB/year
```

Same pattern as transaction history elsewhere in this repo: keep 12–24 months
hot, sharded by `card_id`/`account_id`, stream older rows to S3/Parquet for
cheap long-term retention.

### Audit log (WORM, hash-chained)

Row ≈ 300 B (actor, action, target, before/after hash, prev-hash, timestamp).

```
40 M/day × 300 B ≈ 12 GB/day ≈ 4.4 TB/year
```

Streamed to S3 with Object Lock, same tamper-evident approach as
[the online banking platform's audit trail](../online_banking_platform/06-detailed-design.md#64-tamper-evident-audit-trail).

## Takeaways

1. **Standing active-card count is small** (tens of GB) — the real driver is
   **one-time-use churn**: millions of cards minted and burned daily, which
   only matters if kept hot forever. Tiering to cold storage after a short
   retention window is what keeps the hot store cheap.
2. **Authorizations and the audit log dominate long-term growth** (multi-TB/
   year each), the same small-hot-window-plus-cheap-archive pattern used by
   the ledger and audit designs elsewhere in this repo.
3. **The scaling-sensitive resource is authorization latency and throughput**,
   not storage — a ~3,500 TPS peak against a tight SLA is why the hot path
   leans on an in-memory cache rather than a general-purpose database read
   (see [04](04-high-level-design.md)).
