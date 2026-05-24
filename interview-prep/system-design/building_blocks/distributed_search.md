# Distributed Search (e.g., Elasticsearch)

## What is it?
A distributed search engine indexes large volumes of data and enables fast full-text search, filtering, and aggregations across it. Unlike a database query that scans rows, search engines use inverted indexes for sub-second lookups over billions of documents. Examples: Elasticsearch, OpenSearch, Apache Solr.

## Core concept: Inverted Index
Instead of "document → words", an inverted index maps "word → list of documents containing it". This is why searching for "coffee shop" across 10 million articles is fast: you just look up those two words in the index and intersect the document lists.

## How Elasticsearch works (simplified)
1. You **index** a document (send JSON to ES)
2. ES analyzes the text (tokenizes, lowercases, removes stop words, etc.)
3. ES writes to an inverted index on one of its **shards**
4. On search, ES queries all relevant shards in parallel and merges results
5. Results are ranked by **relevance score** (TF-IDF or BM25)

## Key concepts
- **Index** — like a database; a collection of documents
- **Document** — a JSON record (like a row)
- **Shard** — a horizontal partition of an index; ES distributes shards across nodes
- **Replica** — a copy of a shard for fault tolerance and read scalability
- **Analyzer** — pipeline that transforms text before indexing (tokenizer + filters)
- **Relevance scoring** — documents are ranked, not just filtered

## Trade-offs

| Pro | Con |
|-----|-----|
| Extremely fast full-text search | Near real-time, not real-time — new docs take ~1s to appear |
| Scales horizontally across many nodes | Eventual consistency — not suitable as primary data store |
| Rich query DSL: fuzzy match, aggregations, geo-search | Operationally complex (cluster management, reindexing) |
| Built-in relevance ranking | High memory usage |
| Good for analytics and log aggregation (ELK stack) | Schema changes require reindexing |

## Typical architecture
- Primary data lives in a database (Postgres, MySQL)
- On write, events are published and a worker indexes them into Elasticsearch
- Search queries go to Elasticsearch; everything else goes to the DB
- This means ES is a derived, read-optimized view of your data

## When to use
- Full-text search on large datasets (product search, article search)
- Log aggregation and analysis (ELK stack: Elasticsearch + Logstash + Kibana)
- Complex filtering + ranking (e.g., "find hotels near me, sorted by reviews")
- Autocomplete and fuzzy matching

## When NOT to use
- As your only database (no ACID, eventual consistency)
- Simple exact-match queries that SQL handles fine
- Small datasets where a DB `LIKE` query is fast enough
