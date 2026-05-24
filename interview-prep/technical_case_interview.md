
Technical case interview overview 

At BCG X, you will communicate with both technical and non-technical clients and work within a broader BCG team, including members who 
might not have a technical background. As such, the technical case interview is designed to test both your ability to draft a technical solution to a 
real-world problem as well as your ability to communicate and explain your ideas. The setting of the technical case interview is hypothetical. Your 
interviewer will describe a potential scenario that might arise at a client. She or he will also describe the type of data and information you would 
have access to. Your discussion will involve building a scalable solution to solve the problem at hand using the tools you know.

• Yourinterviewer will want to evaluate your technicaland analytical capabilities on the job
• You needto leverage theinformationyou receive and make suitable 
recommendations, both froma technical standpoint and within the business context 
• Theremay not onlybeonesingle good answer tothe case, you may find a 
different solution than a co-worker or friend and both be successful.
• Do notuse someone else'sanswers
• Throughout theentire interview, makesure you answerthe right questions to the right problem
• Alwayskeep inmind: What are wedoing? Why? How should we doit?Isthis goingto help 
the company?​
Technical Case:
What to focus on 
• Afterreceiving the case introduction, you may ask yourself: what aspects do I want to​ look at in 
the overall problem?​
• Once theproblemis defined, identify the algorithm/system you want to use or build
• Walkyour interviewer through how you would proceed.
• Alongtheway youmay needadditional information
• Youmay askforthem or makeassumptions butmindto always confirm you can make 
them
• Incaseof acomplexsolution, you needto present clear explanations
• Yourfinal solution may beright, but you must be able to present it in a simple 
andconvincing way. Will the client go for my solution if I present it this way?​


Frequently asked questions
Will I be expected to codeduring the second and final rounds?
• Youwon’t haveto code during the caseinterview , butyou may expect questions abouthowyou would structure code for the 
question at hand​. You might utilize a whiteboard to demonstrate your thinking. 
Should I expect to have to calculate everything by hand?
• Technical case interviews are primarily designed to test your technical problem solving and assess your way of thinking
• Wewon’taskyouto calculate all numbers outexactly,we are expecting quantitatively sound answers. This means that we 
might ask you to estimate numbers or, in case of uncertainty, give lower and upper bounds.
How far should I expand onthe technical details of mysolutions?
• Be readyto goin-depth – you will be challenged on your technical knowledge. Always explain your choices and clearly 
communicate whyyou think it’s the most suitable solution and not simply a random guess. That said, remember that the case lasts 
roughly 30 minutes, so don’t get hung up on unnecessary details. Ultimately, it’s about finding the right balance between proving 
your hands-on approachwith in-depth answers and touching on high-level topics. Always be mindful of the following:– The structureof your solution: Too many details may get you lost​.– Overall topics you want to cover: Focus on what is relevant and feel freeto suggest a step further if you feel a second use case 
could arise.
Will the interviewer expect meto be as strong on theconsulting/business approachas well on the technical side?
• The caseinterview focuses on a real client issue; your interviewer will challenge both your business recommendations 
and your technical choices.
• You areexpectedto be proficient with the typical consulting case framework (afterall, you are applying to a consulting firm), but you 
are not expected to perform the same as a generalist consulting track candidate who has beenextensively trained.


What’s the right balance between expanding on business and technical elements?​
• Unfortunately, there is no straightforward answer here. Often, you can infer technical details from your business recommendation 
while you can deduce commercial​ insights from your technical analysis. 
• The key is to have a logicaland structured approach. Always think and ask yourself: does thisapproachas a wholemake sense? Am 
I tackling the problem at hand?​
How much preparation do I needto bereally ready?​
• Also, here, there’s no straightforward answer. We strongly recommend you feel comfortable with solving typical 
consulting problems and leveraging technical solutions in a business setting.
• For more tips, please see our recommendations at page21.​
Am I allowed to use online resources like Stack Overflow?​
• Please refrain from using these resources during in-personinterviews (through Zoom or otherwise) and ask all questions you have to 
the interviewer instead. This promotes a more conversation interview and allows us to better understand your though-process.


