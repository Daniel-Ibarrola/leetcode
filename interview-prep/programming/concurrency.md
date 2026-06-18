# Concurrency

At a high level, **concurrency** is the concept of a program structuring its work into tasks that can be managed and run in overlapping time periods. It's about _dealing_ with many things at once.
This is often confused with **parallelism**, which is about _doing_ many things at once. Parallelism requires hardware with multiple cores or processors. Concurrency is a way to structure your code to _enable_ parallelism if the hardware is available, but it's also useful on a single core to improve responsiveness and handle waiting for external resources efficiently.
Here’s a breakdown of the common models for achieving concurrency:

### Multiprocessing
- **What it is:** This model uses multiple independent processes, where each process has its own memory space and runs on a separate CPU core.
- **Analogy:** Imagine a restaurant with several separate, fully-equipped kitchens. Each kitchen is a **process**. They can all cook full meals in parallel. If one kitchen needs something from another, they have to use a specific communication channel (like a dumbwaiter), which is a deliberate and relatively slow action.
- **When to use it:** It's best for **CPU-bound tasks**—computationally heavy work that can be broken down into independent chunks (e.g., video processing, large-scale data analysis). Because the processes don't share memory, it's a way to bypass Python's Global Interpreter Lock (GIL) and achieve true parallelism.
- **Pros:**
    - Achieves true parallelism, utilizing multiple CPU cores.
    - Memory isolation means one process crashing won't affect others.

- **Cons:**
    - Higher memory usage since memory isn't shared.
    - Inter-Process Communication (IPC) is slower and more complex than communication between threads.

### Multithreading
- **What it is:** This model uses multiple threads of execution within a single process. All threads share the same memory space.
- **Analogy:** Imagine a single large kitchen (the **process**) with several chefs (the **threads**). They all share the same ingredients and equipment (the **memory**). They can work on different tasks, but they must be careful not to get in each other's way (e.g., two chefs trying to use the same knife).
- **When to use it:** It's best for **I/O-bound tasks**. These are tasks where the program spends most of its time waiting for something external, like a network request to finish or a file to be read from a disk. While one thread is waiting, the system can switch to another thread to do useful work.
- **Pros:**
    - Lower memory footprint than multiprocessing.
    - Sharing data between threads is easy because they share memory.

- **Cons:**
    - In CPython, the Global Interpreter Lock (GIL) prevents multiple threads from executing Python code at the same time, so it doesn't help with CPU-bound tasks.
    - Shared memory can lead to race conditions and deadlocks, requiring complex synchronization tools like locks to manage safely.

### Asynchronous Programming (Async/Await)
- **What it is:** This is a concurrent programming paradigm that runs on a **single thread**. An event loop manages multiple tasks. When a task reaches a point where it has to wait for I/O, it explicitly tells the event loop, "I'm waiting," and yields control. The event loop then runs another task that is ready to do work.
- **Analogy:** Imagine a single, highly-efficient chef in a kitchen. The chef starts cooking a steak (Task A). When the steak needs to sear for five minutes (an I/O wait), the chef doesn't just stand there. They set a timer and immediately start chopping vegetables for a salad (Task B). When the timer rings (the event loop signals completion), the chef can switch back to the steak. The key is that the chef is never idle and only works on one thing at a exact moment.
- **When to use it:** It excels at **high-volume I/O-bound tasks**, like a web server handling thousands of simultaneous network connections. It is far more efficient in terms of memory and context-switching overhead than multithreading for these scenarios.
- **Pros:**
    - Extremely efficient with very low overhead, allowing for tens of thousands of concurrent operations.
    - No risk of race conditions in the same way as multithreading, as control is explicitly yielded, not preemptively taken away.

- **Cons:**
    - Doesn't help at all with CPU-bound tasks; a long-running computation will block the entire event loop.
    - Requires a different style of programming and for your code (and the libraries you use) to be designed to support the `async/await` model.

### Summary: Which One to Choose?
- **For CPU-bound tasks:** Use **multiprocessing** to leverage multiple cores.
- **For I/O-bound tasks:** **Multithreading** is a solid, traditional choice.
- **For a massive number of I/O-bound tasks:** **Async** is the most scalable and efficient solution.