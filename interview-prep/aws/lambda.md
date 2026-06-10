# AWS Lambda Fundamentals

> AWS Lambda lets you run code without managing servers.

Core idea:

```text id="9v3q2u"
Upload code -> Lambda runs it on demand
```

AWS handles:

* servers
* scaling
* patching
* availability

You focus on:

* code
* permissions
* event flow

---

# 1. The Mental Model

Lambda is:

> event-driven compute.

Something happens:

* HTTP request
* S3 upload
* queue message
* cron schedule

→ Lambda executes code.

---

# 2. Common Event Sources

You should know these well:

| Service          | Trigger               |
| ---------------- | --------------------- |
| API Gateway      | HTTP request          |
| S3               | File upload           |
| SQS              | Queue messages        |
| EventBridge      | Scheduled jobs/events |
| DynamoDB Streams | Table changes         |

Example:

```text id="jlwm0k"
Image uploaded to S3
-> Lambda resizes image
```

Classic interview example.

---

# 3. Lambda Execution Model

Each invocation runs in an isolated environment.

Important concepts:

* cold starts
* statelessness
* ephemeral runtime

---

# 4. Statelessness

Lambda should not rely on local memory/files persisting.

Why?
Because executions can happen:

* anywhere
* in parallel
* on newly created environments

Store persistent data in:

* S3
* DynamoDB
* RDS
* ElastiCache

NOT inside Lambda memory.

---

# 5. Cold Starts

Very important interview topic.

## Cold Start

When AWS must initialize a new execution environment.

Includes:

* container startup
* runtime initialization
* code loading

Adds latency.

---

## Warm Start

Reuse existing environment.

Faster.

---

# 6. What Affects Cold Starts

Main factors:

* runtime
* package size
* VPC configuration
* initialization work

Typically:

* Python/Node.js faster
* Java/.NET slower startup

Though AWS has improved this a lot.

---

# 7. Lambda Scaling

Huge concept.

Lambda scales automatically.

If 1,000 requests arrive:

```text id="xqmx0f"
AWS can run many Lambda instances in parallel
```

This is a major reason serverless is attractive.

---

# 8. Concurrency

Concurrency =

> number of executions happening simultaneously.

Important because:

* account limits exist
* downstream systems can get overloaded

---

## Reserved Concurrency

Guarantees capacity for a function.

Also limits max concurrency.

Useful for:

* protecting databases
* critical services

---

# 9. Timeout

Lambda has max execution duration.

Important interview consideration:

> Long-running tasks may not fit Lambda well.

Historically max:

```text id="3gn3xg"
15 minutes
```

Good for:

* APIs
* automation
* event processing

Less ideal for:

* huge batch jobs
* long video rendering
* persistent connections

---

# 10. Memory and CPU

Important:

> More memory also increases CPU allocation.

People often miss this.

Increasing memory can:

* reduce runtime
* sometimes reduce total cost

---

# 11. Pricing Model

Lambda pricing is mainly:

* number of invocations
* execution duration
* allocated memory

Good interview phrase:

> “You pay for execution time, not idle servers.”

---

# 12. IAM Roles for Lambda

Every Lambda function usually has an execution role.

Example:

```text id="1xk6i0"
Lambda reads S3
Lambda writes DynamoDB
```

Role permissions:

```text id="5h71qg"
s3:GetObject
dynamodb:PutItem
```

This connects directly to IAM fundamentals.

---

# 13. Environment Variables

Used for:

* config
* API endpoints
* feature flags

Avoid hardcoding values.

Sensitive values often stored in:

* AWS Secrets Manager
* AWS Systems Manager Parameter Store

---

# 14. API Gateway + Lambda

Extremely common architecture.

> Amazon API Gateway receives HTTP request → invokes Lambda.

Example:

```text id="mbd9yb"
Client
-> API Gateway
-> Lambda
-> DynamoDB
```

Classic serverless backend.

---

# 15. Lambda + SQS

Very important for scalable systems.

Pattern:

```text id="g34jdb"
Producer
-> SQS queue
-> Lambda consumers
```

Benefits:

* decoupling
* retries
* buffering traffic spikes

Interviewers love this.

---

# 16. Retries and Failure Handling

Lambda retry behavior depends on trigger source.

Examples:

* async invocation retries automatically
* SQS retries via visibility timeout
* stream sources retry batches

You should know:

> failure handling differs by event source.

---

# 17. Dead Letter Queues (DLQ)

Failed events can go to:

* SQS
* SNS

Used for:

* debugging
* replaying failures

Important production concept.

---

# 18. VPC Integration

Lambda can run inside a VPC.

Needed for:

* private RDS access
* internal services

Historically this increased cold starts significantly. AWS improved this, but it still matters.

Important interview tradeoff:

> VPC access increases complexity.

---

# 19. Lambda Layers

Reusable shared code/packages.

Example:

```text id="m7mb1l"
shared utilities
database libraries
monitoring SDKs
```

Helps reduce duplication.

---

# 20. Monitoring and Logging

Main logging service:

> Amazon CloudWatch

Know:

* logs
* metrics
* alarms

Typical debugging flow:

```text id="4m6w2i"
Lambda failing
-> check CloudWatch logs
```

---

# 21. Idempotency

Extremely important distributed systems concept.

Because retries happen:

> Lambda functions should ideally be idempotent.

Meaning:

```text id="fwh8mk"
running twice != duplicate side effects
```

Example:

* avoid double-charging customers

Very high-value interview point.

---

