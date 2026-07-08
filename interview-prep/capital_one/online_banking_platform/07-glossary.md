# 7. Glossary

Terms referenced throughout this design that are worth defining explicitly.

## KYC (Know Your Customer)

The identity-verification process required before onboarding a customer: confirms
the applicant is who they claim to be (name, DOB, address, SSN match) and screens
them against sanctions/watchlists (OFAC, PEP). Legally mandated under the Bank
Secrecy Act / AML regulations — an account cannot be opened without it. In this
design it's the first step of the [onboarding workflow](06-detailed-design.md#61-onboarding-workflow),
run as a slow, auditable third-party call rather than inline validation, so a
failure here rejects the application before the more expensive credit-bureau
pull happens.

## PCI-DSS (Payment Card Industry Data Security Standard)

A security standard mandated by the card networks for anyone who stores,
processes, or transmits cardholder data (PAN, expiration date, CVV, cardholder
name). Requires encryption in transit/at rest, network segmentation, restricted
access, and regular audits. Compliance scope is defined by *what touches card
data* — which is why this design tokenizes the PAN in an isolated vault
([03-storage-schema.md](03-storage-schema.md), [06-detailed-design.md](06-detailed-design.md#65-adminsecurity-controls))
so only that small enclave carries the full audit burden.

## SOC 2 (System and Organization Controls 2)

A broader attestation standard (AICPA) certifying an organization's internal
controls across security, availability, processing integrity, confidentiality,
and privacy. Unlike PCI-DSS's fixed card-data checklist, an auditor reviews
actual operational controls — access reviews, change management, incident
response, logging — over a period. Concrete controls in this design that map to
SOC 2 (§6.5): least-privilege IAM roles, four-eyes approval on admin actions,
and the tamper-evident audit log.

## Dispute

A customer's formal challenge to a specific charge ("I don't agree this
transaction should stand"), which triggers a regulated investigation rather than
a simple refund. Reasons include fraud, non-receipt, duplicate charges, or
incorrect amounts. Regulated under Reg E (electronic transfers) / Reg Z (credit
cards) with mandatory bank timelines, including **provisional credit** — a
temporary credit issued to the customer before the investigation concludes,
reversed via a compensating ledger entry if the merchant's evidence prevails.
Modeled as a timed state machine in [06-detailed-design.md §6.2](06-detailed-design.md#62-dispute-workflow).
