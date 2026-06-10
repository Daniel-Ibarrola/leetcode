# What Is Docker?

Docker is a platform that helps you:

1. Build container images
2. Store container images
3. Run containers
4. Manage container networking
5. Manage container storage

Docker did **not invent containers**. Linux container technologies already existed.

Docker made them easy to use.

---

# Docker Architecture

At a high level:

```text
Docker CLI
     │
     ▼
Docker Daemon
     │
     ▼
Container Runtime
     │
     ▼
Linux Kernel
```

### Docker CLI

Commands you type:

```bash
docker build
docker run
docker ps
```

---

### Docker Daemon

Background service responsible for:

* Building images
* Creating containers
* Managing networks
* Managing volumes

Think of it as the Docker server.

---

### Container Runtime

Actually launches containers.

Responsible for:

* Creating namespaces
* Applying cgroups
* Starting processes

---

# Images vs Containers

This is probably the most important Docker concept.

---

## Image

An image is:

> A blueprint/template.

Example:

```text
Ubuntu
Python 3.11
Application code
```

An image is not running.

---

## Container

A container is:

> A running instance of an image.

Think:

```text
Class → Object
Image → Container
```

---

Example:

```text
Image
   │
   ├── Container A
   ├── Container B
   └── Container C
```

Multiple containers can come from the same image.

---

# Dockerfile

A Dockerfile describes how to build an image.

Example:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

## FROM

Defines the base image.

```dockerfile
FROM ubuntu
```

or

```dockerfile
FROM python:3.11
```

Every image starts from something.

---

## WORKDIR

Sets the working directory.

```dockerfile
WORKDIR /app
```

Equivalent to:

```bash
cd /app
```

for future instructions.

---

## COPY

Copies files into image.

```dockerfile
COPY . .
```

Host:

```text
project/
```

gets copied into container filesystem.

---

## RUN

Executes commands during image build.

```dockerfile
RUN pip install -r requirements.txt
```

Runs once during image creation.

---

## CMD

Defines default command when container starts.

```dockerfile
CMD ["python", "app.py"]
```

Runs every time container starts.

---

# RUN vs CMD

Very common interview question.

### RUN

Executed while building image.

```dockerfile
RUN apt-get install curl
```

Becomes part of image.

---

### CMD

Executed when container starts.

```dockerfile
CMD ["python", "app.py"]
```

Becomes runtime behavior.

---

# Image Layers

Every Dockerfile instruction creates a layer.

Example:

```dockerfile
FROM ubuntu
RUN apt-get update
RUN apt-get install python
COPY . .
```

Creates layers:

```text
Layer 1: Ubuntu
Layer 2: apt update
Layer 3: Python install
Layer 4: Application code
```

---

# Layer Caching

Docker caches layers.

Suppose:

```dockerfile
FROM python:3.11
RUN pip install flask
COPY . .
```

You change only:

```python
app.py
```

Docker can reuse:

```text
python image
pip install flask
```

and rebuild only:

```text
COPY . .
```

This dramatically speeds up builds.

---

# Container Lifecycle

### Create

```bash
docker create
```

Creates container.

Not running.

---

### Start

```bash
docker start
```

Starts container.

---

### Stop

```bash
docker stop
```

Graceful shutdown.

---

### Remove

```bash
docker rm
```

Deletes container.

---

### Run

```bash
docker run
```

Equivalent to:

```text
Create
+
Start
```

---

# Container Process Model

This is frequently misunderstood.

A container usually runs:

```text
ONE MAIN PROCESS
```

Example:

```text
Container
   └── python app.py
```

When the main process exits:

```text
Container exits
```

The container's lifetime is tied to its primary process.

---

# Docker Networking

Containers need communication.

Docker creates virtual networks.

Example:

```text
Container A
      │
      ▼
Docker Network
      ▲
      │
Container B
```

Containers can communicate through these virtual networks.

---

## Port Mapping

Container:

```text
Application
Port 8080
```

Host:

```text
Laptop
Port 8080
```

Docker maps traffic:

```text
Host:8080
      ↓
Container:8080
```

Without port mapping, external clients typically can't reach the container.

---

# Docker Volumes

Important interview topic.

Containers are ephemeral.

If container dies:

```text
Container deleted
Data deleted
```

Potentially disastrous for databases.

---

Volumes solve this.

```text
Container
      │
      ▼
Volume
```

Data lives outside the container lifecycle.

---

Example:

```text
Postgres Container
      │
      ▼
Database Volume
```

Delete container:

```text
Container removed
Volume remains
```

Data survives.

---

# Bind Mounts vs Volumes

### Bind Mount

Uses a host directory.

```text
Host Folder
      │
      ▼
Container Folder
```

Good for development.

---

### Volume

Managed by Docker.

```text
Docker Managed Storage
      │
      ▼
Container
```

Preferred for production.

---

# Docker Registry

Images need a place to live.

Registry stores images.

Workflow:

```text
Build Image
      │
      ▼
Push Registry
      │
      ▼
Pull Image
      │
      ▼
Run Container
```

Common registries:

* Docker Hub
* Amazon Web Services ECR
* Google Cloud Artifact Registry
* GitHub Container Registry

---

# Multi-Stage Builds

Very common senior-level topic.

Bad image:

```dockerfile
FROM python:3.11

COPY . .

RUN build stuff
```

Contains:

* Build tools
* Temporary files
* Compilers

Large image.

---

Multi-stage build:

```dockerfile
Build Stage
     │
     ▼
Compile App
     │
     ▼
Copy Result
     │
     ▼
Runtime Stage
```

Final image contains only what's necessary to run.

Benefits:

* Smaller image
* Faster deployments
* Better security

---

# Common Docker Interview Questions

### Why are Docker images immutable?

Once built, image layers don't change.

Instead:

```text
Build New Image
Deploy New Image
```

This improves reproducibility.

---

### Why shouldn't containers store critical data?

Containers are disposable.

If removed:

```text
Container filesystem disappears
```

Use volumes or external storage.

---

### Why keep images small?

Benefits:

* Faster builds
* Faster pushes
* Faster pulls
* Lower storage costs
* Reduced attack surface

---

### What happens when you run a container?

A strong answer:

1. Docker pulls image if necessary.
2. Docker creates a writable layer.
3. Namespaces are created.
4. Cgroups are applied.
5. Networking is configured.
6. Volumes are mounted.
7. Main process starts.
8. Container runs until the main process exits.

---

### Why would a container restart repeatedly?

Common causes:

* Application crash
* Bad configuration
* Missing environment variables
* Dependency failure
* Health check failures
* Out-of-memory termination

