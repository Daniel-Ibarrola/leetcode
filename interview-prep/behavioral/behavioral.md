# Behavioral Questions

## Most Challenging Project

**(Situation)**

"At a previous role in a private security company, I led a project for a web application used internally to manage and schedule thousands of security officers across the country. I started as a full-stack engineer on the team and eventually became the owner of this critical project.
When I took over, the system was struggling. It was built on a microservices architecture on AWS with a React frontend, but it was burdened by years of technical debt. This resulted in severe performance issues, instability, and a slow pace for delivering new features, which was a constant source of frustration for our users—the company's own schedulers and managers."

**(Task)**
"My primary goal was two-fold. First, I needed to drastically improve the application's performance and stability to provide a usable and efficient experience for our users. Second, I wanted to uplift the engineering culture on my team to prevent this level of technical debt from happening again.
The core challenge was how to execute this crucial refactoring and cultural shift while still responding to the business's continuous demand for new features."

**(Action)**
"I developed a multi-pronged strategy, focusing my efforts on the areas where my team could deliver the most immediate and significant impact.
First, I tackled the most critical user-facing problems: **performance and stability**. My analysis showed the biggest bottleneck was on the frontend and in our direct APIs, which my team owned. I led the effort to:
- **Implement Pagination:** This was our biggest and quickest win. I designed and implemented pagination across our core APIs, which stopped the frontend from trying to load thousands of records at once.
- **Refactor Frontend State:** I also identified severe performance issues in our React code caused by incorrect dependency management in hooks. I personally refactored several key components and mentored my team on best practices to eliminate unnecessary re-renders.

Next, to **improve our team's internal codebase and practices**, I created an incremental refactoring plan and got my manager's buy-in. I led by example by adding unit and integration tests to my own work, and we established team-wide code review standards that required tests for all new code. This began to build a culture of quality and ownership.
Finally, I attempted to **address the root architectural flaw**. The entire system suffered from a design where Salesforce data was replicated directly into a DynamoDB database. This caused data consistency bugs and forced our services to perform slow, expensive joins in the application layer. I designed a more robust, API-first approach and presented it to the other team that owned the Salesforce integration, complete with data on the performance impact.
However, that team was very resistant to changing their established workflows. After several discussions, it became clear that pushing this change would be a long, political battle with no guarantee of success. Recognizing this, I made the strategic decision to pivot. I chose to focus my team's energy where we could have an immediate and guaranteed impact—on the frontend and our own microservices—rather than getting stalled by a roadblock we couldn't control."

**(Result)**
"Even without solving the core architectural problem, our focused efforts yielded significant results:
- **Massive Performance Improvement:** By implementing pagination and optimizing the frontend, we reduced the load time of our main scheduling page by over 70%. This completely eliminated the API gateway timeouts that had plagued our users and made their workflow far more efficient.
- **Improved Team Velocity and Quality:** On my team, the new testing practices and refactoring efforts increased our confidence and velocity. Our bug count dropped, and we could ship new features much more reliably.
- **A Key Leadership Lesson:** The experience was invaluable. While the data replication issue persisted due to the organizational roadblock, it taught me a critical lesson about senior engineering leadership: you must learn to differentiate between the _'ideal'_ solution and the _'optimal'_ solution within your current constraints. My goal was to deliver value to our users and the business, and I learned that the most effective path forward is sometimes to focus your energy on what you can control to deliver that value, rather than getting blocked by a pursuit of architectural purity. It was a powerful lesson in pragmatism."


#### Describe a time when you had to prioritize the integrity of the system (e.g., security, data privacy, or code quality) over a deadline or a feature request. What was the situation and what was the result?

**(Situation)** "Certainly. On a project to build a new Applicant Tracking System, we were approaching a critical launch deadline. During a final infrastructure review, I discovered a significant security vulnerability. The person who had set up our cloud environment had left the company, and our application load balancer—the main entry point to the entire system—was configured in a public subnet, making it directly exposed to the internet. This was a major risk, leaving our core application and its data vulnerable to network-level attacks."

