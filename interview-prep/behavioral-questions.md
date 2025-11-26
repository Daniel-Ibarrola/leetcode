# Behavioral Questions

## What to look for in a code review.

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

---
## Software Development Management

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
## Mentoring People

### "How would you approach mentoring a junior developer who has just joined the team?"

My approach to mentoring a new junior developer is to focus on gradually building their confidence and independence.
**First, I focus on building a connection.** In the first week, I'd set up regular, informal check-ins, not just to talk about work, but to make them feel welcome and establish a line of communication where they feel safe asking 'dumb' questions.
**Second, I'd start with small, well-defined tasks.** The goal is to give them an early win. I’d pair-program with them on their first task to walk them through our team's workflow—how we use git, our code review process, and our CI/CD pipeline.
**Third, my goal is to empower them.** When they get stuck, my first response isn't to give them the answer, but to ask questions like, 'What have you tried so far?' or 'Where in the codebase do you think you might find the answer?' This helps them develop their own problem-solving skills.
**Finally, I'd help them integrate with the wider team** by encouraging them to ask questions in public channels and by actively seeking their opinion in team meetings. The ultimate goal is for them to become a self-sufficient and confident member of the team."

### What do you think are the most important qualities of a good mentor?

- **Patience and Empathy:** Do you understand that people learn at different paces and have different communication styles?
- **Leadership and Influence:** Can you guide others without formal authority? Can you build consensus and foster a positive team culture?
- **Technical Depth:** Do you understand concepts well enough to explain them clearly to someone else?
- **Investment in the Team:** Are you focused only on your own success, or are you committed to the team's growth?
- **Time Management:** Can you balance your own project work with the responsibility of helping others?

### Describe a time you helped a struggling team member improve their performance

Absolutely. In a recent project, I had a great opportunity to mentor a teammate on some core React principles.

**(S) Situation:** We were developing a complex application in React. A junior developer was responsible for a feature with a lot of interactive elements, and we noticed it was suffering from significant performance issues—the UI was laggy and slow to respond to user input. During a code review, I saw that the root cause was a series of chained `useEffect` hooks being used to handle state changes that were dependent on each other. This was causing a cascade of re-renders on every interaction.

**(T) Task:** My responsibility was twofold. The immediate task was to fix the performance bottleneck to get the feature ready for our users. But the more important, long-term task was to help the developer understand _why_ this was an anti-pattern and how to use `useEffect` correctly, in line with React's intended design.

**(A) Action:** I took a multi-step, collaborative approach:
1. **First, I built trust by showing empathy.** I started a one-on-one session by sharing a story of how I had made similar mistakes with `useEffect` when I was first learning Hooks. This helped create a safe space and showed that this is a common learning hurdle, not a personal failure.
2. **Next, we distinguished the concepts.** I explained the key difference between code that needs to run in response to a user action (which belongs in an **event handler**) and code that needs to run to synchronize with an external system or prop/state changes (which is what **Effects** are for).
3. **Then, I pointed him to a great resource.** I mentioned that the React team has an awesome guide called "You Might Not Need an Effect" that explains this exact issue. We took about 15 minutes to read through it together, discussing the examples. This empowered him by showing him how to find high-quality answers himself.
4. **Finally, we refactored together.** With the concepts fresh in our minds, we pair-programmed to move the logic out of the unnecessary `useEffect` calls and into the correct event handlers (`onClick`, `onChange`, etc.).

**(R) Result:** The outcome was a huge success. The performance of the component improved dramatically, and the code became much simpler and easier to understand. More importantly, the developer had a real 'aha!' moment. In all his future work, he used `useEffect` correctly and with confidence. The best part was that a few weeks later, I saw him explaining the very same concepts to another new developer on the team.


### What if a developer you were mentoring became defensive or didn't seem to want your help?

That's a challenging scenario, and my first priority would be to understand the 'why' behind their defensiveness.
**My first step would be to have a private, one-on-one conversation** with them, and I would start by listening. I'd try to depersonalize the feedback and ask open-ended questions like, 'How are you feeling about the project? I've made some suggestions in code reviews, and I want to make sure my feedback is coming across as helpful and not critical. Is there a better way we can work together?'
The defensiveness could be a sign of imposter syndrome, stress, or maybe my feedback style isn't working for them.
**If that approach works,** great. We can agree on a better way to collaborate, maybe through more pair programming or by focusing feedback on a different area.
**If they remain closed off,** my next step would be to focus on demonstrating value in a less direct way. For example, I could work on a task adjacent to theirs and produce very clear, well-documented code that they could use as a reference. Sometimes, showing is better than telling.
If the issue persists and starts to impact the team's goals, I would then discreetly and professionally **bring it up with our manager.** I'd frame it as a request for advice, saying something like, 'I'm trying to support [Name] but I'm struggling to connect. Do you have any suggestions on how I can better support them?' This makes it a collaborative problem-solving effort rather than just a complaint."

