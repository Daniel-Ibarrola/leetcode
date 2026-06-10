# AWS ECS Fundamentals

> Amazon ECS (Elastic Container Service) is a fully managed container orchestration service.

Core idea:

```text
Package app as Docker container
  ↓
ECS runs and manages it at scale
```

AWS handles:

* cluster management
* container placement
* health checks
* scaling

You control:

* container definition
* networking
* IAM permissions
* scaling rules

---

# 1. The Mental Model

ECS answers the question:

> How do I run containers in production without managing Kubernetes myself?

```text
Docker image
  ↓
Task Definition (what to run)
  ↓
Service (how many, where)
  ↓
Cluster (compute pool)
```

---

# 2. Core Concepts

## Cluster

A logical grouping of compute resources where tasks run.

```text
ECS Cluster
  ↓
Tasks running on EC2 or Fargate
```

---

## Task Definition

A blueprint for your container.

Defines:

* Docker image
* CPU and memory
* environment variables
* port mappings
* IAM role
* logging config

Think of it as a docker-compose file, but for ECS.

```json
{
  "family": "web-app",
  "containerDefinitions": [
    {
      "name": "web",
      "image": "nginx:latest",
      "cpu": 256,
      "memory": 512,
      "portMappings": [
        { "containerPort": 80 }
      ]
    }
  ]
}
```

---

## Task

A running instance of a Task Definition.

```text
Task Definition (blueprint)
  ↓
Task (running container)
```

Tasks are ephemeral — they start, run, and stop.

---

## Service

A Service keeps a specified number of tasks running at all times.

```text
Service: desired count = 3
  ↓
ECS ensures 3 tasks are always running
  ↓
If one dies → ECS launches a replacement
```

Use a Service for:

* long-running web servers
* APIs
* background workers

Use a standalone Task for:

* one-off jobs
* batch processing
* migrations

---

# 3. Launch Types

## Fargate (Serverless)

```text
You define CPU and memory
  ↓
AWS provisions and manages the underlying compute
  ↓
No EC2 instances to manage
```

Good for:

* most modern workloads
* teams that don't want to manage servers
* variable or unpredictable load

---

## EC2 Launch Type

```text
You manage a pool of EC2 instances
  ↓
ECS places containers on those instances
```

Good for:

* GPU workloads
* very high throughput at lower cost
* workloads that need specific instance types

---

## Comparison

| Feature             | Fargate                    | EC2 Launch Type             |
| ------------------- | -------------------------- | --------------------------- |
| Server management   | None                       | You manage EC2 instances    |
| Cost model          | Per vCPU/memory used       | Per EC2 instance hour       |
| Startup time        | Slightly slower            | Faster (instances pre-warm) |
| GPU support         | No                         | Yes                         |
| Cost at scale       | Can be higher              | Can be lower with Reserved  |

Interview answer for "which launch type would you choose?":

> Fargate for most workloads — less operational overhead. EC2 launch type for GPU, compliance, or very high-scale cost optimization.

---

# 4. Networking

ECS tasks run inside a VPC.

## awsvpc Network Mode (recommended)

Each task gets its own Elastic Network Interface (ENI) and private IP.

```text
Task A → 10.0.1.5
Task B → 10.0.1.6
```

Benefits:

* security groups applied directly to tasks
* same networking model as EC2 instances
* required for Fargate

---

## Service + Load Balancer

Standard production pattern:

```text
Users
  ↓
Application Load Balancer
  ↓
ECS Service (multiple tasks across AZs)
```

ECS registers/deregisters tasks with the ALB automatically as they scale.

---

# 5. IAM Roles for ECS

Two separate roles matter:

## Task Execution Role

Used by ECS itself to:

* pull the Docker image from ECR
* write logs to CloudWatch

```text
ECS agent
  ↓
Task Execution Role
  ↓
Pull image, write logs
```

---

## Task Role

Used by your application code inside the container.

```text
App inside container
  ↓
Task Role
  ↓
Access S3, DynamoDB, SQS, etc.
```

Interview insight:

> Never hardcode AWS credentials in a container. The Task Role provides temporary credentials automatically via the container metadata endpoint.

---

# 6. ECR (Elastic Container Registry)

The AWS-native Docker image registry.

```text
docker build -t my-app .
docker push → ECR repository
  ↓
ECS pulls image from ECR at launch
```

Benefits over Docker Hub:

* private by default
* IAM-controlled access
* image scanning for vulnerabilities
* works natively with ECS/EKS

---

# 7. Auto Scaling

ECS Services can scale automatically.

Two levels of scaling:

## Service Auto Scaling