**(Task)** "My immediate task was to resolve this critical security flaw without completely derailing the launch. I knew that just pointing out the problem wasn't enough. I had to convince my manager and the team that launching in this state was a non-negotiable risk, propose a solution that could be implemented very quickly, and then lead the implementation myself under the pressure of the impending deadline."

**(Action)** "First, I immediately documented the risk in clear, non-technical terms and presented it to my manager. I explained that while we were all focused on the deadline, launching with this vulnerability would be irresponsible.
Next, I proposed a concrete and actionable solution. I designed a new architecture where we would move the load balancer to a private subnet, making it inaccessible from the public internet. The new entry point would be Amazon CloudFront, which would communicate with the load balancer securely using a VPC Link. I highlighted that this architecture would not only fix the immediate exposure but also give us the long-term benefits of CloudFront's caching and Web Application Firewall (WAF) capabilities.
Seeing the tight timeline, I took ownership of the fix. I told my manager, 'I can get this done,' and volunteered to personally script all the necessary infrastructure changes in our Terraform configuration over the next day or two."

**(Result)** "My manager and the team immediately understood the severity of the risk and approved the plan. We did have to negotiate a very slight delay of two days to safely implement and test the new infrastructure, but I framed it as a necessary trade-off for the long-term security and health of the application.
We successfully deployed the new architecture, and the application launched with a much more secure and robust posture, protected from the vulnerabilities I had identified. In the end, we not only averted a major security incident but also ended up with a better system architecture for the future. My proactive approach in this high-pressure situation solidified my role as a security-conscious leader on the team and set a higher standard for how we reviewed our infrastructure going forward."

#### Describe a situation where you had a technical disagreement with a colleague. How did you approach the discussion, and what was the outcome?

**(S) Situation:** We were in the early stages of a new application, and we needed to decide on a global state management strategy. A friendly but firm technical disagreement emerged: I initially favored using React's built-in Context API because it was simple, dependency-free, and sufficient for our initial needs. My colleague, however, strongly advocated for MobX, based on his positive past experiences with its powerful reactive model and developer-friendly API.

**(T) Task:** My goal was to resolve this debate in a way that didn't just pick a winner, but ensured we chose the best possible tool for the project's long-term health. It was crucial to make a decision that the whole team could support and to maintain a positive and collaborative relationship with my colleague.

**(A) Action:** I took a structured, collaborative approach to navigate the disagreement:
1. **First, I suggested a dedicated meeting.** Instead of a prolonged debate over Slack, I proposed we set aside 30 minutes to formally discuss the options. We agreed that each of us would present the pros and cons of our preferred library, specifically in the context of our project's expected scale and features.
2. **During the discussion, I focused on active listening.** When he presented the benefits of MobX, I made sure to acknowledge its strengths, particularly its excellent performance and minimal boilerplate compared to a raw Context implementation. This showed I was taking his perspective seriously.
3. **Then, I reframed the problem.** After our presentations, it became clear both options had drawbacks we weren't excited about. I said, 'It sounds like we want the simplicity of Context but the performance and developer experience of MobX. What if the choice isn't just between A and B? Maybe there's a third option that gives us the best of both worlds.'
4. **This turned the discussion into a joint research effort.** We decided to spend an hour investigating newer, lighter-weight state management libraries. We both independently came across Zustand, which seemed to fit our exact criteria: a simple, hook-based API built on top of Context, but with performance optimizations and a much leaner feel. We built a tiny proof-of-concept together in just a few minutes.

**(R) Result:** We were both immediately impressed with Zustand and jointly presented it to the team as our unified recommendation. The team adopted it, and we've been extremely happy with the choice. It has scaled perfectly with our application, and it's been very easy for new developers to pick up. The most important outcome, however, was how we resolved the conflict. We transformed a potential 'me vs. you' argument into an 'us vs. the problem' collaboration, which ultimately led us to a better solution than either of us had originally proposed. It set a really positive tone for how our team makes technical decisions."

