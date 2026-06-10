Absolutely. For a DevOps or Cloud Engineer interview, Terraform questions usually focus on **core concepts, state management, infrastructure lifecycle, modules, and collaboration practices** rather than memorizing syntax.

---

# 1. What is Terraform?

Terraform is an **Infrastructure as Code (IaC)** tool created by HashiCorp.

It allows you to define infrastructure declaratively and provision resources across cloud providers such as:

* AWS
* Azure
* GCP
* Kubernetes
* GitHub
* Databases
* SaaS platforms

Example:

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "my-app-logs"
}
```

Terraform compares:

**Current State → Desired State**

and generates an execution plan.

---

# 2. Terraform Workflow

Interviewers often ask:

> "Walk me through a typical Terraform deployment."

Answer:

### Initialize

```bash
terraform init
```

Downloads providers and modules.

---

### Validate

```bash
terraform validate
```

Checks syntax and configuration.

---

### Plan

```bash
terraform plan
```

Shows what changes will occur.

Example:

```txt
+ create S3 bucket
~ modify security group
- destroy EC2 instance
```

No changes are made yet.

---

### Apply

```bash
terraform apply
```

Executes the plan.

---

### Destroy

```bash
terraform destroy
```

Removes resources.

---

# 3. State File (Very Important)

Terraform keeps track of infrastructure using:

```txt
terraform.tfstate
```

This is one of the most common interview topics.

The state file stores:

* Resource IDs
* Metadata
* Dependencies
* Current infrastructure mapping

Example:

```txt
aws_instance.web
   -> i-123456789
```

Without state, Terraform wouldn't know which AWS resource corresponds to which Terraform resource.

---

## Why not query AWS every time?

Terraform needs to know:

* what it created
* dependencies
* relationships
* previous configuration

State provides this.

---

# 4. Local vs Remote State

Bad:

```txt
terraform.tfstate
```

stored on your laptop.

Problems:

* team conflicts
* lost state
* no locking

---

Good:

Store remotely.

AWS example:

```hcl
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "prod.tfstate"
    region = "us-east-1"
  }
}
```

Typically paired with:

```txt
S3 + DynamoDB
```

Historically DynamoDB was used for state locking.

Interview answer:

> We store state remotely in S3 to allow team collaboration and state durability.

---

# 5. What Happens During terraform plan?

Terraform:

1. Reads configuration
2. Reads state
3. Queries provider APIs
4. Computes differences
5. Generates execution plan

Example:

Current:

```txt
instance_type=t2.micro
```

Desired:

```txt
instance_type=t3.micro
```

Plan:

```txt
~ update in place
```

---

# 6. Resources vs Data Sources

Very common interview question.

---

## Resource

Terraform creates/manages it.

```hcl
resource "aws_vpc" "main" {
}
```

Terraform owns it.

---

## Data Source

Terraform reads existing infrastructure.

```hcl
data "aws_vpc" "existing" {
  id = "vpc-123"
}
```

Terraform does not create it.

---

Interview answer:

> Resources are managed by Terraform. Data sources allow Terraform to reference existing infrastructure.

---

# 7. Variables

Example:

```hcl
variable "environment" {
  type = string
}
```

Usage:

```hcl
tags = {
  Environment = var.environment
}
```

Set value:

```bash
terraform apply -var="environment=prod"
```

---

## tfvars

Usually:

```txt
dev.tfvars
prod.tfvars
```

Example:

```hcl
environment = "prod"
instance_count = 3
```

Apply:

```bash
terraform apply -var-file=prod.tfvars
```

---

# 8. Outputs

Expose useful information.

```hcl
output "alb_dns" {
  value = aws_lb.main.dns_name
}
```

After apply:

```txt
alb_dns = my-alb.amazonaws.com
```

Useful in pipelines.

---

# 9. Dependencies

Terraform automatically builds a dependency graph.

Example:

```hcl
resource "aws_subnet" "app" {
  vpc_id = aws_vpc.main.id
}
```

Terraform knows:

```txt
VPC
 ↓
Subnet
```

VPC created first.

---

## Explicit Dependency

```hcl
depends_on = [
  aws_vpc.main
]
```

Used when Terraform cannot infer relationships.

---

# 10. Modules

A module is reusable Terraform code.

Think:

```txt
Function
```

for infrastructure.

Example:

```hcl
module "network" {
  source = "./modules/network"
}
```

The module may create:

* VPC
* Subnets
* Route tables
* NAT gateways

---

Interview question:

> Why use modules?

Answer:

* Reusability
* Consistency
* Reduced duplication
* Easier maintenance

---

# 11. Workspaces

Allow multiple state files from one configuration.

Example:

```bash
terraform workspace new dev
terraform workspace new prod
```

Each workspace has separate state.

---

Interview caveat:

Large organizations often prefer:

```txt
separate folders/repos
```

over workspaces for environment separation.

---

# 12. Drift Detection

Infrastructure drift occurs when someone changes resources manually.

Example:

```txt
Terraform says:
t3.micro

Engineer changes:
t3.large
```

Next plan:

```txt
~ revert t3.large -> t3.micro
```

Terraform detects drift by comparing:

```txt
State
vs
Actual Infrastructure
vs
Configuration
```

---

# 13. Import Existing Resources

Sometimes resources already exist.

```bash
terraform import aws_s3_bucket.logs my-bucket
```

This:

* imports state
* does NOT generate code

You still must write the resource block.

---

# 14. Lifecycle Rules

Useful interview topic.

Prevent accidental destruction:

```hcl
lifecycle {
  prevent_destroy = true
}
```

---

Create replacement before destruction:

```hcl
lifecycle {
  create_before_destroy = true
}
```

Useful for:

* load balancers
* databases
* production systems

---

# 15. CI/CD Integration

A common DevOps interview question:

> How would Terraform fit into a pipeline?

Typical flow:

```txt
Git Push
   ↓
Lint
   ↓
terraform validate
   ↓
terraform plan
   ↓
Approval
   ↓
terraform apply
```

The plan artifact is often reviewed before apply.

---

# 16. Terraform vs CloudFormation

Terraform:

* Multi-cloud
* Huge provider ecosystem
* Declarative
* More portable

CloudFormation:

* AWS-only
* Native AWS integration
* AWS support

For AWS-focused companies you'll often see both.

---

# Interview Questions You Should Be Ready For

### What is Terraform state?

Stores mappings between Terraform configuration and real infrastructure.

---

### Why use remote state?

Collaboration, durability, consistency, and state locking.

---

### Difference between resource and data source?

Resources are managed by Terraform; data sources read existing infrastructure.

---

### What does terraform plan do?

Calculates changes needed to reach desired state without modifying infrastructure.

---

### How do you manage multiple environments?

Modules + environment-specific variables, separate state, and typically separate deployment pipelines.

---

### What is infrastructure drift?

Manual changes outside Terraform causing actual infrastructure to differ from declared configuration.
