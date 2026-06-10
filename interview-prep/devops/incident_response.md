Incident response is a high-signal interview topic because it shows whether you can **stay calm under pressure, communicate clearly, and drive a system back to health** — not just whether you can code.

---

# What Is Incident Response?

An incident is any unplanned disruption to a service that affects users or violates an SLA.

Incident response is the structured process to:

```text
Detect
  ↓
Triage
  ↓
Mitigate
  ↓
Resolve
  ↓
Learn
```

---

# The Incident Lifecycle

## 1. Detection

Something goes wrong before a human notices it.

Sources:

```text
Monitoring alerts      ← PagerDuty, Alertmanager
User reports           ← support tickets, social media
Automated health checks ← load balancer, Kubernetes liveness probes
On-call engineer notices ← during deploy, log review
```

The goal of good observability is to detect incidents before users do.

---

## 2. Triage

Once detected, the on-call engineer must answer:

```text
What is broken?
Who is affected?
How severe is it?
```

### Severity Levels

| Severity | Name     | Description                                      | Example                         |
| -------- | -------- | ------------------------------------------------ | ------------------------------- |
| SEV-1    | Critical | Full outage, all users affected                  | Checkout is down                |
| SEV-2    | Major    | Partial outage, core feature degraded            | Login failing for 30% of users  |
| SEV-3    | Minor    | Degraded performance, workaround available       | Slow search results              |
| SEV-4    | Low      | Minor issue, no user impact                      | Non-critical background job late |

Interviewers often ask:

> How do you decide severity?

Answer:

> I look at user impact first — how many users, what functionality, how long. Then I consider revenue and SLA risk.

---

## 3. Mitigation (Stop the Bleeding)

Mitigation is not the same as root cause fix.

The goal is to **restore service as fast as possible**, even if you don't know why it broke.

Common mitigations:

```text
Rollback deployment
  ↓ undo the last change

Restart service
  ↓ clears transient state

Scale up
  ↓ handle traffic spike

Feature flag off
  ↓ disable broken feature

Traffic reroute
  ↓ point load balancer away from bad nodes

Circuit breaker
  ↓ stop cascading failures
```

Key interview insight:

> Mitigation first, investigation second. An outage is not the time for a root cause deep-dive.

---

## 4. Communication

During an incident, communication is as important as technical action.

### Internal Communication

```text
Incident channel created in Slack (#incident-2026-06-10-checkout)
  ↓
Incident commander assigned
  ↓
Status updates every 15-30 minutes
  ↓
Stakeholders notified (product, support, leadership)
```

### Incident Roles

| Role                  | Responsibility                                      |
| --------------------- | --------------------------------------------------- |
| Incident Commander    | Coordinates response, owns communication            |
| Technical Lead        | Drives mitigation and investigation                 |
| Scribe                | Documents timeline, actions taken, findings         |
| Communications Lead   | Updates status page, notifies stakeholders          |

### External Communication (Status Page)

```text
Investigating: We are aware of an issue affecting checkout.
Identified:    The issue has been identified, mitigation underway.
Monitoring:    A fix has been applied, we are monitoring.
Resolved:      The incident has been resolved.
```

---

## 5. Resolution

Resolution happens when:

```text
Service is restored
  ↓
Error rates back to baseline
  ↓
Monitoring shows healthy signal
  ↓
Stakeholders confirmed
```

Document:

```text
Timeline of events
Actions taken
Who was involved
Current status
```

---

## 6. Postmortem (Post-Incident Review)

The most important part for long-term reliability.

A good postmortem:

* Is blameless — people, not root cause
* Identifies what happened and why
* Produces concrete action items

### Postmortem Structure

```text
Summary
  ↓
Timeline
  ↓
Root Cause
  ↓
Impact
  ↓
Detection: how was it found?
  ↓
Resolution: what fixed it?
  ↓
Action Items: what prevents recurrence?
```

