# Software Estimation Demystifying the Black Art

## **Welcome** 

_The most unsuccessful three years in the education of cost estimators appears to be fifth-grade arithmetic._ 

_—Norman R. Augustine_ 

Software estimation is not hard. Experts have been researching and writing about software estimation for four decades, and they have developed numerous techniques that support accurate software estimates. Creating accurate estimates is straightforward—once you understand how to create them. But not all estimation practices are intuitively obvious, and even smart people won’t discover all the good practices on their own. The fact that someone is an expert developer doesn’t make that person an expert estimator. 

Numerous aspects of estimation are not what they seem. Many so-called estimation problems arise from misunderstanding what an “estimate” is or blurring other similar-but-not-identical concepts with estimation. Some estimation practices that seem intuitively useful don’t produce accurate results. Complex formulas sometimes do more harm than good, and some deceptively simple practices produce surprisingly accurate results. 

This book distills four decades of research and even more decades of hands-on experience to help developers, leads, testers, and managers become effective estimators. Learning about software estimation turns out to be generally useful because the influences that affect software estimates are the influences that affect software development itself. 

## **Art vs. Science of Software Estimation** 

Software estimation research is currently focused on improving estimation techniques so that sophisticated organizations can achieve project results within ±5% of estimated results instead of within ±10%. These techniques are mathematically intensive. Understanding them requires a strong math background and concentrated study. Using them requires number crunching well beyond what you can do on your hand calculator. These techniques work best when embodied in commercial software estimation tools. I refer to this set of practices as the _science of estimation_ . 

Meanwhile, the typical software organization is not struggling to improve its estimates from ±10% to ±5% accuracy. The typical software organization is struggling to avoid estimates that are incorrect by 100% or more. (The reasons for this are manifold and will be discussed in detail in Chapters 3 and 4.) 

**xv** 

**xvi Welcome** 

Our natural tendency is to believe that complex formulas like this: 

**==> picture [180 x 15] intentionally omitted <==**

will always produce more accurate results than simple formulas like this: 

## Effort = NumberOfRequirements * AverageEffortPerRequirement 

But complex formulas aren’t necessarily better. Software projects are influenced by numerous factors that undermine many of the assumptions contained in the complex formulas of the science of estimation. Those dynamics will be explained later in this book. Moreover, most software practitioners have neither the time nor the inclination to learn the intensive math required to understand the science of estimation. 

Consequently, this book emphasizes rules of thumb, procedures, and simple formulas that are highly effective and understandable to practicing software professionals. These techniques will not produce estimates that are accurate to within ±5%, but they will reduce estimation error to about 25% or less, which turns out to be about as useful as most projects need, anyway. I call this set of techniques the _art of estimation_ . 

This book draws from both the art and science of software estimation, but its focus is on software estimation as an art. 

## **Why This Book Was Written and Who It Is For** 

The literature on software estimation is widely scattered. Researchers have published hundreds of articles, and many of them are useful. But the typical practitioner doesn’t have time to track down dozens of papers from obscure technical journals. A few previous books have described the science of estimation. Those books are 800–1000 pages long, require a good math background, and are targeted mainly at professional estimators—consultants or specialists who estimate large projects and do so frequently. 

I wrote this book for developers, leads, testers, and managers who need to create estimates occasionally as one of their many job responsibilities. I believe that most practitioners want to improve the accuracy of their estimates but don’t have the time to obtain a Ph.D. in software estimation. These practitioners struggle with practical issues like how to deal with the politics that surround the estimate, how to present an estimate so that it will actually be accepted, and how to avoid having someone change your estimate arbitrarily. If you are in this category, this book was written for you. 

The techniques in this book apply to Internet and intranet development, embedded software, shrink-wrapped software, business systems, new development, legacy systems, large projects, small projects—essentially, to estimates for all kinds of software. 

**Welcome xvii** 

## **Key Benefits Of This Book** 

By focusing on the art of estimation, this book provides numerous important estimation insights: 

- What an “estimate” is. (You might think you already know what an estimate is, but common usages of the term are inaccurate in ways that undermine effective estimation.) 

- The specific factors that have made your past estimates less accurate than they could have been. 

- Ways to distinguish a good estimate from a poor one. 

- Numerous techniques that will allow _you personally_ to create good estimates. 

- Several techniques you can use to help _other people on your team_ create good estimates. 

- Ways that _your organization_ can create good estimates. (There are important differences between personal techniques, group techniques, and organizational techniques.) 

- Estimation approaches that work on agile projects, and approaches that work on traditional, sequential (plan-driven) projects. 

- Estimation approaches that work on small projects and approaches that work on large projects. 

- How to navigate the shark-infested political waters that often surround software estimation. 

In addition to gaining a better understanding of estimation concepts, the practices in this book will help you estimate numerous specific attributes of software projects, including: 

- New development work, including schedule, effort, and cost 

- Schedule, effort, and cost of legacy systems work 

- How many features you can deliver within a specific development iteration 

- The amount of functionality you can deliver for a whole project when schedule and team size are fixed 

- Proportions of different software development activities needed, including how much management work, requirements, construction, testing, and defect correction will be needed 

- Planning parameters, such as tradeoffs between cost and schedule, best team size, amount of contingency buffer, ratio of developers to testers, and so on 

**xviii Welcome** 

- Quality parameters, including time needed for defect correction work, defects that will remain in your software at release time, and other factors 

- Practically anything else you want to estimate 

In many cases, you’ll be able to put this book’s practices to use right away. 

Most practitioners will not need to go any further than the concepts described in this book. But understanding the concepts in this book will lay enough groundwork that you’ll be able to graduate to more mathematically intensive approaches later on, if you want to. 

## **What This Book Is Not About** 

This book is not about how to estimate the very largest projects—more than 1 million lines of code, or more than 100 staff years. Very large projects should be estimated by professional estimators who have read the dozens of obscure journal articles, who have studied the 800–1000-page books, who are familiar with commercial estimation software, and who are as skilled in both the art and science of estimation. 

## **Where to Start** 

Where you start will depend on what you want to get out of the book. 

_**If you bought this book because you need to create an estimate right now…**_ Begin with Chapter 1 (“What Is an “Estimate”?), and then move to Chapter 7 (“Count, Compute, Judge”) and Chapter 8 (“Calibration and Historical Data”). After that, skim the tips in Chapters 10–20 to find the techniques that will be the most immediately useful to you. By the way, this book’s tips are highlighted in the text and numbered, and all of the tips—118 total—are also collected in Appendix C, “Software Estimation Tips.” 

_**If you want to improve your personal estimation skills, if you want to improve your organization’s estimation track record, or if you’re looking for a better understanding of software estimation in general…**_ You can read the whole book. If you like to understand general principles before you dive into the details, read the book in order. If you like to see the details first and then draw general conclusions from the details, you can start with Chapter 1, read Chapters 7 through 23, and then go back and read the earlier chapters that you skipped. 

_Bellevue, Washington New Year’s Day, 2006_ 

**Welcome xix** 

## **Microsoft Press Support** 

Every effort has been made to ensure the accuracy of this book. Microsoft Press provides corrections for books through the World Wide Web at the following address: _http://www.microsoft.com/learning/support/books/_ 

To connect directly to the Microsoft Press Knowledge Base and enter a query regarding a question or issue that you may have, go to: _http://www.microsoft.com/mspress/support/search.asp_ 

If you have comments, questions, or ideas regarding this book, please send them to Microsoft Press using either of the following methods: 

Postal Mail: 

_Microsoft Press Attn:_ Software Estimation _Editor One Microsoft Way Redmond, WA 98052-6399_ E-Mail: _mspinput@microsoft.com_ 

## **Acknowledgments** 

I continue to be amazed at the many ways the Internet supports high-quality work. My first book’s manuscript was reviewed almost entirely by people who lived within 50 miles of me. This book’s manuscript included reviewers from Argentina, Australia, Canada, Denmark, England, Germany, Iceland, The Netherlands, Northern Ireland, Japan, Scotland, Spain, and the United States. The book has benefited enormously from these reviews. 

Thanks first to the people who contributed review comments on significant portions of the book: Fernando Berzal, Steven Black, David E. Burgess, Stella M. Burns, Gavin Burrows, Dale Campbell, Robert A. Clinkenbeard, Bob Corrick, Brian Donaldson, Jason Hills, William Horn, Carl J Krzystofczyk, Jeffrey D. Moser, Thomas Oswald, Alan M. Pinder, Jon Price, Kathy Rhode, Simon Robbie, Edmund Schweppe, Gerald Simon, Creig R. Smith, Linda Taylor, and Bernd Viefhues. 

Thanks also to the people who reviewed selected portions of the book: Lisa M. Adams, Hákon Ágústsson, Bryon Baker, Tina Coleman, Chris Crawford, Dominic Cronin, Jerry Deville, Conrado Estol, Eric Freeman, Hideo Fukumori, C. Dale Hildebrandt, Barbara Hitchings, Jim Holmes, Rick Hower, Kevin Hutchison, Finnur Hrafn Jonsson, Aaron Kiander, Mehmet Kerem K ~~izi~~ ltunç, Selimir Kustudic, Molly J. Mahai, Steve Mattingly, Joe Nicholas, Al Noel, David O’Donoghue, Sheldon Porcina, David J. Preston, Daniel Read, David Spokane, Janco Tanis, Ben Tilly, and Wendy Wilhelm. 

I’d especially like to acknowledge Construx’s estimation seminar instructors. After years of stimulating discussions, it’s often impossible to tell which ideas originated with me and which originated with them. Thanks to Earl Beede, Gregg Boer, Matt Peloquin, Pamela Perrott, and Steve Tockey. 

This book focuses on estimation as an art, and this book’s simplifications were made possible by researchers who have spent decades clarifying estimation as a science. My heartfelt appreciation to three of the giants of estimation science: Barry Boehm, Capers Jones, and Lawrence Putnam. 

Working with Devon Musgrave, project editor for this book, has once again been a privilege. Thanks, Devon! Becka McKay, assistant editor, also improved my original manuscript in countless ways. Thanks also to the rest of the Microsoft Press staff, including Patricia Bradbury, Carl Diltz, Tracey Freel, Jessie Good, Patricia Masserman, Joel Panchot, and Sandi Resnick. And thanks to indexer Seth Maislin. 

Thanks finally to my wife, Ashlie, who is—in my estimation—the best life partner I could ever hope for. 

**xxi** 

## **Equations** 

**Equation #1** Program Evaluation and Review Technique (PERT) Formula 109 **Equation #2** Pessimistic PERT Formula 109 **Equation #3** Magnitude of Relative Error (MRE) Formula 110 **Equation #4** Simple Standard Deviation Formula 121 **Equation #5** Complex Standard Deviation Formula 122 **Equation #6** Modified Complex Standard Deviation Formula 124 **Equation #7** PERT Formula for Estimating Number of Components 139 **Equation #8** Dutch Method’s Indicative Function Point Count Formula 203 **Equation #9** ISBSG Effort Formula for General Projects 216 **Equation #10** ISBSG Effort Formula for Mainframe Projects 216 **Equation #11** ISBSG Effort Formula for Mid-Range Projects 217 **Equation #12** ISBSG Effort Formula for Desktop Projects 217 **Equation #13** ISBSG Effort Formula for Third Generation Projects 217 **Equation #14** ISBSG Effort Formula for Fourth Generation Projects 217 **Equation #15** ISBSG Effort Formula for Enhancement Projects 217 **Equation #16** ISBSG Effort Formula for New Development Projects 217 **Equation #17** The Basic Schedule Equation 221 **Equation #18** Informal Comparison to Past Projects Formula 223 

**xxiii** 

## **Figures** 

- **Figure 1-1** Single-point estimates assume 100% probability of the actual outcome equaling the planned outcome. This isn’t realistic. 6 

- **Figure 1-2** A common assumption is that software project outcomes follow a bell curve. This assumption is incorrect because there are limits to how efficiently a project team can complete any given amount of work. 7 

- **Figure 1-3** An accurate depiction of possible software project outcomes. There is a limit to how well a project can go but no limit to how many problems can occur. 8 

- **Figure 1-4** The probability of a software project delivering on or before a particular date (or less than or equal to a specific cost or level of effort). 8 

- **Figure 1-5** All single-point estimates are associated with a probability, explicitly or implicitly. 9 

- **Figure 1-6** Improvement in estimation of a set of U.S. Air Force projects. The predictability of the projects improved dramatically as the organizations moved toward higher CMM levels. 10 

- **Figure 1-7** Improvement in estimation at the Boeing Company. As with the U.S. Air Force projects, the predictability of the projects improved dramatically at higher CMM levels. 10 

- **Figure 1-8** Schlumberger improved its estimation accuracy from an average overrun of 35 weeks to an average underrun of 1 week. 11 

- **Figure 1-9** Projects change significantly from inception to delivery. Changes are usually significant enough that the project delivered is not the same as the project that was estimated. Nonetheless, if the outcome is similar to the estimate, we say the project met its estimate. 12 

- **Figure 2-1** Results from administering the “How Good an Estimator Are You?” quiz. Most quiz-takers get 1–3 answers correct. 17 

- **Figure 3-1** The penalties for underestimation are more severe than the penalties for overestimation, so, if you can’t estimate with complete accuracy, try to err on the side of overestimation rather than underestimation. 24 

- **Figure3-2** Project outcomes reported in The Standish Group’s Chaos report have fluctuated year to year. About three quarters of all software projects are delivered late or fail outright. 25 

- **Figure 3-3** Estimation results from one organization. General industry data suggests that this company’s estimates being about 100% low is typical. Data used by permission. 26 

**xxv** 

**xxvi** 

**Figures** 

|**Figure**|**3-4**|When given the option of a shorter average schedule with higher|
|---|---|---|
|||variability or a longer average schedule with lower variability, most|
|||businesses will choose the second option.<br>30|
|**Figure**|**4-1**|The Cone of Uncertainty based on common project|
|||milestones.<br>36|
|**Figure**|**4-2**|The Cone of Uncertainty based on calendar time. The Cone narrows|
|||much more quickly than would appear from the previous depiction|
|||in Figure 4-1.<br>37|
|**Figure**|**4-3**|If a project is not well controlled or well estimated, you can end up|
|||with a Cloud of Uncertainty that contains even more estimation|
|||error than that represented by the Cone.<br>38|
|**Figure**|**4-4**|The Cone of Uncertainty doesn’t narrow itself. You narrow the Cone|
|||by making decisions that remove sources of variability from the|
|||project. Some of these decisions are about what the project will|
|||deliver; some are about what the project will_not_deliver. If these deci-|
|||sions change later, the Cone will widen.<br>39|
|**Figure**|**4-5**|A Cone of Uncertainty that allows for requirements increases over|
|||the course of the project.<br>43|
|**Figure**|**4-6**|Example of variations in estimates when numerous adjustment fac-|
|||tors are present. The more adjustment factors an estimation method|
|||provides, the more opportunity there is for subjectivity to creep into|
|||the estimate.<br>48|
|**Figure**|**4-7**|Example of low variation in estimates resulting from a small number|
|||of adjustment factors. (The scales of the two graphs are different, but|
|||they are directly comparable when you account for the difference in|
|||the average values on the two graphs.)<br>49|
|**Figure**|**4-8**|Average error from off-the-cuff estimates vs. reviewed estimates.<br>50|
|**Figure**|**5-1**|Growth in effort for a typical business-systems project. The specific|
|||numbers are meaningful only for the average business-systems|
|||project. The general dynamic applies to software projects of all|
|||kinds.<br>56|
|**Figure**|**5-2**|The number of communication paths on a project increases propor-|
|||tionally to the square of the number of people on the team.<br>57|
|**Figure**|**5-3**|Diseconomy of scale for a typical business-systems project ranging|
|||from 10,000 to 100,000 lines of code.<br>58|
|**Figure**|**5-4**|Diseconomy of scale for projects with greater size differences and|
|||the worst-case diseconomy of scale.<br>59|



**Figures xxvii** 

- **Figure 5-5** Differences between ratio-based estimates and estimates based on diseconomy of scale will be minimal for projects within a similar size range. 61 

- **Figure 5-6** Effect of personnel factors on project effort. Depending on the strength or weakness in each factor, the project results can vary by the amount indicated—that is, a project with the worst requirements analysts would require 42% more effort than nominal, whereas a project with the best analysts would require 29% less effort than nominal. 63 

- **Figure 5-7** Cocomo II factors arranged in order of significance. The relative lengths of the bars represent the sensitivity of the estimate to the different factors. 67 

- **Figure 5-8** Cocomo II factors arranged by potential to increase total effort (gray bars) and potential to decrease total effort (blue bars). 68 

- **Figure 5-9** Cocomo II factors with diseconomy of scale factors highlighted in blue. Project size is 100,000 LOC. 71 

- **Figure 5-10** Cocomo II factors with diseconomy of scale factors highlighted in blue. Project size is 5,000,000 LOC. 72 

- **Figure 8-1** An example of estimated outcomes for an estimate calibrated using industry-average data. Total variation in the effort estimates is about a factor of 10 (from about 25 staff months to about 250 staff months). 100 

- **Figure 8-2** An estimate calibrated using historical productivity data. The effort estimates vary by only about a factor of 4 (from about 30 staff months to about 120 staff months). 101 

- **Figure 10-1** Software projects tend to progress from large-grain focus at the beginning to fine-grain focus at the end. This progression supports increasing the use of estimation by decomposition as a project progresses. 116 

- **Figure 13-1** A simple review of individually created estimates significantly improves the accuracy of the estimates. 150 

- **Figure 13-2** A Wideband Delphi estimating form. 151 **Figure 13-3** A Wideband Delphi estimating form after three rounds of estimates. 152 

- **Figure 13-4** Estimation accuracy of simple averaging compared to Wideband Delphi estimation. Wideband Delphi reduces estimation error in about two-thirds of cases. 153 

**xxviii** 

**Figures** 