#### Can you give an example of how you've actively sought out diverse perspectives when designing a solution? How did that collaboration improve the final product?

(S) Situation: I was working on a web application that displayed Gantt charts for scheduling security officers. However, the charts were slow to load and difficult to navigate, frustrating users who needed efficiency in their day-to-day tasks.
(T) Task: I was assigned to implement a new React component that would function as a Gantt chart while addressing the performance and usability issues. This required recalculating the positions of elements on the chart dynamically, but my initial implementation was slow and complex.
(A) Action: Realizing that my initial approach was not optimal, I sought feedback from a coworker known for their expertise in CSS. I asked how we could better calculate and render positions for the chart elements. They introduced the idea of using CSS Grid, explaining that it was a natural fit for this type of component due to its layout capabilities. After researching Grid documentation and experimenting with prototypes, I implemented the new component using Grid. The redesign simplified the positioning logic and leveraged CSS for efficient rendering.
(R) Result: The new implementation drastically improved both performance and maintainability. Render times reduced by 50%, and user feedback highlighted that navigation felt more intuitive and responsive. Collaborating with my coworker taught me the value of seeking and applying diverse expertise while building scalable solutions.

#### Tell me about a time when you pushed back on a requirement

(S) Situation: I was working on a web application designed to help with the planning and scheduling of security officers. The app displayed plans for active contracts starting from the present day into the future. However, the app's performance was already hampered due to unoptimized database queries, causing significant delays when retrieving data for larger contracts.
(T) Task: I was assigned to implement a new requirement to allow users to view planning data for previous dates, in addition to future schedules. However, I quickly realized that the current backend performance wouldn't support this functionality, as adding past data would substantially increase the query load and lead to timeouts for large contracts.
(A) Action: To demonstrate the issue, I created a prototype and tested it with large contract data, confirming that the feature caused frequent timeouts. I presented these findings to one of the product managers and explained the technical challenges in clear, non-technical terms. I also highlighted the risk of frustrating users if the feature was implemented without addressing the underlying performance issues.
To provide a solution, I suggested deferring the requirement and focusing instead on delivering a new separate view specifically for historical data. This would isolate the issue and give the team time to refactor the backend properly in the future. I worked collaboratively with the product manager to prioritize this proposal and ensure alignment with the project's goals and resources.
(R) Result: Ultimately, it was decided that the feature wasn't critical and could be scheduled as a future enhancement, allowing the team to focus on more immediate priorities. This decision not only saved time in the short term but also avoided releasing a feature that could negatively impact user experience. My proactive approach helped the product team assess the trade-offs realistically and align stakeholders around a better long-term solution.

#### Explain a mistake you made and how you fixed it

I was working on a web app that displayed a list of employees with the option to filter them using several criteria.
The implementation of the filters was really messy—there were numerous filters, all managed within a 
single massive component. The code was difficult to understand, lacked proper tests, and had poor state 
management that triggered frequent and unnecessary re-renders, making the app frustratingly slow.

I decided to tackle this by refactoring the component. I split it into smaller, reusable components, 
each with a clear, single responsibility, and I improved the state management by introducing more efficient 
mechanisms to minimize re-renders. This not only made the codebase cleaner and easier to test but also significantly
improved the app's performance.

However, while the structural improvements were promising, the refactoring introduced 
new bugs that our existing tests missed. These bugs made it into production, causing issues for our users. 
After investigating, I realized the gaps in our test coverage came from how we had relied too heavily on manual 
testing and hadn't properly tested edge cases for the filters.
To fix the mistakes, I went back to the drawing board and wrote a comprehensive suite of unit and integration tests 
for the filter components. I also spent time improving our test strategies with the team, 
ensuring that our tests validated not only core functionality but also edge cases and performance under load. 
Additionally, we integrated these tests into our CI/CD pipeline to catch issues earlier in the cycle.
When the improved version was deployed, the filters worked flawlessly, and we received positive feedback 
from users about the performance improvements. Although the initial bugs caused temporary friction, 
the experience taught me a valuable lesson: changes to legacy codebases, no matter how small or positive they seem, 
require rigorous testing and validation to ensure smooth rollouts. It reinforced the importance 
of balancing technical improvement with a comprehensive safety net for production stability.

