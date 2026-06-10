# AWS EC2 Fundamentals

> Amazon EC2 (Elastic Compute Cloud) gives you virtual servers in the cloud.

Core idea:

```text
Rent compute capacity on demand
→ pay only for what you use
```

AWS handles:

* physical hardware
* data center operations
* hypervisor

You control:

* OS
* software
* networking
* scaling

---

# 1. The Mental Model

EC2 is:

> virtual machine as a service.

You choose:

* CPU and memory (instance type)
* operating system (AMI)
* networking (VPC, subnet)
* storage (EBS)

```text
AMI + Instance Type + Network + Storage
  ↓
Running EC2 instance
```

---

# 2. AMI (Amazon Machine Image)

An AMI is the template used to launch an instance.

It contains:

* operating system
* pre-installed software
* configuration

```text
AMI
  ↓
Launch instance
  ↓
Running server
```

Types:

| AMI Type              | Description                              |
| --------------------- | ---------------------------------------- |
| AWS-provided          | Amazon Linux, Ubuntu, Windows Server     |
| AWS Marketplace       | Pre-configured vendor images             |
| Custom                | Your own image from a running instance   |

Custom AMIs are used for:

* pre-baking software
* faster auto scaling launches
* consistent environments

---

# 3. Instance Types

Instance types define CPU, memory, storage, and network performance.

Naming convention:

```text
m5.xlarge

m  = family (general purpose)
5  = generation
xlarge = size
```

Main families:

| Family | Use Case                          | Example         |
| ------ | --------------------------------- | --------------- |
| T      | Burstable general purpose         | t3.micro        |
| M      | Balanced general purpose          | m5.large        |
| C      | Compute optimized                 | c5.xlarge       |
| R      | Memory optimized                  | r6i.2xlarge     |
| I      | Storage optimized (NVMe)          | i3.large        |
| P/G    | GPU (ML, graphics)                | p3.2xlarge      |
| Inf    | Inferentia (ML inference)         | inf1.xlarge     |

Common interview question:

> When would you choose a C-family vs R-family instance?

Answer:

> C-family for CPU-heavy workloads like video encoding or web servers with high concurrency. R-family for memory-heavy workloads like in-memory caches, large databases, or analytics.

---

# 4. Purchasing Options

One of the most-tested EC2 topics.

## On-Demand

```text
Pay by the second
No commitment
Highest per-unit cost
```

Good for:

* unpredictable workloads
* dev/test environments
* short-lived jobs

---

## Reserved Instances

```text
1-year or 3-year commitment
Up to 75% cheaper than on-demand
```

Good for:

* predictable baseline capacity
* production workloads running 24/7

---

## Savings Plans

Similar discounts to Reserved Instances but more flexible.

```text
Commit to $/hour spend
  ↓
Applies automatically across instance types and regions
```

---

## Spot Instances

```text
Bid on unused AWS capacity
Up to 90% cheaper than on-demand
Can be interrupted by AWS with 2-minute warning
```

Good for:

* batch processing
* fault-tolerant workloads
* big data jobs
* stateless workers

Not good for:

* databases
* stateful applications
* anything that can't tolerate interruption

---

## Dedicated Hosts

```text
Physical server dedicated to you
Required for some compliance needs
Most expensive option
```

Interview cheat sheet:

| Option     | Cost    | Flexibility | Use Case                    |
| ---------- | ------- | ----------- | --------------------------- |
| On-Demand  | High    | Max         | Short-lived, unpredictable  |
| Reserved   | Low     | Low         | Stable long-running workload|
| Spot       | Lowest  | Medium      | Fault-tolerant batch jobs   |
| Dedicated  | Highest | Low         | Compliance, licensing       |

---

# 5. EC2 Storage

## EBS (Elastic Block Store)

Network-attached persistent block storage.

```text
EC2 instance
  ↓
EBS volume (survives instance stop/start)
```

Important:

* EBS volumes are in a specific Availability Zone
* Data persists after instance stops
* Can be detached and re-attached

Volume types:

| Type       | Use Case                          | IOPS         |
| ---------- | --------------------------------- | ------------ |
| gp3        | General purpose SSD (default)     | Up to 16,000 |
| io2        | High-performance databases        | Up to 64,000 |
| st1        | Throughput-optimized HDD          | Sequential   |
| sc1        | Cold HDD, infrequent access       | Low          |

---

## Instance Store

```text
Physically attached to the host
Extremely fast
Ephemeral — data lost on stop/terminate
```

Good for:

* temp buffers
* caches
* scratch data

Not good for:

* anything you need to keep

---

## EFS (Elastic File System)

```text
Shared file system
Multiple instances can mount simultaneously
```

Good for:

* shared content
* home directories
* CMS storage

---

# 6. Networking

## VPC Integration

Every EC2 instance runs inside a VPC.

```text
VPC
  ↓
Subnet (public or private)
  ↓
EC2 instance
```

Public subnet:

* has route to Internet Gateway
* instances can have public IP

Private subnet:

* no direct internet access
* outbound via NAT Gateway

---

## Security Groups

Acts as a virtual firewall around an EC2 instance.

```text
Inbound rules  → what traffic can reach the instance
Outbound rules → what traffic can leave the instance
```

Rules are stateful:

```text
Allow inbound on port 443
  ↓
Response traffic automatically allowed outbound
```

Common setup:

```text
Web server security group:
  Inbound: 443 from 0.0.0.0/0
  Inbound: 22 from your IP only
```

