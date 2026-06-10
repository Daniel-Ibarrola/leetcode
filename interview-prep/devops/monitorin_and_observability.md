# Monitoring vs Observability

These terms are related but not identical.

### Monitoring

Monitoring answers:

> "Is something wrong?"

Examples:

* CPU > 90%
* API latency > 500ms
* Error rate > 5%
* Disk nearly full

Monitoring is usually based on predefined metrics and alerts.

---

### Observability

Observability answers:

> "Why is something wrong?"

Imagine you receive:

```text
Alert:
Checkout API error rate increased from 0.1% to 20%
```

Monitoring detected the problem.

Observability helps investigate:

* Which requests are failing?
* Which service caused the failure?
* Which deployment introduced the issue?
* Which customers are affected?

---

# The Three Pillars of Observability

You'll hear this phrase often.

## 1. Metrics

Numeric measurements over time.

Examples:

```text
CPU Usage
Memory Usage
Request Count
Error Rate
Latency
```

A metric might look like:

```text
Time      CPU
10:00     20%
10:05     35%
10:10     90%
```

Metrics are lightweight and great for alerting.

---

## 2. Logs

Detailed event records.

Example:

```text
2026-06-09 10:05:21
User 123 requested /checkout

2026-06-09 10:05:22
Database timeout

2026-06-09 10:05:22
Request failed
```

Logs provide context that metrics can't.

---

## 3. Traces

Traces follow a request through multiple services.

Imagine:

```text
Client
  ↓
API Gateway
  ↓
Order Service
  ↓
Payment Service
  ↓
Database
```

A trace might reveal:

```text
API Gateway     5ms
Order Service   15ms
Payment Service 3000ms
Database        10ms
```

Now you know exactly where the slowdown occurred.

---

# Metrics You Should Know

A lot of interview questions revolve around what should be monitored.

## Infrastructure Metrics

### CPU

```text
Current CPU utilization
```

Useful for:

* Capacity planning
* Detecting runaway processes

---

### Memory

```text
RAM usage
```

Very important because:

* Memory leaks are common
* Containers can be killed when memory limits are exceeded

---

### Disk

Monitor:

```text
Disk space
Disk I/O
```

Running out of disk space can crash services.

---

### Network

Monitor:

```text
Bandwidth
Packet loss
Connection count
```

---

# Application Metrics

These are often more valuable than infrastructure metrics.

Suppose CPU is normal:

```text
CPU = 30%
```

But:

```text
Checkout failures = 80%
```

Users still can't buy anything.

Business metrics often matter more.

---

## Request Rate

Often called throughput.

Example:

```text
Requests per second
```

or

```text
Requests per minute
```

---

## Error Rate

One of the most important metrics.

Example:

```text
1%
```

might be normal.

```text
20%
```

is a major incident.

---

## Latency

How long requests take.

Example:

```text
Average response time = 50ms
```

versus

```text
Average response time = 5 seconds
```

---

# The Golden Signals

A very common interview topic.

Popularized by Google.

The four golden signals are:

### Latency

How long requests take.

---

### Traffic

How much demand exists.

Examples:

```text
Requests/sec
Messages/sec
Transactions/sec
```

---

### Errors

How many requests fail.

Examples:

```text
HTTP 500s
Failed jobs
Failed payments
```

---

### Saturation

How close a system is to its limits.

Examples:

```text
CPU
Memory
Connections
Queue depth
```

---

If asked:

> "What would you monitor for a backend service?"

Mentioning the four golden signals is a strong answer.

---

# Logging Best Practices

Bad logs:

```text
Something went wrong
```

Not useful.

---

Good logs:

```json
{
  "request_id": "abc123",
  "user_id": 456,
  "endpoint": "/checkout",
  "error": "database timeout"
}
```

Structured logs are much easier to search and analyze.

---

# Correlation IDs

Very important in distributed systems.

Suppose a request flows through:

```text
API
 ↓
Orders
 ↓
Payments
 ↓
Database
```

Generate:

```text
request_id=abc123
```

Every service logs it.

Now you can find all logs related to one request.

---

# Health Checks

Critical for deployments.

Typical health endpoint:

```text
/health
```

Returns:

```json
{
  "status": "healthy"
}
```

Load balancers and orchestrators use these checks.

---

# Types of Health Checks

## Liveness

Answers:

> "Should this process be restarted?"

---

## Readiness

Answers:

> "Can this service receive traffic?"

Example:

```text
Application started
Database connection not ready
```

Liveness:

```text
PASS
```

Readiness:

```text
FAIL
```

Traffic is withheld.

---

# Alerting

The purpose of monitoring isn't dashboards.

It's action.

Bad alert:

```text
CPU > 80%
```

This may be noisy.

---

Better alert:

```text
Error rate > 5%
for 5 minutes
```

This reflects actual user impact.

---

# SLI, SLO, and SLA

Very popular in senior interviews.

## SLI

Service Level Indicator

A measurement.

Example:

```text
99.95% successful requests
```

---

## SLO

Service Level Objective

Target.

Example:

```text
99.9% uptime
```

---

## SLA

Service Level Agreement

Contractual promise.

Example:

```text
99.9% uptime guaranteed
```

May involve penalties.

---

# Monitoring an ECS Application

Suppose you have:

```text
ALB
 ↓
ECS
 ↓
RDS
```

I would monitor:

### ALB

* Request count
* Response codes
* Latency

---

### ECS

* CPU
* Memory
* Task restarts

---

### Application

* Request rate
* Error rate
* Response times

---

### Database

* Connections
* Query latency
* CPU
* Storage

---

# Common Incident Question

Interviewers love this scenario:

> "Users report the API is slow. How do you investigate?"

A strong approach:

1. Check dashboards
2. Verify latency increase
3. Identify affected endpoints
4. Check recent deployments
5. Review logs
6. Review traces
7. Identify bottleneck
8. Roll back if necessary

Notice:

```text
Metrics → Logs → Traces
```

That's often the investigation flow.

---

# AWS-Specific Tools You Should Know

For your interview, be familiar with:

* Amazon CloudWatch

  * Metrics
  * Dashboards
  * Alarms
  * Logs

* AWS X-Ray

  * Request tracing

* Datadog

  * Monitoring and observability

* Grafana Labs

  * Dashboards

* Prometheus

  * Metrics collection

---

# Interview Cheat Sheet

If they ask:

> "What are the most important things to monitor for a production backend service?"

A concise senior-level answer:

> I start with the four golden signals: latency, traffic, errors, and saturation. I collect metrics for alerting, structured logs for debugging, and traces for understanding request flow across services. I also monitor infrastructure health, application health, and business-critical metrics such as successful transactions or completed orders. That gives both monitoring for detection and observability for root-cause analysis.
