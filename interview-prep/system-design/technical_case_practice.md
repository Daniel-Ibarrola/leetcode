# Technical Case Interview — Practice Session

> **Format:** Read each section, write your answer below the prompt, then move on. After you finish, I'll review your responses.
> 
> **Remember:** Think out loud — explain *what*, *why*, and *how*. Keep business context in mind alongside technical choices.

---

## Case Scenario

**Client:** A large e-commerce marketplace (think Amazon-scale) with millions of daily active users.

**Background:** The data science team built a Proof of Concept (POC) for a real-time product recommendation engine. The system ingests clickstream events, runs a collaborative filtering model, and returns the top-5 recommended products to display on the homepage. During lab tests it performed well, but in a limited production rollout it struggles to serve more than **500 recommendations per second** with P99 latency exceeding 2 seconds — far above the acceptable 200ms SLA.

The client wants to scale to handle **50,000 recommendations per second** during peak shopping events (Black Friday, flash sales).

---

## Part 1 — Problem Framing (5 min)

Before jumping into solutions, make sure you understand the problem.

**Prompt:**
1. Restate the core problem in your own words.
2. List **3–5 clarifying questions** you would ask the interviewer — both from a business and engineering perspective.
3. State any assumptions you are making to proceed.

> **Your answer:**

> The recommendation system isn't able to scale to 500 RPS. Our goal is to be able to increase to 50k RPS during peak shopping events.
> - What is the current architecture of the POC?
> - How does the recommendation system interact with other systems in the e-commerce platform?
> - What are the current limitations of the recommendation system in terms of scalability and performance?

---

## Part 2 — High-Level Architecture (10 min)


23inteRestella-rC0yote

**Prompt:**
1. Describe the high-level components of your solution (you can use a bullet-point diagram or ASCII art).
2. Identify the main bottleneck in the POC and explain why it can't scale as-is.
3. What architectural pattern(s) would you apply to reach the 50k RPS target?

> **Your answer:**
>
> *(Write here)*

---

## Part 3 — Deep Dive on a Key Component (8 min)

Choose **one** of the following to go deep on:

- **A)** The feature store / data pipeline feeding the model
- **B)** The serving layer (inference + caching)
- **C)** The monitoring & feedback loop

**Prompt:**
1. Explain your chosen component in detail: data flow, technology choices, and trade-offs.
2. Justify why this component is the most critical to get right.
3. Name one thing you would *not* do and why.

> **Your answer:**
>
> *(Write here)*

---

## Part 4 — Operational & Business Considerations (5 min)

**Prompt:**
1. How would you roll this out safely? Describe a deployment strategy.
2. What metrics would you monitor to declare success (both technical and business KPIs)?
3. Estimate the order-of-magnitude infrastructure cost change (relative to the POC). You don't need exact numbers — explain your reasoning.

> **Your answer:**
>
> *(Write here)*

---

## Part 5 — Wrap-Up Recommendation (2 min)

**Prompt:**
Summarize your proposed solution in 3–5 sentences as if presenting to a non-technical client executive. Cover: what you're building, why it solves the problem, and what the next step is.

> **Your answer:**
>
> *(Write here)*

---

## Interviewer Review

*(This section will be filled in after you submit your answers.)*

| Section | Score (1–5) | Feedback |
|---------|-------------|----------|
| Problem Framing | | |
| High-Level Architecture | | |
| Deep Dive | | |
| Operational & Business | | |
| Executive Summary | | |
| **Overall** | | |

### Strengths

*(To be filled)*

### Areas to Improve

*(To be filled)*

### Model Answer Notes

*(To be filled)*