### A time when you received negative feedback or feedback you disagreed with

In a previous role, I received feedback that my pull requests were too large and hard to review. 
I initially disagreed because I thought grouping related changes together was more efficient.

However, I stepped back and asked the team for clarification on what specifically 
made them difficult to review. I realized that while my changes were logically grouped, 
they still created a high cognitive load for reviewers.

So I started breaking my work into smaller, incremental PRs and added clearer descriptions.

As a result, reviews became faster, and collaboration improved. It also helped me catch issues earlier. 
Even though I initially disagreed, the feedback helped me become more effective

### One weakness

One weakness I've worked on is that I tend to spend too much time trying to solve problems independently before asking for help. 
I like to be self-sufficient, but I realized this can sometimes slow things down.

To improve, I've started setting time limits — for example,
if I'm stuck for more than 30–60 minutes, I'll reach out to a teammate or document my approach and ask for feedback.

This has helped me move faster and also improved collaboration with the team

### Tell me about a time you took initiative

**Situation:** 
In a previous role, I inherited an AWS infrastructure project managed via Terraform. 
The codebase had grown into a single, monolithic 3,000-line file. 
To manage staging and production, the team relied on scripts that manually injected variables, which led to deploymentv errors.

**Task:**
I volunteered to lead a refactoring effort to modernize our terraform code.

**Action:**
I made a plan with the team to move toward a modular architecture. 
- **Modularization:** I broke the monolith into logical, reusable modules (VPC, RDS, ECS).
- **Environment Management:** I replaced the custom scripts with Terraform Workspaces.
- **Security Audit:** During the migration, I discovered resources exposed in public subnets.

**Result:**
The refactor reduced the time required to onboard new developers to the infrastructure. 
We achieved reduction in deployment failures related to environment configuration. 
Most importantly, it established a new team standard for code reviews, 
where we now prioritize modularity and automated security scanning as part of our CI/CD pipeline.

### Tell me about a time requirements were unclear

**Situation**
I was tasked with building a tool to visualize our CI infrastructure, which had grown highly complex. 
The goal was to create a "source of truth" table mapping relationships between pre-submit, continuous, 
and post-submit jobs. However, the initial brief was vague: it didn’t define what "related" meant (logic-wise), 
where the table should live, or how the automation should be triggered.

**Task**
My goal was to resolve these ambiguities before development started to avoid technical debt or 
building a tool that didn't meet the team's needs. I needed to define the data schema, the delivery mechanism, 
and the automation cadence.

**Action**
I took a proactive approach by performing a gap analysis before seeking clarification.
*   **Drafted Proposals:** Instead of just asking "what do you want?", I prepared three potential mapping criteria: hardware type (GPU/TPU), Environment (OS/Python version), and Trigger Chain.
*   **Stakeholder Alignment:** I scheduled a sync with the Product Owner. I presented my proposed mapping logic and suggested hosting the table on our internal Wiki (with a Markdown auto-updater) rather than a standalone file, to ensure visibility.
*   **Technical Design:** I proposed a GitHub Action-based trigger that would run the Python tool on a cron schedule to keep the table "live."

**Result**
By clarifying these requirements upfront, I reduced the project's estimated timeline by a week because we avoided two major re-designs of the data parsing logic. 
The final tool was adopted as a standard reference for the DevOps team, reducing the onboarding time for new engineers who previously struggled to understand our CI hierarchy.


### Describe a challenging bug

I worked on a tool to identify which commit caused a regression in a GitHub workflow. The tool would create a branch from a specific commit SHA and trigger a workflow on that branch.

