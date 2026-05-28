# Architecture: Video Upload & Streaming (YouTube-like)

**Scale target:** 500 hours of video uploaded per minute, 1B daily active viewers, global distribution

---

## Problem

Design a system where users upload videos, which are transcoded into multiple formats/resolutions, and then streamed to millions of concurrent viewers worldwide.

---

## Architecture Diagram

```
                        ┌──────────────────────────────────────┐
                        │           UPLOAD FLOW                │
                        └──────────────────────────────────────┘

 Client ──► API Gateway ──► Upload Service ──► Presigned URL ──► Blob Storage (S3)
                                │                                       │
                                │ stores metadata                       │ upload complete
                                ▼                                       ▼
                         PostgreSQL (video              Message Queue (SQS/Kafka)
                          metadata, status)                      topic: raw-uploads
                                                                        │
                                                     ┌──────────────────▼────────────────┐
                                                     │       Transcoding Workers         │
                                                     │  (ffmpeg in containers)           │
                                                     │  720p, 1080p, 4K, HLS segments   │
                                                     └──────────────────┬────────────────┘
                                                                        │
                                                               Blob Storage (S3)
                                                             /videos/{id}/720p/
                                                             /videos/{id}/1080p/
                                                                        │
                                                     ┌──────────────────▼────────────────┐
                                                     │    Update DB: status = READY      │
                                                     │    Notify user (email/push)       │
                                                     └───────────────────────────────────┘

                        ┌──────────────────────────────────────┐
                        │           STREAMING FLOW             │
                        └──────────────────────────────────────┘

 Viewer ──► DNS (GeoDNS) ──► CDN Edge Node ──────────────────► serve HLS segment
                                    │ (cache miss)
                                    ▼
                              Blob Storage (S3)
                              (origin server)

 Viewer ──► API Gateway ──► Search Service ──► Elasticsearch
                        │
                        └──► Recommendations ──► Redis (pre-cached)
```

---

## Component Mapping

| Component | Building Block / Pattern | Notes File |
|---|---|---|
| API Gateway | API Gateway | `building_blocks/api_gateway.md` |
| Presigned URL + direct upload | Handling Large Blobs | `patterns/handling_large_blobs.md` |
| Blob Storage (S3) | Blob Storage | `building_blocks/blob_storage.md` |
| Message Queue (SQS) | Message Queues | `building_blocks/message_queues.md` |
| Transcoding workers | Long-Running Tasks | `patterns/long_running_tasks.md` |
| CDN | CDN | `building_blocks/cdn.md` |
| DNS + GeoDNS | DNS | `building_blocks/dns.md` |
| PostgreSQL (metadata) | Relational Databases | `building_blocks/relational_databases.md` |
| Elasticsearch (search) | Distributed Search | `building_blocks/distributed_search.md` |
| Redis (recommendations cache) | Caches | `building_blocks/caches.md` |
| Search & autocomplete | Search & Autocomplete | `patterns/search_and_autocomplete.md` |

---

## Key Decisions

### 1. Direct-to-storage upload via presigned URLs
The upload service never handles raw bytes — it issues a presigned S3 URL and the client uploads directly.  
This keeps app servers free from bandwidth/memory pressure.  
→ See `patterns/handling_large_blobs.md`

For files > 100MB, the client uses **multipart upload**: split into chunks, upload in parallel, S3 assembles.

### 2. Async transcoding via message queue
Upload complete → S3 triggers an event → SQS message → transcoding worker pool.  
The worker produces multiple renditions (360p, 720p, 1080p, 4K) stored as HLS segments.  
Status polling or webhook notifies the user when processing finishes.  
→ See `patterns/long_running_tasks.md`

```
Video ID: abc123
/videos/abc123/360p/seg001.ts
/videos/abc123/720p/seg001.ts
/videos/abc123/1080p/seg001.ts
/videos/abc123/master.m3u8   ← HLS manifest listing all variants
```

### 3. CDN for video delivery — the most critical component
Videos are large, access patterns are read-heavy, and viewers are global.  
CDN caches HLS segments at edge nodes: viewer requests the nearest edge, edge fetches from S3 on miss.  
Adaptive bitrate streaming (ABR): client switches between renditions based on network conditions.  
→ See `building_blocks/cdn.md`

### 4. HLS over WebSocket for streaming
HTTP-based streaming (HLS/DASH) is preferred over persistent connections:
- Works through firewalls/proxies
- CDN-cacheable (each segment is a small static file)
- Adaptive bitrate built-in  
→ See `concepts/networking_essentials.md`

### 5. Separate metadata DB from blob storage
PostgreSQL stores: video ID, title, uploader, duration, status (UPLOADING / PROCESSING / READY), storage keys.  
Video bytes live in S3 — never the DB.  
Index on `(uploader_id, created_at)` for profile page queries; index on `status` for admin/monitoring.

### 6. Elasticsearch for search
Video titles, descriptions, and tags are indexed in Elasticsearch after transcoding completes.  
Inverted index enables full-text search with relevance ranking.  
→ See `building_blocks/distributed_search.md` and `patterns/search_and_autocomplete.md`

---

## Scaling Considerations

| Bottleneck | Solution |
|---|---|
| Transcoding CPU | Auto-scale worker pool; GPU instances for 4K |
| Storage cost | S3 lifecycle policies: move old/cold videos to cheaper tiers (Glacier) |
| Global viewer latency | CDN with edge nodes in every region |
| Hot videos (trending) | CDN absorbs the load; S3 origin rarely hit |
| Search freshness | Elasticsearch indexer as another consumer of the upload-complete event |
| Metadata DB reads | Read replicas for profile/search queries → see `concepts/replication.md` |

---

## Interview Tips

- Clarify: "Is this upload-heavy or view-heavy?" — almost always view-heavy (design around CDN).
- Transcoding is the hardest part operationally: mention retry logic and dead-letter queues for failed jobs.
- Mention adaptive bitrate: the system doesn't serve one video file, it serves many small segments.
- Cost insight: CDN bandwidth is the biggest cost driver at scale.
