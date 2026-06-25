# System Design: Online Banking Platform

## Problem

Design an online banking platform with scope similar to a credit card application system.

## Requirements

**Functional:**
- Allow new customers to apply for a credit card account (identity verification, credit check, approval workflow)
- Authenticated customers can log in and view account details, statements, and transaction history
- Customers can make payments toward their balance
- Customers can dispute a charge
- Send notifications (email, SMS, push) for account events (payment due, transaction posted, dispute status)
- Administrators can view and manage accounts

**Non-functional:**
- Secure authentication and authorization (MFA support)
- PII and financial data must be encrypted at rest and in transit
- The platform must meet regulatory compliance requirements (PCI-DSS, SOC 2)
- High availability — 99.99% uptime target
- The system must handle millions of concurrent users, with peak traffic around statement close dates and payment due dates
- All user actions must produce a tamper-evident audit trail