We started seeing intermittent issues where the workflow would run on the default branch instead of the newly created one, which made the tool get stuck. 
What made it tricky was that before triggering the workflow, we verified via the GitHub API that the branch existed.

Since it was inconsistent and hard to reproduce, I focused on narrowing down the conditions. I added logging around branch creation and workflow triggers to better understand the timing.

Eventually, I realized this was a race condition: even though the API confirmed the branch existed, there was a short delay before it was fully available for other operations like triggering workflows.

To fix it, I introduced a small delay and validation step before triggering the workflow to ensure the branch was fully ready.

After this change, the issue stopped occurring and the tool became reliable again.

### Have you scaled an application or product? Share details about the refactoring and or architecture improvements

I managed the scaling of a workforce application for a private security firm. As the database grew, we faced critical performance issues: requests frequently exceeded API Gateway’s 29-second timeout, and AWS costs were spiking due to inefficient resource usage.

To resolve this, I implemented the following architectural improvements:

*   **Optimized DynamoDB Access Patterns:** I replaced expensive full-table scans with **Global Secondary Indexes (GSIs)**. For our primary query (fetching shifts by contract and date), I added a GSI using a composite Partition Key (`contractId#date`), which shifted the workload from $O(n)$ scans to targeted queries.
*   **Reduced Payload & Throughput:** I implemented **pagination** to prevent fetching thousands of records at once and used **ProjectionExpressions** to retrieve only the required attributes. This significantly lowered Consumed Read Capacity Units (RCUs) and reduced memory overhead in the Lambda.
*   **Asynchronous I/O with `aioboto3`:** I refactored the Python backend to use **`aioboto3`**. This allowed the Lambda to fetch data from multiple tables simultaneously rather than sequentially, drastically reducing the total execution time.
*   **Rigorous Integration Testing:** To ensure the refactor didn't break business logic, I utilized **`pytest`** to build a suite of integration tests that validated the new async query patterns against our existing data requirements.
*   **Canary Deployments & Monitoring:** We deployed changes using **Lambda Aliases** to shift traffic gradually. I used **AWS X-Ray** to identify bottlenecks and verified the success of the refactor via **CloudWatch**, observing significant improvements in **API Gateway Latency**, **Lambda Duration**, and **ConsumedReadCapacityUnits**.

**Result:** We successfully moved from frequent 29-second timeouts to **sub-second latency**, while also reducing our monthly AWS bill by optimizing DynamoDB throughput.

### Have you ever build a product from scratch? What was the product? Tech stack used and challenges to launch?
Yes, I recently led the development of a greenfield **Applicant Tracking System (ATS)** from the ground up. 

**The Product & Stack:**
The goal was to build a high-performance, internal tool to streamline our entire hiring pipeline. We chose **Next.js and TypeScript** for the frontend and API layers to take advantage of Server-Side Rendering and fast development cycles, with **Terraform** for our AWS infrastructure.

**The Challenges to Launch:**
While the tight deadline was a factor, the most significant challenge occurred just days before our scheduled launch. During a final infrastructure audit, I discovered a critical security flaw: our **Application Load Balancer (ALB)** had been configured in a **public subnet**, leaving the entry point to our system—and all our sensitive candidate data—directly exposed to the internet.

**The Action I Took:**
1.  **Risk Communication:** I immediately documented the vulnerability and presented it to my manager. I explained that while we were close to the deadline, launching with this exposure was a non-negotiable risk.
2.  **Architectural Pivot:** I proposed a more robust architecture: moving the ALB to a **private subnet** and using **Amazon CloudFront** as the sole entry point. This allowed us to leverage CloudFront’s caching and **Web Application Firewall (WAF)** while keeping our internal resources hidden.
3.  **Hands-on Resolution:** To minimize the delay, I took full ownership of the fix. I personally refactored our **Terraform configurations** to redeploy the networking stack, ensuring the change was version-controlled and repeatable.

