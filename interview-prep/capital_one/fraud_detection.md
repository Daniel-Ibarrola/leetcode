# System Design: Real-Time Fraud Detection System

## Problem

Design a real-time fraud detection system that evaluates every card transaction and returns an allow or decline decision.

## Requirements

**Functional:**
- Receive a transaction event (card, merchant, amount, location, timestamp) and return allow/decline within **150 ms**
- Evaluate transactions against rules derived from the customer's historical behavior (up to 10 years of data)
- Incorporate streaming features computed from recent transactions (e.g., velocity checks over the last 1/5/30 minutes)
- Flag suspicious transactions for human review even when they are allowed
- Allow analysts to add, modify, or disable detection rules without a code deployment
- Feed final outcomes (approved, declined, confirmed fraud, false positive) back into the system to improve future decisions

**Non-functional:**
- End-to-end latency for a decision must be under 150 ms at the 99th percentile
- Must evaluate 100% of transactions — no sampling
- High availability (a failure must not block legitimate transactions; fail-open vs. fail-closed policy must be defined)
- Must scale to thousands of transactions per second across all cardholders
- 10 years of historical transaction data must be queryable efficiently for feature computation
