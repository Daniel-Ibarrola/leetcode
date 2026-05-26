# RAG (Retrieval-Augmented Generation)

Augment an LLM's response with relevant context retrieved from an external knowledge source. Addresses the key LLM limitations: knowledge cutoff, hallucination, and lack of private/domain knowledge.

---

## The Problem RAG Solves

LLMs have a training cutoff and don't know about your proprietary data. Without RAG:
- "What are our Q3 revenue figures?" → LLM hallucinates.
- "What does our internal policy say about X?" → LLM doesn't know.
- "What happened in the news yesterday?" → LLM's knowledge is stale.

---

## Core Flow

```
[User query]
    → [Retriever]: embed query → ANN search → top-K relevant documents
    → [Augmentation]: inject retrieved docs into LLM prompt
    → [LLM]: generates answer grounded in the retrieved context
    → [Response]
```

---

## Components

### Knowledge Base
The corpus of documents the retriever searches over.
- Internal docs, PDFs, wikis, database records, web pages.
- Must be preprocessed: chunked, embedded, indexed.

### Document Chunking
Split documents into smaller pieces before embedding.
- Chunk too large → noisy, irrelevant content in context; hits token limits.
- Chunk too small → loses context (a sentence without its paragraph is ambiguous).
- Typical: 256–512 tokens per chunk, with overlap (e.g., 50 tokens) to avoid cutting sentences mid-thought.

### Retriever
Embeds the query and finds the most relevant chunks via ANN search in a vector DB.
- Uses the same embedding model as the indexing step.
- Returns top-K chunks (K typically 3–10).

### Reranker (Optional)
After retrieval, rerank the candidates with a more accurate (but slower) cross-encoder model.
- Cross-encoder scores query + document together → more accurate relevance judgment.
- Only runs on the small retrieved set (affordable at K=10–20).

### LLM
Receives the query + retrieved chunks as context. Generates the final answer.
- System prompt instructs the LLM to use only the provided context.
- Temperature low (0–0.3) for factual, grounded answers.

---

## Indexing Pipeline (Offline)

```
[Documents] → [Chunking] → [Embedding model] → [Vector DB index]
```

Must be re-run when documents are added or updated.

---

## Query Pipeline (Online)

```
[Query] → [Embed query] → [ANN search] → [Rerank (optional)]
       → [Build prompt with context] → [LLM] → [Answer]
```

---

## Key Design Decisions

| Decision | Options | Trade-off |
|---|---|---|
| Chunk size | Small (128T) vs large (1024T) | Precision vs context richness |
| K (retrieved chunks) | 3–20 | More context vs token limit / distraction |
| Embedding model | OpenAI, BGE, Cohere | API cost vs self-hosted control |
| Reranker | Cross-encoder vs none | Better relevance vs added latency |
| Vector DB | Pinecone, pgvector, Chroma | Managed simplicity vs control |

---

## Failure Modes

- **Retrieval fails**: wrong chunks retrieved → LLM answers with wrong context or hallucinates.
- **Context too long**: retrieved chunks hit token limit → truncation loses key info.
- **Stale index**: document updated but not re-indexed → outdated answer.
- **LLM ignores context**: LLM falls back to parametric knowledge despite retrieved evidence.

---

## Evaluation

RAG systems have two evaluation targets:
1. **Retrieval quality**: Did we retrieve the right chunks? (Recall@K, MRR)
2. **Generation quality**: Is the answer correct and grounded in the context? (Faithfulness, answer relevance)

Tools: RAGAS, TruLens.

---

## Trade-offs

| RAG | Grounded, updatable without retraining | Adds retrieval latency; quality depends on retrieval |
| Fine-tuning | Bakes knowledge into model | Expensive; knowledge goes stale |
| Prompting alone | Simple | LLM doesn't have the knowledge |