**Figure 13-5** Wideband Delphi when applied to terrible initial estimates. In this data set, Wideband Delphi improved results in 8 out of 10 cases. 153 **Figure 13-6** In about one-third of cases, Wideband Delphi helps groups that don’t initially include the correct answer to move outside their initial range and closer to the correct answer. 154 **Figure 14-1** A tool-generated simulation of 1,000 project outcomes. Output from Construx Estimate. 158 **Figure 14-2** Example of probable project outcomes based on output from estimation software. 159 **Figure 14-3** In this simulation, only 8 of the 1,000 outcomes fall within the desired combination of cost and schedule. 161 **Figure 14-4** Calculated effect of shortening or lengthening a schedule. 161 **Figure 15-1** An example of multiple estimates for a software project. 168 **Figure 16-1** Estimation on a poorly estimated project. Neither the inputs nor the process are well defined, and the inputs, process, and outputs are all open to debate. 172 **Figure 16-2** Estimation on a well-estimated project. The inputs and process are well defined. The process and outputs are not subject to debate; however, the inputs are subject to iteration until acceptable outputs are obtained. 172 **Figure 16-3** Flow of a single estimate on a well-estimated project. Effort, schedule, cost, and features that can be delivered are all computed from the size estimate. 173 **Figure 16-4** Summary of applicability of different estimation techniques by kind of project and project phase. 174 **Figure 16-5** A well-estimated project. The single-point estimates miss the mark, but the ranges all include the eventual outcome. 179 **Figure 16-6** A poorly estimated project. The project is uniformly underestimated, and the estimation ranges are too narrow to encompass the eventual outcome. 180 **Figure 17-1** A typical stage-gate product development life cycle. 182 **Figure 19-1** Industry-average effort for real-time projects. 211 **Figure 19-2** Industry-average effort for embedded systems projects. 212 **Figure 19-3** Industry-average effort for telecommunications projects. 212 **Figure 19-4** Industry-average effort for systems software and driver projects. 213 

**Figures xxix** 

- **Figure 19-5** Industry-average effort for scientific systems and engineering research projects. 213 

- **Figure 19-6** Industry-average effort for shrink-wrap and packaged software projects. 214 

- **Figure 19-7** Industry-average effort for public internet systems projects. 214 **Figure 19-8** Industry-average effort for internal intranet projects. 215 **Figure 19-9** Industry-average effort for business systems projects. 215 **Figure 19-10** Ranges of estimates derived by using the methods discussed in this chapter. The relative dot sizes and line thicknesses represent the weight I would give each of the estimation techniques in this case. 219 

- **Figure 20-1** The Cone of Uncertainty, including schedule adjustment numbers on the right axis. The schedule variability is much lower than the scope variability because schedule is a cube-root function of scope. 222 

- **Figure 20-2** The effects of compressing or extending a nominal schedule and the Impossible Zone. All researchers have found that there is a maximum degree to which a schedule can be compressed. 226 

- **Figure 20-3** Relationship between team size, schedule, and effort for businesssystems projects of about 57,000 lines of code. For team sizes greater than 5 to 7 people, effort and schedule both increase. 229 

- **Figure 20-4** Ranges of schedule estimates produced by the methods discussed in this chapter. The relative dot sizes and line thicknesses represent the weights I would give each of these estimates. Looking at all the estimates, including those that aren’t well founded, hides the real convergence among these estimates. 231 

- **Figure 20-5** Ranges of schedule estimates produced by the most accurate methods. Once the estimates produced by overly generic methods are eliminated, the convergence of the estimates becomes clear. 232 

- **Figure 22-1** Example of documenting estimate assumptions. 250 **Figure 22-2** Example of presenting percentage-confident estimates in a form that’s more visually appealing than a table. 253 

- **Figure 22-3** Example of presenting case-based estimates in a visual form. 254 

# **Part I Critical Estimation Concepts** 

## Chapter 1 **What Is an “Estimate”?** 

_It is very difficult to make a vigorous, plausible, and job-risking defense of an estimate that is derived by no quantitative method, supported by little data, and certified chiefly by the hunches of the managers._ 

_—Fred Brooks_ 

You might think you already know what an estimate is. My goal by the end of this chapter is to convince you that an estimate is different from what most people think. A _good_ estimate is even more different. 

Here is a dictionary definition of _estimate_ : 1. A tentative evaluation or rough calculation. 2. A preliminary calculation of the cost of a project. 3. A judgment based upon one’s impressions; opinion. (Source: _The American Heritage Dictionary_ , Second College Edition, 1985.) 

Does this sound like what you are asked for when you’re asked for an estimate? Are you asked for a _tentative_ or _preliminary_ calculation—that is, do you expect that you can change your mind later? 

Probably not. When executives ask for an “estimate,” they’re often asking for a commitment or for a plan to meet a target. The distinctions between estimates, targets, and commitments are critical to understanding what an estimate is, what an estimate is not, and how to make your estimates better. 

## **1.1 Estimates, Targets, and Commitments** 

Strictly speaking, the dictionary definition of _estimate_ is correct: an estimate is a prediction of how long a project will take or how much it will cost. But estimation on software projects interplays with business targets, commitments, and control. 

A _target_ is a statement of a desirable business objective. Examples include the following: 

- “We need to have Version 2.1 ready to demonstrate at a trade show in May.” 

- “We need to have this release stabilized in time for the holiday sales cycle.” 

- “These functions need to be completed by July 1 so that we’ll be in compliance with government regulations.” 

- “We must limit the cost of the next release to $2 million, because that’s the maximum budget we have for that release.” 

**3** 

**4 Part I Critical Estimation Concepts** 

Businesses have important reasons to establish targets independent of software estimates. But the fact that a target is desirable or even mandatory does not necessarily mean that it is achievable. 

While a target is a description of a desirable business objective, a _commitment_ is a promise to deliver defined functionality at a specific level of quality by a certain date. A commitment can be the same as the estimate, or it can be more aggressive or more conservative than the estimate. In other words, do not assume that the commitment has to be the same as the estimate; it doesn’t. 

**Tip #1** Distinguish between estimates, targets, and commitments. 

## **1.2 Relationship Between Estimates and Plans** 

Estimation and planning are related topics, but estimation is not planning, and planning is not estimation. Estimation should be treated as an unbiased, analytical process; planning should be treated as a biased, goal-seeking process. With estimation, it’s hazardous to want the estimate to come out to any particular answer. The goal is accuracy; the goal is not to seek a particular result. But the goal of planning is to seek a particular result. We deliberately (and appropriately) bias our plans to achieve specific outcomes. We plan specific means to reach a specific end. 

Estimates form the foundation for the plans, but the plans don’t have to be the same as the estimates. If the estimates are dramatically different from the targets, the project plans will need to recognize that gap and account for a high level of risk. If the estimates are close to the targets, then the plans can assume less risk. 

Both estimation and planning are important, but the fundamental differences between the two activities mean that combining the two tends to lead to poor estimates _and_ poor plans. The presence of a strong planning target can lead to substitution of the target for an analytically derived estimate; project members might even refer to the target as an “estimate,” giving it a halo of objectivity that it doesn’t deserve. 

Here are examples of planning considerations that depend in part on accurate estimates: 

- Creating a detailed schedule 

- Identifying a project’s critical path 

- Creating a complete work breakdown structure 

- Prioritizing functionality for delivery 

- Breaking a project into iterations 

Accurate estimates support better work in each of these areas (and Chapter 21, “Estimating Planning Parameters,” goes into more detail on these topics). 

**Chapter 1 What Is an “Estimate”?** 

**5** 

## **1.3 Communicating about Estimates, Targets, and Commitments** 

One implication of the close and sometimes confusing relationship between estimation and planning is that project stakeholders sometimes miscommunicate about these activities. Here’s an example of a typical miscommunication: 

_EXECUTIVE: How long do you think this project will take? We need to have this software ready in 3 months for a trade show. I can’t give you any more team members, so you’ll have to do the work with your current staff. Here’s a list of the features we’ll need._ 

_PROJECT LEAD: OK, let me crunch some numbers, and get back to you._ 

Later… 

_PROJECT LEAD: We’ve estimated the project will take 5 months._ 

_EXECUTIVE: Five months!? Didn’t you hear me? I said we needed to have this software ready in 3 months for a trade show!_ 

In this interaction, the project lead will probably walk away thinking that the executive is irrational, because he is asking for the team to deliver 5 months’ worth of functionality in 3 months. The executive will walk away thinking that the project lead doesn’t “get” the business reality, because he doesn’t understand how important it is to be ready for the trade show in 3 months. 

Note in this example that the executive was not really asking for an estimate; he was asking the project lead to come up with a _plan_ to hit a _target_ . Most executives don’t have the technical background that would allow them to make fine distinctions between estimates, targets, commitments, and plans. So it becomes the technical leader’s responsibility to translate the executive’s request into more specific technical terms. 

Here’s a more productive way that the interaction could go: 

_EXECUTIVE: How long do you think this project will take? We need to have this software ready in 3 months for a trade show. I can’t give you any more team members, so you’ll have to do the work with your current staff. Here’s a list of the features we’ll need._ 

_PROJECT LEAD: Let me make sure I understand what you’re asking for. Is it more important for us to deliver 100% of these features, or is it more important to have something ready for the trade show?_ 

**6 Part I Critical Estimation Concepts** 

_EXECUTIVE: We have to have something ready for the trade show. We’d like to have 100% of those features if possible._ 

_PROJECT LEAD: I want to be sure I follow through on your priorities as best I can. If it turns out that we can’t deliver 100% of the features by the trade show, should we be ready to ship what we’ve got at trade show time, or should we plan to slip the ship date beyond the trade show?_ 

_EXECUTIVE: We have to have something for the trade show, so if push comes to shove, we have to ship something, even if it isn’t 100% of what we want._ 

_PROJECT LEAD: OK, I’ll come up with a plan for delivering as many features as we can in the next 3 months._ 

**Tip #2** When you’re asked to provide an estimate, determine whether you’re supposed to be estimating or figuring out how to hit a target. 

## **1.4 Estimates as Probability Statements** 

If three-quarters of software projects overrun their estimates, the odds of any given software project completing on time and within budget are not 100%. Once we recognize that the odds of on-time completion are not 100%, an obvious question arises: “If the odds aren’t 100%, what are they?” This is one of the central questions of software estimation. 

Software estimates are routinely presented as single-point numbers, such as “This project will take 14 weeks.” Such simplistic single-point estimates are meaningless because they don’t include any indication of the probability associated with the single point. They imply a probability as shown in Figure 1-1—the only possible outcome is the single point given. 

