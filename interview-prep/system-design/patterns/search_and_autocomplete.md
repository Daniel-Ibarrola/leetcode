# Search & Autocomplete

Two related but distinct problems: **full-text search** (find documents matching a query) and **autocomplete** (suggest completions as a user types).

---

## Full-Text Search

### How It Works: Inverted Index
Map each word → list of documents containing it.

```
"python" → [doc3, doc7, doc12]
"tutorial" → [doc1, doc3, doc9]
```

Query "python tutorial" → intersect the two lists → [doc3].

- Building the index is expensive; querying it is fast.
- The index must be updated when documents are added/changed.

### Relevance Ranking
Results are scored, not just matched:
- **TF-IDF**: rare words in a document score higher.
- **BM25**: improved TF-IDF, standard in Elasticsearch/Solr.
- **Vector search**: embed text as vectors, find nearest neighbors. Powers semantic search ("find similar articles").

### Tools
- **Elasticsearch / OpenSearch**: most common. Distributed, near-real-time.
- **Solr**: older, similar to Elasticsearch.
- **Postgres full-text search**: sufficient for small-scale or when you want to avoid another service.
- **Typesense / Meilisearch**: simpler, faster to set up, less scalable.

### Write Path
Don't write directly to the search index from your API. Pattern:
1. Write to primary DB.
2. Publish a change event.
3. Search indexer consumes the event and updates the index.

This keeps the search index eventually consistent and decoupled from your write path.

---

## Autocomplete (Typeahead)

Goal: return top-N completions for a prefix in < 100ms.

### Approach 1: Trie
Tree where each node is a character. Walk the prefix, collect all completions below it.
- Fast lookup: O(prefix length)
- Memory-hungry for large vocabularies
- Hard to distribute

### Approach 2: Prefix Hash Table
Precompute all prefixes → top-N results:
```
"py"     → ["python", "pytest", "pypi"]
"pyt"    → ["python", "pytest"]
"pyth"   → ["python"]
```
- Very fast reads (hash lookup)
- Large storage cost
- Precomputed offline; not real-time

### Approach 3: Search Engine Prefix Query
Use Elasticsearch with `prefix` or `edge ngram` queries.
- Handles it natively, no custom index
- Slightly higher latency than pure hash lookup

### Ranking Autocomplete Suggestions
- By global frequency (most searched terms first)
- By personalization (user's own history)
- By recency (trending terms)

### Caching Autocomplete
Most queries cluster around popular prefixes. Cache top-N results per prefix in Redis with a short TTL (minutes). Eliminates most backend calls.

---

## Trade-offs

| Decision | Pro | Con |
|---|---|---|
| Dedicated search engine | Feature-rich, scalable | Ops overhead, eventual consistency with DB |
| Postgres FTS | No extra service | Limited scale, fewer features |
| Trie for autocomplete | Very fast, space-efficient for small vocab | Hard to scale/distribute |
| Prefix hash cache | Fastest reads | Large storage, stale suggestions |

---

## Interview Tips

- Always separate the **indexing pipeline** from the **query path**.
- Clarify: exact match or fuzzy/typo-tolerant? (requires edit-distance, e.g., Levenshtein)
- For autocomplete at scale: cache popular prefixes, pre-rank results offline.