Adjusts the number of tasks in a Service.

```text
CPU > 70%
  ↓
Add more tasks
```

Policies:

* Target Tracking (keep metric at target)
* Step Scaling (scale by alarm threshold)

---

## Cluster Auto Scaling (EC2 launch type only)

Adjusts the number of EC2 instances in the cluster.

```text
Tasks can't be placed (no capacity)
  ↓
Add EC2 instances to cluster
```

With Fargate this is not needed — AWS handles it.

---

# 8. Logging

ECS tasks send logs to CloudWatch Logs via the `awslogs` log driver.

Task Definition config:

```json
"logConfiguration": {
  "logDriver": "awslogs",
  "options": {
    "awslogs-group": "/ecs/web-app",
    "awslogs-region": "us-east-1",
    "awslogs-stream-prefix": "web"
  }
}
```

Each container writes to its own log stream.

---

# 9. Common Architecture

```text
ECR (image registry)
  ↓
ECS Cluster (Fargate)
  ↓
ECS Service
  ↓
Tasks in multiple AZs
  ↓
ALB distributes traffic
  ↓
RDS / DynamoDB (data layer)
```

This covers:

* container deployment
* high availability
* auto scaling
* secure networking

---

# 10. ECS vs Kubernetes

This is one of the most common interview questions for any container/DevOps role.

---

## What They Share

Both solve the same core problem:

```text
Run containers at scale
  ↓
Handle scheduling, health checks, scaling, networking
```

---

## ECS

```text
AWS-native
Simpler to operate
Tight integration with AWS services
Less control over internals
```

---

## Kubernetes (EKS on AWS)

```text
Open standard, portable
More complex
Greater control and extensibility
Larger ecosystem (Helm, Istio, Argo CD, etc.)
```

---

## Head-to-Head Comparison

| Dimension              | ECS                              | Kubernetes (EKS)                        |
| ---------------------- | -------------------------------- | --------------------------------------- |
| Learning curve         | Low                              | High                                    |
| Operational overhead   | Low (especially with Fargate)    | High (even managed control plane needs work) |
| Portability            | AWS only                         | Any cloud or on-prem                    |
| Ecosystem              | AWS services                     | CNCF ecosystem (Helm, Istio, etc.)      |
| Networking             | Simpler (awsvpc)                 | More powerful (CNI plugins, service mesh) |
| Scheduling             | Basic                            | Advanced (affinities, taints, etc.)     |
| Custom resource types  | No                               | Yes (CRDs)                              |
| Cost                   | No control plane cost            | EKS control plane ~$72/month            |
| Multi-cloud/hybrid     | No                               | Yes                                     |
| Community              | AWS-only                         | Massive open-source community           |

---

## When to Choose ECS

```text
Team is AWS-focused and doesn't need portability
Speed of delivery matters more than flexibility
Running Fargate → zero infra management
Strong AWS service integrations needed (ALB, IAM, CloudWatch)
Smaller team or org that wants simplicity
```

---

## When to Choose Kubernetes

```text
Multi-cloud or hybrid cloud strategy
Need advanced scheduling (GPU nodes, spot mixed fleets)
Require service mesh (Istio, Linkerd)
Already have Kubernetes expertise in the team
Need custom resource types (CRDs) or operators
Platform team that can absorb the complexity
```

---

## The Honest Trade-off

ECS:

> Lower operational cost, less flexibility. Right for most AWS-native teams.

Kubernetes:

> Higher operational cost, much greater power. Right for large platforms or multi-cloud strategies.

Strong interview answer if asked:

> I'd default to ECS with Fargate for most new AWS projects — it removes the cluster management burden and integrates tightly with ALB, IAM, and CloudWatch. I'd choose EKS when the team needs portability across clouds, advanced scheduling, or a service mesh that ECS can't provide natively.

---

# 11. Common Interview Questions

* What is the difference between a Task and a Service in ECS?
* What is the difference between Fargate and EC2 launch types?
* How do containers in ECS access AWS services securely?
* How does ECS handle a failed task?
* How would you scale an ECS Service?
* What is the difference between the Task Execution Role and the Task Role?
* When would you use ECS over Kubernetes?
* How does ECS integrate with a load balancer?
* Where are ECS container logs stored?
* What is ECR and why use it instead of Docker Hub?

---

# 12. The Big Picture Mental Model

Think of ECS as:

```text
Docker image → define what runs (Task Definition)
  ↓
Service → define how many run and where
  ↓
Fargate → AWS handles the servers
  ↓
ALB + auto scaling → handle traffic at any scale
```

That model answers almost every ECS interview question.
