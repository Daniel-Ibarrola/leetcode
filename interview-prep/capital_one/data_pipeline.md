# System Design: Transaction Data Pipeline

## Problem

Design a data pipeline to process billions of financial transactions daily.

## Requirements

**Functional:**
- Ingest transaction events in real time from multiple upstream sources
- Process, validate, and transform each transaction record
- Store processed data in a queryable form for downstream consumers (analytics, reporting, fraud detection)
- Support both real-time streaming and batch processing use cases

**Non-functional:**
- Must handle billions of transactions per day
- Low-latency ingestion (transactions should be available to consumers within seconds)
- High durability — no transaction data can be lost
- The pipeline must be fault-tolerant and recoverable after failures
- Support schema evolution as transaction formats change over time
