# IAM Fundamentals

> AWS Identity and Access Management IAM controls:
>
> **Who can do what on which resources under what conditions.**

This is one of the highest-signal AWS interview topics because security mistakes are expensive.

---

# 1. Core IAM Concepts

There are 4 things to know first:

| Concept | Meaning                      |
| ------- | ---------------------------- |
| User    | Person/app identity          |
| Group   | Collection of users          |
| Role    | Temporary assumable identity |
| Policy  | Permissions document         |

---

# 2. IAM Users

Represents a person or application.

Example:

* developer account
* CI/CD bot
* legacy app

Users can have:

* password
* access keys
* policies

Interview reality:

> Modern AWS best practice is to avoid long-lived IAM users when possible.

Companies prefer:

* SSO
* roles
* temporary credentials

---

# 3. IAM Groups

Groups simplify permission management.

Example:

```text id="d4fwhd"
Developers
Admins
ReadOnlyUsers
```

You attach policies to groups instead of individually to users.

---

# 4. IAM Policies

Policies define permissions.

JSON document with:

* Effect
* Action
* Resource
* optional Condition

Example:

```json id="f57l9m"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

---

# 5. Important Policy Elements

## Effect

```text id="chmvnn"
Allow
Deny
```

---

## Action

What operation is allowed.

Examples:

```text id="ndcb5u"
s3:GetObject
ec2:StartInstances
lambda:InvokeFunction
```

Wildcard:

```text id="ryft0l"
s3:*
```

---

## Resource

What resource applies.

Example:

```text id="jz8i1r"
arn:aws:s3:::my-bucket/*
```

---

## Condition

Extra rules.

Example:

* IP restrictions
* MFA required
* time-based access

Example:

```json id="13uk5t"
"Condition": {
  "Bool": {
    "aws:MultiFactorAuthPresent": "true"
  }
}
```

---

# 6. Explicit Deny Wins

This is extremely important.

Evaluation logic:

1. Explicit deny
2. Explicit allow
3. Implicit deny (default)

If:

* one policy allows
* another explicitly denies

→ DENY wins.

Interviewers ask this constantly.

---

# 7. IAM Roles

Probably the most important IAM concept.

A role is:

> a temporary identity that can be assumed.

Used everywhere in AWS.

---

# 8. Why Roles Matter

Without roles:

* apps need stored credentials
* secrets become dangerous

With roles:

* AWS issues temporary credentials automatically

Much safer.

---

# 9. Common Role Examples

## EC2 Role

EC2 instance accesses S3.

```text id="z7hx1m"
EC2 -> Assume role -> Access S3
```

No hardcoded keys needed.

---

## Lambda Execution Role

Function gets permissions:

* DynamoDB
* S3
* CloudWatch

---

## Cross-Account Role

Account A assumes role in Account B.

Very common enterprise setup.

---

# 10. Trust Policy vs Permission Policy

Huge interview topic.

## Trust Policy

Defines:

> WHO can assume the role

Example:

```json id="gqov3n"
{
  "Effect": "Allow",
  "Principal": {
    "Service": "ec2.amazonaws.com"
  },
  "Action": "sts:AssumeRole"
}
```

---

## Permission Policy

Defines:

> WHAT the role can do after assuming

Example:

```json id="f1j8wt"
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "*"
}
```

This distinction matters a lot.

---

# 11. Temporary Credentials

Roles use:

> AWS Security Token Service (STS)

STS generates:

* temporary access key
* secret key
* session token

Benefits:

* auto expiration
* reduced blast radius

---

# 12. Principle of Least Privilege

Security best practice:

> Give only minimum required permissions.

Bad:

```text id="tqop8m"
AdministratorAccess
```

Better:

```text id="m1n7ov"
s3:GetObject on one bucket only
```

This phrase appears in almost every AWS interview.

---

# 13. Managed vs Inline Policies

## AWS Managed

Created by AWS.

Example:

```text id="x7r8c0"
AmazonS3ReadOnlyAccess
```

---

## Customer Managed

Created by organization.

Reusable.

Preferred for production.

---

## Inline Policies

Attached directly to one identity.

Less reusable.

---

# 14. Resource-Based Policies

Some AWS services support policies attached directly to resources.

Examples:

* S3 bucket policy
* Lambda resource policy

This differs from identity-based IAM policies.

---

# 15. Authentication vs Authorization

Interview favorite.

## Authentication

Who are you?

Example:

```text id="4u9m6u"
login/password/MFA
```

---

## Authorization

What can you do?

Controlled by IAM policies.

---

# 16. MFA

Multi-factor authentication.

Critical for:

* root account
* admin users

Interview-safe statement:

> MFA dramatically reduces account compromise risk.

---

# 17. Root Account

The AWS account root user:

* has unlimited permissions
* should rarely be used

Best practice:

* enable MFA
* lock it away

Interviewers like hearing:

> “Never use root for daily operations.”

---

# 18. Common Permission Problems

You should understand:

* missing permissions
* wrong resource ARN
* explicit deny
* trust relationship failures
* SCP restrictions (Organizations)

---

# 19. IAM Policy Evaluation (Simplified)

AWS evaluates:

* identity policies
* resource policies
* SCPs
* permission boundaries
* session policies

But for interviews:

```text id="f8o3u0"
Explicit deny > allow > default deny
```

is usually enough unless it’s a senior/cloud-security role.

---

# 20. IAM in Real Architectures

## Example: Web App Uploading to S3

```text id="4z9zll"
User uploads file
-> backend authenticates user
-> backend generates pre-signed URL
-> client uploads directly to S3
```

IAM role permissions:

```text id="u7xhva"
Backend role:
s3:PutObject
```

---

## Example: Lambda Reading DynamoDB

```text id="6j5z8u"
Lambda execution role
-> dynamodb:GetItem
```

No credentials stored in code.

---

# 21. High-Value Interview Topics

You should confidently explain:

* IAM user vs role
* Why roles are preferred
* Least privilege
* Explicit deny precedence
* Temporary credentials
* Trust policy vs permission policy
* Identity vs resource policies
* How EC2 accesses S3 securely
* Why hardcoded keys are bad

---

# 22. Extremely Common Interview Question

> “How would an EC2 instance securely access S3?”

Correct high-level answer:

1. Create IAM role
2. Attach S3 permissions
3. Attach role to EC2 instance
4. EC2 automatically receives temporary credentials via metadata service

That answer alone signals real AWS understanding.

---

# 23. One Mental Model That Helps

Think of IAM like:

```text id="7p5o6r"
Authentication = identity
Authorization = policies
Roles = temporary identities
STS = credential vending machine
```
