# Unique ID Generation

Every distributed system needs globally unique IDs for records. Auto-increment from a single DB doesn't work at scale — it's a bottleneck and single point of failure.

---

## Requirements to Clarify

- Must IDs be globally unique, or unique per table/entity?
- Must they be sortable by time?
- Does the ID need to be unpredictable (security)?
- What's the expected volume (IDs/second)?
- How long can the ID be (storage, URL friendliness)?

---

## Approaches

### 1. UUID (v4)
128-bit random identifier. `550e8400-e29b-41d4-a716-446655440000`
- **Globally unique** with astronomically low collision probability.
- **No coordination needed** — generate anywhere.
- **Not sortable** — random, so no time ordering.
- Large (36 chars as string, 16 bytes binary).
- Bad for DB primary keys: random insertion causes index fragmentation.

### 2. UUID v7 (time-ordered UUID)
Like v4 but the first 48 bits are a millisecond timestamp.
- **Sortable** by creation time.
- Still no coordination needed.
- Better for DB indexes than v4.
- Becoming the preferred default for new systems.

### 3. Snowflake ID (Twitter)
64-bit integer composed of:
```
[41 bits: timestamp ms] [10 bits: machine ID] [12 bits: sequence]
```
- **Sortable** by time (timestamp prefix).
- Compact (64-bit int fits in a long).
- Requires each node to have a unique machine ID.
- Generates up to 4096 IDs/ms per machine.
- Used by: Twitter, Discord, Instagram (with variations).

### 4. ULID (Universally Unique Lexicographically Sortable Identifier)
128-bit: 48-bit timestamp + 80-bit random.
- **Sortable** and URL-safe string format.
- No coordination needed.
- Good middle ground between UUID and Snowflake.

### 5. DB Sequence / Auto-increment
Let the DB generate sequential integers.
- Simple, sortable, compact.
- Single point of failure and throughput bottleneck.
- OK for single-node or low-scale systems.

### 6. Ticket Server
A dedicated service that hands out pre-allocated ranges of IDs to each app server. App server uses its range locally.
- Avoids per-ID network round trips.
- Ticket server is a bottleneck; mitigate with multi-server setup.

---

## Comparison

| Approach | Sortable | Coordination | Size | Use Case |
|---|---|---|---|---|
| UUID v4 | No | None | 128-bit | General purpose, no ordering needed |
| UUID v7 | Yes | None | 128-bit | Modern default, DB-friendly |
| Snowflake | Yes | Machine ID | 64-bit | High throughput, compact |
| ULID | Yes | None | 128-bit | URL-safe, sortable |
| DB sequence | Yes | DB | 64-bit | Simple, single-node |

---

## Interview Tips

- For most systems: **UUID v7** or **Snowflake** are the right answers.
- If asked to design the ID generator itself: describe Snowflake's bit layout and clock skew handling (don't generate IDs if clock goes backwards).
- Sortable IDs improve DB write patterns (sequential inserts → less index fragmentation).
- Never expose auto-increment IDs in public APIs — they reveal enumeration info.