**==> picture [344 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Only Possible Outcome<br>(100% Likely)<br>100%<br>Probability<br>Schedule (or Cost or Effort)<br>**----- End of picture text -----**<br>


**Figure 1-1** Single-point estimates assume 100% probability of the actual outcome equaling the planned outcome. This isn’t realistic. 

**Chapter 1 What Is an “Estimate”?** 

**7** 

A single-point estimate is usually a target masquerading as an estimate. Occasionally, it is the sign of a more sophisticated estimate that has been stripped of meaningful probability information somewhere along the way. 

**Tip #3** When you see a single-point “estimate,” ask whether the number is an estimate or whether it’s really a target. 

Accurate software estimates acknowledge that software projects are assailed by uncertainty from all quarters. Collectively, these various sources of uncertainty mean that project outcomes follow a probability distribution—some outcomes are more likely, some outcomes are less likely, and a cluster of outcomes in the middle of the distribution are most likely. You might expect that the distribution of project outcomes would look like a common bell curve, as shown in Figure 1-2. 

**==> picture [333 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
Nominal Outcome<br>Probability<br>Schedule (or Cost or Effort)<br>**----- End of picture text -----**<br>


**Figure 1-2** A common assumption is that software project outcomes follow a bell curve. This assumption is incorrect because there are limits to how efficiently a project team can complete any given amount of work. 

Each point on the curve represents the chance of the project finishing exactly on that date (or costing exactly that much). The area under the curve adds up to 100%. This sort of probability distribution acknowledges the possibility of a broad range of outcomes. But the assumption that the outcomes are symmetrically distributed about the mean (average) is not valid. There is a limit to how well a project can be conducted, which means that the tail on the left side of the distribution is truncated rather than extending as far to the left as it does in the bell curve. And while there is a limit to how well a project can go, there is no limit to how poorly a project can go, and so the probability distribution does have a very long tail on the right. 

Figure 1-3 provides an accurate representation of the probability distribution of a software project’s outcomes. 

**8 Part I Critical Estimation Concepts** 

**==> picture [343 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Nominal Outcome<br>100% (50/50 estimate)<br>Probability<br>Schedule (or Cost or Effort)<br>**----- End of picture text -----**<br>


**Figure 1-3** An accurate depiction of possible software project outcomes. There is a limit to how well a project can go but no limit to how many problems can occur. 

The vertical dashed line shows the “nominal” outcome, which is also the “50/50” outcome—there’s a 50% chance that the project will finish better and a 50% chance that it will finish worse. Statistically, this is known as the “median” outcome. 

Figure 1-4 shows another way of expressing this probability distribution. While Figure 1-3 showed the probabilities of delivering on specific dates, Figure 1-5 shows the probabilities of delivering on each specific date _or earlier_ . 

**==> picture [357 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
100%<br>Probability of<br>delivering on a<br>specific date or 50% Nominal Outcome<br>earlier (or for a (50/50 Estimate)<br>particular cost or<br>effort or less)<br>Schedule (or Cost or Effort)<br>**----- End of picture text -----**<br>


**Figure 1-4** The probability of a software project delivering on or before a particular date (or less than or equal to a specific cost or level of effort). 

Figure 1-5 presents the idea of probabilistic project outcomes in another way. As you can see from the figure, a naked estimate like “18 weeks” leaves out the interesting information that 18 weeks is only 10% likely. An estimate like “18 to 24 weeks” is more informative and conveys useful information about the likely range of project outcomes. 

**9** 

**Chapter 1 What Is an “Estimate”?** 

**==> picture [227 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
Probability Estimated<br>of Success Completion Time<br>90% 24 weeks<br>75% 22 weeks<br>50% 20 weeks<br>10% 18 weeks<br>0% 16 weeks<br>14 weeks<br>12 weeks<br>10 weeks<br>8 weeks<br>6 weeks<br>4 weeks<br>2 weeks<br>**----- End of picture text -----**<br>


**Figure 1-5** All single-point estimates are associated with a probability, explicitly or implicitly. 

**Tip #4** When you see a single-point estimate, that number’s probability is not 100%. Ask what the probability of that number is. 

You can express probabilities associated with estimates in numerous ways. You could use a “percent confident” attached to a single-point number: “We’re 90% confident in the 24-week schedule.” You could describe estimates as best case and worst case, which implies a probability: “We estimate a best case of 18 weeks and a worst case of 24 weeks.” Or you could simply state the estimated outcome as a range rather than a single-point number: “We’re estimating 18 to 24 weeks.” The key point is that all estimates include a probability, whether the probability is stated or implied. An explicitly stated probability is one sign of a good estimate. 

You can make a commitment to the optimistic end or the pessimistic end of an estimation range—or anywhere in the middle. The important thing is for you to know where in the range your commitment falls so that you can plan accordingly. 

## **1.5 Common Definitions of a “Good” Estimate** 

The answer to the question of what an “estimate” is still leaves us with the question of what a _good_ estimate is. Estimation experts have proposed various definitions of a good estimate. Capers Jones has stated that accuracy with ±10% is possible, but only on well-controlled projects (Jones 1998). Chaotic projects have too much variability to achieve that level of accuracy. 

**10** 

**Part I Critical Estimation Concepts** 

In 1986, Professors S.D. Conte, H.E. Dunsmore, and V.Y. Shen proposed that a good estimation approach should provide estimates that are within 25% of the actual results 75% of the time (Conte, Dunsmore, and Shen 1986). This evaluation standard is the most common standard used to evaluate estimation accuracy (Stutzke 2005). 

Numerous companies have reported estimation results that are close to the accuracy Conte, Dunsmore, and Shen and Jones have suggested. Figure 1-6 shows actual results compared to estimates from a set of U.S. Air Force projects. 

**==> picture [302 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
600%<br>500%<br>400%<br>Actual Results as<br>a Percentage of  300%<br>Estimated Results<br>200%<br>100%<br>0%<br>1 2 3<br>CMM Level of Organization Conducting the Project<br>**----- End of picture text -----**<br>


_Source: “A Correlational Study of the CMM and Software Development Performance” (Lawlis, Flowe, and Thordahl 1995)._ 

**Figure 1-6** Improvement in estimation of a set of U.S. Air Force projects. The predictability of the projects improved dramatically as the organizations moved toward higher CMM levels.[1] 

Figure 1-7 shows results of a similar improvement program at the Boeing Company. 

**==> picture [226 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
+150%<br>Historical data used for<br>all project estimates<br>Estimation<br>0%<br>Error<br>-150%<br>1 2 3 4 5<br>CMM Level<br>**----- End of picture text -----**<br>


**Figure 1-7** Improvement in estimation at the Boeing Company. As with the U.S. Air Force projects, the predictability of the projects improved dramatically at higher CMM levels. 

> 1 The CMM (Capability Maturity Model) is a system defined by the Software Engineering Institute to assess the effectiveness of software organizations. 

**11** 

**Chapter 1 What Is an “Estimate”?** 

A final, similar example, shown in Figure 1-8, comes from improved estimation results at Schlumberger. 

**==> picture [316 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
35<br>30<br>25<br>20<br>Average Overrun<br>15<br>(weeks)<br>10<br>5<br>0<br>−5<br>1 2 3 4 5 6 7<br>(4) (0) (3) (3) (4) (2) (3)<br>Starting Period Half Year<br>(# of projects)<br>**----- End of picture text -----**<br>


**Figure 1-8** Schlumberger improved its estimation accuracy from an average overrun of 35 weeks to an average underrun of 1 week. 

One of my client companies delivers 97% of its projects on time and within budget. Telcordia reported that it delivers 98% of its projects on time and within budget (Pitterman 2000). Numerous other companies have published similar results (Putnam and Myers 2003). Organizations are creating good estimates by both Jones’s definition and Conte, Dunsmore, and Shen’s definition. However, an important concept is missing from both of these definitions—namely, that accurate estimation results cannot be accomplished through estimation practices alone. They must also be supported by effective project control. 

## **1.6 Estimates and Project Control** 

Sometimes when people discuss software estimation they treat estimation as a purely predictive activity. They act as though the estimate is made by an impartial estimator, sitting somewhere in outer space, disconnected from project planning and prioritization activities. 

In reality, there is little that is pure about software estimation. If you ever wanted an example of Heisenberg’s Uncertainty Principle applied to software, estimation would be it. (Heisenberg’s Uncertainty Principle is the idea that the mere act of observing a thing changes it, so you can never be sure how that thing would behave if you weren’t observing it.) Once we make an estimate and, on the basis of that estimate, make a 

**12** 

**Part I Critical Estimation Concepts** 

commitment to deliver functionality and quality by a particular date, then we _control_ the project to meet the target. Typical project control activities include removing noncritical requirements, redefining requirements, replacing less-experienced staff with more-experienced staff, and so on. Figure 1-9 illustrates these dynamics. 

**==> picture [349 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
Staff diverted<br>to support<br>Staff not trade show<br>ready when Unstable<br>planned Requirements functionality<br>removed  removed<br>“Estimate” = Outcome =<br>20 staff months The Project 20 staff months<br>Requirements<br>added More<br>Staff diverted requirements<br>to support added<br>Less-experienced<br>old project<br>staff than planned<br>**----- End of picture text -----**<br>


**Figure 1-9** Projects change significantly from inception to delivery. Changes are usually significant enough that the project delivered is not the same as the project that was estimated. Nonetheless, if the outcome is similar to the estimate, we say the project met its estimate. 

In addition to project control activities, projects are often affected by unforeseen external events. The project team might need to create an interim release to support a key customer. Staff might be diverted to support an old project, and so on. 

Events that happen during the project nearly always invalidate the assumptions that were used to estimate the project in the first place. Functionality assumptions change, staffing assumptions change, and priorities change. It becomes impossible to make a clean analytical assessment of whether the project was estimated accurately— because the software project that was ultimately delivered is not the project that was originally estimated. 

In practice, if we deliver a project with about the level of functionality intended, using about the level of resources planned, in about the time frame targeted, then we typically say that the project “met its estimates,” despite all the analytical impurities implicit in that statement. 

Thus, the criteria for a “good” estimate cannot be based on its predictive capability, which is impossible to assess, but on the estimate’s ability to support project success, which brings us to the next topic: the Proper Role of Estimation. 

**Chapter 1 What Is an “Estimate”? 13** 

## **1.7 Estimation’s Real Purpose** 

Suppose you’re preparing for a trip and deciding which suitcase to take. You have a small suitcase that you like because it’s easy to carry and will fit into an airplane’s overhead storage bin. You also have a large suitcase, which you don’t like because you’ll have to check it in and then wait for it at baggage claim, lengthening your trip. You lay your clothes beside the small suitcase, and it appears that they will almost fit. What do you do? You might try packing them very carefully, not wasting any space, and hoping they all fit. If that approach doesn’t work, you might try stuffing them into the suitcase with brute force, sitting on the top and trying to squeeze the latches closed. If that still doesn’t work, you’re faced with a choice: leave a few clothes at home or take the larger suitcase. 

Software projects face a similar dilemma. Project planners often find a gap between a project’s business targets and its estimated schedule and cost. If the gap is small, the planner might be able to control the project to a successful conclusion by preparing extra carefully or by squeezing the project’s schedule, budget, or feature set. If the gap is large, the project’s targets must be reconsidered. 

The primary purpose of software estimation is not to predict a project’s outcome; it is to determine whether a project’s targets are realistic enough to allow the project to be controlled to meet them. Will the clothes you want to take on your trip fit into the small suitcase or will you be forced to take the large suitcase? Can you take the small suitcase if you make minor adjustments? Executives want the same kinds of answers. They often don’t want an accurate estimate that tells them that the desired clothes won’t fit into the suitcase; they want a plan for making as many of the clothes fit as possible. 

Problems arise when the gap between the business targets and the schedule and effort needed to achieve those targets becomes too large. I have found that if the initial target and initial estimate are within about 20% of each other, the project manager will have enough maneuvering room to control the feature set, schedule, team size, and other parameters to meet the project’s business goals; other experts concur (Boehm 1981, Stutzke 2005). If the gap between the target and what is actually needed is too large, the manager will not be able to control the project to a successful conclusion by making minor adjustments to project parameters. No amount of careful packing or sitting on the suitcase will squeeze all your clothes into the smaller suitcase, and you’ll have to take the larger one, even if it isn’t your first choice, or you’ll have to leave some clothes behind. The project targets will need to be brought into better alignment with reality before the manager can control the project to meet its targets. 

Estimates don’t need to be perfectly accurate as much as they need to be _useful_ . When we have the combination of accurate estimates, good target setting, and good planning and control, we can end up with project results that are close to the 

**14 Part I Critical Estimation Concepts** 

“estimates.” (As you’ve guessed, the word “estimate” is in quotation marks because the project that was estimated is not the same project that was ultimately delivered.) 

These dynamics of changing project assumptions are a major reason that this book focuses more on the art of estimation than on the science. Accuracy of ±5% won’t do you much good if the project’s underlying assumptions change by 100%. 

## **1.8 A Working Definition of a “Good Estimate”** 

With the background provided in the past few sections, we’re now ready to answer the question of what qualifies as a good estimate. 

_A good estimate is an estimate that provides a clear enough view of the project reality to allow the project leadership to make good decisions about how to control the project to hit its targets.._ 

This definition is the foundation of the estimation discussion throughout the rest of this book. 

## **Additional Resources** 

Conte, S. D., H. E. Dunsmore, and V. Y. Shen. _Software Engineering Metrics and Models._ Menlo Park, CA: Benjamin/Cummings, 1986. Conte, Dunsmore, and Shen’s book contains the definitive discussion of evaluating estimation models. It discusses the “within 25% of actual 75% of the time” criteria, as well as many other evaluation criteria. 

DeMarco, Tom. _Controlling Software Projects._ New York, NY: Yourdon Press, 1982. DeMarco discusses the probabilistic nature of software projects. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ . Upper Saddle River, NJ: Addison-Wesley, 2005. Appendix C of Stutzke’s book contains a summary of measures of estimation accuracy. 

## Chapter 2 

## **How Good an Estimator Are You?** 

_The process is called estimation, not exactimation._ 

_—Phillip Armour_ 

Now that you know what a good estimate is, how good an estimator are you? The following section will help you find out. 

## **2.1 A Simple Estimation Quiz** 

Table 2-1, appearing on the following page, contains a quiz designed to test your estimation skills. Please read and observe the following directions carefully: 

For each question, fill in the upper and lower bounds that, in your opinion, give you a 90% chance of including the correct value. Be careful not to make your ranges either too wide or too narrow. Make them wide enough so that, in your best judgment, the ranges give you a 90% chance of including the correct answer. Please do not research any of the answers—this quiz is intended to assess your estimation skills, not your research skills. You must fill in an answer for each item; an omitted item will be scored as an incorrect item. Please limit your time on this exercise to 10 minutes. 

(Also, you might want to photocopy the quiz before taking it so that the next person who reads this book can take it, too.) 

The correct answers to this exercise (the latitude of Shanghai, for example) are listed in Appendix B in the back of the book. Give yourself one point for each of your ranges that includes the related correct answer. 

**15** 

**16 Part I Critical Estimation Concepts** 

**Table 2-1 How Good an Estimator Are You?** 

|**[Low Estimate – High Estimate]**|**Description**|
|---|---|
|[ _______________ – _______________ ]|Surface temperature of the Sun|
|[ _______________ – _______________ ]|Latitude of Shanghai|
|[ _______________ – _______________ ]|Area of the Asian continent|
|[ _______________ – _______________ ]|The year of Alexander the Great’s birth|
|[ _______________ – _______________ ]|Total value of U.S. currency in circulation in 2004|
|[ _______________ – _______________ ]|Total volume of the Great Lakes|
|[ _______________ – _______________ ]|Worldwide box office receipts for the movie_Titanic_|
|[ _______________ – _______________ ]|Total length of the coastline of the Pacific Ocean|
|[ _______________ – _______________ ]|Number of book titles published in the U.S. since 1776|
|[ _______________ – _______________ ]|Heaviest blue whale ever recorded|



Source: Inspired by a similar quiz in _Programming Pearls_ , Second Edition (Bentley 2000). 

This quiz is from _Software Estimation_ by Steve McConnell (Microsoft Press, 2006) and is © 2006 Steve McConnell. All Rights Reserved. Permission to copy this quiz is granted provided that this copyright notice is included. 

How did you do? (Don’t feel bad. Most people do poorly on this quiz!) Please write your score here: _____________ 

## **2.2 Discussion of Quiz Results** 

The purpose of this quiz is not to determine whether you know when Alexander the Great was born or the latitude of Shanghai. Its purpose is to determine how well you understand your own estimation capabilities. 

## **How Confident Is “90% Confident”?** 

The directions above are specific that the goal of the exercise is to estimate at the 90% confidence level. Because there are 10 questions in the quiz, if you were truly estimating at the 90% confidence level, you should have gotten about 9 answers correct.[1] 

If you were cautious, you made your ranges conservatively wide, in which case you scored 10 out of 10 correctly. If you were just a little hasty, you made your ranges narrower than they needed to be, in which case you scored 7 or 8 out of 10 correctly. I’ve given this quiz to hundreds of estimators. Figure 2-1 shows the results from the most recent 600 people who have taken the quiz. 

> 1 The mathematics behind “90% confident” are a little complicated. If you were really estimating with 90% confidence, you would have a 34.9% chance of getting 10 answers correct, 38.7% chance of getting 9 answers correct, and a 19.4% chance of getting 8 answers correct. In other words, you’d have a 93% chance of getting 8 or more answers correct. 

**Chapter 2 How Good an Estimator Are You? 17** 

**==> picture [252 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
25%<br>20%<br>15%<br>Test<br>Takers<br>10%<br>5%<br>0%<br>1 2 3 4 5 6 7 9 10<br>Correct Answers<br>0 8<br>**----- End of picture text -----**<br>


**Figure 2-1** Results from administering the “How Good an Estimator Are You?” quiz. Most quiz-takers get 1–3 answers correct. 

For the test takers whose results are shown in the figure, the average number of correct answers is 2.8. Only 2 percent of quiz takers score 8 or more answers correctly. No one has ever gotten 10 correct. I’ve concluded that most people’s intuitive sense of “90% confident” is really comparable to something closer to “30% confident.” Other studies have confirmed this basic finding (Zultner 1999, Jørgensen 2002). 

Similarly, I’ve seen numerous project teams present “90% confident” schedules, and I’ve frequently seen those project teams overrun their “90% confident” schedules— more often than not. If those schedules represented a true 90% confidence, the project teams would overrun them only about 1 time out of 10. 

I’ve concluded that specific percentages such as “90%” are not meaningful unless they are supported through some kind of statistical analysis. Otherwise those specific percentages are just wishful thinking. How to get to a _real_ 90% confidence level will be discussed later in the book. 

## **Tip #5** 

Don’t provide “percentage confident” estimates (especially “90% confident”) unless you have a quantitatively derived basis for doing so. 

If you didn’t take the quiz earlier in this chapter, this would be a good time to go back and take it. I think you’ll be surprised at how few answers you get correct even after reading this explanation. 

**18 Part I Critical Estimation Concepts** 

## **How Wide Should You Make Your Ranges?** 

When I find the rare person who gets 7 or 8 answers correct, I ask “How did you get that many correct?” The typical response? “I made my ranges too wide.” 

My response is, “No, you didn’t! You didn’t make your ranges wide enough!” If you got only 7 or 8 correct, your ranges were still too narrow to include the correct answer as often as you should have. 

We are conditioned to believe that estimates expressed as narrow ranges are more accurate than estimates expressed as wider ranges. We believe that wide ranges make us appear ignorant or incompetent. The opposite is usually the case. (Of course, narrow ranges are desirable in the cases when the underlying data supports them.) 

**Tip #6** Avoid using artificially narrow ranges. Be sure the ranges you use in your estimates don’t misrepresent your confidence in your estimates. 

## **Where Does Pressure to Use Narrow Ranges Come From?** 

When you were taking the quiz, did you feel pressure to make your ranges wider? Or did you feel pressure to make your ranges narrower? Most people report that they feel pressure to make the ranges as narrow as possible. But if you go back and review the instructions, you’ll find that they do not encourage you to use narrow ranges. Indeed, I was careful to state that you should make your ranges neither too wide nor too narrow—just wide enough to give you a 90% confidence in including the correct answer. 

After discussing this issue with hundreds of developers and managers, I’ve concluded that much of the pressure to provide narrow ranges is self-induced. Some of the pressure comes from people’s sense of professional pride. They believe that narrow ranges are a sign of a better estimate, even though that isn’t the case. And some of the pressure comes from experiences with bosses or customers who insisted on the use of overly narrow ranges. 

This same self-induced pressure has been found in interactions between customers and estimators. Jørgensen and Sjøberg reported that information about customers’ expectations exerts strong influence on estimates and that estimators are typically not conscious of the degree to which their estimates are affected (Jørgensen and Sjøberg 2002). 

**Tip #7** If you are feeling pressure to make your ranges narrower, verify that the pressure actually is coming from an external source and not from yourself. 

**19** 

**Chapter 2 How Good an Estimator Are You?** 

For those cases in which the pressure truly is coming from an external source, Chapter 22, “Estimate Presentation Styles,” and Chapter 23, “Politics, Negotiation, and Problem Solving,” discuss how to deal with that pressure. 

## **How Representative Is This Quiz of Real Software Estimates?** 

In software, you aren’t often asked to estimate the volume of the Great Lakes or the surface temperature of the Sun. Is it reasonable to expect you to be able to estimate the amount of U.S. currency in circulation or the number of books published in the U.S., especially if you’re not in the U.S.? 

Software developers are often asked to estimate projects in unfamiliar business areas, projects that will be implemented in new technologies, the impacts of new programming tools on productivity, the productivity of unidentified personnel, and so on. Estimating in the face of uncertainty is business as usual for software estimators. The rest of this book explains how to succeed in such circumstances. 

## Chapter 3 **Value of Accurate Estimates** 

_[The common definition of estimate is] “the most optimistic prediction that has a non-zero probability of coming true.” … Accepting this definition leads irrevocably toward a method called what’s-the-earliest-date-by-which-youcan’t-prove-you-won’t-be-finished estimating._ 

_—Tom DeMarco_ 

The inaccuracy of software project estimates—as muddied by unrealistic targets and unachievable commitments—has been a problem for many years. In the 1970s, Fred Brooks pointed out that “more software projects have gone awry for lack of calendar time than all other causes combined” (Brooks 1975). A decade later, Scott Costello observed that “deadline pressure is the single greatest enemy of software engineering” (Costello 1984). In the 1990s, Capers Jones reported that “excessive or irrational schedules are probably the single most destructive influence in all of software” (Jones 1994, 1997). 

Tom DeMarco wrote his common definition of an estimate in 1982. Despite the successes I mentioned in the first chapter, not much has changed in the years since he wrote that definition. You might already agree that accurate estimates are valuable. This chapter details the specific benefits of accurate estimates and provides supporting data for them. 

## **3.1 Is It Better to Overestimate or Underestimate?** 

Intuitively, a perfectly accurate estimate forms the ideal planning foundation for a project. If the estimates are accurate, work among different developers can be coordinated efficiently. Deliveries from one development group to another can be planned to the day, hour, or minute. We know that accurate estimates are rare, so if we’re going to err, is it better to err on the side of overestimation or underestimation? 

## **Arguments Against Overestimation** 

Managers and other project stakeholders sometimes fear that, if a project is overestimated, Parkinson’s Law will kick in—the idea that work will expand to fill available time. If you give a developer 5 days to deliver a task that could be completed in 4 days, the developer will find something to do with the extra day. If you give a project team 6 months to complete a project that could be completed in 4 months, the project team will find a way to use up the extra 2 months. As a result, some managers consciously squeeze the estimates to try to avoid Parkinson’s Law. 

**21** 

**22 Part I Critical Estimation Concepts** 

Another concern is Goldratt’s “Student Syndrome” (Goldratt 1997). If developers are given too much time, they’ll procrastinate until late in the project, at which point they’ll rush to complete their work, and they probably won’t finish the project on time. 

A related motivation for underestimation is the desire to instill a sense of urgency in the development team. The line of reason goes like this: 

_The developers say that this project will take 6 months. I think there’s some padding in their estimates and some fat that can be squeezed out of them. In addition, I’d like to have some schedule urgency on this project to force prioritizations among features. So I’m going to insist on a 3-month schedule. I don’t really believe the project can be completed in 3 months, but that’s what I’m going to present to the developers. If I’m right, the developers might deliver in 4 or 5 months. Worst case, the developers will deliver in the 6 months they originally estimated._ 

Are these arguments compelling? To determine that, we need to examine the arguments in favor of erring on the side of overestimation. 

## **Arguments Against Underestimation** 

Underestimation creates numerous problems—some obvious, some not so obvious. 

_**Reduced effectiveness of project plans**_ Low estimates undermine effective planning by feeding bad assumptions into plans for specific activities. They can cause planning errors in the team size, such as planning to use a team that’s smaller than it should be. They can undermine the ability to coordinate among groups—if the groups aren’t ready when they said they would be, other groups won’t be able to integrate with their work. If the estimation errors caused the plans to be off by only 5% or 10%, those errors wouldn’t cause any significant problems. But numerous studies have found that software estimates are often inaccurate by 100% or more (Lawlis, Flowe, and Thordahl 1995; Jones 1998; Standish Group 2004; ISBSG 2005). When the planning assumptions are wrong by this magnitude, the average project’s plans are based on assumptions that are so far off that the plans are virtually useless. 

_**Statistically reduced chance of on-time completion**_ Developers typically estimate 20% to 30% lower than their actual effort (van Genuchten 1991). Merely using their normal estimates makes the project plans optimistic. Reducing their estimates even further simply reduces the chances of on-time completion even more. 

_**Poor technical foundation leads to worse-than-nominal results**_ A low estimate can cause you to spend too little time on upstream activities such as requirements and design. If you don’t put enough focus on requirements and design, you’ll get to redo 

**Chapter 3 Value of Accurate Estimates 23** 

your requirements and redo your design later in the project—at greater cost than if you’d done those activities well in the first place (Boehm and Turner 2004, McConnell 2004a). This ultimately makes your project take longer than it would have taken with an accurate estimate. 

_**Destructive late-project dynamics make the project worse than nominal**_ Once a project gets into “late” status, project teams engage in numerous activities that they don’t need to engage in during an “on-time” project. Here are some examples: 

- More status meetings with upper management to discuss how to get the project back on track. 

- Frequent reestimation, late in the project, to determine just when the project will be completed. 

- Apologizing to key customers for missing delivery dates (including attending meetings with those customers). 

- Preparing interim releases to support customer demos, trade shows, and so on. If the software were ready on time, the software itself could be used, and no interim release would be necessary. 

- More discussions about which requirements absolutely must be added because the project has been underway so long. 

- Fixing problems arising from quick and dirty workarounds that were implemented earlier in response to the schedule pressure. 

The important characteristic of each of these activities is that they don’t need to occur _at all_ when a project is meeting its goals. These extra activities drain time away from productive work on the project and make it take longer than it would if it were estimated and planned accurately. 

## **Weighing the Arguments** 

Goldratt’s Student Syndrome can be a factor on software projects, but I’ve found that the most effective way to address Student Syndrome is through active task tracking and buffer management (that is, project control), similar to what Goldratt suggests, not through biasing the estimates. 

As Figure 3-1 shows, the best project results come from the most accurate estimates (Symons 1991). If the estimate is too low, planning inefficiencies will drive up the actual cost and schedule of the project. If the estimate is too high, Parkinson’s Law kicks in. 

**24** 

**Part I Critical Estimation Concepts** 

**==> picture [272 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
Nonlinear penalty<br>due to planning errors,<br>upstream defects,<br>high-risk practices Effort<br>Cost Linear penalty due<br>Schedule to Parkinson’s Law<br>Underestimation Overerestimation<br><100% 100% >100%<br>Target as a Percentage of Nominal Estimate<br>**----- End of picture text -----**<br>


**Figure 3-1** The penalties for underestimation are more severe than the penalties for overestimation, so, if you can’t estimate with complete accuracy, try to err on the side of overestimation rather than underestimation. 

I believe that Parkinson’s Law does apply to software projects. Work does expand to fill available time. But deliberately underestimating a project because of Parkinson’s Law makes sense only if the penalty for overestimation is worse than the penalty for underestimation. In software, the penalty for overestimation is _linear and bounded_ — work will expand to fill available time, but it will not expand any further. But the penalty for underestimation is _nonlinear and unbounded_ —planning errors, shortchanging upstream activities, and the creation of more defects cause more damage than overestimation does, and with little ability to predict the extent of the damage ahead of time. 

## **Tip #8** 

Don’t intentionally underestimate. The penalty for underestimation is more severe than the penalty for overestimation. Address concerns about overestimation through planning and control, not by biasing your estimates. 

## **3.2 Details on the Software Industry’s Estimation Track Record** 

The software industry’s estimation track record provides some interesting clues to the nature of software’s estimation problems. In recent years, The Standish Group has published a biennial survey called “The Chaos Report,” which describes software project outcomes. In the 2004 report, 54% of projects were delivered late, 18% failed outright, and 28% were delivered on time and within budget. Figure 3-2 shows the results for the 10 years from 1994 to 2004. 

What’s notable about The Standish Group’s data is that it doesn’t even have a category for early delivery! The best possible performance is meeting expectations “On Time/On Budget”—and the other options are all downhill from there. 

**25** 

**Chapter 3 Value of Accurate Estimates** 

**==> picture [309 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
100%<br>90%<br>80%<br>70%<br>60%<br>Percentage 50%<br>40%<br>30%<br>20%<br>10%<br>0%<br>1994 1996 1998 2000 2002 2004<br>Late / Over  On Time /<br>Failed<br>Budget On Budget<br>**----- End of picture text -----**<br>


**Figure 3-2** Project outcomes reported in The Standish Group’s Chaos report have fluctuated year to year. About three quarters of all software projects are delivered late or fail outright. 

Capers Jones presents another view of project outcomes. Jones has observed for many years that project success depends on project size. That is, larger projects struggle more than smaller projects do. Table 3-1 illustrates this point. 

**Table 3-1 Project Outcomes by Project Size** 

|**Table 3-1**<br>**Project Outcomes b**|**y Project Si**|**ze**|||
|---|---|---|---|---|
|**Size in Function Points (and**||||**Failed**|
|**Approximate Lines of Code)**|**Early**|**On Time**|**Late**|**(Canceled)**|
|10 FP (1,000 LOC)|11%|81%|6%|2%|
|100 FP (10,000 LOC)|6%|75%|12%|7%|
|1,000 FP (100,000 LOC)|1%|61%|18%|20%|
|10,000 FP (1,000,000 LOC)|<1%|28%|24%|48%|
|100,000 FP (10,000,000 LOC)|0%|14%|21%|65%|



Source: _Estimating Software Costs_ (Jones 1998). 

As you can see from Jones’s data, the larger a project, the less chance the project has of completing on time and the greater chance it has of failing outright. 

Overall, a compelling number of studies have found results in line with the results reported by The Standish Group and Jones, that about one quarter of all projects are delivered on time; about one quarter are canceled; and about half are delivered late, over budget, or both (Lederer and Prasad 1992; Jones 1998; ISBSG 2001; Krasner 2003; Putnam and Myers 2003; Heemstra, Siskens and van der Stelt 2003; Standish Group 2004). 

**26** 

**Part I Critical Estimation Concepts** 

The reasons that projects miss their targets are manifold. Poor estimates are one reason but not the only reason. We’ll discuss the reasons in depth in Chapter 4, “Where Does Estimation Error Come From?” 

## **How Late Are the Late Projects?** 

The number of projects that run late or over budget is one consideration. The degree to which these projects miss their targets is another consideration. According to the first Standish Group survey, the average project schedule overrun was about 120% and the average cost overrun was about 100% (Standish Group 1994). But the estimation accuracy is probably worse than those numbers reflect. The Standish Group found that late projects routinely threw out significant amounts of functionality to achieve the schedules and budgets they eventually did meet. Of course, these projects’ estimates weren’t for the abbreviated versions they eventually delivered; they were for the originally specified, full-featured versions. If these late projects had delivered all of their originally specified functionality, they would have overrun their plans even more. 

## **One Company’s Experience** 

A more company-specific view of project outcomes is shown in the data reported by one of my clients in Figure 3-3. 

**==> picture [255 x 259] intentionally omitted <==**

**----- Start of picture text -----**<br>
280<br>260<br>240<br>220<br>200<br>180<br>160<br>Actual<br>Completion 140<br>Date (days) 120<br>100 Average<br>Target: 22 days<br>80 Actual: 56 days<br>60<br>40 Perfect accuracy<br>(Actual Completion = Target Completion)<br>20<br>0<br>0 20 40 60 80 100 120 140 160 180 200 220<br>Target Completion Date (days)<br>**----- End of picture text -----**<br>


**Figure 3-3** Estimation results from one organization. General industry data suggests that this company’s estimates being about 100% low is typical. Data used by permission. 

**Chapter 3 Value of Accurate Estimates 27** 

The points that are clustered on the “0” line on the left side of the graph represent projects for which the developers reported that they were done but which were found not to be complete when the software teams began integrating their work with other groups. 

The diagonal line represents perfect scheduling accuracy. Ideally, the graph would show data points clustering tightly around the diagonal line. Instead, nearly all of the 80 data points shown are above the line and represent project overruns. One point is below the line, and a handful of points are on the line. The line illustrates DeMarco’s common definition of an “estimate”—the earliest date by which you could possibly be finished. 

## **The Software Industry’s Systemic Problem** 

We often speak of the software industry’s estimation problem as though it were a neutral estimation problem—that is, sometimes we overestimate, sometimes we underestimate, and we just can’t get our estimates right. 

_But the software does not have a neutral estimation problem._ The industry data shows clearly that _the software industry has an underestimation problem._ Before we can make our estimates more accurate, we need to start making the estimates _bigger_ . That is the key challenge for many organizations. 

## **3.3 Benefits of Accurate Estimates** 

Once your estimates become accurate enough that you get past worrying about large estimation errors on either the high or low side, truly accurate estimates produce additional benefits. 

_**Improved status visibility**_ One of the best ways to track progress is to compare planned progress with actual progress. If the planned progress is realistic (that is, based on accurate estimates), it’s possible to track progress according to plan. If the planned progress is fantasy, a project typically begins to run without paying much attention to its plan and it soon becomes meaningless to compare actual progress with planned progress. Good estimates thus provide important support for project tracking. 

_**Higher quality**_ Accurate estimates help avoid schedule-stress-related quality problems. About 40% of all software errors have been found to be caused by stress; those errors could have been avoided by scheduling appropriately and by placing less stress on the developers (Glass 1994). When schedule pressure is extreme, about four times as many defects are reported in the released software as are reported for software developed under less extreme pressure (Jones 1994). One reason is that 

**28** 

**Part I Critical Estimation Concepts** 

teams implement quick-and-dirty versions of features that absolutely must be completed in time to release the software. Excessive schedule pressure has also been found to be the most significant cause of extremely costly error-prone modules (Jones 1997). 

Projects that aim from the beginning to have the lowest number of defects usually also have the shortest schedules (Jones 2000). Projects that apply pressure to create unrealistic estimates and subsequently shortchange quality are rudely awakened when they discover that they have also shortchanged cost and schedule. 

_**Better coordination with nonsoftware functions**_ Software projects usually need to coordinate with other business functions, including testing, document writing, marketing campaigns, sales staff training, financial projections, software support training, and so on. If the software schedule is not reliable, that can cause related functions to slip, which can cause the _entire project schedule_ to slip. Better software estimates allow for tighter coordination of the whole project, including both software and nonsoftware activities. 

_**Better budgeting**_ Although it is almost too obvious to state, accurate estimates support accurate budgets. An organization that doesn’t support accurate estimates undermines its ability to forecast the costs of its projects. 

_**Increased credibility for the development team**_ One of the great ironies in software development is that after a project team creates an estimate, managers, marketers, and sales staff take the estimate and turn it into an optimistic business target—over the objections of the project team. The developers then overrun the optimistic business target, at which point, managers, marketers, and sales staff blame the developers for being poor estimators! A project team that holds its ground and insists on an accurate estimate will improve its credibility within its organization. 

_**Early risk information**_ One of the most common wasted opportunities in software development is the failure to correctly interpret the meaning of an initial mismatch between project goals and project estimates. Consider what happens when the business sponsor says, “This project needs to be done in 4 months because we have a major trade show coming up,” and the project team says, “Our best estimate is that this project will take 6 months.” The most typical interaction is for the business sponsor and the project leadership to negotiate the _estimate_ , and for the project team eventually to be pressured into committing to try to achieve the 4-month schedule. 

Bzzzzzt! Wrong answer! The detection of a mismatch between the project goal and the project estimate should be interpreted as incredibly useful, incredibly rare, earlyin-the-project risk information. The mismatch indicates a substantial chance that the project will fail to meet its business objective. Detected early, numerous corrective actions are available, and many of them are high leverage. You might redefine the scope of the project, you might increase staff, you might transfer your best staff onto 

**29** 

**Chapter 3 Value of Accurate Estimates** 

the project, or you might stagger the delivery of different functionality. You might even decide the project is not worth doing after all. 

But if this mismatch is allowed to persist, the options that will be available for corrective action will be far fewer and will be much lower leverage. The options will generally consist of “overrun the schedule and budget” or “cut painful amounts of functionality.” 

**Tip #9** Recognize a mismatch between a project’s business target and a project’s estimate for what it is: valuable risk information that the project might not be successful. Take corrective action early, when it can do some good. 

## **3.4 Value of Predictability Compared with Other Desirable Project Attributes** 

Software organizations and individual software projects try to achieve numerous objectives for their projects. Here are some of the goals they strive for: 

- **Schedule** Shortest possible schedule for the desired functionality at the desired quality level 

- **Cost** Minimum cost to deliver the desired functionality in the desired time 

- **Functionality** Maximum feature richness for the time and money available 

Projects will prioritize these generic goals as well as more specific goals differently. Agile development tends to focus on the goals of flexibility, repeatability, robustness, sustainability, and visibility (Cockburn 2001, McConnell 2002). The SEI’s CMM tends to focus on the goals of efficiency, improvability, predictability, repeatability, and visibility. 

In my discussions with executives, I’ve frequently asked, “What is more important to you: the ability to change your mind about features, or the ability to know cost, schedule, and functionality in advance?” At least 8 times out of 10, executives respond “The ability to know cost, schedule, and functionality in advance”—in other words, _predictability_ . Other software experts have made the same observation (Moseman 2002, Putnam and Myers 2003). 

I often follow up by saying, “Suppose I could offer you project results similar to either Option #1 or Option #2 in Figure 3-4. Let’s suppose Option #1 means that I can deliver a project with an expected duration of 4 months, but it might be 1 month early and it might be as many as 4 months late. Let’s suppose Option #2 means that I can deliver a project with an expected duration of 5 months (rather than 4), and I can guarantee that it will be completed within a week of that date. Which would you prefer?” 

**30 Part I Critical Estimation Concepts** 

**==> picture [142 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
8<br>7<br>6<br>Range of 5<br>Project<br>4<br>Outcomes<br>(months)<br>3<br>2<br>1<br>0<br>Option  Option<br>1 2<br>**----- End of picture text -----**<br>


**Figure 3-4** When given the option of a shorter average schedule with higher variability or a longer average schedule with lower variability, most businesses will choose the second option. 

In my experience, nearly all executives will choose Option #2. The shorter schedule offered by Option #1 won’t do the business any good because the business can’t depend on it. Because the overrun could easily be as large as 4 months, the business has to plan on an 8-month schedule rather than a 4-month schedule. Or it delays making any plans at all until the software is actually ready. In comparison, the guaranteed 5-month schedule of Option #2 looks much better. 

Over the years, the software industry has focused on time to market, cost, and flexibility. Each of these goals is desirable, but what top executives usually value most is predictability. Businesses need to make commitments to customers, investors, suppliers, the marketplace, and other stakeholders. These commitments are all supported by predictability. 

None of this proves that predictability is the top priority for your business, but it suggests that you shouldn’t make assumptions about your business’s priorities. 

**Tip #10** Many businesses value predictability more than development time, cost, or flexibility. Be sure you understand what your business values the most. 

## **3.5 Problems with Common Estimation Techniques** 

Considering the widespread poor results from software estimation, it shouldn’t be a surprise that the techniques used to produce the estimates are not effective. These techniques should be carefully examined and thrown out! 

**31** 

**Chapter 3 Value of Accurate Estimates** 

Albert Lederer and Jayesh Prasad found that the most commonly used estimation technique was comparing a new project with a similar past project, based solely on personal memory. This technique was not found to be correlated with accurate estimates. The common techniques of “intuition” and “guessing” were found to be correlated with cost and schedule overruns (Lederer and Prasad 1992). Numerous other researchers have found that guessing, intuition, unstructured expert judgment, use of informal analogies, and similar techniques are the dominant strategies used for about 60 to 85% of all estimates (Hihn and Habib-Agahi 1991, Heemstra and Kusters 1991, Paynter 1996, Jørgensen 2002, Kitchenham et al. 2002). 

Chapter 5, “Estimate Influences,” presents a more detailed examination of sources of estimation error, and the rest of this book provides alternatives to these common techniques. 

## **Additional Resources** 

Goldratt, Eliyahu M. _Critical Chain_ . Great Barrington, MA: The North River Press, 1997. Goldratt describes an approach to dealing with Student Syndrome as well as an approach to buffer management that addresses Parkinson’s Law. 

Putnam, Lawrence H. and Ware Myers. _Five Core Metrics_ . New York, NY: Dorset House, 2003. Chapter 4 contains an extended discussion of the importance of predictability compared to other project objectives. 

## Chapter 4 **Where Does Estimation Error Come From?** 

_There’s no point in being exact about something if you don’t even know what you’re talking about._ 

_—John von Neumann_ 

A University of Washington Computer Science Department project was in serious estimation trouble. The project was months late and $20.5 million over budget. The causes ranged from design problems and miscommunications to last-minute changes and numerous errors. The university argued that the plans for the project weren’t adequate. But this wasn’t an ordinary software project. In fact, it wasn’t a software project at all; it was the creation of the university’s new Computer Science and Engineering Building (Sanchez 1998). 

Software estimation presents challenges because estimation itself presents challenges. The Seattle Mariners’ new baseball stadium was estimated in 1995 to cost $250 million. It was finally completed in 1999 at a cost of $517 million—an estimation error of more than 100% (Withers 1999). The most massive cost overrun in recent times was probably Boston’s Big Dig highway construction project. Originally estimated to cost $2.6 billion, costs eventually totaled about $15 billion—an estimation error of more than 400% (Associated Press 2003). 

Of course, the software world has its own dramatic estimation problems. The Irish Personnel, Payroll and Related Systems (PPARS) system was cancelled after it overran its ¤8.8 million system by ¤140 million (The Irish Times 2005). The FBI’s Virtual Case File (VCF) project was shelved in March 2005 after costing $170 million and delivering only one-tenth of its planned capability (Arnone 2005). The software contractor for VCF complained that the FBI went through 5 different CIOs and 10 different project managers, not to mention 36 contract changes (Knorr 2005). Background chaos like that is not unusual in projects that have experienced estimation problems. 

A chapter on sources of estimation error might just as well be titled “Classic Mistakes in Software Estimation.” Merely avoiding the problems identified in this chapter will get you halfway to creating accurate estimates. 

Estimation error creeps into estimates from four generic sources: 

■ Inaccurate information about the project being estimated 

**33** 

**34** 

**Part I Critical Estimation Concepts** 

- Inaccurate information about the capabilities of the organization that will perform the project 

- Too much chaos in the project to support accurate estimation (that is, trying to estimate a moving target) 

- Inaccuracies arising from the estimation process itself 

This chapter describes each source of estimation error in detail. 

## **4.1 Sources of Estimation Uncertainty** 

How much does a new house cost? It depends on the house. How much does a Web site cost? It depends on the Web site. Until each specific feature is understood in detail, it’s impossible to estimate the cost of a software project accurately. It isn’t possible to estimate the amount of work required to build something when that “something” has not been defined. 

Software development is a process of gradual refinement. You start with a general product concept (the vision of the software you intend to build), and you refine that concept based on the product and project goals. Sometimes your goal is to estimate the budget and schedule needed to deliver a specific amount of functionality. Other times your goal is to estimate how much functionality can be built in a predetermined amount of time under a fixed budget. Many projects navigate under a happy medium of some flexibility in budget, schedule, and features. In any of these cases the different ways the software could ultimately take shape will produce widely different combinations of cost, schedule, and feature set. 

Suppose you’re developing an order-entry system and you haven’t yet pinned down the requirements for entering telephone numbers. Some of the uncertainties that could affect a software estimate from the requirements activity through release include the following: 

- When telephone numbers are entered, will the customer want a Telephone Number Checker to check whether the numbers are valid? 

- If the customer wants the Telephone Number Checker, will the customer want the cheap or expensive version of the Telephone Number Checker? (There are typically 2-hour, 2-day, and 2-week versions of any particular feature—for example, U.S.-only versus international phone numbers.) 

- If you implement the cheap version of the Telephone Number Checker, will the customer later want the expensive version after all? 

- Can you use an off-the-shelf Telephone Number Checker, or are there design constraints that require you to develop your own? 

**35** 

**Chapter 4 Where Does Estimation Error Come From?** 

- How will the Telephone Number Checker be designed? (Typically there is at least a factor of 10 difference in design complexity among different designs for the same feature.) 

- How long will it take to code the Telephone Number Checker? (There can be a factor of 10 difference—or more—in the time that different developers need to code the same feature.) 

- Do the Telephone Number Checker and the Address Checker interact? How long will it take to integrate the Telephone Number Checker and the Address Checker? 

- What will the quality level of the Telephone Number Checker be? (Depending on the care taken during implementation, there can be a factor of 10 difference in the number of defects contained in the original implementation.) 

- How long will it take to debug and correct mistakes made in the implementation of the Telephone Number Checker? (Individual performance among different programmers with the same level of experience varies by at least a factor of 10 in debugging and correcting the same problems.) 

As you can see just from this short list of uncertainties, potential differences in how a single feature is specified, designed, and implemented can introduce cumulative differences of a hundredfold or more in implementation time for any given feature. When you combine these uncertainties across hundreds or thousands of features in a large feature set, you end up with significant uncertainty in the project itself. 

## **4.2 The Cone of Uncertainty** 

Software development consists of making literally thousands of decisions about all the feature-related issues described in the previous section. Uncertainty in a software estimate results from uncertainty in how the decisions will be resolved. As you make a greater percentage of those decisions, you reduce the estimation uncertainty. 

As a result of this process of resolving decisions, researchers have found that project estimates are subject to predictable amounts of uncertainty at various stages. The Cone of Uncertainty in Figure 4-1 shows how estimates become more accurate as a project progresses. (The following discussion initially describes a sequential development approach for ease of explanation. The end of this section will explain how to apply the concepts to iterative projects.) 

The horizontal axis contains common project milestones, such as Initial Concept, Approved Product Definition, Requirements Complete, and so on. Because of its origins, this terminology sounds somewhat product-oriented. “Product Definition” just refers to the agreed-upon vision for the software, or the _software concept_ , and applies equally to Web services, internal business systems, and most other kinds of software projects. 

**36 Part I Critical Estimation Concepts** 

**==> picture [359 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x<br>2x<br>1.5x<br>Variability in the 1.25x<br>Estimate of 1.0x<br>Project Scope 0.8x<br>(effort, cost, features)<br>0.67x<br>0.5x<br>0.25x<br>Initial Approved Requirements User Detailed Software<br>Concept Product Complete Interface Design Complete<br>Definition Design Complete<br>Complete<br>**----- End of picture text -----**<br>


**Figure 4-1** The Cone of Uncertainty based on common project milestones. 

The vertical axis contains the degree of error that has been found in estimates created by skilled estimators at various points in the project. The estimates could be for how much a particular feature set will cost and how much effort will be required to deliver that feature set, or it could be for how many features can be delivered for a particular amount of effort or schedule. This book uses the generic term _scope_ to refer to project size in effort, cost, features, or some combination thereof. 

As you can see from the graph, estimates created very early in the project are subject to a high degree of error. Estimates created at Initial Concept time can be inaccurate by a factor of 4 _x_ on the high side or 4 _x_ on the low side (also expressed as 0.25 _x_ , which is just 1 divided by 4). The total range from high estimate to low estimate is 4 _x_ divided by 0.25 _x_ , or 16 _x_ ! 

One question that managers and customers ask is, “If I give you another week to work on your estimate, can you refine it so that it contains less uncertainty?” That’s a reasonable request, but unfortunately it’s not possible to deliver on that request. Research by Luiz Laranjeira suggests that the accuracy of the software estimate depends on the level of refinement of the software’s definition (Laranjeira 1990). The more refined the definition, the more accurate the estimate. The reason the estimate contains variability is that the software project itself contains variability. The only way to reduce the variability in the estimate is to reduce the variability in the project. 

**37** 

**Chapter 4 Where Does Estimation Error Come From?** 

One misleading implication of this common depiction of the Cone of Uncertainty is that it looks like the Cone takes forever to narrow—as if you can’t have very good estimation accuracy until you’re nearly done with the project. Fortunately, that impression is created because the milestones on the horizontal axis are equally spaced, and we naturally assume that the horizontal axis is calendar time. 

In reality, the milestones listed tend to be front-loaded in the project’s schedule. When the Cone is redrawn on a calendar-time basis, it looks like Figure 4-2. 

**==> picture [345 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x<br>2x<br>1.5x<br>Variability in the 1.25x<br>Estimate of 1.0x Requirements<br>Project Scope 0.8x Complete Software<br>(effort, cost, features) 0.67x User DetailedDesign Complete<br>Interface Complete<br>0.5x Design<br>Approved Complete<br>Product<br>0.25x Definition<br>Initial<br>Concept Time<br>**----- End of picture text -----**<br>


**Figure 4-2** The Cone of Uncertainty based on calendar time. The Cone narrows much more quickly than would appear from the previous depiction in Figure 4-1. 

As you can see from this version of the Cone, estimation accuracy improves rapidly for the first 30% of the project, improving from ±4 _x_ to ±1.25 _x_ . 

## **Can You Beat the Cone?** 

An important—and difficult—concept is that the Cone of Uncertainty represents the _best-case accuracy_ that is possible to have in software estimates at different points in a project. The Cone represents the error in estimates created by skilled estimators. It’s easily possible to do worse. It isn’t possible to be more accurate; it’s only possible to be more lucky. 

**Tip #11** Consider the effect of the Cone of Uncertainty on the accuracy of your estimate. Your estimate cannot have more accuracy than is possible at your project’s current position within the Cone. 

**38 Part I Critical Estimation Concepts** 

## **The Cone Doesn’t Narrow Itself** 

Another way in which the Cone of Uncertainty represents a best-case estimate is that if the project is not well controlled, or if the estimators aren’t very skilled, estimates can fail to improve. Figure 4-3 shows what happens when the project doesn't focus on reducing variability—the uncertainty isn’t a Cone, but rather a Cloud that persists to the end of the project. The issue isn’t really that the estimates don’t converge; the issue is that the project itself doesn’t converge—that is, it doesn’t drive out enough variability to support more accurate estimates. 

**==> picture [342 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x<br>2x<br>1.5x<br>Variability in the 1.25x<br>Estimate of 1.0x<br>Project Scope 0.8x<br>(effort, cost, features)<br>0.67x<br>0.5x<br>0.25x<br>Time<br>**----- End of picture text -----**<br>


**Figure 4-3** If a project is not well controlled or well estimated, you can end up with a Cloud of Uncertainty that contains even more estimation error than that represented by the Cone. 

The Cone narrows only as you make decisions that eliminate variability. As Figure 4-4 illustrates, defining the product vision (including committing to what you will _not_ do) reduces variability. Defining requirements—again, including what you are _not_ going to do—eliminates variability further. Designing the user interface helps to reduce the risk of variability arising from misunderstood requirements. Of course, if the product isn’t really defined, or if the product definition gets redefined later, the Cone will widen, and estimation accuracy will be poorer. 

## **Tip #12** 

Don’t assume that the Cone of Uncertainty will narrow itself. You must force the Cone to narrow by removing sources of variability from your project. 

**Chapter 4 Where Does Estimation Error Come From? 39** 

**==> picture [341 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x<br>Product Definition<br>2x<br>Detailed Requirements<br>User Interface Design<br>1.5x<br>Variability in the 1.25x<br>Estimate of 1.0x<br>Project Scope 0.8x<br>(effort, cost, features)<br>0.67x<br>0.5x<br>0.25x<br>Time<br>**----- End of picture text -----**<br>


**Figure 4-4** The Cone of Uncertainty doesn’t narrow itself. You narrow the Cone by making decisions that remove sources of variability from the project. Some of these decisions are about what the project will deliver; some are about what the project will _not_ deliver. If these decisions change later, the Cone will widen. 

## **Accounting for the Cone of Uncertainty in Software Estimates** 

Studies of software estimates have found that estimators who start with single-point estimates and create ranges based on their original single-point numbers do not usually adjust their minimum and maximum values sufficiently to account for the uncertainty in the estimate, especially in circumstances that contain high uncertainty (Jørgensen 2002). This tendency to use ranges that are too narrow can be addressed two ways. The first is to start with a “most likely” estimate and then compute the ranges using predefined multipliers, as shown in Table 4-1. 

**Table 4-1 Estimation Error by Software-Development Activity** 

||**Table 4-1**<br>**Estimation Error by Software-Development Activity**|
|---|---|
||**Scoping Error**|
||**Phase**<br>**Possible Error**<br>**on Low Side**<br>**Possible Error**<br>**on High Side**<br>**Range of High to**<br>**Low Estimates**|
||Initial Concept<br>0.25_x_(–75%)<br>4.0_x_(+300%)<br>16_x_<br>Approved Product Definition<br>0.50_x_(–50%)<br>2.0_x_(+100%)<br>4_x_<br>Requirements Complete<br>0.67_x_(–33%)<br>1.5_x_(+50%)<br>2.25_x_<br>User Interface Design<br>Complete<br>0.80_x_(–20%)<br>1.25_x_(+25%)<br>1.6_x_<br>Detailed Design Complete<br>(for sequential projects)<br>0.90_x_(–10%)<br>1.10_x_(+10%)<br>1.2_x_|



Source: Adapted from _Software Estimation with Cocomo II_ (Boehm et al. 2000). 

**40 Part I Critical Estimation Concepts** 

If you use the entries from this table, recognize that at the point when you create the estimate you won’t know whether the actual project outcome will fall toward the high end or the low end of your range. 

**Tip #13** Account for the Cone of Uncertainty by using predefined uncertainty ranges in your estimates. 

A second approach is based on the finding that estimation “know-how-much” and estimation “know-how-uncertain” are two different skills. You can have one person estimate the best-case and worst-case ends of the range and a second person estimate the likelihood that the actual result will fall within that range (Jørgensen 2002). 

**Tip #14** Account for the Cone of Uncertainty by having one person create the “how much” part of the estimate and a different person create the “how uncertain” part of the estimate. 

## **Relationship Between the Cone of Uncertainty and Commitment** 

Software organizations routinely sabotage their own projects by making commitments too early in the Cone of Uncertainty. If you commit at Initial Concept or Product Definition time, you will have a factor of 2 _x_ to 4 _x_ error in your estimates. As discussed in Chapter 1, “What Is an ‘Estimate’?”, a skilled project manager can navigate a project to completion if the estimate is within about 20% of the project reality. But no manager can navigate a project to a successful conclusion when the estimates are off by several hundred percent. 

Meaningful commitments are not possible in the early, wide part of the Cone. Effective organizations delay their commitments until they have done the work to force the Cone to narrow. Meaningful commitments in the early-middle part of the project (about 30% of the way in) are possible and appropriate. 

## **The Cone of Uncertainty and Iterative Development** 

Applying the Cone of Uncertainty to iterative projects is somewhat more involved than applying it to sequential projects is. 

If you’re working on a project that does a full development cycle each iteration—that is, from requirements definition through release—you’ll go through a miniature Cone on each iteration. Before you do the requirements work for the iteration, you’ll be at the Approved Product Definition point in the Cone, subject to 4 _x_ variability from high to low estimates. With short iterations (less than a month), you can move from Approved Product Definition to Requirements Complete and User Interface Design 

**41** 

**Chapter 4 Where Does Estimation Error Come From?** 

Complete in a few days, reducing your variability from 4 _x_ to 1.6 _x_ . If your schedule is immovable, the 1.6 _x_ variability will apply to the specific features you can deliver in the time available, rather than to the effort or schedule. There are estimation advantages that flow from short iterations, which are discussed in Section 8.4, “Using Data from Your Current Project.” 

What you give up with approaches that leave requirements undefined until the beginning of each iteration is long-range predictability about the combination of cost, schedule, and features you’ll deliver several iterations down the road. As Chapter 3, “Value of Accurate Estimates,” discussed, your business might prioritize that flexibility highly, or it might prefer that your projects provide more predictability. 

The alternative to _total_ iteration is not _no_ iteration. That option has been found to be almost universally ineffective. The alternatives are _less_ iteration or _different_ iteration. 

Many development teams settle on a middle ground in which a majority of requirements are defined at the front end of the project, but design, construction, test, and release are performed in short iterations. In other words, the project moves sequentially through the User Interface Design Complete milestone (about 30% of the calendar time into the project) and then shifts to a more iterative approach from that point forward. This drives down the variability arising from the Cone to about ±25%, which allows for project control that is good enough to hit a target while still tapping into major benefits of iterative development. Project teams can leave some amount of planned time for as-yet-to-be-determined requirements at the end of the project. That introduces a little bit of variability related to the feature set, which in this case is positive variability because you’ll exercise it only if you identify desirable features to implement. This middle ground supports long-range predictability of cost and schedule as well as a moderate amount of requirements flexibility. 

## **4.3 Chaotic Development Processes** 

The Cone of Uncertainty represents uncertainty that is inherent even in well-run projects. Additional variability can arise from poorly run projects—that is, from avoidable project chaos. 

Common examples of project chaos include the following: 

- Requirements that weren’t investigated very well in the first place 

- Lack of end-user involvement in requirements validation 

- Poor designs that lead to numerous errors in the code 

- Poor coding practices that give rise to extensive bug fixing 

**42** 

**Part I Critical Estimation Concepts** 

- Inexperienced personnel 

- Incomplete or unskilled project planning 

- Prima donna team members 

- Abandoning planning under pressure 

- Developer gold-plating 

- Lack of automated source code control 

This is just a partial list of possible sources of chaos. For a more complete discussion, see Chapter 3, “Classic Mistakes,” of my book _Rapid Development_ (McConnell 1996) and on the Web at _www.stevemcconnell.com/rdenum.htm_ . 

These sources of chaos share two commonalities. The first is that each introduces variability that makes accurate estimation difficult. The second is that the best way to address each of these issues is not through estimation, but through better project control. 

## **Tip #15** 

Don’t expect better estimation practices alone to provide more accurate estimates for chaotic projects. You can’t accurately estimate an out-of-control process. As a first step, fixing the chaos is more important than improving the estimates. 

## **4.4 Unstable Requirements** 

Requirements changes have often been reported as a common source of estimation problems (Lederer and Prasad 1992, Jones 1994, Stutzke 2005). In addition to all the general challenges that unstable requirements create, they present two specific estimation challenges. 

The first challenge is that unstable requirements represent one specific flavor of project chaos. If requirements cannot be stabilized, the Cone of Uncertainty can’t be narrowed, and estimation variability will remain high through the end of the project. 

The second challenge is that requirements changes are often not tracked and the project is often not reestimated when it should be. In a well-run project, an initial set of requirements will be baselined, and cost and schedule will be estimated from that baselined set of requirements. As new requirements are added or old requirements are revised, cost and schedule estimates will be modified to reflect those changes. In practice, project managers often neglect to update their cost and schedule assumptions as their requirements change. The irony in these cases is that the estimate for the original functionality might have been accurate, but after dozens of new requirements have been piled onto the project—requirements that have been agreed to but not accounted for—the project won’t have any chance of meeting its original estimates, 

**43** 

**Chapter 4 Where Does Estimation Error Come From?** 

and the project will be perceived as being late, even though everyone agreed that the feature additions were good ideas. 

The estimation techniques described in this book will certainly help you estimate _better_ when you have high requirements volatility, but better estimation alone cannot address problems arising from requirements instability. The more powerful responses are project control responses rather than estimation responses. If your environment doesn’t allow you to stabilize requirements, consider alternative development approaches that are designed to work in high-volatility environments, such as short iterations, Scrum, Extreme Programming, DSDM (Dynamic Systems Development Method), time box development, and so on. 

**Tip #16** To deal with unstable requirements, consider project control strategies instead of or in addition to estimation strategies. 

## **Estimating Requirements Growth** 

If you do want to estimate the effect of unstable requirements, you might consider simply incorporating an allowance for requirements growth, requirements changes, or both into your estimates. Figure 4-5 shows a revised Cone of Uncertainty that accounts for approximately 50% growth in requirements over the course of a project. (This particular Cone is for purposes of illustration only. The specific data points are not supported by the same research as the original Cone.) 

**==> picture [344 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x<br>2x<br>1.5x<br>Variability in the 1.25x<br>Estimate of 1.0x<br>Project Scope 0.8x<br>(effort, cost, features)<br>0.67x<br>0.5x<br>0.25x<br>Time<br>**----- End of picture text -----**<br>


**Figure 4-5** A Cone of Uncertainty that allows for requirements increases over the course of the project. 

**44 Part I Critical Estimation Concepts** 

This approach has been used by leading organizations, including NASA’s Software Engineering Laboratory, which plans on a 40% increase in requirements (NASA SEL 1990). A similar concept is incorporated into the Cocomo II estimation model, which includes the notion of requirements “breakage” (Boehm et al. 2000). 

## **4.5 Omitted Activities** 

The previous sections described sources of error arising from the project itself. The remaining sections in this chapter turn to a discussion of errors that arise from the estimation practices. 

One of the most common sources of estimation error is forgetting to include necessary tasks in the project estimates (Lederer and Prasad 1992, Coombs 2003). Researchers have found that this phenomenon applies both at the project planning level and at the individual developer level. One study found that developers tended to estimate pretty accurately the work they remembered to estimate, but they tended to overlook 20% to 30% of the necessary tasks, which led to a 20 to 30% estimation error (van Genuchten 1991). 

Omitted work falls into three general categories: missing requirements, missing software-development activities, and missing non-software-development activities. 

Table 4-2 lists requirements that are commonly missing from estimates. 

**Table 4-2 Functional and Nonfunctional Requirements Commonly Missing from Software Estimates** 

|**Table 4-2**<br>**Functional and Nonfunctiona**<br>**Software Estimates**|**l Requirements Commonly Missing from**|
|---|---|
|**Functional Requirements Areas**|**Nonfunctional Requirements**|
|Setup/installation program|Accuracy|
|Data conversion utility|Interoperability|
|Glue code needed to use third-party or|Modifiability|
|open-source software|Performance|
|Help system|Portability|
|Deployment modes|Reliability|
|Interfaces with external systems|Responsiveness|
||Reusability|
||Scalability|
||Security|
||Survivability|
||Usability|



**Tip #17** Include time in your estimates for stated requirements, implied requirements, and nonfunctional requirements—that is, _all_ requirements. Nothing can be built for free, and your estimates shouldn’t imply that it can. 

**Chapter 4 Where Does Estimation Error Come From? 45** 

Table 4-3 lists software activities that estimators often overlook. 

**Table 4-3 Software-Development Activities Commonly Missing from Software Estimates** 

|**Table 4-3**<br>**Software-Development Activiti**<br>**Estimates**|**es Commonly Missing from Software**|
|---|---|
|Ramp-up time for new team members|Technical support of existing systems during|
|Mentoring of new team members|the project|
|Management coordination/manager<br>meetings|Maintenance work on previous systems<br>during the project|
|Cutover/deployment|Defect-correction work|
|Data conversion|Performance tuning|
|Installation|Learning new development tools|
|Customization|Administrative work related to defect tracking|
|Requirements clarifications|Coordination with test (for developers)|
|Maintaining the revision control system|Coordination with developers (for test)|
|Supporting the build|Answering questions from quality assurance|
|Maintaining the scripts required to run<br>the daily build|Input to user documentation and review of<br>user documentation|
|Maintaining the automated smoke test|Review of technical documentation|
|used in conjunction with the daily build|Demonstrating software to customers or users|
|Installation of test builds at user location(s)|Demonstrating software at trade shows|
|Creation of test data|Demonstrating the software or prototypes|
|Management of beta test program<br>Participation in technical reviews<br>Integration work|of the software to upper management,<br>clients, and end users<br>Interacting with clients or end users; sup-<br>porting beta installations at client locations|
|Processing change requests|Reviewing plans, estimates, architecture,|
|Attendance at change-control/triage meetings|detailed designs, stage plans, code, test|
|Coordinating with subcontractors|cases, and so on|



|**Tip #18**|Include all necessary software-development activities in your estimates, not just|
|---|---|
||coding and testing.|



Table 4-4 lists the non-software-development activities that are often missing from estimates. 

**Table 4-4 Non-Software-Development Activities Commonly Missing from Software Estimates** 

|Vacations<br>Holidays<br>Sick days<br>Training<br>Weekends<br>Company meetings<br>Department meetings<br>Setting up new workstations<br>Installing new versions of tools on workstations<br>Troubleshooting hardware and software problems||
|---|---|



**46 Part I Critical Estimation Concepts** 

Some projects deliberately plan to exclude many of the activities in Table 4-4 for a small project. That can work for a short time, but these activities tend to creep back into any project that lasts longer than a few weeks. 

## **Tip #19** 

On projects that last longer than a few weeks, include allowances for overhead activities such as vacations, sick days, training days, and company meetings. 

In addition to using the entries in these tables to avoid omitting parts of the software or kinds of activities from your estimates, you might also consider looking at a Work Breakdown Structure (WBS) for the standard kinds of activities to be considered. Section 10.3, “Hazards of Adding Up Best Case and Worst Case Estimates,” discusses estimating with a WBS and provides a generic WBS. 

## **4.6 Unfounded Optimism** 

Optimism assails software estimates from all sources. On the developer side of the project, Microsoft Vice President Chris Peters observed that “You never have to fear that estimates created by developers will be too pessimistic, because developers will always generate a too-optimistic schedule” (Cusumano and Selby 1995). In a study of 300 software projects, Michiel van Genuchten reported that developer estimates tended to contain an optimism factor of 20% to 30% (van Genuchten 1991). Although managers sometimes complain otherwise, developers don’t tend to sandbag their estimates—their estimates tend to be too low! 

## **Tip #20** Don’t reduce developer estimates—they’re probably too optimistic already. 

Optimism applies within the management ranks as well. A study of about 100 schedule estimates within the U.S. Department of Defense found a consistent “fantasy factor” of about 1.33 (Boehm 1981). Project managers and executives might not _assume_ that projects can be done 30% faster or cheaper than they can be done, but they certainly _want_ the projects to be done faster and cheaper, and that is a kind of optimism in itself. 

Common variations on this optimism theme include the following: 

- We’ll be more productive on this project than we were on the last project. 

- A lot of things went wrong on the last project. Not so many things will go wrong on this project. 

- We started the project slowly and were climbing a steep learning curve. We learned a lot of lessons the hard way, but all the lessons we learned will allow us to finish the project much faster than we started it. 

**Chapter 4 Where Does Estimation Error Come From?** 

**47** 

Considering that optimism is a near-universal fact of human nature, software estimates are sometimes undermined by what I think of as a Collusion of Optimists. Developers present estimates that are optimistic. Executives like the optimistic estimates because they imply that desirable business targets are achievable. Managers like the estimates because they imply that they can support upper management’s objectives. And so the software project is off and running with no one ever taking a critical look at whether the estimates were well founded in the first place. 

## **4.7 Subjectivity and Bias** 

Subjectivity creeps into estimates in the form of optimism, in the form of conscious bias, and in the form of unconscious bias. I differentiate between estimation _bias_ , which suggests an intent to fudge an estimate in one direction or another, and estimation _subjectivity_ , which simply recognizes that human judgment is influenced by human experience, both consciously and unconsciously. 

As far as bias is concerned, the response of customers and managers when they discover that the estimate does not align with the business target is sometimes to apply more pressure to the estimate, to the project, and to the project team. Excessive schedule pressure occurs in 75% to 100% of large projects (Jones 1994). 

As far as subjectivity is concerned, when considering different estimation techniques our natural tendency is to believe that the more “control knobs” we have on an estimate—that is, the more places there are to tweak the estimate to match our specific project—the more accurate the estimate will be. 

The reality is the opposite. The more control knobs an estimate has, the more chances there are for subjectivity to creep in. The issue is not so much that estimators deliberately bias their estimates. The issue is more that the estimate gets shaded slightly higher or slightly lower with each of the subjective inputs. If the estimation technique has a large number of subjective inputs, the cumulative effect can be significant. 

I've seen one example of this while teaching several hundred estimators to use the Cocomo II estimation model. Cocomo II includes 17 Effort Multipliers and 5 Scaling Factors. To create a Cocomo II estimate, the estimator must decide what adjustment is needed for each of these 22 factors. The factors adjust for whether your team is above average or below average, whether your software is more or less complex than average, and so on. In theory, these 22 control knobs should allow virtually any estimate to be fine-tuned. In practice, the control knobs seem to introduce 22 chances for error to creep into the estimate. 

Figure 4-6 shows the ranges of results of about 100 groups of estimators applying Cocomo II’s 17 Effort Multipliers to the same estimation problem. For each bar, the 

**48** 

**Part I Critical Estimation Concepts** 

bottom of the bar represents the lowest group estimate in a session and the top of the bar represents the highest group estimate in a session. The total height of the bar represents the variation in the estimates. 

**==> picture [340 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
60<br>55<br>50<br>45<br>40<br>Estimate<br>(staff 35<br>months)<br>30<br>25<br>20<br>15<br>10<br>(3) (3) (4) (4) (4) (5) (5) (5) (6) (6) (6) (6) (6) (7) (8) (8) (9) (10)<br>Estimating Session (number of groups in estimating session)<br>**----- End of picture text -----**<br>


**Figure 4-6** Example of variations in estimates when numerous adjustment factors are present. The more adjustment factors an estimation method provides, the more opportunity there is for subjectivity to creep into the estimate. 

If the estimation technique produced consistent results, we would see a tight clustering of results along the horizontal blue bar (the average of all the estimates). But, as you can see, the variation among the estimates is enormous. The total variation from highest to lowest is a factor of 4. The average variation from the low group to the high group within any one session is a factor of 1.7. 

An important aspect of this data is that _this particular estimation exercise is free of external bias_ . It occurs in an estimation class in which the emphasis is on accuracy. The only bias that is affecting these estimates are the biases inherent in the estimators’ experiences. In a real estimation situation, the range of results would probably be even greater because of the increased amount of external bias that would affect the estimates. 

In contrast, Figure 4-7 illustrates the range of estimation outcomes with an estimation technique that includes only one place to insert a subjective judgment into the estimate—that is, one control knob. (The control knob in this case is unrelated to the Cocomo II factors.) 

**Chapter 4 Where Does Estimation Error Come From? 49** 

**==> picture [340 x 206] intentionally omitted <==**

**----- Start of picture text -----**<br>
150<br>125<br>100<br>Estimate<br>(staff<br>months)<br>75<br>50<br>25<br>(4) (4) (5) (5) (5) (6) (6) (6) (6) (6) (7) (7) (8) (9) (9) (11)<br>Estimating Session (number of groups in estimating session)<br>**----- End of picture text -----**<br>


**Figure 4-7** Example of low variation in estimates resulting from a small number of adjustment factors. (The scales of the two graphs are different, but they are directly comparable when you account for the difference in the average values on the two graphs.) 

As you can see, the variation in these results is dramatically smaller than the variation when there are 17 control knobs present. The average variation from the low group to the high group within any one session is a factor of only 1.1. 

The finding that “more control knobs isn’t better” extends beyond software estimation. As forecasting guru J. Scott Armstrong states, “One of the most enduring and useful conclusions from research on forecasting is that simple methods are generally as accurate as complex methods” (Armstrong 2001). 

## **Tip #21** 

Avoid having “control knobs” on your estimates. While control knobs might give you a feeling of better accuracy, they usually introduce subjectivity and degrade actual accuracy. 

## **4.8 Off-the-Cuff Estimates** 

Project teams are sometimes trapped by off-the-cuff estimates. Your boss asks, for example, “How long would it take to implement print preview on the Gigacorp Web site?” You say, “I don’t know. I think it might take about a week. I’ll check into it.” You go off to your desk, look at the design and code for the program you were asked about, notice a few things you’d forgotten when you talked to your manager, add up 

**50** 

**Part I Critical Estimation Concepts** 

the changes, and decide that it would take about five weeks. You hurry over to your manager’s office to update your first estimate, but the manager is in a meeting. Later that day, you catch up with your manager, and before you can open your mouth, your manager says, “Since it seemed like a small project, I went ahead and asked for approval for the print-preview function at the budget meeting this afternoon. The rest of the budget committee was excited about the new feature and can’t wait to see it next week. Can you start working on it today?” 

I’ve found that the safest policy is not to give off-the-cuff estimates. Lederer and Prasad found that intuition and guessing in software project estimates were both correlated with cost and schedule overruns (Lederer and Prasad 1992). I’ve collected data on off-the-cuff estimates from 24 groups of estimators. Figure 4-8 shows the average error of estimates in these 24 groups of estimators for off-the-cuff estimates versus estimates that go through a group review process. 

**==> picture [346 x 235] intentionally omitted <==**

**----- Start of picture text -----**<br>
225%<br>200% Reviewed<br>Estimates<br>175%<br>Off-the-Cuff<br>150% Estimates<br>125%<br>100%<br>Error 75%<br>50%<br>25%<br>0%<br>-25%<br>-50%<br>-75%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24<br>Estimation Group<br>**----- End of picture text -----**<br>


**Figure 4-8** Average error from off-the-cuff estimates vs. reviewed estimates. 

The average off-the-cuff estimate has a mean magnitude of relative error (MMRE[1] ) of 67%, whereas the average reviewed estimate has an error of only 30%—less than half. (These are not software estimates, so the percentage errors shouldn’t be applied literally to software project estimates.) 

> 1 MMRE is equal to AbsoluteValue [(ActualResult – EstimatedResult) / ActualResult]. 

**51** 

**Chapter 4 Where Does Estimation Error Come From?** 

One of the errors people commit when estimating solely from personal memory is that they compare the new project to their memory of how long a past project took, or how much effort it required. Unfortunately, people sometimes remember their _estimate_ for the past project rather than the _actual outcome_ of the past project. If they use their past estimate as the basis for a new estimate, and the past project’s actual outcome was that it overran its estimate, guess what? The estimator has just calibrated a project overrun into the estimate for the new project. 

While Lederer and Prasad found that guessing and intuition were positively correlated with project overruns, they also found that the use of “documented facts” was _negatively_ correlated with project overruns. In other words, there is a world of difference between giving your boss an off-the-cuff answer versus saying, “I can’t give you an answer off the top of my head, but let me go back to my desk, check a few notes, and get back to you in 15 minutes. Would that be OK?” 

While this is a simple point, off-the-cuff estimation is one of the most common errors that project teams make (Lederer and Prasad 1992, Jørgensen 1997, Kitchenham et al. 2002). Avoiding off-the-cuff estimates is one of the most important points in this book. 

**Tip #22** Don’t give off-the-cuff estimates. Even a 15-minute estimate will be more accurate. 

What if your boss calls on a cell phone and insists on getting an estimate _right now?_ Consider your performance on the estimation quiz in Chapter 2, “How Good an Estimator Are You?” Did you get 8 to 10 answers correct? If not, what are the odds that the off-the-cuff answer you give your boss on the cell phone—even an estimate padded for uncertainty—will give you a 90% chance of including the correct answer? 

## **4.9 Unwarranted Precision** 

In casual conversation, people tend to treat “accuracy” and “precision” as synonyms. But for estimation purposes, the distinctions between these two terms are critical. 

_Accuracy_ refers to how close to the real value a number is. _Precision_ refers merely to how exact a number is. In software estimation, this amounts to how many significant digits an estimate has. A measurement can be precise without being accurate, and it can be accurate without being precise. The single digit 3 is an accurate representation of pi to one significant digit, but it is not precise. 3.37882 is a more precise representation of pi than 3 is, but it is not any more accurate. 

Airline schedules are precise to the minute, but they are not very accurate. Measuring people’s heights in whole meters might be accurate, but it would not be at all precise. 

**52 Part I Critical Estimation Concepts** 

Table 4-5 provides examples of numbers that are accurate, precise, or both. 

**Table 4-5 Examples of Accuracy and Precision** 

|**Table 4-5**<br>**Examples of Accu**|**racy and Precision**|
|---|---|
|**Example**|**Comment**|
|pi = 3|Accurate to 1 significant digit, but not precise|
|pi = 3.37882|Precise to 6 significant digits, but accurate only to 1 signifi-|
||cant digit|
|pi = 3.14159|Both accurate and precise, to 6 significant digits|
|My height = 2 meters|Accurate to 1 significant digit, but not very precise|
|Airline flight times|Precise to the minute, but not very accurate|
|“This project will take|Highly precise, but not accurate to the precision stated|
|395.7 days, ± 2 months”||
|“This project will take 1 year”|Not very precise, but could be accurate|
|“This project will require|Highly precise, but probably not accurate to the precision|
|7,214 staff hours”|stated|
|“This project will require|Not very precise, but could be accurate|
|4 staff years”||



For software estimation purposes, the distinction between accuracy and precision is critical. Project stakeholders make assumptions about project accuracy based on the precision with which an estimate is presented. When you present an estimate of 395.7 days, stakeholders assume the estimate is accurate to 4 significant digits! The accuracy of the estimate might be better reflected by estimating 1 year, 4 quarters, or 13 months, rather than 395.7 days. Using an estimate of 395.7 days instead of 1 year is like representing pi as 3.37882—the number is more precise, but it’s really less accurate. 

**Tip #23** Match the number of significant digits in your estimate (its precision) to to your estimate's accuracy. 

## **4.10 Other Sources of Error** 

The sources of error described in the first nine sections of this chapter are the most common and the most significant, but they are not exhaustive.  Here are some of the other ways that error can creep into an estimate: 

- Unfamiliar business area 

- Unfamiliar technology area 

- Incorrect conversion from estimated time to project time (for example, assuming the project team will focus on the project eight hours per day, five days per week) 

- Misunderstanding of statistical concepts (especially adding together a set of “best case” estimates or a set of “worst case” estimates) 

**Chapter 4 Where Does Estimation Error Come From? 53** 

- Budgeting processes that undermine effective estimation (especially those that require final budget approval in the wide part of the Cone of Uncertainty) 

- Having an accurate size estimate, but introducing errors when converting the size estimate to an effort estimate 

- Having accurate size and effort estimates, but introducing errors when converting those to a schedule estimate 

- Overstated savings from new development tools or methods 

- Simplification of the estimate as it’s reported up layers of management, fed into the budgeting process, and so on 

These topics are all discussed in more detail in later chapters. 

## **Additional Resources** 

Armstrong, J. Scott, ed. _Principles of forecasting: A handbook for researchers and practitioners_ . Boston, MA: Kluwer Academic Publishers, 2001. Armstrong is one of the leading researchers in forecasting in a marketing context. Many of the observations in this book are relevant to software estimation. Armstrong has been a leading critic of overly complex estimation models. 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: AddisonWesley, 2000. Boehm was the first to popularize the Cone of Uncertainty (he calls it a funnel curve). This book contains his most current description of the phenomenon. 

Cockburn, Alistair. _Agile Software Development_ . Boston, MA: Addison-Wesley, 2001. Cockburn’s book introduces Agile development approaches, which are especially useful in environments characterized by highly volatile requirements. 

Laranjeira, Luiz. “Software Size Estimation of Object-Oriented Systems,” _IEEE Transactions on Software Engineering_ , May 1990. This paper provided a theoretical-research foundation for the empirical observation of the Cone of Uncertainty. 

Tockey, Steve. _Return on Software_ . Boston, MA: Addison-Wesley, 2005. Chapters 21 through 23 discuss basic estimation concepts, general estimation techniques, and allowing for inaccuracy in estimates. Tockey includes a detailed discussion of how to build your own Cone of Uncertainty. 

Wiegers, Karl. _More About Software Requirements: Thorny Issues and Practical Advice_ . Redmond, WA: Microsoft Press, 2006. 

Wiegers, Karl. _Software Requirements_ , _Second Edition_ . Redmond, WA: Microsoft Press, 2003. In these two books, Wiegers describes numerous practices that help elicit good requirements in the first place, which substantially reduces requirements volatility later in a project. 

## Chapter 5 **Estimate Influences** 

_How much is 68 + 73?_ 

_ENGINEER: “It’s 141.” Short and sweet._ 

_MATHEMATICIAN: “68 + 73 = 73 + 68 by the commutative law of addition.” True, but not very helpful._ 

_ACCOUNTANT: “Normally it’s 141, but what are you going to use it for?”_ 

_—Barry W. Boehm and Richard E. Fairley_ 

Influences on a software project can be sliced and diced in several ways. Understanding these influences helps improve estimation accuracy and helps improve understanding of software project dynamics overall. 

Project size is easily the most significant determinant of effort, cost, and schedule. The kind of software you’re developing comes in second, and personnel factors are a close third. The programming language and environment you use are not first-tier influences on the project outcome, but they are a first-tier influence on the estimate. This chapter presents these first-tier influences in decreasing order of significance and concludes with a discussion of second-tier influences. 

## **5.1 Project Size** 

The largest driver in a software estimate is the size of the software being built, because there is more variation in the size than in any other factor. Figure 5-1 shows the way that effort grows in an average business-systems project as project size increases from 25,000 lines of code to 1,000,000 lines of code. The figure expresses size in lines of code (LOC), but the dynamic would be the same whether you measured size in function points, number of requirements, number of Web pages, or any other measure that expressed the same range of sizes. 

As the diagram shows, a system consisting of 1,000,000 LOC requires dramatically more effort than a system consisting of only 100,000 LOC. 

These comments about software size being the largest cost driver might seem obvious, yet organizations routinely violate this fundamental fact in two ways: 

- Costs, effort, and schedule are estimated without knowing how big the software will be. 

- Costs, effort, and schedule are not adjusted when the size of the software is consciously increased (that is, in response to change requests). 

**55** 

**56 Part I Critical Estimation Concepts** 

**==> picture [352 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
2,250<br>2,000<br>1,750<br>1,500<br>Effort 1,250<br>(staff<br>months) 1,000<br>750<br>500<br>250<br>0<br>Project Size (LOC)<br>050,000100,000150,000200,000250,000300,000350,000400,000450,000500,000550,000600,000650,000700,000750,000800,000850,000900,000950,0001,000,000<br>**----- End of picture text -----**<br>


_Source: Computed using data from the Cocomo II estimation model, assuming nominal diseconomy of scale (Boehm, et al 2000)._ 

**Figure 5-1** Growth in effort for a typical business-systems project. The specific numbers are meaningful only for the average business-systems project. The general dynamic applies to software projects of all kinds. 

**Tip #24** 

Invest an appropriate amount of effort assessing the size of the software that will be built. The size of the software is the single most significant contributor to project effort and schedule. 

## **Why Is This Book Discussing Size in Lines of Code?** 

People new to estimation sometimes have questions about whether lines of code are really a meaningful way to measure software size. One issue is that many modern programming environments are not as lines-of-code-oriented as older environments were. Another issue is that a lot of software development work—such as requirements, design, and testing—doesn’t produce lines of code. If you’re interested in seeing how these issues affect the usefulness of measuring size in lines of code, see Section 18.1, “Challenges with Estimating Size.” 

## **Diseconomies of Scale** 

People naturally assume that a system that is 10 times as large as another system will require something like 10 times as much effort to build. But the effort for a 

**Chapter 5 Estimate Influences 57** 

1,000,000-LOC system is more than 10 times as large as the effort for a 100,000LOC system, as is the effort for a 100,000-LOC system compared to the effort for a 10,000-LOC system. 

The basic issue is that, in software, larger projects require coordination among larger groups of people, which requires more communication (Brooks 1995). As project size increases, the number of communication paths among different people increases as a _squared_ function of the number of people on the project.[1] Figure 5-2 illustrates this dynamic. 

**==> picture [295 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3 6<br>Communication path Communication paths Communication paths<br>with 2 people with 3 people with 4 people<br>**----- End of picture text -----**<br>


**==> picture [188 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 45<br>Communication paths Communication paths<br>with 5 people with 10 people<br>**----- End of picture text -----**<br>


**Figure 5-2** The number of communication paths on a project increases proportionally to the square of the number of people on the team. 

The consequence of this exponential increase in communication paths (along with some other factors) is that projects also have an exponential increase in effort as a project size increases. This is known as a _diseconomy of scale_ . 

Outside software, we usually discuss _economies_ of scale rather than _diseconomies_ of scale. An economy of scale is something like, “If we build a larger manufacturing plant, we’ll be able to reduce the cost per unit we produce.” An economy of scale implies that the bigger you get, the smaller the unit cost becomes. 

A diseconomy of scale is the opposite. In software, the larger the system becomes, the greater the cost of each unit. If software exhibited economies of scale, a 100,000-LOC 

> 1 The actual number of paths is n x (n – 1) / 2, which is an n2 function. 

**58** 

**Part I Critical Estimation Concepts** 

system would be less than 10 times as costly as a 10,000-LOC system. But the opposite is almost always the case. 

Figure 5-3 illustrates a typical diseconomy of scale in software compared with the increase of effort that would be associated with linear growth. 

**==> picture [336 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
180<br>160<br>140<br>120<br>Effort 100<br>(staff<br>months) 80<br>60<br>40<br>Linear Growth<br>20 Typical Growth<br>0<br>Project Size (LOC)<br>10,000 20,000 30,000 40,000 50,000 60,000 70,000 80,000 90,000 100,000<br>**----- End of picture text -----**<br>


_Source: Computed using data from the Cocomo II estimation model, assuming nominal diseconomy of scale (Boehm, et al 2000)._ 

**Figure 5-3** Diseconomy of scale for a typical business-systems project ranging from 10,000 to 100,000 lines of code. 

As you can see from the graph, in this example, the 10,000-LOC system would require 13.5 staff months. If effort increased linearly, a 100,000-LOC system would require 135 staff months, but it actually requires 170 staff months. 

As Figure 5-3 is drawn, the effect of the diseconomy of scale doesn’t look very dramatic. Indeed, within the 10,000 LOC to 100,000 LOC range, the effect is usually not all that dramatic. But two factors make the effect more dramatic. One factor is greater difference in project size, and the other factor is project conditions that degrade productivity more quickly than average as project size increases. Figure 5-4 shows the range of outcomes for projects ranging from 10,000 LOC to 1,000,000 LOC. In addition to the nominal diseconomy, the graph also shows the worst-case diseconomy. 

**Chapter 5 Estimate Influences 59** 

**==> picture [324 x 235] intentionally omitted <==**

**----- Start of picture text -----**<br>
6,000<br>Linear Growth<br>Typical Growth<br>5,000 Worst Case<br>4,000<br>Effort<br>(staff 3,000<br>months)<br>2,000<br>1,000<br>0<br>Project Size (LOC)<br>050,000100,000150,000200,000250,000300,000350,000400,000450,000500,000550,000600,000650,000700,000750,000800,000850,000900,000950,0001,000,000<br>**----- End of picture text -----**<br>


_Source: Computed using data from the Cocomo II estimation model, assuming nominal and worst-case diseconomies of scale (Boehm, et al 2000)._ 

**Figure 5-4** Diseconomy of scale for projects with greater size differences and the worst-case diseconomy of scale. 

In this graph, you can see that the worst-case effort growth increases much faster than the nominal effort growth, and that the effect becomes much more pronounced at larger project sizes. Along the nominal effort growth curve, effort at 100,000 lines of code is 13 times what it is at 10,000 lines of code, rather than 10 times. At 1,000,000 LOC, effort is 160 times the 10,000-LOC effort, rather than 100 times. 

The worst-case growth is much worse. Effort on the worst-case curve at 100,000 LOC is 17 times what it is at 10,000 LOC, and at 1,000,000 LOC it isn’t 100 times as large— it’s 300 times as large! 

Table 5-1 illustrates the general relationship between project size and productivity. 

**Table 5-1 Relationship Between Project Size and Productivity** 

|**Table 5-1**<br>**Relatio**|**nship Between Project Size and Productivity**|
|---|---|
|**Project Size (in**||
|**Lines of Code)**|**Lines of Code per Staff Year (Cocomo II Nominal in Parentheses)**|
|10K|2,000–25,000 (3,200)|
|100K|1,000–20,000 (2,600)|
|1M|700–10,000 (2,000)|
|10M|300–5,000 (1,600)|



Source: Derived from data in _Measures for Excellence_ (Putnam and Meyers 1992), _Industrial Strength Software_ (Putnam and Meyers 1997), _Software Cost Estimation with Cocomo II_ (Boehm et al. 2000), and “Software Development Worldwide: The State of the Practice” (Cusumano et al. 2003). 

**60 Part I Critical Estimation Concepts** 

The numbers in this table are valid only for purposes of comparison between size ranges. But the general trend the numbers show is significant. Productivity on small projects can be 2 to 3 times as high as productivity on large projects, and productivity can vary by a factor of 5 to 10 from the smallest projects to the largest. 

**Tip #25** Don’t assume that effort scales up linearly as project size does. Effort scales up exponentially. 

For software estimation, the implications of diseconomies of scale are a case of good news, bad news. The bad news is that if you have large variations in the sizes of projects you estimate, you can’t just estimate a new project by applying a simple effort ratio based on the effort from previous projects. If your effort for a previous 100,000-LOC project was 170 staff months, you might figure that your productivity rate is 100,000/170, which equals 588 LOC per staff month. That might be a reasonable assumption for another project of about the same size as the old project, but if the new project is 10 times bigger, the estimate you create that way could be off by 30% to 200%. 

There’s more bad news: There isn’t a simple technique in the art of estimation that will account for a significant difference in the size of two projects. If you’re estimating a project of a significantly different size than your organization has done before, you’ll need to use estimation software that applies the science of estimation to compute the estimate for the new project based on the results of past projects. My company provides a free software tool called Construx® Estimate™ that will do this kind of estimate. You can download a copy at _www.construx.com/estimate_ . 

**Tip #26** Use software estimation tools to compute the impact of diseconomies of scale. 

## **When You Can Safely Ignore Diseconomies of Scale** 

After all that bad news, there is actually some good news. The majority of projects in an organization are often similar in size. If the new project you’re estimating will be similar in size to your past projects, it is usually safe to use a simple effort ratio, such as lines of code per staff month, to estimate a new project. Figure 5-5 illustrates the relatively minor difference in linear versus exponential estimates that occurs within a specific size range. 

If you use a ratio-based estimation approach within a restricted range of sizes, your estimates will not be subject to much error. If you used an average ratio from projects in the middle of the size range, the estimation error introduced by economies of scale would be no more than about 10%. If you work in an environment that experiences higher-than-average diseconomies of scale, the differences could be higher. 

**Chapter 5 Estimate Influences 61** 

**==> picture [318 x 229] intentionally omitted <==**

**----- Start of picture text -----**<br>
300<br>250<br>200<br>Effort<br>(staff 150<br>months)<br>100<br>Linear Grow<br>50<br>Typical Grow<br>0<br>Project Size (LOC)<br>50,000 60,000 70,000 80,000 90,000 100,000 110,000 120,000 130,000 140,000 150,000<br>**----- End of picture text -----**<br>


_Source: Computed using data from the Cocomo II estimation model, assuming nominal disecon of scale (Boehm, et al 2000)._ 

**Figure 5-5** Differences between ratio-based estimates and estimates based on diseconomy of scale will be minimal for projects within a similar size range. 

**Tip #27** 

If you’ve completed previous projects that are about the same size as the project you’re estimating—defined as being within a factor of 3 from largest to smallest— you can safely use a ratio-based estimating approach, such as lines of code per staff month, to estimate your new project. 

## **Importance of Diseconomy of Scale in Software Estimation** 

Much of the software-estimating world’s focus has been on determining the exact significance of diseconomies of scale. Although that is a significant factor, remember that the raw size is the largest contributor to the estimate. The effect of diseconomy of scale on the estimate is a second-order consideration, so put the majority of your effort into developing a good size estimate. We’ll discuss how to create software size estimates more specifically in Chapter 18, “Special Issues in Estimating Size.” 

## **5.2 Kind of Software Being Developed** 

After project size, the kind of software you’re developing is the next biggest influence on the estimate. If you’re working on life-critical software, you can expect your project to require far more effort than a similarly sized business-systems project. Table 5-2 shows examples of lines of code per staff month for projects of different kinds. 

**62 Part I Critical Estimation Concepts** 

**Table 5-2 Productivity Rates for Common Project Types** 

|**Table 5-2**<br>**Productivity Ra**|**tes for Common Proj**|**ect Types**||
|---|---|---|---|
||**LOC/Staff**|**Month Low-High**|**(Nominal)**|
||**10,000-LOC**|**100,000-LOC**|**250,000-LOC**|
|**Kind of Software**|**Project**|**Project**|**Project**|
|Avionics|100–1,000|20–300|20–200|
||**(200)**|**(50)**|**(40)**|
|Business Systems|800–18,000|200–7,000|100–5,000|
||**(3,000)**|**(600)**|**(500)**|
|Command and Control|200–3,000|50–600|40–500|
||**(500)**|**(100)**|**(80)**|
|Embedded Systems|100–2,000|30–500|20–400|
||**(300)**|**(70)**|**(60)**|
|Internet Systems (public)|600–10,000|100–2,000|100–1,500|
||**(1,500)**|**(300)**|**(200)**|
|Intranet Systems (internal)|1,500–18,000|300–7,000|200–5,000|
||**(4,000)**|**(800)**|**(600)**|
|Microcode|100–800|20–200|20–100|
||**(200)**|**(40)**|**(30)**|
|Process Control|500–5,000|100–1,000|80–900|
||**(1,000)**|**(300)**|**(200)**|
|Real-Time|100–1,500|20–300|20–300|
||**(200)**|**(50)**|**(40)**|
|Scientific Systems/|500–7,500|100–1,500|80–1,000|
|Engineering Research|**(1,000)**|**(300)**|**(200)**|
|Shrink wrap/Packaged|400–5,000|100–1,000|70–800|
|Software|**(1,000)**|**(200)**|**(200)**|
|Systems Software/Drivers|200–5,000|50–1,000|40–800|
||**(600)**|**(100)**|**(90)**|
|Telecommunications|200–3,000|50–600|40–500|
||**(600)**|**(100)**|**(90)**|



Source: Adapted and extended from _Measures for Excellence_ (Putnam and Meyers 1992), _Industrial Strength Software_ (Putnam and Meyers 1997), and _Five Core Metrics_ (Putnam and Meyers 2003). 

As you can see from the table, a team developing an intranet system for internal use might generate code 10 to 20 times faster than a team working on an avionics project, real-time project, or embedded systems project. The table also again illustrates the diseconomy of scale: projects of 100,000 LOC generate code far less efficiently than 10,000-LOC projects. Projects of 250,000 LOC generate code even less efficiently. 

You can account for the industry in which you’re working in one of three ways: 

- Use the results from Table 5-2 as a starting point. If you do that, notice that the ranges in the table are large—typically a factor of 10 difference between the high and the low ends of the ranges. 

**Chapter 5 Estimate Influences 63** 

   - Use an estimating model such as Cocomo II, and adjust the estimating parameters to match the kind of software you develop. If you do that, remember the cautions from Chapter 4, “Where Does Estimation Error Come From?” about using too many control knobs on your estimates. 

   - Use historical data from your own organization, which will automatically incorporate the development factors specific to the industry you work in. This is by far the best approach, and we’ll discuss the use of historical data in more detail in Chapter 8, “Calibration and Historical Data.” 

- **Tip #28** Factor the kind of software you develop into your estimate. The kind of software you’re developing is the second-most significant contributor to project effort and schedule. 

## **5.3 Personnel Factors** 

Personnel factors also exert significant influence on project outcomes. According to Cocomo II, on a 100,000-LOC project the combined effect of personnel factors can swing a project estimate by as much as a factor of 22! In other words, if your project ranked worst in each category shown in Figure 5-6 (shown by the gray bars), it would require 22 times as much total effort as a project that ranked best in each category (shown by the blue bars). 

**==> picture [296 x 178] intentionally omitted <==**

**----- Start of picture text -----**<br>
Requirements Analyst Capability −29% 42%<br>Programmer Capability (General) −24% 34%<br>Personnel Continuity (Turnover) −19% 29%<br>Applications (Business Area) Experience −19% 22%<br>Language and Tools Experience −16% 20%<br>Platform Experience  −15% 19%<br>Team Cohesion −14% 11%<br>**----- End of picture text -----**<br>


**Figure 5-6** Effect of personnel factors on project effort. Depending on the strength or weakness in each factor, the project results can vary by the amount indicated—that is, a project with the worst requirements analysts would require 42% more effort than nominal, whereas a project with the best analysts would require 29% less effort than nominal. 

**64 Part I Critical Estimation Concepts** 

The magnitude of these factors from the Cocomo II model is confirmed by numerous studies since the 1960s that show 10:1 to 20:1 differences in individual and team performance (Sackman, Erikson, and Grant 1968; Weinberg and Schulman 1974; Curtis 1981; Mills 1983; Boehm, Gray, and Seewaldt 1984; DeMarco and Lister 1985; Curtis et al. 1986; Card 1987; Boehm 1987b; Boehm and Papaccio 1988; Valett and McGarry 1989; Boehm et al. 2000). 

One implication of these variations among individuals is that you can’t accurately estimate a project if you don’t have some idea of who will be doing the work—because individual performance varies by a factor of 10 or more. Within any particular organization, however, your estimates probably won’t need to account for that much variation because both top-tier and bottom-tier developers tend to migrate toward organizations that employ other people with similar skill levels (Mills 1983, DeMarco and Lister 1999). 

Another implication is that the most accurate estimation approach will depend on whether you know who specifically will be doing the work that’s being estimated. That issue is discussed in Chapter 16, “Flow of Software Estimates on a WellEstimated Project.” 

## **5.4 Programming Language** 

The specific programming language a project uses will affect your estimates in at least four ways. 

First, as Figure 5-6 suggested, the project team’s experience with the specific language and tools that will be used on the project has about a 40% impact on the overall productivity rate of the project. 

Second, some languages generate more functionality per line of code than others. Table 5-3 shows the amount of functionality that several languages produce relative to the C programming language. 

**Table 5-3 Ratio of High-Level-Language Statements to Equivalent C Code** 

|**Table 5-3**<br>**Ratio of**|**High-Level-Language Statements to Equivalent C Code**|
|---|---|
|**Language**|**Level Relative to C**|
|C|1 to 1|
|C#|1 to 2.5|
|C++|1 to 2.5|
|Cobol|1 to 1.5|
|Fortran 95|1 to 2|
|Java|1 to 2.5|
|Macro Assembly|2 to 1|



**65** 

**Chapter 5 Estimate Influences** 

> **Table 5-3 Ratio of High-Level-Language Statements to Equivalent C Code** 

|**Table 5-3**<br>**Ratio o**|**f High-Level-Language Statements to Equivalent C Code**|
|---|---|
|**Language**|**Level Relative to C**|
|Perl|1 to 6|
|Smalltalk|1 to 6|
|SQL|1 to 10|
|Visual Basic|1 to 4.5|



Source: Adapted from _Estimating Software Costs_ (Jones 1998) and _Software Cost Estimation with Cocomo II_ (Boehm 2000). 

If you don’t have any choice about the programming language you’re using, this point is not relevant to your estimate. But if you have some leeway in choosing a programming language, you can see that using a language such as Java, C#, or Microsoft Visual Basic would tend to be more productive than using C, Cobol, or Macro Assembly. 

A third factor related to languages is the richness of the tool support and environment associated with the language. According to Cocomo II, the weakest tool set and environment will increase total project effort by about 50% compared to the strongest tool set and environment (Boehm et al. 2000). Realize that the choice of programming language might determine the choice of tool set and environment. 

A final factor related to programming language is that developers working in interpreted languages tend to be more productive than those working in compiled languages, perhaps as much as a factor of 2 (Jones 1986a, Prechelt 2000). 

The concept of amount of functionality produced per line of code will be discussed further in Section 18.2, “Function-Point Estimation.” 

## **5.5 Other Project Influences** 

I’ve mentioned the Cocomo II estimating model several times in this chapter. As discussed in Chapter 4, I have reservations about subjectivity creeping into the use of Cocomo II’s adjustment factors. However, my reservations stem from concerns about “usage failure” more than concerns about “method failure.” The Cocomo II project has done a much better job than other studies of rigorously isolating the impacts of specific factors on project outcomes. Most studies combine multiple factors intentionally or unintentionally. A study might examine the impact of software process improvement, but it might not isolate the impact of switching from one programming language to another, or of consolidating staff 

**66** 

**Part I Critical Estimation Concepts** 

from two locations to one location. The Cocomo II project has conducted the most statistically rigorous analysis of specific factors that I’ve seen. So, although I prefer other methods for estimation, I do recommend studying Cocomo II’s adjustment factors to gain an understanding of the significance of different software project influences. 

Table 5-4 lists the Cocomo II ratings factors for Cocomo’s 17 Effort Multipliers (EMs). The Very Low column represents the amount you would adjust an effort estimate for the best (or worst) influence of that factor. For example, if a team had very low “Applications (Business Area) Experience,” you would multiply your nominal Cocomo II effort estimate by 1.22. If the team had very high experience, you would multiply the estimate by 0.81 instead. 

**Table 5-4 Cocomo II Adjustment Factors** 

|**Table 5-4**<br>**Cocomo II A**|**djustme**|**nt Facto**|**rs**|||||
|---|---|---|---|---|---|---|---|
|||||**Ratings**||||
||**Very**||||**Very**|**Extra**||
|**Factor**|**Low**|**Low**|**Nominal**|**High**|**High**|**High**|**Influence**|
|Applications (Business|1.22|1.10|1.00|0.88|0.81||1.51|
|Area) Experience||||||||
|Database Size||0.90|1.00|1.14|1.28||1.42|
|Developed for||0.95|1.00|1.07|1.15|1.24|1.31|
|Reuse||||||||
|Extent of|0.81|0.91|1.00|1.11|1.23||1.52|
|Documentation Required||||||||
|Language and Tools|1.20|1.09|1.00|0.91|0.84||1.43|
|Experience||||||||
|Multisite Development|1.22|1.09|1.00|0.93|0.86|0.78|1.56|
|Personnel Continuity|1.29|1.12|1.00|0.90|0.81||1.59|
|(turnover)||||||||
|Platform Experience|1.19|1.09|1.00|0.91|0.85||1.40|
|Platform Volatility||0.87|1.00|1.15|1.30||1.49|
|Product Complexity|0.73|0.87|1.00|1.17|1.34|1.74|2.38|
|Programmer Capability|1.34|1.15|1.00|0.88|0.76||1.76|
|(general)||||||||
|Required Software|0.82|0.92|1.00|1.10|1.26||1.54|
|Reliability||||||||
|Requirements Analyst|1.42|1.19|1.00|0.85|0.71||2.00|
|Capability||||||||
|Storage Constraint|||1.00|1.05|1.17|1.46|1.46|
|Time Constraint|||1.00|1.11|1.29|1.63|1.63|
|Use of Software Tools|1.17|1.09|1.00|0.90|0.78||1.50|



**Chapter 5 Estimate Influences 67** 

The Influence column on the far right of the table shows the degree of influence that each factor, in isolation, has on the overall effort estimate. The Applications (Business Area) Experience factor has an influence of 1.51, which means that a project performed by a team with very low skills in that area will require 1.51 times as much total effort as a project performed by a team with very high skills in that area. (Influence is computed by dividing the largest value by the smallest value. For example, 1.51 is 1.22/0.8.) 

Figure 5-7 presents another view of the impact of the Cocomo II factors, in which the factors are arranged from most significant influence to least significant influence. 

**==> picture [332 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Product Complexity 2.38<br>Requirements Analyst Capability 2.00<br>Programmer Capability (General) 1.76<br>Time Constraint 1.63<br>Personnel Continuity (Turnover) 1.59<br>Multisite Development 1.56<br>Required Software Reliability 1.54<br>Extent of Documentation Required 1.52<br>Applications (Business Area) Experience 1.51<br>Use of Software Tools 1.50<br>Platform Volatility 1.49<br>Storage Constraint 1.46<br>Process Maturity 1.43<br>Language and Tools Experience 1.43<br>Database Size 1.42<br>Platform Experience 1.40<br>Architecture and Risk Resolution 1.38<br>Precedentedness 1.33<br>Developed for Reuse 1.31<br>Team Cohesion 1.29<br>Development Flexibility 1.26<br>**----- End of picture text -----**<br>


**Figure 5-7** Cocomo II factors arranged in order of significance. The relative lengths of the bars represent the sensitivity of the estimate to the different factors. 

Figure 5-8 shows the same factors represented in terms of their potential to increase total effort (the gray bars) versus decrease effort (the blue bars). 

**68** 

**Part I Critical Estimation Concepts** 

**==> picture [339 x 343] intentionally omitted <==**

**----- Start of picture text -----**<br>
Product Complexity −27% 74%<br>Requirements Analyst Capability −29% 42%<br>Programmer Capability (General) −24% 34%<br>Time Constraint 0% 63%<br>Personnel Continuity (Turnover) −19% 29%<br>Multi-Site Development −22% 22%<br>Required Software Reliability −18% 26%<br>Extent of Documentation Required −19% 23%<br>Applications (Business Area) Experience −19% 22%<br>Use of Software Tools −22% 17%<br>Platform Volatility −13% 30%<br>Storage Constraint 0% 46%<br>Precedentedness −19% 15%<br>Process Maturity −19% 15%<br>Language and Tools Experience −16% 20%<br>Database Size −10% 28%<br>Platform Experience −15% 19%<br>Architecture and Risk Resolution −18% 14%<br>Development Flexibility −16% 12%<br>Developed for Reuse −5% 24%<br>Team Cohesion −14% 11%<br>**----- End of picture text -----**<br>


**Figure 5-8** Cocomo II factors arranged by potential to increase total effort (gray bars) and potential to decrease total effort (blue bars). 

I’ve listed some observations about these factors in Table 5-5 in alphabetical order. 

**Table 5-5 Cocomo II Adjustment Factors** 

|**Table 5-5**<br>**Cocomo II A**|**djustment Fact**|**ors**|
|---|---|---|
|**Cocomo II Factor**|**Influence**|**Observation**|
|Applications (Business|1.51|Teams that aren’t familiar with the project’s|
|Area) Experience||business area need significantly more time. This|
|||shouldn’t be a surprise.|
|Architecture and|1.38*|The more actively the project attacks risks, the|
|Risk Resolution||lower the effort and cost will be. This is one of|
|||the few Cocomo II factors that is controllable by|
|||the project manager.|
|Database Size|1.42|Large, complex databases require more effort|
|||project-wide. Total influence is moderate.|



**69** 

**Chapter 5 Estimate Influences** 

> **Table 5-5 Cocomo II Adjustment Factors** 

|**Table 5-5**<br>**Cocomo II Adj**|**ustment Fact**|**ors**|
|---|---|---|
|**Cocomo II Factor**|**Influence**|**Observation**|
|Developed for|1.31|Software that is developed with the goal of later|
|Reuse||reuse can increase costs as much as 31%. This|
|||doesn’t say whether the initiative actually|
|||succeeds. Industry experience has been that|
|||forward-looking reuse programs often fail.|
|Extent of Documentation|1.52|Too much documentation can negatively affect|
|Required||the whole project. Impact is moderately high.|
|Language and Tools|1.43|Teams that have experience with the program-|
|Experience||ming language and/or tool set work moderately|
|||more productively than teams that are climbing|
|||a learning curve. This is not a surprise.|
|Multi-Site|1.56|Projects conducted by a team spread across|
|Development||multiple sites around the globe will take 56%|
|||more effort than projects that are conducted by|
|||a team co-located at one facility. Projects that|
|||are conducted at multiple sites, including out-|
|||sourced or offshore projects, need to take this|
|||effect seriously.|
|Personnel Continuity|1.59|Project turnover is expensive—in the top one-|
|(turnover)||third of influential factors.|
|Platform Experience|1.40|Experience with the underlying technology|
|||platform affects overall project performance|
|||moderately.|
|Platform Volatility|1.49|If the platform is unstable, development can take|
|||moderately longer. Projects should weigh this|
|||factor in their decision about when to adopt a|
|||new technology. This is one reason that systems|
|||projects tend to take longer than applications|
|||projects.|
|Precedentedness|1.33*|Refers to how “precedented” (we usually say|
|||“unprecedented”) the application is. Familiar sys-|
|||tems are easier to create than unfamiliar systems.|
|Process Maturity|1.43*|Projects that use more sophisticated develop-|
|||ment processes take less effort than projects that|
|||use unsophisticated processes. Cocomo II uses|
|||an adaptation of the CMM process maturity|
|||model to apply this criterion to a specific project.|
|Product Complexity|2.38|Product complexity (software complexity) is the|
|||single most significant adjustment factor in the|
|||Cocomo II model. Product complexity is largely|
|||determined by the type of software you’re|
|||building.|
|Programmer Capability|1.76|The skill of the programmers has an impact of|
|(general)||a factor of almost 2 on overall project results.|



**70 Part I Critical Estimation Concepts** 

**Table 5-5 Cocomo II Adjustment Factors** 

|**Table 5-5**<br>**Cocomo II Ad**|**justment Fact**|**ors**|
|---|---|---|
|**Cocomo II Factor**|**Influence**|**Observation**|
|Required Reliability|1.54|More reliable systems take longer. This is one|
|||reason (though not the only reason) that|
|||embedded systems and life-critical systems|
|||tend to take more effort than other projects of|
|||similar sizes. In most cases, your marketplace|
|||determines how reliable your software must be.|
|||You don’t usually have much latitude to|
|||change this.|
|Requirements Analyst|2.00|The single largest personnel factor—good|
|Capability||requirements capability—makes a factor of|
|||2 difference in the effort for the entire project.|
|||Competency in this area has the potential to|
|||reduce a project’s overall effort from nominal|
|||more than any other factor.|
|Requirements Flexibility|1.26*|Projects that allow the development team|
|||latitude in how they interpret requirements|
|||take less effort than projects that insist on rigid,|
|||literal interpretations of all requirements.|
|Storage Constraint|1.46|Working on a platform on which you’re butting|
|||up against storage limitations moderately|
|||increases project effort.|
|Team Cohesion|1.29*|Teams with highly cooperative interactions|
|||develop software more efficiently than teams|
|||with more contentious interactions.|
|Time Constraint|1.63|Minimizing response time increases effort|
|||across the board. This is one reason that|
|||systems projects and real-time projects tend|
|||to consume more effort than other projects of|
|||similar sizes.|
|Use of Software Tools|1.50|Advanced tool sets can reduce effort significantly.|



> * Exact effect depends on project size. Effect listed is for a project size of 100,000 LOC. These factors are discussed in the next section. 

As I hinted earlier, studying the Cocomo II adjustment factors to gain insight into your project’s strengths and weaknesses is a high-leverage activity. For the estimate itself, using historical data from your past or current projects tends to be easier and more accurate than tweaking Cocomo’s 22 adjustment factors. 

Chapter 8 will discuss the ins and outs of collecting and using historical data. 

## **5.6 Diseconomies of Scale Revisited** 

The Cocomo II adjustment factors provide an interesting viewpoint into how diseconomies of scale operate. In Figure 5-9, 5 of the factors in the figure are called _scaling factors_ . These are the factors that contribute to software’s diseconomies of scale. They 

**Chapter 5 Estimate Influences 71** 

affect projects to different degrees at different sizes. Figure 5-9 shows the same graph with these factors highlighted in blue. 

|Development Flexibility<br>Team Cohesion<br>Developed for Reuse<br>Precedentedness<br>Architecture and Risk Resolution<br>Platform Experience<br>Database Size<br>Language and Tools Experience<br>Process Maturity<br>Storage Constraint<br>Platform Volatility<br>Use of Software Tools <br>Applications Experience<br>Documentation Match to Lifecycle Needs<br>Required Software Reliability <br>Multisite Development<br>Personnel Continuity (Turnover)<br>Time Constraint<br>Programmer Capability (General)<br>Requirements Analyst Capability<br>Product Complexity|2.38|
|---|---|
||2.00|
||1.76|
||1.63|
||1.59|
||1.56|
||1.54|
||1.52|
||1.51|
||1.50|
||1.33|
||1.31|
||1.29|
||1.26|



**Figure 5-9** Cocomo II factors with diseconomy of scale factors highlighted in blue. Project size is 100,000 LOC. 

None of the factors that contribute to software’s diseconomy of scale is in the top half of factors in terms of significance. In fact, 4 of the 5 least-influential factors are scaling factors. However, because the scaling factors contribute different amounts at different project sizes, this diagram must be drawn from the point of view of a project of a specific size. The factors in Figure 5-9 are shown for a project of 100,000 lines of code. Figure 5-10 shows what happens when the factors are recalculated for a much larger project of 5,000,000 lines of code. 

The scaling factors all become significant as project size increases. Although none of them was in the top half at 100,000 LOC, all the scaling factors are in the top half at 5,000,000 LOC. 

**72 Part I Critical Estimation Concepts** 

|Developed for Reuse<br>Platform Experience<br>Database Size<br>Language and Tools Experience<br>Storage Constraint<br>Platform Volatility<br>Use of Software Tools<br>Applications Experience<br>Documentation Match to Lifecycle Needs<br>Required Software Reliability<br>Development Flexibility<br>Multi-site Development<br>Personnel Continuity (Turnover)<br>Team Cohesion<br>Time Constraint<br>Precedentedness<br>Programmer Capability (General)<br>Architecture and Risk Resolution<br>Process Maturity<br>Requirements Analyst Capability<br>Product Complexity|2.38|
|---|---|
||2.00|
||1.94|
||1.83|
||1.76|
||1.70|
||1.63|
||1.59|
||1.59|
||1.56|
||1.54|
||1.54|
||1.52|
||1.51|
||1.50|
||1.46|
||1.43|
||1.42|
||1.40|
||1.31|



**Figure 5-10** Cocomo II factors with diseconomy of scale factors highlighted in blue. Project size is 5,000,000 LOC. 

What this means from an estimating point of view is that different factors need to be weighted differently at different project sizes. What this means from a project planning and control point of view is that small and medium-sized projects can succeed largely on the basis of strong individuals. Large projects still need strong individuals, but how well the project is managed (especially in terms of risk management), how mature the organization is, and how well the individuals coalesce into a team become as significant. 

## **Additional Resources** 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: AddisonWesley, 2000. This book is the definitive description of Cocomo II. The book’s size is daunting, but it describes the basic Cocomo model within the first 80 pages, 

**73** 

**Chapter 5 Estimate Influences** 

including detailed definitions of the effort multipliers and scaling factors discussed in this chapter and how Cocomo II accounts for diseconomies of scale. The rest of the book describes extensions of the model. 

Putnam, Lawrence H. and Ware Myers. _Measures for Excellence: Reliable Software On Time, Within Budget_ . Englewood Cliffs, NJ: Yourdon Press, 1992. This book describes Putnam’s estimation method including how it addresses diseconomies of scale. I like Putnam’s model because it contains few control knobs and works best when it is calibrated with historical data. The book is mathematically oriented, so it can be slow going. 

