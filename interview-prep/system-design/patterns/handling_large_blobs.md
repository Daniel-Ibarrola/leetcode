# Handling Large Blobs

A "blob" is any large binary object: images, videos, documents, backups. Storing and serving them requires a different approach than structured data.

## Core Principle

**Never send blobs through your application servers.** Let clients upload/download directly to object storage.

---

## Upload Pattern: Presigned URLs

1. Client asks your API: "I want to upload a file."
2. API generates a short-lived presigned URL pointing directly to object storage (S3, GCS, Azure Blob).
3. Client uploads directly to storage using that URL.
4. Storage notifies your backend (event/webhook) when upload is complete.
5. Backend records metadata (filename, size, storage key) in the DB.

**Why**: your app servers never touch the bytes → no memory pressure, no bandwidth cost on your fleet.

---

## Download Pattern: CDN + Presigned URLs

- For **public** content: put a CDN in front of object storage. Users get files from the nearest edge node.
- For **private** content: generate a short-lived presigned download URL. Client downloads directly from storage; link expires after N minutes.

---

## Storage Options

| Service | Use Case |
|---|---|
| AWS S3 / GCS / Azure Blob | General object storage. Durable, cheap at scale. |
| CDN (CloudFront, Fastly) | Cache and serve blobs close to users. |
| Distributed FS (HDFS, Ceph) | Large-scale internal data pipelines. |

---

## Chunked / Multipart Upload

For large files (>100MB), split into chunks and upload in parallel.
- Resume interrupted uploads
- Parallel chunks = faster upload
- S3, GCS both support multipart upload natively

---

## Processing Blobs (e.g., video transcoding, image resizing)

Don't do it synchronously in the request path.

Pattern:
1. Upload completes → storage event triggers a queue message.
2. Worker picks up the job, processes the blob (transcode, resize, scan for malware).
3. Worker writes the processed output back to storage.
4. Worker updates DB with the result (or new storage key).

---

## Trade-offs

| Decision | Pro | Con |
|---|---|---|
| Direct-to-storage upload | Offloads bandwidth from app servers | More complex client logic |
| Chunked upload | Resumable, faster | More round trips, more state to manage |
| CDN for downloads | Low latency, high throughput | Cache invalidation when content changes |
| Async processing | Non-blocking for users | User has to poll or be notified when done |

---

## Common Pitfalls

- **Storing blobs in the DB**: works for tiny thumbnails but kills DB performance at any real scale.
- **Serving blobs through app servers**: saturates memory and bandwidth quickly.
- **No expiry on presigned URLs**: overly long TTLs mean leaked URLs stay valid too long.
- **Not validating file type server-side**: presigned URL approach must still validate MIME type / file contents after upload.
