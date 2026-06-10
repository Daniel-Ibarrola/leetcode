# VPC Fundamentals

> Amazon Virtual Private Cloud VPC is your private network inside AWS.

Everything eventually connects back to networking:

* EC2
* EKS
* RDS
* Lambda (when attached to a VPC)
* Load Balancers

Many AWS interviews eventually become VPC interviews because architecture decisions often depend on networking.

---

# 1. Mental Model

Think of a VPC as:

```text
your own private datacenter network in AWS
```

You define:

* IP ranges
* subnets
* routing
* internet access
* security rules

---

# 2. Basic VPC Architecture

A common setup:

```text
VPC (10.0.0.0/16)

├── Public Subnet
│   ├── Load Balancer
│   └── Bastion Host
│
├── Private Subnet
│   ├── Application Servers
│   ├── EKS Nodes
│   └── Lambda
│
└── Private DB Subnet
    └── RDS
```

This pattern appears constantly in interviews.

---

# 3. CIDR Blocks

Every VPC gets an IP range.

Example:

```text
10.0.0.0/16
```

This means:

```text
10.0.x.x
```

available within the VPC.

Interviewers rarely ask you to calculate exact address counts, but you should understand CIDR notation conceptually.

---

# 4. Subnets

Subnets divide a VPC into smaller networks.

Example:

```text
VPC: 10.0.0.0/16

Public Subnet:
10.0.1.0/24

Private Subnet:
10.0.2.0/24

DB Subnet:
10.0.3.0/24
```

Subnets live within a single Availability Zone.

Important interview point:

> A subnet cannot span multiple AZs.

---

# 5. Availability Zones

An AZ is an isolated datacenter.

Example in a region:

```text
us-east-1a
us-east-1b
us-east-1c
```

High availability architecture:

```text
Public Subnet A
Public Subnet B

Private Subnet A
Private Subnet B
```

spread across multiple AZs.

---

# 6. Public vs Private Subnets

This is one of the most common AWS interview topics.

---

## Public Subnet

Has a route to the Internet Gateway.

Resources can be reachable from the internet.

Examples:

* ALB
* Bastion hosts
* Public web servers

---

## Private Subnet

No direct internet route.

Examples:

* RDS
* Internal services
* EKS worker nodes
* Application servers

Best practice:

> Databases should almost always be in private subnets.

---

# 7. Internet Gateway (IGW)

Provides internet connectivity for the VPC.

Architecture:

```text
Internet
    |
Internet Gateway
    |
Public Subnet
```

Without an IGW:

```text
no internet access
```

---

# 8. Route Tables

Route tables determine where traffic goes.

Example:

```text
Destination      Target

10.0.0.0/16      local
0.0.0.0/0        IGW
```

Meaning:

```text
internal traffic -> local
everything else -> internet
```

Every subnet is associated with a route table.

---

# 9. NAT Gateway

Extremely common interview topic.

Problem:

```text
Private Subnet
```

needs outbound internet access for:

* updates
* package downloads
* AWS API calls

but should not be publicly reachable.

Solution:

> AWS NAT Gateway

---

Architecture:

```text
Private Subnet
    |
NAT Gateway
    |
Internet Gateway
    |
Internet
```

Key point:

```text
outbound allowed
inbound blocked
```

Interviewers ask this constantly.

---

# 10. Security Groups

Probably the most important VPC security concept.

Think:

```text
instance firewall
```

Security groups are:

```text
stateful
```

Meaning:

If inbound traffic is allowed:

```text
return traffic automatically allowed
```

---

Example:

Allow:

```text
TCP 443
from ALB
```

Common production pattern.

---

# 11. Network ACLs (NACLs)

Another layer of security.

Think:

```text
subnet firewall
```

Unlike security groups:

```text
stateless
```

Meaning:

* inbound rules required
* outbound rules required

---

Interview shortcut:

| Security Group    | NACL         |
| ----------------- | ------------ |
| Stateful          | Stateless    |
| Resource level    | Subnet level |
| Usually used more | Less common  |

---

# 12. Security Group Example

Web server:

Inbound:

```text
443 from internet
```

Outbound:

```text
all traffic
```

Database:

Inbound:

```text
5432 from app security group
```

Outbound:

```text
all traffic
```

Notice:

```text
DB not exposed publicly
```

Very common architecture question.

---

# 13. VPC Endpoints

Huge topic in modern AWS architectures.

Without endpoint:

```text
EC2
-> Internet
-> S3
```

With endpoint:

```text
EC2
-> AWS private network
-> S3
```

Benefits:

* more secure
* lower latency
* no NAT costs

Common services:

* S3
* DynamoDB

---

# 14. VPC Peering

Connects two VPCs.

Example:

```text
VPC A <-> VPC B
```

Private communication.

Limitations:

* non-transitive

Meaning:

```text
A -> B
B -> C

does NOT imply

A -> C
```

Interview favorite.

---

# 15. Transit Gateway

Used when many VPCs exist.

Instead of:

```text
A <-> B
A <-> C
B <-> C
```

mesh networking,

you create:

> AWS Transit Gateway

```text
A
 \
  TGW
 /
B
 \
  C
```

Much easier to manage.

---

# 16. Load Balancers and VPCs

Typically:

```text
Internet
-> ALB
-> Private Services
```

Public-facing load balancer.

Private application services.

Very common design.

---

# 17. RDS Networking

Typical production setup:

```text
Private Subnet A
Private Subnet B

RDS Multi-AZ
```

No public access.

Access only through security groups.

Interviewers expect this answer.

---

# 18. Lambda and VPC

By default:

```text
Lambda
```

runs outside your VPC.

Attach Lambda to VPC only when needed.

Example:

```text
Lambda -> RDS
```

requires VPC access.

Interview point:

> Putting Lambda in a VPC increases networking complexity.

---

# 19. EKS Networking

In EKS:

```text
pods receive VPC IPs
```

through the VPC CNI.

This is why IP exhaustion can become a real operational issue in large clusters.

Senior-level topic.

---

# 20. Common Interview Architecture

A classic answer:

```text
Internet
    |
ALB (Public Subnet)
    |
Application Tier (Private Subnet)
    |
RDS (Private DB Subnet)
```

This architecture demonstrates:

* security
* scalability
* separation of concerns

---

# 21. Common Interview Questions

Be ready for:

### What is a VPC?

Private virtual network in AWS.

---

### Difference between public and private subnet?

Public:

* route to IGW

Private:

* no route to IGW

---

### Why use a NAT Gateway?

Allow outbound internet from private resources.

---

### Security Group vs NACL?

Stateful vs stateless.

---

### Why put RDS in private subnets?

Security.

---

### What is a VPC Endpoint?

Private access to AWS services.

---

### What is VPC Peering?

Private connection between VPCs.

---

### When use Transit Gateway?

Large multi-VPC architectures.

---

# 22. The Architecture Answer Interviewers Love

If asked:

> "Design a secure web application."

A strong high-level answer is:

```text
Internet
-> ALB (public subnet)

-> App servers/EKS (private subnets)

-> RDS (private DB subnets)

NAT Gateway for outbound traffic

Security groups restricting access
```

That answer touches:

* VPC
* subnets
* routing
* security
* high availability

which is exactly what interviewers want to hear.

---

# 23. Key Mental Model

Think of a VPC as:

```text
the networking foundation for everything in AWS
```

And think of the major components like this:

```text
VPC          = network

Subnet       = neighborhood

Route Table  = road map

IGW          = highway to internet

NAT Gateway  = outbound-only internet access

Security Group = resource firewall

NACL         = subnet firewall
```
