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

---

## Why do you want to be a lead / why are you interested in this role?

I've been building technical depth for several years, and I've noticed that the moments where I've had the most impact weren't just when I wrote good code — they were when I helped the team make a better decision, stepped in to own an ambiguous problem, or made a colleague more effective.

At my previous roles, I found myself naturally gravitating toward things like establishing code review standards, proposing architectural improvements to other teams, or taking the initiative to drive infrastructure refactors — even when those weren't formally part of my job. I enjoyed that work more than I expected, and I got more done through it than through individual contribution alone.

I want a role where technical leadership and making others more effective is the core of the job, not a side effect. I'm ready to own outcomes at that level — both the technical direction and the people involved.

---

## Tell me about a time you disagreed with your manager

**(S)** While leading the scheduling application team, the business was pushing hard for a new reporting dashboard with a stakeholder deadline. At the same time, the app was suffering from severe performance issues — the main scheduling page was regularly timing out for our users. My manager's initial position was to keep the feature delivery pace up to meet the business commitment and treat performance as a "stretch goal" alongside the new work.

**(T)** I believed this was the wrong call. Shipping a new feature into a system users were already frustrated with would erode trust further and generate even more bugs and hotfixes to manage. I needed to make the case for reprioritizing without appearing to be blocking progress.

**(A)** Rather than just pushing back in conversation, I prepared data. I pulled API Gateway metrics and X-Ray traces showing the frequency of timeouts and which user flows were affected most. I also estimated the hidden developer cost: a significant portion of our sprint capacity was going toward bugs and hotfixes directly caused by the performance problems. I scheduled a one-on-one with my manager and presented this, saying: "I understand we need to move fast on features, but I want to show you that the performance issues are actively slowing us down, not just affecting users." I proposed a concrete plan: one sprint focused on the two or three changes with the highest ROI on stability — pagination and DynamoDB access pattern fixes — after which we'd be in a much stronger position to ship features reliably.

**(R)** My manager agreed to the one-sprint investment. We implemented the changes, page load times dropped by over 70%, and the timeouts stopped entirely. With that foundation in place, we shipped the reporting dashboard in the following sprint faster and with fewer bugs than we would have otherwise. My manager later said the data-driven framing was what made the difference — it turned a disagreement into a shared decision.

---

## Tell me about a time you influenced a decision without formal authority

**(S)** When I joined the infrastructure project, there were no established standards for how Terraform code should be written or reviewed. The codebase had grown into a single monolithic file, and there was no formal process for catching security or configuration issues before deployment. I had no management authority — I was a peer on the team.

**(T)** I wanted to move the team toward modular code, meaningful peer review, and automated security scanning in CI. But proposing a formal process change from a peer position is tricky — it can easily land as overstepping or adding bureaucracy.

**(A)** Instead of proposing a top-down process change, I led by example first. I started by refactoring my own contributions into modules and writing PR descriptions that explained the architectural reasoning. I made my code reviews thorough and constructive — pointing to the why behind suggestions, not just flagging issues. When I found a resource exposed in a public subnet during my own audit, I documented it clearly and shared it with the team, framing it as: "Here's a class of problem I think we should catch systematically." I used that as a natural entry point to propose a lightweight infrastructure PR checklist and to suggest adding `tfsec` to our CI pipeline. Crucially, I socialized both ideas with teammates one-on-one before raising them in a team meeting — so there was already buy-in before the formal discussion.

**(R)** The team adopted both the modular architecture pattern and the automated security scan without friction. The approach became self-sustaining: new teammates followed the patterns naturally because the codebase itself modeled the right approach. The experience reinforced something important: the most durable influence comes from making the right path the easiest path.

---

## How do you keep your team motivated during a difficult period?

**(S)** During the scheduling application performance overhaul, the team was under pressure from multiple directions: the business wanted new features, our users were frustrated with daily timeouts, and the underlying problems we were fixing were invisible to everyone outside engineering. Progress felt slow, and morale was dipping — some teammates felt like we were constantly fighting fires with no clear end in sight.

**(T)** As the person leading the technical effort, I recognized that motivation was as much my problem to solve as the architecture was.

**(A)** I took a few concrete steps. First, I made progress visible. When we shipped pagination and the timeout rate dropped, I shared the CloudWatch graphs in our team channel with context on what they meant for actual users. Making invisible backend work visible changed how people felt about it. Second, I gave teammates ownership of specific pieces of the refactor rather than directing everything myself — people were more invested in work they could personally point to. Third, I was honest in our syncs about where we were and what was left, instead of projecting false optimism. People trust leaders who level with them. Finally, I made sure our retrospectives actually resulted in process changes, so voicing frustration felt worth it.

**(R)** The team's energy shifted noticeably once we had that first visible metric improvement to point to. Getting to an early, concrete win was the key — it turned the narrative from "this is a slog with no end" to "this is working, and we're the ones doing it." Several teammates later said that having clear ownership of their piece and being kept honestly informed made a significant difference to how they experienced that period.
