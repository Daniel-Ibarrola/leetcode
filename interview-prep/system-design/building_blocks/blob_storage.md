# Blob Storage

## What is it?
Blob (Binary Large Object) storage is a service for storing unstructured files — images, videos, audio, backups, logs, PDFs — at massive scale. You store a file with a key (path/name) and retrieve it by that key. Not a database; no joins, no queries. Examples: AWS S3, Google Cloud Storage, Azure Blob Storage.

## How it works
- Files are stored as "objects" with a key, metadata, and the raw bytes
- Organized into "buckets" (S3) or "containers" (Azure)
- Access via HTTP — you upload with PUT, download with GET
- Can generate pre-signed URLs to let users upload/download directly without going through your servers

## Key concepts
- **Object** — a file + its metadata + a unique key (path-like name)
- **Bucket** — a top-level namespace for objects
- **Pre-signed URL** — a temporary URL that grants access to a specific object (great for user uploads)
- **Storage classes** — hot (frequent access, higher cost) vs. cold/archive (rare access, much cheaper)
- **Versioning** — keep old versions of files on overwrite/delete
- **Lifecycle policies** — auto-move old files to cheaper storage or delete them

## Trade-offs

| Pro | Con |
|-----|-----|
| Near-unlimited storage capacity | Not a database — can't query by content |
| Very cheap per GB | High latency for small, frequent reads compared to local disk |
| Highly durable (e.g., S3 is 99.999999999% durability) | No atomic multi-object operations |
| Built-in CDN integration | Eventual consistency for overwrites in some providers |
| Managed — no servers to maintain | Egress costs can be high (charges for data leaving the cloud) |

## When to use
- User-uploaded content (profile photos, documents, videos)
- Static assets for your website (often paired with CDN)
- Backups and data exports
- ML training data, logs, analytics files
- Anything too big to store in a database

## When NOT to use
- Frequently updated small records (use a database instead)
- When you need to query file contents (use a search engine or DB)