### 5 Whys — Root Cause Technique

Example:

```text
Why did checkout go down?
  → Payment service returned 503s

Why did it return 503s?
  → Database connection pool exhausted

Why was the pool exhausted?
  → A slow query held connections for too long

Why was the query slow?
  → Missing index on the orders table

Why was the index missing?
  → New migration didn't include it
```

Root cause: missing database index.

---

# Key Concepts for Interviews

## Mean Time to Detect (MTTD)

How long between failure starting and your team knowing.

```text
Failure starts at 14:00
Alert fires at 14:03
MTTD = 3 minutes
```

Good MTTD: under 5 minutes for critical services.

---

## Mean Time to Resolve (MTTR)

How long between detection and full resolution.

```text
Detected: 14:03
Resolved: 14:45
MTTR = 42 minutes
```

This is the most-watched reliability metric for on-call teams.

---

## Error Budget

Every service has an SLO (Service Level Objective), e.g.:

```text
99.9% availability per month
  ↓
Allowed downtime: ~43 minutes/month
```

Each incident consumes error budget.

```text
Incident burns 20 minutes
Remaining budget: 23 minutes
```

When the error budget is exhausted, reliability work takes priority over feature development.

---

## On-Call Best Practices

```text
Clear runbooks for common alerts
  ↓
Escalation paths defined
  ↓
Alerts are actionable (no noisy non-actionable alerts)
  ↓
On-call rotations are sustainable (don't burn people out)
```

Common interview question:

> What makes a good alert?

Answer:

> A good alert fires only when human action is required, has a clear runbook, and tells you what is broken — not just what metric crossed a threshold.

---

# Tools Commonly Used

| Category         | Tools                              |
| ---------------- | ---------------------------------- |
| Alerting         | PagerDuty, OpsGenie, Alertmanager  |
| Monitoring       | Prometheus, Datadog, CloudWatch    |
| Logging          | ELK Stack, Loki, Datadog Logs      |
| Tracing          | Jaeger, Zipkin, Datadog APM        |
| Status Pages     | Statuspage.io, Atlassian Status    |
| Incident Comms   | Slack, Opsgenie, PagerDuty         |
| Runbooks         | Confluence, Notion, internal wikis |

---

# Runbooks

A runbook is a documented set of steps to resolve a known type of incident.

Example runbook for "High Database Latency":

```text
1. Check active queries: SELECT * FROM pg_stat_activity WHERE state = 'active';
2. Identify long-running queries
3. Kill offending query if > 60s: SELECT pg_terminate_backend(<pid>);
4. Check connection count vs max_connections
5. Restart connection pooler if connections exhausted
6. Escalate to DBA if not resolved in 10 minutes
```

Good runbooks reduce cognitive load during high-stress incidents.

---

# Interview Cheat Sheet

| Concept          | One-line answer                                              |
| ---------------- | ------------------------------------------------------------ |
| MTTD             | Time from failure to detection                               |
| MTTR             | Time from detection to resolution                            |
| Mitigation       | Restore service fast, root cause later                       |
| Postmortem       | Blameless review that produces action items                  |
| Error budget     | Allowed downtime derived from SLO                            |
| Incident command | Single coordinator who owns communication and decisions      |
| Runbook          | Pre-written steps to resolve a known class of failure        |
| 5 Whys           | Iterative root cause technique                               |

---

# Common Interview Scenario

> "You're on call. At 2am you receive an alert: checkout error rate spiked to 15%. Walk me through what you do."

Strong answer:

> First I check whether there was a recent deploy — that's the most common cause. I'd look at deployment history and correlate timing with the spike. While investigating, I'd open an incident channel and notify my team. If a recent deploy is the culprit, I roll back immediately without waiting for a root cause. If no deploy, I look at downstream dependencies — database, payment service, third-party APIs. I use traces and logs to narrow the blast radius. Once service is restored I write up a timeline and schedule a postmortem for the next business day.