Scenario:
Our client is a large online travel agent composed of multiple brands and 
agencies. In an effort to unify their offerings, the client asked BCG X if they could 
help increase customers' cross-brand discovery. X AI Scientists worked hard on a 
Proof of Concept (POC) recommendation system that provide small, relevant, 
advertising banners to users.
However, when scaling up, they struggled to serve more than 150 banners a 
minute. In order to complete the test, they must match the client traffic and 
monitor the algorithm's performance on user's behavior

It shows the interviewer that you listened and understood the problem. The global question should help 
you to have the first element of your answer
Business Domain
Ask yourself about the situation and context
Example: What are the specific goals that the 
client wants to achieve through this system?
Reframe the problem with a question
Example: Could the problem be reframed as a 
need for optimizing the existing system rather 
than scaling it in its current form?
Engineering Domain
Understand the problem by asking questions 
and clarifying ambiguities
Example: How much traffic are we processing?


Business Domain
Ask about the company, process, tech stack…
Ex: What is the current tech stack used for the 
recommendation system, and are there any constraints 
regarding technology choices?
Ex: What is the current process for updating and maintaining 
the recommendation system?
Be precise in your question to get directly what you 
need for your design 
Tell what you are trying to achieve
Don't ask out-of-scope questions
• Ex: How does your company handle customer service 
inquiries related to travel bookings?
Engineering Domain
Ask about the requirements you may need for your 
solution design
Example: Are we keeping the same scope of the 
PoC or expanding?
Copyright © 2023 by Boston Consulting Group. All rights reserved.
17
Draft an architecture diagram and explain from high-level 
overview to technical details
It shows the interviewer that you think logically and you structure your approach. 
Business Domain
Make assumptions with data
Detail the key steps of your solution
Put yourself in the customers shoes and transpose 
the situation to an industry you know
Engineering Domain
Detail your solution approach: System design, data 
model, interaction between components, 
bottlenecks, etc.
Don't forget to tell why your solution is suitable 
with the business issue
• Ex: "Adopting Apache Spark for our recommendation 
system boosts processing efficiency, enhancing user 
engagement and aligning with our client's goal of 
scalable cross-brand discovery."
Copyright © 2023 by Boston Consulting Group. All rights reserved.
18
Provide a complete and realistic recommendation from 
your solution design
Your recommendation should mix business and engineering.
Business domain
Be creative in your solution
• Example: Instead of just serving banners, integrate real-time 
user behavior analytics to adaptively change banner content, 
ensuring relevancy and increasing engagement." (This solution 
thinks outside the box by suggesting adaptive content based on 
real-time analytics.)
Don't provide qualitative recommendations, you 
could not link to a feasible engineering approach 
• Example: "The system should be more user-friendly." 
(This is too vague and doesn't provide a clear 
engineering approach to address the problem.)
Engineering domain
Fit your solution with reality & don't forget business 
coherence in your approach
• Example: Instead of an expensive multi-cloud solution, 
optimizing our current infrastructure aligns better with 
business scale and cost concerns.
Master your system design and argue good and bad 
technological choices
• Example: Serverless scales well but can have latency issues; 
containerization, like Kubernetes, offers balance but 
demands more expertise.
Don't stay focused on the technical design only
• Example: How can we ensure consistency in our application 
while scaling up?
Copyright © 2023 by Boston Consulting Group. All rights reserved.
19
Conclude about implementation and impact
Expand on a possible project timeline given a certain team size. Discuss what resources are 
necessary and risks that might occur during execution. Elaborate on costs, risks, and possible 
alternatives. Your interviewer will also appreciate seeing things from the client's perspective.
Business domain
Be sure that your solution design addresses the 
initial problem
• Ex: The distributed framework directly addresses the 
bottleneck issue, ensuring the recommendation system 
can handle the client's high traffic demands
Highlight the logic between the system design and 
the business problem
• Ex: By optimizing banner load speeds, we enhance user 
experience which aligns with the business goal of 
boosting cross-brand discovery
Engineering domain
In a real case, implementation is often as crucial 
as the design
• Ex: While our design ensures scalability, it's vital to 
choose the right cloud provider and monitor 
deployments to maintain system uptime and 
performance
Don't provide an unrealistic solution
• Ex: Implementing a cutting-edge tech without industry 
adoption might lead to future integration challenges 
and isn't advised given the current business need