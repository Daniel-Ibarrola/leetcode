# Two-Tower Architecture

A neural network design for large-scale retrieval and matching problems: recommendations, semantic search, ads targeting.

---

## The Problem

You have millions of users and millions of items. You need to find the top-K items most relevant to each user. You can't run a full model on every (user, item) pair — that's O(users × items) at inference time.

---

## The Architecture

Two separate neural networks (towers) that encode the query side and the candidate side independently.

```
[User features] → [User Tower] → user embedding (e.g., 128-dim vector)

[Item features] → [Item Tower] → item embedding (e.g., 128-dim vector)

Score = dot_product(user_embedding, item_embedding)
```

**Key insight**: the towers are independent. You can pre-compute all item embeddings offline, store them in a vector DB, and at serving time only run the user tower.

---

## Training

Trained with **contrastive learning**:
- **Positive pair**: (user, item they interacted with) → score should be high.
- **Negative pair**: (user, random item) → score should be low.

The model learns to place users near items they like in the embedding space.

**Hard negatives**: randomly sampled negatives are too easy. Mix in "hard negatives" — items the user almost interacted with — for better model quality.

---

## Serving: Two-Stage Retrieval + Ranking

```
Stage 1 — Retrieval (Two-Tower ANN)
  User embedding → ANN search in item vector DB → top-500 candidates

Stage 2 — Ranking (Heavy Model)
  (user, candidate_item) pairs → full feature set → ranking model → top-10
```

- **Retrieval**: fast, approximate, returns hundreds of candidates.
- **Ranking**: accurate, expensive, runs only on the small candidate set.

This is the standard architecture at Google, YouTube, Pinterest, Twitter, LinkedIn.

---

## Offline vs Online Computation

| Component | When Computed |
|---|---|
| Item embeddings | Offline (batch), updated periodically |
| User embeddings | Online (at request time) or near-real-time |
| ANN index | Rebuilt periodically (daily or hourly) |
| Ranking model inference | Online, per candidate item |

---

## When to Update Embeddings

- **Items**: when item content changes significantly. Batch update overnight or on change events.
- **Users**: depends on freshness requirement. Some systems update user embeddings every hour (streaming), others per session.

---

## Trade-offs

| Pro | Con |
|---|---|
| Scales to millions of items (ANN search) | Two separate models to train and maintain |
| User tower runs once per request | Item embeddings can become stale |
| Item embeddings pre-computed (cheap serving) | Contrastive training requires careful negative sampling |
| Flexible: towers can have different architectures | Retrieval stage uses approximate matching — not perfect |

---

## Variations

- **Single tower**: same encoder for both query and document (used in symmetric semantic search).
- **Asymmetric towers**: different-sized networks for query vs. document (query encoder must be fast; document encoder can be large since it runs offline).
- **Multi-task towers**: shared tower with task-specific heads (simultaneously optimize for clicks and purchases).