# 22. When Lambda Is a Good Fit

Excellent for:

* APIs
* event processing
* automation
* lightweight ETL
* scheduled jobs

---

# 23. When Lambda Is NOT Ideal

Weak fit for:

* ultra-low-latency systems
* very long-running compute
* GPU workloads
* large monoliths
* persistent websocket-heavy stateful apps

Important interview skill:

> knowing tradeoffs instead of saying Lambda solves everything.

---

# 24. Common Architecture Patterns

## Serverless API

```text id="kkgnl7"
API Gateway
-> Lambda
-> DynamoDB
```

---

## File Processing

```text id="juyrb6"
S3 upload
-> Lambda
-> image resize/transcoding
```

---

## Async Processing

```text id="rtsc8n"
App
-> SQS
-> Lambda workers
```

---

# 25. Common Interview Questions

You should be ready for these:

* What is serverless?
* Explain Lambda cold starts
* Why should Lambda be stateless?
* How does Lambda scale?
* How does Lambda pricing work?
* How do retries work?
* What is reserved concurrency?
* Why use SQS with Lambda?
* How does Lambda access S3 securely?
* When would you NOT use Lambda?
* How would you process millions of uploads?
* How do you avoid duplicate processing?

---

# 26. One Strong Interview Answer

If asked:

> “Design an image upload service.”

Good high-level answer:

```text id="4qg9q9"
Client
-> pre-signed S3 upload
-> S3 event
-> Lambda resize
-> store metadata in DB
-> CDN serves final image
```

That demonstrates:

* S3
* IAM
* Lambda
* event-driven architecture
* scalability

Very strong foundational AWS answer.

---

# 27. The Big Picture Mental Model

Think of Lambda as:

```text id="7z3mqv"
event arrives
-> short-lived compute runs
-> scales automatically
-> disappears
```

That mental model helps almost every interview question.

Here’s a realistic but interview-friendly example.

This Lambda:

* gets triggered by an S3 upload
* reads the uploaded file info
* logs metadata

---

# Example Lambda Function (Python)

```python
import json
import urllib.parse

def lambda_handler(event, context):
    # S3 event structure
    record = event['Records'][0]

    bucket_name = record['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(
        record['s3']['object']['key']
    )

    print(f"New file uploaded!")
    print(f"Bucket: {bucket_name}")
    print(f"Key: {object_key}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "File processed successfully"
        })
    }
```

---

# What’s Happening Here

## Lambda Entry Point

```python
def lambda_handler(event, context):
```

This is the function AWS invokes.

* `event` → trigger payload
* `context` → runtime metadata

---

# The `event` Object

For S3 triggers, AWS sends JSON like:

```json
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "my-upload-bucket"
        },
        "object": {
          "key": "photos/image.jpg"
        }
      }
    }
  ]
}
```

Your code extracts:

* bucket name
* uploaded object key

---

# Why `urllib.parse.unquote_plus`?

S3 keys may contain:

* spaces
* URL-encoded characters

Example:

```text id="zfrt9f"
my file.jpg
```

becomes:

```text id="n9zvcu"
my+file.jpg
```

This decodes it safely.

---

# CloudWatch Logging

```python
print(...)
```

In Lambda:

* stdout automatically goes to
  Amazon CloudWatch logs.

Very common debugging flow:

```text id="smr28s"
Lambda fails
-> check CloudWatch logs
```

---

# Typical Real Architecture

```text id="hmuqyk"
User uploads image
-> S3
-> Lambda triggered
-> resize/process image
-> save results
```

This is one of the most common serverless patterns.

---

# Example With boto3

Now a more realistic example.

This Lambda:

* triggered by S3
* reads uploaded object metadata

```python
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    record = event['Records'][0]

    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    response = s3.head_object(
        Bucket=bucket,
        Key=key
    )

    print("File size:", response['ContentLength'])

    return {
        "statusCode": 200
    }
```

---

# Important Interview Point

Notice:

```python
s3 = boto3.client('s3')
```

outside the handler.

Why?

Because Lambda execution environments can be reused.

Creating clients outside handler:

* improves performance
* reduces cold start overhead

This is a strong interview signal.

---

# Required IAM Permissions

This Lambda execution role would need:

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

Important connection:

> Lambda permissions come from its IAM execution role.

---

# Example API Lambda

Very common interview scenario.

Using Amazon API Gateway:

```python
import json

def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "world")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": f"Hello, {name}"
        })
    }
```

Request:

```text id="p4ksq7"
GET /hello?name=Daniel
```

Response:

```json
{
  "message": "Hello, Daniel"
}
```

---

# High-Value Interview Best Practices

## 1. Keep Functions Small

Lambda works best for focused tasks.

---

## 2. Make Functions Idempotent

Retries happen.

Avoid:

* duplicate charges
* duplicate emails
* duplicate DB writes

---

## 3. Avoid Heavy Initialization

Large imports slow cold starts.

---

## 4. Use Environment Variables

Don’t hardcode config.

---

## 5. Handle Errors Properly

Example:

```python
try:
    # work
except Exception as e:
    print(f"Error: {e}")
    raise
```

Re-raising matters because:

* Lambda needs to know invocation failed
* retries/DLQs depend on this

---

# Very Common Interview Follow-Up

> “How does Lambda authenticate to AWS services?”

Correct answer:

```text id="c8a5ec"
IAM execution role with temporary credentials
```

NOT:

```text id="ewquw2"
hardcoded access keys
```

That distinction matters a lot.

