# System Design: Virtual Credit Card Product

## Problem

Design a system that issues and manages virtual credit cards for customers.

## Requirements

**Functional:**
- Generate a unique virtual card number (PAN), expiry date, and CVV on demand for a customer
- Associate each virtual card with the customer's underlying physical card or account
- Allow customers to set per-card spending limits, merchant restrictions, or expiry dates
- Support one-time-use and recurring-use virtual cards
- Allow customers to freeze, unfreeze, or permanently cancel a virtual card
- Ensure that charges made to a virtual card are routed and settled against the linked account

**Non-functional:**
- Card numbers must conform to the Luhn algorithm and card network (Visa/Mastercard) standards
- Card credentials must be stored and transmitted with PCI-DSS compliance
- Issuance must be near-instant (sub-second response to the customer)
- The system must support millions of active virtual cards per customer cohort
- Audit log every action taken on a virtual card (creation, update, deletion, transaction)
