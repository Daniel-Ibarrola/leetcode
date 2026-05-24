# Indexes

An index is a separate data structure that lets the DB find rows without scanning the entire table. Faster reads, slower writes.

---

## How It Works (B-Tree Index)

The default index type. A balanced tree sorted by the indexed column(s).

- **Read**: walk the tree to find the value → O(log N) instead of O(N).
- **Write**: every insert/update/delete must also update the index tree → extra cost.

---

## Index Types

### B-Tree (Default)
- Good for: equality (`=`), range queries (`>`, `<`, `BETWEEN`), sorting (`ORDER BY`), prefix matching (`LIKE 'abc%'`).
- Not good for: full-text search, very high cardinality random writes.

### Hash Index
- Maps keys → memory location. O(1) equality lookup.
- Good for: exact match only (`=`).
- Not good for: range queries (no ordering).
- Used internally by Postgres for hash joins; explicit hash indexes are rarely chosen manually.

### Full-Text Index
- Inverted index mapping words → document IDs.
- Good for: `MATCH ... AGAINST`, text search.
- Used by: Postgres FTS, MySQL FULLTEXT, Elasticsearch.

### Composite Index (Multi-Column)
Index on multiple columns: `(last_name, first_name)`.
- Order matters: this index helps queries filtering on `last_name` or `last_name + first_name`, but NOT on `first_name` alone.
- **Leftmost prefix rule**: a composite index on (A, B, C) supports queries on A, (A,B), and (A,B,C) — not B alone or C alone.

### Covering Index
An index that includes all columns a query needs, so the DB never has to read the actual table row.
```sql
-- Query: SELECT email FROM users WHERE user_id = 42
-- Index on (user_id, email) → covers the query entirely
```

### Partial Index
Index only a subset of rows that match a condition:
```sql
CREATE INDEX ON orders (created_at) WHERE status = 'pending';
```
Smaller index, faster for that specific query pattern.

---

## When Indexes Help vs Hurt

| Scenario | Indexes help | Indexes hurt |
|---|---|---|
| Read-heavy workload | Yes | — |
| Write-heavy workload | — | Yes (every write updates all indexes) |
| High-cardinality column | Yes | — |
| Low-cardinality column (e.g., boolean) | No (DB may prefer full scan) | Wastes space |
| Small table | No (full scan may be faster) | — |

---

## Query Planner

The DB decides whether to use an index based on statistics (estimated row count, cardinality). Use `EXPLAIN` / `EXPLAIN ANALYZE` to see what the planner chose and why.

---

## Common Pitfalls

- **Too many indexes**: each one slows writes and takes disk space. Only index columns you actually query on.
- **Index on the wrong side of a function**: `WHERE LOWER(email) = 'abc'` won't use an index on `email`. Create a function-based index or store the value pre-lowercased.
- **Ignoring composite index order**: `(A, B)` is not the same as `(B, A)`. Know your query patterns.
- **Forgetting foreign keys need indexes**: FK columns are frequently joined on; always index them.

---

## Quick Rules of Thumb

- Index every foreign key column.
- Index columns used in `WHERE`, `JOIN`, `ORDER BY` for frequent, slow queries.
- Use `EXPLAIN` to verify the index is actually being used.
- Composite index column order: most selective / most frequently filtered column first.
