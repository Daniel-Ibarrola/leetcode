
# What Problem Do Containers Solve?

Before containers became popular, applications often suffered from:

> "It works on my machine."

A developer might have:

* Python 3.11
* Specific libraries
* Particular OS packages
* Custom configurations

While production had:

* Python 3.8
* Different dependencies
* Different OS configuration

Containers package an application together with everything it needs to run consistently across environments.

---

# What Is a Container?

A container is:

> An isolated process running on a shared operating system kernel.

This is the most important definition.

Many people think containers are lightweight VMs.

They are not.

A container is just a process (or group of processes) that the operating system isolates from other processes.

---

# Container vs VM

## Virtual Machine

A VM virtualizes hardware.

```text
Physical Server
│
├── Hypervisor
│
├── VM 1
│   ├── Guest OS
│   ├── Libraries
│   └── Application
│
├── VM 2
│   ├── Guest OS
│   ├── Libraries
│   └── Application
```

Each VM has:

* Its own kernel
* Its own operating system
* Its own filesystem

This provides strong isolation but uses more resources.

---

## Containers

Containers virtualize the operating system.

```text
Host OS
│
├── Container A
│   ├── App
│   └── Dependencies
│
├── Container B
│   ├── App
│   └── Dependencies
│
└── Container C
    ├── App
    └── Dependencies
```

All containers share:

* Same host kernel
* Same operating system

They only get isolated views of resources.

---

## Resource Comparison

VM:

```text
Hardware
  ↓
Hypervisor
  ↓
Guest OS
  ↓
Application
```

Container:

```text
Hardware
  ↓
Host OS Kernel
  ↓
Container Runtime
  ↓
Application
```

Because there's no extra guest OS:

* Faster startup
* Less memory
* Higher density

A VM might take minutes to boot.

A container often starts in seconds or less.

---

# What Makes a Container Isolated?

Linux provides several kernel features.

The two most important are:

1. Namespaces
2. Cgroups

---

# Namespaces

Namespaces give a process its own view of system resources.

Without namespaces:

```text
Process A
Process B
Process C
```

Every process can see all other processes.

---

With namespaces:

```text
Container A
  PID 1
  PID 2

Container B
  PID 1
  PID 2
```

Each container believes it owns the machine.

Even though the host actually sees:

```text
Host PID 1001
Host PID 1002
Host PID 2001
Host PID 2002
```

The container gets a filtered view.

---

## Types of Namespaces

### PID Namespace

Controls process visibility.

Container sees:

```text
PID 1
PID 2
PID 3
```

Host may see:

```text
PID 1024
PID 1025
PID 1026
```

---

### Network Namespace

Provides separate networking.

Each container can have:

* Its own IP
* Its own routing table
* Its own interfaces
* Its own ports

Container A:

```text
10.0.0.2
```

Container B:

```text
10.0.0.3
```

Even though they're on the same machine.

---

### Mount Namespace

Provides isolated filesystem views.

Container sees:

```text
/app
/config
/logs
```

Not the entire host filesystem.

---

### User Namespace

Maps container users to host users.

Allows running as root inside container while limiting host privileges.

---

# Cgroups

Namespaces provide isolation.

Cgroups provide resource control.

Without cgroups:

```text
Container A consumes:
100% CPU
100% Memory
```

Everything else suffers.

---

Cgroups let you set limits:

```text
Container A

CPU:
2 cores

Memory:
1GB
```

The kernel enforces these limits.

---

# The Container Filesystem

Every container has its own filesystem view.

But how is that filesystem created?

This is where images come in.

---

# Container Images

An image is:

> A read-only template used to create containers.

Think of it like a blueprint.

Example contents:

```text
Linux libraries
Python runtime
Application code
Configuration
```

---

Container lifecycle:

```text
Image
   ↓
Run
   ↓
Container
```

You can create thousands of containers from the same image.

---

# Layers

One of the most important image concepts.

Images are built from layers.

Example:

```text
Layer 1:
Base Linux

Layer 2:
Python

Layer 3:
Application Dependencies

Layer 4:
Application Code
```

Stacked together:

```text
App Code
Dependencies
Python
Linux
```

---

Why layers matter:

If only app code changes:

```text
Linux      Reused
Python     Reused
Deps        Reused
Code       Rebuilt
```

Faster builds.

Less storage.

Faster transfers.

---

# Copy-On-Write

Images are read-only.

Containers need writable storage.

Solution:

```text
Read-only Image Layers
+
Writable Layer
=
Running Container
```

Container writes go into the writable layer.

Original image remains unchanged.

---

# Networking Fundamentals

Containers are isolated.

But applications need communication.

Typically:

```text
Container A
      │
      ▼
Virtual Network
      ▲
      │
Container B
```

The operating system creates virtual interfaces and bridges traffic between containers.

To the application:

```text
send request to 10.0.0.3
```

Looks like normal networking.

---

# Why Containers Are Ephemeral

Containers are designed to be disposable.

If a container dies:

```text
Destroy
Create New One
```

Rather than fixing it manually.

This is a major cloud-native principle.

Pets vs cattle:

```text
Pet:
Repair it

Cattle:
Replace it
```

Containers are cattle.

---

# Common Interview Question

### "Why are containers lighter than VMs?"

Correct answer:

Because containers share the host operating system kernel and do not require a separate guest OS per application.

---

# Common Interview Question

### "Are containers completely isolated?"

Answer:

No.

Containers provide process-level isolation but share the host kernel.

VMs provide stronger isolation because each VM runs its own kernel.

---

# Common Interview Question

### "What happens when a container starts?"

A good answer:

1. Container runtime creates namespaces.
2. Resource limits are configured using cgroups.
3. Filesystem layers are mounted.
4. Network interfaces are created.
5. The application process starts.
6. That process becomes the main process of the container.

---

# The One-Sentence Summary

If an interviewer asks for a high-level explanation:

> A container is an isolated process running on a shared operating system kernel. Linux namespaces provide isolation, cgroups enforce resource limits, images provide the filesystem template, and containers are lightweight because they do not require a full guest operating system like virtual machines do.
