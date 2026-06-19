# Mentoring People

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


### Tell me about a time you gave someone difficult feedback

**(S)** During the ATS project, I was working with a colleague who was responsible for a key part of the backend. As the project progressed, I noticed a consistent pattern in their pull requests: they were skipping tests for anything they described as a "simple" change. A couple of those changes had caused regressions that we only caught late in the review cycle, costing us time we didn't have with our launch deadline approaching. Code review comments alone hadn't changed the behavior.

**(T)** I needed to have a more direct conversation — one that could feel personal — without damaging our working relationship or making them defensive.

**(A)** I asked if we could have a brief one-on-one. I started by acknowledging the context: "I know we're both moving fast right now." Then I was specific rather than general: I referenced two concrete PRs where untested changes had caused regressions, rather than making a broad claim about their habits. I framed it as a project risk, not a character judgment: "These two regressions cost us review cycles we don't have to spare before launch. I want to make sure we're not in that position again." I also proposed a concrete agreement rather than just naming the problem: any change touching business logic — however small — gets at least one test. Then I asked for their perspective on why it was happening, which turned out to be time pressure — they were worried about keeping up with sprint pace and felt tests would slow them down.

**(R)** That context changed the conversation. We adjusted how we estimated tasks to explicitly include test-writing time, which removed the pressure they were feeling. The regression rate dropped significantly in subsequent sprints and we shipped with a solid test suite. The key was being specific and framing it as a shared problem rather than a critique — it meant they left the conversation with a solution, not just a warning.

### What if a developer you were mentoring became defensive or didn't seem to want your help?

That's a challenging scenario, and my first priority would be to understand the 'why' behind their defensiveness.
**My first step would be to have a private, one-on-one conversation** with them, and I would start by listening. I'd try to depersonalize the feedback and ask open-ended questions like, 'How are you feeling about the project? I've made some suggestions in code reviews, and I want to make sure my feedback is coming across as helpful and not critical. Is there a better way we can work together?'
The defensiveness could be a sign of imposter syndrome, stress, or maybe my feedback style isn't working for them.
**If that approach works,** great. We can agree on a better way to collaborate, maybe through more pair programming or by focusing feedback on a different area.
**If they remain closed off,** my next step would be to focus on demonstrating value in a less direct way. For example, I could work on a task adjacent to theirs and produce very clear, well-documented code that they could use as a reference. Sometimes, showing is better than telling.
If the issue persists and starts to impact the team's goals, I would then discreetly and professionally **bring it up with our manager.** I'd frame it as a request for advice, saying something like, 'I'm trying to support [Name] but I'm struggling to connect. Do you have any suggestions on how I can better support them?' This makes it a collaborative problem-solving effort rather than just a complaint."

### Tell me about a time you had to address an underperforming team member

**(S)** On one of my teams, I noticed an engineer was consistently missing their sprint commitments over two or three sprints. They would commit to tasks in planning, make visible progress midway through, but the work frequently came in either incomplete or requiring significant rework after review. The rest of the team had started factoring this in when planning, which was creating a two-tier dynamic I didn't want to solidify.

**(T)** I didn't have formal management authority over this person, but as the technical lead I was accountable for the team's output. I needed to address the pattern without making them feel singled out or demoralized, and I needed to understand the root cause before drawing conclusions about their performance.

**(A)** I started with a private conversation framed around curiosity rather than accountability: "I've noticed the last couple of sprints have been tough to close out — how are you feeling about the work? Is there something about how we're scoping or estimating that isn't working?" This surfaced that they were struggling with unfamiliar parts of the codebase and were reluctant to ask for help mid-sprint because they didn't want to seem slow. With that understanding, I made two changes: I started pairing with them briefly at the start of each task to unblock the first steps, and I introduced explicit mid-sprint check-ins so they could surface blockers early without it feeling like an admission of failure. I also flagged the situation to our manager — not as a complaint, but to ensure visibility: "I'm working with [Name] to get them more support; I wanted you to know the last few sprints have been difficult and I'm actively addressing it."

**(R)** The following sprint showed clear improvement. With earlier unblocking and regular check-ins, they closed out their tasks and the rework rate dropped. The key insight for me was distinguishing between a motivation problem and a support problem — in this case it was the latter, and removing the blocker was the fix. If the pattern had continued, I would have escalated more formally, but making that distinction first protected both the relationship and the team dynamic.
