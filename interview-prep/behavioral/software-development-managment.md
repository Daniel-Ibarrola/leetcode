## Software Development Management

### What to look for in a code review.

When I do a code review, I focus first on correctness, readability, and maintainability. 
I also check test coverage and edge cases, and I make sure the changes align with our 
architectural standards. I avoid nitpicking things that can be automated with linters. 
I try to ask questions rather than make demands, to keep reviews collaborative. 
And I tailor my feedback depending on the developer’s level — more context for juniors, 
broader discussions for seniors.

1. High-level approach
	- Goal first: “I see code reviews as a way to improve code quality, share knowledge, and maintain team standards.”
	- Tone: “I try to keep reviews collaborative, not adversarial.”

2. Checklist of focus areas (in order of priority)
	- Correctness & clarity: Does the code do what it’s supposed to do? Is it readable and maintainable?
	- Tests: Are there adequate unit/integration tests? Do they cover edge cases?
	- Architecture & design: Does the change align with existing patterns and project conventions?
	- Performance & security: Any potential bottlenecks, leaks, or vulnerabilities?
	- Documentation: Is code commented where necessary? Is README/API doc updated if relevant?

3. Process/style considerations
	- Avoid nitpicking (use linters/formatters for style so reviews focus on logic and design).
	- Ask questions instead of dictating (“What do you think about extracting this into a helper?”).
	- Keep reviews scoped and timely — don’t block progress with overly broad requests.

4. Mentorship & team impact
	- “I tailor reviews to the experience of the author. For juniors, I might add more context/explanation. For seniors, I focus on architecture decisions or broader implications.”
	- “I also try to highlight positives in the code, not just issues.”


### The Waterfall Model

The **Waterfall Model** is a traditional, linear, and sequential approach to software development. As the name suggests, progress flows steadily downwards (like a waterfall) through a series of distinct phases. Each phase must be fully completed before the next phase can begin.

**Analogy:** Building a house. You must complete the foundation before you build the walls, and you must complete the walls before you add the roof. You can't go back up the waterfall to change the foundation once the walls are being built.

#### The Phases of Waterfall

The process is typically broken down into these rigid steps:

1.  **Requirements:** All project requirements are gathered and documented upfront. The customer is heavily involved here, but much less so afterward. This phase results in a comprehensive requirements document.
2.  **Design:** The project's architecture and software design are created based on the requirements. This includes designing the system, database, UI, etc.
3.  **Implementation (Coding):** The actual code is written based on the design documents. This is usually the longest phase.
4.  **Testing (Verification):** Once all the code is written, the quality assurance (QA) team tests the entire application to find and report bugs.
5.  **Deployment:** After testing is complete and the product is verified, it is released to the customer and deployed to production.
6.  **Maintenance:** Ongoing support and updates are provided for the finished product.

#### Key Characteristics

*   **Linear & Sequential:** The project proceeds in a straight line from start to finish.
*   **Documentation-Heavy:** A great deal of documentation is created at each stage.
*   **Rigid & Inflexible:** Change is difficult and expensive. If you find a mistake in the requirements during the testing phase, it's very costly to go back and fix.
*   **Low Customer Involvement:** The customer is mostly involved at the beginning (requirements) and the end (delivery).

---

### The Agile Model

**Agile** is not a single method, but a **mindset and a collection of principles** that prioritize flexibility, collaboration, and customer feedback. It is an iterative and incremental approach to software development. Instead of a single, long development cycle, Agile breaks the project down into small, manageable chunks.

**Analogy:** Painting a portrait. The artist starts with a rough sketch (a basic, working version of the product), shows it to the client for feedback, and then iteratively adds layers of detail and color in small cycles, getting feedback at each step until the final masterpiece is complete.

#### The Agile Process (using Scrum as a common example)

Agile is an umbrella term for many frameworks, like Scrum, Kanban, and XP. Scrum is the most popular.

1.  **Product Backlog:** The project starts with a high-level vision and a prioritized list of all desired features, called the product backlog.
2.  **Sprints:** Work is broken down into short, time-boxed iterations, typically lasting 1-4 weeks, called **sprints**.
3.  **Sprint Planning:** At the beginning of each sprint, the team selects a small number of items from the top of the backlog that they believe they can complete in that sprint.
4.  **Development:** The team works on building and testing these features. They typically have a short daily meeting (a "daily stand-up") to sync up.
5.  **Deliver a Working Increment:** At the end of the sprint, the team's goal is to have a **potentially shippable increment**—a small, working, tested piece of the final product.
6.  **Sprint Review & Retrospective:** The team demonstrates the working software to stakeholders to get feedback, which can influence the next sprint. The team also meets to discuss how they can improve their process.
7.  **Repeat:** The cycle repeats until the product is considered complete or the budget runs out.

#### Key Characteristics

*   **Iterative & Incremental:** The product is built in small pieces, with each iteration adding to the whole.
*   **Flexible & Adaptive:** Change is expected and welcomed. The backlog can be reprioritized at any time.
*   **High Customer Collaboration:** The customer is involved throughout the entire process, providing frequent feedback.
*   **Focus on People & Communication:** Emphasizes collaboration within a self-organizing, cross-functional team.

---

### Comparison: Agile vs. Waterfall

| Feature               | Waterfall                                       | Agile                                                   |
| :-------------------- | :---------------------------------------------- | :------------------------------------------------------ |
| **Methodology**       | Linear, sequential                              | Iterative, incremental                                  |
| **Flexibility**       | Rigid, resistant to change                      | Highly flexible, welcomes change                        |
| **Requirements**      | Defined entirely at the start                   | Evolve throughout the project                           |
| **Customer Involvement** | Low (mostly at the beginning and end)           | High (continuous collaboration and feedback)            |
| **Testing**           | Done as a separate, late phase of the project   | Integrated throughout the entire development cycle      |
| **Delivery**          | A single, final product is delivered at the end | Small, working increments are delivered frequently      |
| **Risk**              | High. Problems are often discovered late.       | Low. Risks are identified and mitigated in each sprint. |
| **Best For**          | Simple, unchanging projects with clear requirements | Complex projects where requirements are likely to change |

### When to Use Which?

*   **Use Waterfall when:** The requirements are 100% understood, fixed, and will not change. The project is simple, short, and the technology is well-known. (Examples: A simple informational website, projects with strict regulatory or contractual constraints that demand upfront design).
*   **Use Agile when:** You are in a dynamic environment where requirements are expected to evolve. You want to get a product to market quickly and improve it based on user feedback. This applies to almost all modern software development.
---