**The Result:**
My manager approved the plan, and although it required a 48-hour launch delay, we successfully deployed a secure, production-ready environment. This not only averted a major security risk but also resulted in a faster, more resilient application due to the addition of CloudFront. It set a new standard for our team on how we perform infrastructure reviews for every new product launch."
f you are using CloudFront to talk to an ALB, you usually do this via a **Custom Origin** with a **Security Group rule** that only allows traffic from CloudFront (using prefix lists) or a custom header. If they ask for details on how you secured the ALB after moving it, you can mention: *"I used CloudFront as the origin and added a custom header check or used AWS IP prefix lists to ensure the ALB only accepted traffic from CloudFront."*

### Learning a new technology

### Tell me about a time you owned a production incident

**(S)** At the private security company, we began receiving reports from scheduling managers that the main workforce scheduling page was regularly timing out — often failing to load entirely. This was critical: schedulers used this page daily to manage thousands of officers across contracts. AWS CloudWatch confirmed it: our API Gateway was consistently hitting its 29-second hard timeout limit on the primary endpoint.

**(T)** I took ownership of the incident. My goal was to diagnose the root cause quickly, contain the impact for users in the short term, and implement a durable fix rather than a patch.

**(A)** I started with CloudWatch dashboards and X-Ray traces to identify where time was being spent. The traces made the root cause clear: our Lambda was performing full DynamoDB table scans and then doing expensive join-like operations in application code to assemble the response. For large contracts with thousands of shifts, this was O(n) on every request. As a short-term containment measure, I worked with the team to add a basic caching layer to reduce how often the slow path was hit. For the durable fix, I redesigned the access patterns: I introduced a Global Secondary Index with a composite partition key on `contractId#date`, replaced full scans with targeted queries, added pagination to prevent loading more records than necessary per request, and refactored the Python backend to use `aioboto3` for async parallel fetching across multiple tables. I validated the changes with integration tests against our actual data before deploying via Lambda Aliases for a gradual rollout.

**(R)** The timeouts stopped completely. We went from frequent 29-second failures to sub-second latency on that endpoint, and our DynamoDB consumed read capacity dropped significantly, which also reduced our monthly AWS costs. The incident also led to a lasting improvement in our observability posture: we set up dedicated CloudWatch dashboards and alarms for that endpoint so any future regression would be caught early rather than reported by users.

---

### Tell me about a time you had competing priorities and had to make a hard call

**(S)** While leading the scheduling application team, I was simultaneously responsible for three competing priorities: the business wanted a new reporting dashboard with an upcoming stakeholder deadline, our users were actively suffering from daily timeout failures, and we had a long-accumulated bug backlog. My manager wanted progress on all three fronts.

**(T)** I needed to make a clear sequencing call rather than spreading the team thin across everything. And I needed to defend it to both engineering and the business.

**(A)** I ran a lightweight impact-vs-effort analysis across the three areas: how many users were affected and how severely, the business risk of delay, and a rough engineering effort estimate. The performance issues were affecting every user every day and were the primary source of bugs and hotfixes consuming our sprint capacity — and they were making it harder to build reliably on top of the system. The reporting dashboard had a stakeholder deadline, but it was two sprints out, which gave us a window. The bug backlog had items of varying severity, most low frequency. I brought this framing to my manager: "If we don't fix performance first, any new feature we ship is going to be unreliable and we'll spend more time on bugs than features. Here's what I'd recommend and why." I proposed one sprint prioritizing the two or three highest-ROI stability fixes, followed by the dashboard feature, with the bug backlog handled incrementally as capacity allowed.

**(R)** My manager agreed to the sequencing. The performance sprint delivered ahead of schedule, and the stability improvements meant the dashboard feature was faster to build and test than it would have been otherwise — we hit the stakeholder deadline. It reinforced for me that taking time to make an explicit, data-backed prioritization call is almost always faster than trying to do everything at once.