# Feed / Timeline Generation

A feed shows a user a ranked list of posts from people they follow. The core challenge: how do you efficiently generate a personalized feed for millions of users?

---

## The Two Approaches

### Fan-Out on Write (Push Model)
When a user posts, immediately push the post to the feeds of all their followers.

```
Alice posts → write to feeds of all N followers immediately
Bob opens app → read his pre-built feed (fast)
```

- **Reads are instant**: feed is pre-computed, just read from a cache/DB.
- **Writes are expensive**: posting to a user with 10M followers = 10M writes.
- Bad for **celebrities / high-follower accounts** (write amplification).
- Good for **users with few followers**.

### Fan-Out on Read (Pull Model)
When a user opens the app, fetch posts from all accounts they follow and merge.

```
Bob opens app → fetch posts from all N accounts Bob follows → merge & rank
```

- **Writes are cheap**: just write the post once.
- **Reads are slow**: must query N accounts, merge, sort, rank at read time.
- Bad for users who follow **thousands of accounts**.
- Good for **celebrities**: their one post doesn't trigger millions of writes.

---

## Hybrid Approach (What Twitter/Instagram Actually Do)

- **Regular users** (< N followers): fan-out on write. Pre-populate followers' feeds.
- **Celebrity users** (> N followers): fan-out on read. Fetch their posts at read time and merge into the feed.

Threshold N is tuned based on system load (typically ~10k–100k followers).

---

## Feed Storage

Pre-built feeds are stored in Redis as a sorted set, scored by timestamp or ranking score:

```
feed:user:bob → [(post_id_1, score_1), (post_id_2, score_2), ...]
```

- Trim feeds to a max length (e.g., last 1000 posts) — most users never scroll that far.
- Store only post IDs in the feed; fetch post content separately (avoids duplicating content).

---

## Ranking

Chronological is the simplest. Algorithmic ranking scores posts by:
- Recency
- Engagement (likes, comments, shares)
- User affinity (how often you interact with this author)
- Content type preference

Ranking is typically done offline (pre-score at write time) or on a small candidate set at read time.

---

## Trade-offs

| | Fan-out on Write | Fan-out on Read |
|---|---|---|
| Read latency | Low (pre-built) | High (computed at read time) |
| Write cost | High (amplified) | Low (write once) |
| Celebrity problem | Severe | None |
| Stale feed risk | Low | Low (always fresh) |
| Storage cost | High (N feed copies) | Low |

---

## Interview Tips

- Always ask: "What's the follower distribution?" — it determines which model fits.
- Mention the hybrid approach for celebrity accounts.
- Feed freshness: how stale is acceptable? Real-time vs. eventual consistency?
- Pagination: cursor-based pagination on the feed (never offset at scale).