---
## What was the most challenging thing you've faced in your career?

_"One of the most challenging and rewarding experiences of my career was when I had to step up to secure a new project's infrastructure while still learning the core technology under a tight deadline._
**(S) Situation:** _Our team had just started a new project on AWS, and the infrastructure was being set up using Terraform. I noticed during a review that the architecture had a significant security flaw: the web server's load balancer was publicly exposed to the internet. As a result, we were seeing logs indicating that the application was already being hit by probing attacks, creating a major vulnerability before we had even launched._

**(T) Task:** _My primary task was to get the situation resolved. I had been learning AWS and Terraform on my own time, so I felt a responsibility to act. My goal was twofold: first, to secure the infrastructure immediately to stop the attacks, and second, to do this without derailing the project's tight deadline, even though I was still new to production-level Terraform._

**(A) Action:** *I took a very direct and hands-on approach:
1. **First, I presented a solution.** I proactively went to my manager with a clear, documented proposal. I explained the vulnerability and outlined a more secure architecture where the servers would be in a private subnet, and the only public entry point would be through CloudFront, which would act as our CDN and protective layer.
2. **Next, I took ownership.** My manager was convinced and tasked me with refactoring the infrastructure. This was a huge challenge, as I had to learn and deliver simultaneously. I adopted a disciplined strategy: during the day, I focused on writing and testing the Terraform code for the new networking setup. In the evenings, I spent my time diving deep into Terraform's documentation and best practices, specifically around creating reusable modules and managing state securely.
3. **To minimize risk,** I built a small-scale prototype of the new VPC and security group configuration in a separate environment before applying the changes to our main project.*

**(R) Result:** _The refactor was a complete success. We deployed the new infrastructure, and the attacks stopped immediately. The application was now properly secured, and as a bonus, using CloudFront also improved our potential performance and allowed us to add a Web Application Firewall (WAF) for another layer of security. It was incredibly challenging to learn so quickly under pressure, but it solidified my skills and directly protected the business. It proved to me that my personal investment in learning can have a huge and immediate impact."_

---

## How do you handle conflicts in a team?

I believe the best way to handle conflict is to turn it from a disagreement into a collaborative problem-solving session. A great example of this was when a colleague and I had to choose a state management library for a new React project.

**(S) Situation:** We were in the early stages of a new application, and we needed to decide on a global state management strategy. A friendly but firm technical disagreement emerged: I initially favored using React's built-in Context API because it was simple, dependency-free, and sufficient for our initial needs. My colleague, however, strongly advocated for MobX, based on his positive past experiences with its powerful reactive model and developer-friendly API.

**(T) Task:** My goal was to resolve this debate in a way that didn't just pick a winner, but ensured we chose the best possible tool for the project's long-term health. It was crucial to make a decision that the whole team could support and to maintain a positive and collaborative relationship with my colleague.

**(A) Action:** I took a structured, collaborative approach to navigate the disagreement:
1. **First, I suggested a dedicated meeting.** Instead of a prolonged debate over Slack, I proposed we set aside 30 minutes to formally discuss the options. We agreed that each of us would present the pros and cons of our preferred library, specifically in the context of our project's expected scale and features.
2. **During the discussion, I focused on active listening.** When he presented the benefits of MobX, I made sure to acknowledge its strengths, particularly its excellent performance and minimal boilerplate compared to a raw Context implementation. This showed I was taking his perspective seriously.
3. **Then, I reframed the problem.** After our presentations, it became clear both options had drawbacks we weren't excited about. I said, 'It sounds like we want the simplicity of Context but the performance and developer experience of MobX. What if the choice isn't just between A and B? Maybe there's a third option that gives us the best of both worlds.'
4. **This turned the discussion into a joint research effort.** We decided to spend an hour investigating newer, lighter-weight state management libraries. We both independently came across Zustand, which seemed to fit our exact criteria: a simple, hook-based API built on top of Context, but with performance optimizations and a much leaner feel. We built a tiny proof-of-concept together in just a few minutes.

**(R) Result:** We were both immediately impressed with Zustand and jointly presented it to the team as our unified recommendation. The team adopted it, and we've been extremely happy with the choice. It has scaled perfectly with our application, and it's been very easy for new developers to pick up. The most important outcome, however, was how we resolved the conflict. We transformed a potential 'me vs. you' argument into an 'us vs. the problem' collaboration, which ultimately led us to a better solution than either of us had originally proposed. It set a really positive tone for how our team makes technical decisions."