---

## Elastic IP

A static public IPv4 address you own.

```text
Normal public IP changes on stop/start
Elastic IP stays the same
```

Useful for:

* DNS pointing to a fixed IP
* whitelisting requirements

---

# 7. Auto Scaling

Critical interview topic.

Auto Scaling automatically adjusts the number of EC2 instances based on demand.

```text
High traffic
  ↓
Auto Scaling adds instances

Low traffic
  ↓
Auto Scaling removes instances
```

Components:

```text
Launch Template   → defines instance config (AMI, type, SG)
Auto Scaling Group → defines min, max, desired capacity
Scaling Policy    → defines when to scale
```

Scaling policies:

| Policy Type       | Description                                      |
| ----------------- | ------------------------------------------------ |
| Target Tracking   | Keep metric at target (e.g. 60% CPU)             |
| Step Scaling      | Scale by steps based on alarm thresholds         |
| Scheduled         | Scale at predictable times (e.g. 8am weekdays)   |

---

# 8. Load Balancer + Auto Scaling

The classic highly-available pattern:

```text
Users
  ↓
Application Load Balancer
  ↓
Auto Scaling Group
  ↓
EC2 instances in multiple AZs
```

Why multiple AZs:

```text
AZ-a fails
  ↓
Instances in AZ-b still serve traffic
```

This is the standard answer to:

> How do you make an EC2-based application highly available?

---

# 9. EC2 Instance Lifecycle

```text
Pending
  ↓
Running        ← you are billed here
  ↓
Stopping
  ↓
Stopped        ← EBS data persists, no billing for compute
  ↓
Terminated     ← instance deleted, EBS deleted by default
```

Important:

* Stopping and starting moves the instance to different hardware
* Rebooting keeps the same hardware
* Terminated instances cannot be recovered

---

# 10. IAM Roles for EC2

EC2 instances should use IAM roles, not hardcoded credentials.

```text
EC2 instance
  ↓
IAM Instance Profile (attached role)
  ↓
Temporary credentials via instance metadata
  ↓
Access S3, DynamoDB, etc.
```

Never do this:

```text
Hardcode AWS_ACCESS_KEY_ID in application
```

Always do this:

```text
Attach IAM role → use boto3/SDK without credentials
```

This is a very high-signal interview point.

---

# 11. Instance Metadata Service (IMDS)

Running code inside an EC2 instance can query:

```text
http://169.254.169.254/latest/meta-data/
```

Returns:

* instance ID
* AMI ID
* region
* IAM credentials (rotated automatically)

IMDSv2 (current best practice) requires a session token:

```text
Token required before metadata access
Protects against SSRF attacks
```

---

# 12. EC2 vs Lambda vs Fargate

Common interview comparison:

| Feature        | EC2                      | Lambda                    | Fargate                     |
| -------------- | ------------------------ | ------------------------- | --------------------------- |
| Management     | You manage OS            | No infra management       | No OS management            |
| Scaling        | Manual / Auto Scaling    | Automatic                 | Automatic                   |
| Cost model     | Per hour                 | Per invocation/duration   | Per vCPU/memory used        |
| Workload fit   | Long-running, stateful   | Short event-driven tasks  | Containerized workloads     |
| Cold start     | None (always running)    | Yes                       | Minimal                     |

---

# 13. Placement Groups

Controls how instances are placed on physical hardware.

| Type        | Description                                | Use Case                       |
| ----------- | ------------------------------------------ | ------------------------------ |
| Cluster     | All instances on same rack                 | Low-latency HPC, ML training   |
| Spread      | Each instance on separate hardware         | Maximize fault isolation       |
| Partition   | Groups of instances on separate partitions | Hadoop, Cassandra, Kafka       |

Interview insight:

> Cluster placement gives best network performance but highest blast radius if the rack fails.

---

# 14. Common Interview Questions

You should be ready for these:

* What is the difference between stopping and terminating an instance?
* What are Spot Instances and when would you use them?
* How do you make EC2 highly available?
* What is the difference between a Security Group and a NACL?
* How does Auto Scaling work?
* When would you use EC2 over Lambda?
* How does an EC2 instance access S3 securely?
* What is the difference between EBS and instance store?
* What is an AMI and when would you create a custom one?
* How would you reduce EC2 costs?

---

# 15. One Strong Interview Answer

If asked:

> "Design a scalable web application on AWS."

Strong answer:

```text
Users
  ↓
Route 53 (DNS)
  ↓
CloudFront (CDN)
  ↓
Application Load Balancer
  ↓
Auto Scaling Group (EC2 in multiple AZs)
  ↓
RDS (Multi-AZ)
```

That demonstrates:

* EC2 basics
* Auto Scaling
* high availability
* database integration
* cost efficiency

---

# 16. Cost Optimization Interview Points

> "How would you reduce EC2 costs?"

Strong answer covers:

```text
1. Right-size instances → use CloudWatch to find underutilized instances
2. Use Reserved Instances for stable workloads
3. Use Spot Instances for fault-tolerant batch jobs
4. Use Auto Scaling to avoid over-provisioning
5. Schedule stop/start for dev/test environments
```

---

# The Big Picture Mental Model

Think of EC2 as:

```text
Virtual server you control
  ↓
Choose size and OS
  ↓
Attach storage and networking
  ↓
Scale manually or automatically
  ↓
Pay for running time
```

That mental model handles almost every EC2 interview question.
