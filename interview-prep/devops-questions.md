# DevOps Questions

### 1. What is CI/CD?

**CI/CD** stands for **Continuous Integration** and **Continuous Delivery** / **Continuous Deployment**. It is a cornerstone of modern DevOps, representing a culture and a set of practices that automate the software development and release process.

#### Continuous Integration (CI)
**Continuous Integration** is the practice where developers frequently merge their code changes into a central repository (like a `main` branch in Git). After each merge, an automated build-and-test sequence is triggered.

*   **Goal:** To find and address bugs and integration issues earlier and more easily.
*   **Process:**
    1.  A developer commits code to a shared repository.
    2.  A CI server (like Jenkins, GitHub Actions, or GitLab CI) automatically detects the change.
    3.  The server builds the application and runs a suite of automated tests (unit tests, integration tests).
    4.  If the build or tests fail, the team is notified immediately so they can fix the issue.
*   **Benefit:** Prevents the "integration hell" that happens when developers work in isolation for long periods and try to merge their changes all at once.

#### Continuous Delivery (CD)
**Continuous Delivery** is the practice of automatically preparing and releasing every validated code change to a production-like environment. The CI stage is the first step in the CD pipeline. After the code is built and tested, it's automatically deployed to a staging environment.

*   **Goal:** To ensure that you can release new changes to your users quickly and sustainably.
*   **Process:** After CI passes, the pipeline automatically deploys the application to one or more test environments. The final step—deploying to production—is triggered by a **manual approval**.
*   **Benefit:** Reduces the risk of a release by making deployments a routine, low-ceremony event. It gives you confidence that your application is always in a releasable state.

#### Continuous Deployment (CD)
**Continuous Deployment** is the next step after Continuous Delivery. It is a more advanced practice where every change that passes all the automated tests is **automatically deployed to production** without any human intervention.

*   **Goal:** To accelerate the feedback loop with users and release new features as quickly as possible.
*   **Process:** If the automated pipeline (build, test, deploy to staging) is successful, the change is pushed directly to production users.
*   **Benefit:** Enables a very fast release cadence. This requires a high degree of confidence in your automated testing and monitoring.

---
### 2. What is Infrastructure as Code (IaC)?

**Infrastructure as Code (IaC)** is the practice of managing and provisioning computer data centers (networks, virtual machines, load balancers, etc.) through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

In simple terms, it's **writing code to manage your infrastructure**.

**How it works:** Instead of manually clicking through a web console to create a virtual machine, you write a configuration file that defines the machine's properties (e.g., CPU, RAM, OS, networking rules). An IaC tool then reads this file and creates the infrastructure to match that definition.

**Key Benefits:**
*   **Automation:** Drastically reduces the manual effort and time required to set up and manage infrastructure.
*   **Consistency:** Eliminates configuration drift and ensures that every environment (development, staging, production) is provisioned in the exact same way, reducing "it works on my machine" problems.
*   **Version Control:** Infrastructure code can be stored in a Git repository, giving you a full history of all changes. You can review, audit, and roll back changes just like application code.
*   **Reusability:** You can create reusable modules to define common infrastructure patterns, making it easy to scale or replicate your application in different regions.

**Popular IaC Tools:**
*   **Declarative (what you want):**
    *   **Terraform:** Cloud-agnostic, widely used for provisioning resources across AWS, Azure, GCP, etc.
    *   **AWS CloudFormation, Azure Resource Manager (ARM):** Cloud-specific tools.
*   **Imperative (how to do it):**
    *   **Ansible, Chef, Puppet:** Often called configuration management tools, they focus on installing and managing software on existing servers.

---
### 3. What is the difference between a Docker image and a container?

The difference is best explained with a simple analogy from object-oriented programming: an **image is a class**, and a **container is an instance of that class**.

#### Docker Image
A Docker **image** is a **read-only, inert template** that contains everything needed to run an application: the application code, a runtime (like Python or Node.js), system tools, libraries, and environment settings.

*   **It's a blueprint.** It defines what you want your environment to look like but isn't actually running.
*   Images are built from a `Dockerfile`, which is a list of instructions.
*   Images are stored in a registry (like Docker Hub or Amazon ECR) and can be versioned.

#### Docker Container
A Docker **container** is a **live, running instance of an image**. When you "run" an image, you create a container.

*   **It's the actual running process.** You can have many containers all created from the same image, just like you can create many objects from one class.
*   A container has its own isolated filesystem, network, and process space.
*   Any changes you make inside a running container are isolated to that container and are lost when the container is destroyed, unless you use volumes to persist data.

---
### 4. What is a container orchestration tool?

A **container orchestration tool** is a system that automates the deployment, management, scaling, and networking of containerized applications.

When you are only running a few Docker containers on a single machine, it's easy to manage them manually. But in a production environment, you might need to run hundreds or thousands of containers across a fleet of servers. This is where orchestration becomes essential.

**What problems do orchestrators solve?**
*   **Deployment & Scheduling:** Automatically finds the best server (node) to run a new container on, based on resource availability (CPU, RAM).
*   **High Availability & Fault Tolerance:** If a container crashes or a server goes down, the orchestrator automatically detects it and starts a new container to replace it, ensuring the application stays online.
*   **Scaling:** Automatically scales the number of containers up or down based on traffic or resource usage.
*   **Networking & Service Discovery:** Provides a virtual network that allows containers to communicate with each other, even if they are on different physical servers. It gives a stable DNS name to a group of containers so other services can find them.
*   **Load Balancing:** Distributes incoming network traffic evenly across multiple containers that are part of the same service.
*   **Rolling Updates:** Allows you to deploy a new version of your application with zero downtime by gradually replacing old containers with new ones.

**The de facto standard container orchestrator is Kubernetes.** Other examples include Docker Swarm and Amazon ECS.