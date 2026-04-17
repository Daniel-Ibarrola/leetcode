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


### What if a developer you were mentoring became defensive or didn't seem to want your help?

That's a challenging scenario, and my first priority would be to understand the 'why' behind their defensiveness.
**My first step would be to have a private, one-on-one conversation** with them, and I would start by listening. I'd try to depersonalize the feedback and ask open-ended questions like, 'How are you feeling about the project? I've made some suggestions in code reviews, and I want to make sure my feedback is coming across as helpful and not critical. Is there a better way we can work together?'
The defensiveness could be a sign of imposter syndrome, stress, or maybe my feedback style isn't working for them.
**If that approach works,** great. We can agree on a better way to collaborate, maybe through more pair programming or by focusing feedback on a different area.
**If they remain closed off,** my next step would be to focus on demonstrating value in a less direct way. For example, I could work on a task adjacent to theirs and produce very clear, well-documented code that they could use as a reference. Sometimes, showing is better than telling.
If the issue persists and starts to impact the team's goals, I would then discreetly and professionally **bring it up with our manager.** I'd frame it as a request for advice, saying something like, 'I'm trying to support [Name] but I'm struggling to connect. Do you have any suggestions on how I can better support them?' This makes it a collaborative problem-solving effort rather than just a complaint."
