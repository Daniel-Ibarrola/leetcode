# Data Pagination

Returning large result sets page by page. Two main approaches: offset-based and cursor-based.

---

## Offset Pagination

```
GET /posts?page=3&limit=20
SQL: SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 60
```

- Simple to implement and understand.
- Easy to jump to any page ("go to page 5").
- **Breaks at scale**:
  - DB must scan and discard all rows before the offset (OFFSET 100000 is slow).
  - If new rows are inserted while paginating, rows shift → you see duplicates or skip items.

Use when: small datasets, admin UIs, infrequently updated data.

---

## Cursor Pagination (Keyset Pagination)

Instead of a page number, the client sends a **cursor** — an opaque token encoding the position of the last item seen.

```
GET /posts?limit=20                         ← first page
GET /posts?cursor=<token>&limit=20          ← next page
```

Server decodes the cursor → gets the last item's sort key → queries:
```sql
SELECT * FROM posts
WHERE created_at < :last_seen_created_at
ORDER BY created_at DESC
LIMIT 20
```

- **Consistent**: inserts/deletes don't shift positions.
- **Fast**: uses an index seek, not a scan.
- **No random access**: can't jump to page 47 directly.
- Cursor must encode all sort fields to handle ties.

Use when: infinite scroll, real-time feeds, large datasets, frequently updated data.

---

## Cursor Encoding

Cursors are typically base64-encoded JSON or an opaque string:
```json
{ "created_at": "2024-01-15T10:30:00Z", "id": "abc123" }
```
Encode to make it opaque to clients (prevents manipulation). Always include the ID to break ties when timestamps match.

---

## Seek Method (Composite Cursor)

When sorting by a non-unique column (e.g., `likes`), include the ID to break ties:
```sql
WHERE (likes < :last_likes) OR (likes = :last_likes AND id < :last_id)
ORDER BY likes DESC, id DESC
LIMIT 20
```

---

## Comparison

| | Offset | Cursor |
|---|---|---|
| Random page access | Yes | No |
| Consistent under inserts | No | Yes |
| Performance at large offset | Poor | Good (index seek) |
| Implementation complexity | Low | Medium |
| Use case | Small, stable data; admin UIs | Feeds, infinite scroll, large datasets |

---

## Interview Tips

- Default answer at scale: **cursor-based**.
- Offset pagination is fine to mention as the simple starting point, then explain why it breaks.
- Cursor must include a tiebreaker (usually the ID) to be deterministic.
- Never use `OFFSET` on a table with millions of rows — it scans everything before the offset every time.
