# **Part II Fundamental Estimation Techniques** 

Chapter 6 

## **Introduction to Estimation Techniques** 

Chapters 1 through 5 described the critical concepts that underlie all software estimates. This book now turns to a discussion of detailed estimation techniques that can be applied to specific estimation problems. 

One important consideration in the use of these techniques is that different techniques will apply in different circumstances. This chapter introduces the major considerations in choosing which techniques to choose. 

## **6.1 Considerations in Choosing Estimation Techniques** 

The most useful techniques in any given situation are determined by both a desire to account for the estimation influences described in Chapter 5, “Estimate Influences,” and a desire to avoid the sources of estimation error described in Chapter 4, “Where Does Estimation Error Come From?” The following sections describe the major issues you should consider. 

## **What’s Being Estimated** 

Some projects determine their features and then focus on estimating the schedule and effort needed to deliver those features. Other projects determine their budgets and development time frames and then focus on estimating how many features they can deliver. 

Many estimation techniques are applicable regardless of what is being estimated; a few techniques are better suited to estimating how much effort a project will require, how long a project will take, or how many features can be delivered. 

In this book, estimating _size_ refers to estimating the scope of technical work of a given feature set—in units such as lines of code, function points, stories, or some other measure. Estimating _features_ refers to estimating how many features can be delivered within schedule and budget constraints. These terms are not industry standards; I’m defining them here for the sake of clarity. 

**77** 

**78 Part II Fundamental Estimation Techniques** 

## **Project Size** 

Project size is another factor to consider in choosing the best estimation technique. 

_**Small**_ I characterize a small project as a project with five or fewer total technical staff, but that is a loose characterization. Small projects typically can’t use the statistically oriented techniques that larger projects can use because variations in individual productivity drown out other factors. 

Small projects are more likely to use a flat staffing model (using the same number of people on the team for the entire project), which invalidates some of the more algorithmically oriented large-project estimation approaches. 

The best estimation techniques for small projects tend to be “bottom-up” techniques based on estimates created by the individuals who will actually do the work. 

_**Large**_ A large project is a project with a team of approximately 25 people or more that lasts 6 to 12 months or more. 

The best techniques for large projects change significantly from the beginning of the project to the end. In the early stages, the best estimation approaches tend to be “topdown” techniques based on algorithms and statistics. These are valid at the point in the project when specific team members are not yet known—when plans are based on a team that consists of, for example, “11 senior engineers, 25 staff developers, and 8 testers,” rather than specific individuals. 

In the middle stages, a combination of top-down and bottom-up techniques based on the project’s own historical data will produce the most accurate estimates. In the later stages of large projects, bottom-up techniques will provide the most accurate estimates. 

_**Medium**_ Medium-size projects consist of approximately 5 to 25 people and last 3 to 12 months. They have the advantage of being able to use virtually all the estimation techniques that large projects can use and several of the small-project techniques, too. 

## **Software Development Style** 

For purposes of estimation, the two major development styles are _sequential_ and _iterative_ . Industry terminology surrounding iterative, Agile, and sequential projects can be confusing. For this book’s purposes, the primary difference between these kinds of projects is the percentage of requirements they define early in the project compared to the percentage they define after construction is underway. 

**79** 

**Chapter 6 Introduction to Estimation Techniques** 

Here is how several common development approaches stack up according to these criteria. 

_**Evolutionary prototyping**_ Evolutionary prototyping is used when requirements are unknown, and one of the primary reasons to use evolutionary prototyping is to help define requirements (McConnell 1996). For estimation purposes, this is an iterative development style. 

_**Extreme Programming**_ Extreme Programming deliberately defines only the requirements that will be developed in the next iteration, which typically lasts less than a month (Beck 2004). For estimation purposes, Extreme Programming is a highly iterative approach. 

_**Evolutionary delivery**_ An evolutionary delivery project can define anywhere from “hardly any” to “most” of its requirements up front (Gilb 1988, McConnell 1996). Depending on which end of the scale the project falls on, an evolutionary delivery project can be either sequential or iterative. Most evolutionary delivery projects leave enough requirements undefined at the beginning of construction that the approach as normally practiced is iterative. 

_**Staged delivery**_ Staged delivery attempts to define the majority of its requirements prior to beginning the majority of construction (McConnell 1996). It uses iterations within design, construction, and test, so in some sense it is iterative. For estimation purposes, however, it is a sequential development style. 

_**Rational Unified Process**_ The Rational Unified Process (RUP) describes its stages as “iterations.” However, a nominal RUP project seeks to define about 80% of its requirements before construction begins (Jacobson, Booch, and Rumbaugh 1999). For estimation purposes, RUP is a sequential development style. 

_**Scrum**_ Scrum is a development style in which a project team takes on a set of features that it can implement within a 30-day “sprint” (Schwaber and Beedle 2002). Once a sprint begins, the customer is not allowed to change requirements. From the point of view of an individual sprint, for estimation purposes, Scrum is sequential. Because features are not allocated for more than one sprint at a time, from a multiplesprint (multiple iteration) point of view, Scrum is iterative. 

## **Effect of Development Style on Choice of Estimation Techniques** 

Both iterative and sequential projects tend to start with top-down or statistically based estimation techniques and both eventually migrate toward bottom-up techniques. Iterative projects transition to refining their estimates more quickly using project-specific data. 

**80 Part II Fundamental Estimation Techniques** 

## **Development Stage** 

As a team works its way through a project, it develops information that supports more accurate estimates. Requirements become better understood, designs become more detailed, plans become firmer, and the project itself generates productivity data that can be used to estimate the remainder of the project. 

This book defines development stages as follows: 

_**Early**_ On sequential projects, the early stage will be the period from the beginning of the project concept until requirements have been mostly defined. On iterative projects, _early_ refers to the initial planning period. 

_**Middle**_ The middle stage is the time between initial planning and early construction. On a sequential project, this time will extend from requirements and architecture time until enough construction has been completed to generate project productivity data that can be used for estimation. On iterative projects, _middle_ refers to the first two to four iterations—the iterations that occur before the project can confidently base its estimates on its own productivity data. 

_**Late** Late_ refers to the time from mid-construction through release. 

Some techniques work best in the wide part of the Cone of Uncertainty. Others work better after the project has begun to generate data that can be used to estimate the remainder of the project. 

## **Accuracy Possible** 

The accuracy of a technique is a function partly of the technique, partly of whether the technique is being applied to a suitable estimation problem, and partly of when in the project the technique is applied. 

Some estimation techniques produce high accuracy but at high cost. Others produce lower accuracy, but at lower cost. Normally you’ll want to use the most accurate techniques available, but depending on the stage of the project and how much accuracy is possible at that point in the Cone of Uncertainty, a low-cost, low-accuracy approach can be appropriate. 

**81** 

**Chapter 6 Introduction to Estimation Techniques** 

## **6.2 Technique Applicability Tables** 

Most of the remaining chapters in this book begin with tables that describe the applicability of techniques in the chapter. Here’s an example: 

## **Applicability of Techniques in this Chapter—SAMPLE** 

||**Group Reviews**|**Calibration with Project-Specific Data**|
|---|---|---|
|**What’s Estimated**|Size, Effort, Schedule,|Size, Effort, Schedule, Features|
||Features||
|**Size of project**|- M L|S M L|
|**Development Stage**|Early–Middle|Middle—Late|
|**Iterative or Sequential**|Both|Both|
|**Accuracy Possible**|Medium–High|High|



The entries in the table are based on the considerations described in the previous section. Table 6-1 describes how to interpret the entries in these tables. 

> **Table 6-1 Possible Entries in the “Applicability of Techniques in This Chapter” Tables** 

|**Table 6-1**<br>**Possible Entries**|**in the “Applicability of Techniques in This Chapter” Tables**|
|---|---|
|**Table Entry**|**Possible Entries**|
|What’s estimated|Size, Effort, Schedule, Features|
|Size of project|S M L (Small, Medium, Large)|
|Development stage|Early, Middle, Late|
|Iterative or sequential|Iterative, Sequential, or Both|
|Accuracy possible|Low, Medium, High|



## **Tip #29** 

When choosing estimation techniques, consider what you want to estimate, the size of the project, the development stage, the project’s development style, and what accuracy you need. 

Chapter 7 **Count, Compute, Judge** 

## **Applicability of Techniques in This Chapter** 

||**Count**|**Compute**|
|---|---|---|
|**What’s estimated**|Size, Features|Size, Effort, Schedule, Features|
|**Size of project**|S M L|S M L|
|**Development stage**|Early–Late|Early–Middle|
|**Iterative or sequential**|Both|Both|
|**Accuracy possible**|High|High|



Suppose you’re at a reception for the world’s best software estimators. The room is packed, and you’re seated in the middle of the room at a table with three other estimators. All you can see as you scan the room are wall-to-wall estimators. Suddenly, the emcee steps up to the microphone and says, “We need to know exactly how many people are in this room so that we can order dessert. Who can give me the most accurate estimate for the number of people in the room?” 

The estimators at your table immediately break out into a vigorous discussion about the best way to estimate the answer. Bill, the estimator to your right, says, “I make a hobby of estimating crowds. Based on my experience, it looks to me like we’ve got about 335 people in the room.” 

The estimator sitting across the table from you, Karl, says, “This room has 11 tables across and 7 tables deep. One of my friends is a banquet planner, and she told me that they plan for 5 people per table. It looks to me like most of the tables do actually have about 5 people at them. If we multiple 11 times 7 times 5, we get 385 people. I think we should use that as our estimate.” 

The estimator to your left, Lucy, says, “I noticed on the way into the room that there was an occupancy limit sign that says this room can hold 485 people. This room is pretty full. I’d say 70 to 80 percent full. If we multiply those percentages by the room limit, we get 340 to 388 people. How about if we use the average of 364 people, or maybe just simplify it to 365?” 

Bill says, “We have estimates of 335, 365, and 385. It seems like the right answer must be in there somewhere. I’m comfortable with 365.” 

**83** 

**84 Part II Fundamental Estimation Techniques** 

“Me too,” Karl says. 

Everyone looks at you. You say, “I need to check something. Would you excuse me for a minute?” Lucy, Karl, and Bill give you curious looks and say, “OK.” 

You return a few minutes later. “Remember how we had to have our tickets scanned before we entered the room? I noticed on my way into the room that the handheld ticket scanner had a counter. So I went back and talked to the ticket taker at the front door. She said that, according to her scanner, she has scanned 407 tickets. She also said no one has left the room so far. I think we should use 407 as our estimate. What do you say?” 

## **7.1 Count First** 

What do you think the right answer is? Is it the answer of 335, created by Bill, whose specialty is estimating crowd sizes? Is it the answer of 385, derived by Karl from a few reasonable assumptions? Is it Lucy’s 365, also derived from a few reasonable assumptions? Or is the right number the 407 that was counted by the ticket scanner? _Is there any doubt in your mind that 407 is the most accurate answer?_ For the record, the story ended by your table proposing the answer of 407, which turned out to be the correct number, and your table was served dessert first. 

One of the secrets of this book is that you should avoid doing what we traditionally think of as estimating! If you can _count_ the answer directly, you should do that first. That approach produced the most accurate answer in the story. 

If you can’t count the answer directly, you should count something else and then _compute_ the answer by using some sort of calibration data. In the story, Karl had the historical data of knowing that the banquet was planned to have 5 people per table. He _counted_ the number of tables and then computed the answer from that. 

Similarly, Lucy based her estimate on the documented fact of the room’s occupancy limit. She used her _judgment_ to estimate the room was 70 to 80 percent full. 

The least accurate estimate came from, Bill, the person who used only _judgment_ to create the answer. 

## **Tip #30** 

_Count_ if at all possible. _Compute_ when you can’t count. Use _judgment_ alone only as a last resort. 

**Chapter 7 Count, Compute, Judge 85** 

## **7.2 What to Count** 

Software projects produce numerous things that you can count. Early in the development life cycle, you can count marketing requirements, features, use cases, and stories, among other things. 

In the middle of the project, you can count at a finer level of granularity—engineering requirements, Function Points, change requests, Web pages, reports, dialog boxes, screens, and database tables, just to name a few. 

Late in the project, you can count at an even finer level of detail—code already written, defects reported, classes, and tasks, as well as all the detailed items you were counting earlier in the project. 

You can decide what to count based on a few goals. 

_**Find something to count that’s highly correlated with the size of the software you’re estimating**_ If your features are fixed and you’re estimating cost and schedule, the biggest influence on a project estimate is the size of the software. When you look for something to count, look for something that will be a strong indicator of the software’s size. Number of marketing requirements, number of engineering requirements, and Function Points are all examples of countable quantities that are strongly associated with final system size. 

In different environments, different quantities are the most accurate indicators of project size. In one environment, the best indicator might be the number of Web pages. In another environment, the best indicator might be the number of marketing requirements, test cases, stories, or configuration settings. The trick is to find something that’s a relevant indicator of size in your environment. 

**Tip #31** Look for something you can count that is a meaningful measure of the scope of work in your environment. 

_**Find something to count that’s available sooner rather than later in the development cycle**_ The sooner you can find something meaningful to count, the sooner you’ll be able to provide long-range predictability. The count of lines of code for a project is often a great indicator of project effort, but the code won’t be available to count until the very end of the project. Function Points are strongly associated with ultimate project size, but they aren’t available until you have detailed requirements. If you can find something you can count earlier, you can use that to create an estimate earlier. For example, you might create a rough estimate based on a count of marketing requirements and then tighten up the estimate later based on a Function Point count. 

**86 Part II Fundamental Estimation Techniques** 

_**Find something to count that will produce a statistically meaningful average**_ Find something that will produce a count of 20 or more. Statistically, you need a sample of at least 20 items for the average to be meaningful. Twenty is not a magic number, but it’s a good guideline for statistical validity. 

_**Understand what you’re counting**_ For your count to serve as an accurate basis for estimation, you need to be sure the same assumptions apply to the count that your historical data is based on and to the count that you’re using for your estimate. If you’re counting marketing requirements, be sure that what you counted as a “marketing requirement” for your historical data is similar to what you count as a “marketing requirement” for your estimate. If your historical data indicates that a past project team in your company delivered 7 user stories per week, be sure your assumptions about team size, programmer experience, development technology, and other factors are similar in the project you’re estimating. 

_**Find something you can count with minimal effort**_ All other things being equal, you’d rather count something that requires the least effort. In the story at the beginning of the chapter, the count of people in the room was readily available from the ticket scanner. If you had to go around to each table and count people manually, you might decide it wasn’t worth the effort. 

One of the insights from the Cocomo II project is that a size estimation measure called Object Points is about as strongly correlated with effort as the Function Points measure is but requires only about half as much effort to count. Thus, Object Points are seen as an effective alternative to Function Points for estimation in the wide part of the Cone of Uncertainty (Boehm et al 2000). 

## **7.3 Use Computation to Convert Counts to Estimates** 

If you collect historical data related to counts, you can convert the counts to something useful, such as estimated effort. Table 7-1 lists examples of quantities you might count and the data you would need to compute an estimate from the count. 

**Table 7-1 Examples of Quantities That Can Be Counted for Estimation Purposes** 

|**Table 7-1**<br>**Examples of**|**Quantities That Can Be Counted for Estimation Purposes**|**Quantities That Can Be Counted for Estimation Purposes**|
|---|---|---|
|**Quantity to Count**|**Historical Data Needed to Convert the Count to an Estimate**||
|Marketing requirements|■|Average effort hours per requirement for development|
||■|Average effort hours per requirement for independent|
|||testing|
||■|Average effort hours per requirement for documentation|
||■|Average effort hours per requirement to create engineer-|
|||ing requirements from marketing requirements|



**Chapter 7 Count, Compute, Judge 87** 

> **Table 7-1 Examples of Quantities That Can Be Counted for Estimation Purposes** 

|**Table 7-1**<br>**Examples of Q**|**uantities That Can Be Counted for Estimation Purposes**|**uantities That Can Be Counted for Estimation Purposes**|
|---|---|---|
|**Quantity to Count**|**Historical Data Needed to Convert the Count to an Estimate**||
|Features|■|Average effort hours per feature for development and/or|
|||testing|
|Use cases|■|Average total effort hours per use case|
||■|Average number of use cases that can be delivered in a|
|||particular amount of calendar time|
|Stories|■|Average total effort hours per story|
||■|Average number of stories that can be delivered in a|
|||particular amount of calendar time|
|Engineering requirements|■|Average number of engineering requirements that can|
|||be formally inspected per hour|
||■|Average effort hours per requirement for development/|
|||test/documentation|
|Function Points|■|Average development/test/documentation effort per|
|||Function Point|
||■|Average lines of code in the target language per Function|
|||Point|
|Change requests|■|Average development/test/documentation effort per|
|||change request (depending on variability of the change|
|||requests, the data might be decomposed into average|
|||effort per small, medium, and large change request)|
|Web pages|■|Average effort per Web page for user interface work|
||■|Average whole-project effort per Web page (less reliable,|
|||but can be an interesting data point)|
|Reports|■|Average effort per report for report work|
|Dialog boxes|■|Average effort per dialog for user interface work|
|Database tables|■|Average effort per table for database work|
||■|Average whole-project effort per table (less reliable, but|
|||can be an interesting data point)|
|Classes|■|Average effort hours per class for development|
||■|Average effort hours to formally inspect a class|
||■|Average effort hours per class for testing|
|Defects found|■|Average effort hours per defect to fix|
||■|Average effort hours per defect to regression test|
||■|Average number of defects that can be corrected in|
|||a particular amount of calendar time|
|Configuration settings|■|Average effort per configuration setting|



**88 Part II Fundamental Estimation Techniques** 

**Table 7-1 Examples of Quantities That Can Be Counted for Estimation Purposes** 

|**Table 7-1**<br>**Examples of Q**|**uantities That Can Be Counted for Estimation Purposes**|**uantities That Can Be Counted for Estimation Purposes**|
|---|---|---|
|**Quantity to Count**|**Historical Data Needed to Convert the Count to an Estimate**||
|Lines of code already|■|Average number of defects per line of code|
|written|■|Average lines of code that can be formally inspected|
|||per hour|
||■|Average new lines of code from one release to the next|
|Test cases already written|■|Average amount of release-stage effort per test case|



**Tip #32** Collect historical data that allows you to compute an estimate from a count. 

_**Example of counting defects late in a project**_ Once you have the kind of data described in the table, you can use that data as a more solid basis for creating estimates than expert judgment. If you know that you have 400 open defects, and you know that the 250 defects you’ve fixed so far have averaged 2 hours per defect, you know that you have about 400 x 2 equals 800 hours of work to fix the open defects. 

_**Example of estimation by counting Web pages**_ If your data says that so far your project has taken an average of 40 hours to design, code, and test each Web page with dynamic content, and you have 12 Web pages left, you know that you have something like 12 x 40 equals 480 hours of work left on the remaining Web pages. 

The important point in these examples is that _there is no judgment in these estimates_ . You count, and then you compute. This process helps keep the estimates free from bias that would otherwise degrade their accuracy. For counts that you already have available—such as number of defects—such estimates also require very low effort. 

**Tip #33** Don’t discount the power of simple, coarse estimation models such as average effort per defect, average effort per Web page, average effort per story, and average effort per use case. 

## **7.4 Use Judgment Only as a Last Resort** 

So-called expert judgment is the least accurate means of estimation. Estimates seem to be the most accurate if they can be tied to something concrete. In the story told at the beginning of this chapter, the worst estimate was the one created by the expert who used judgment alone. Tying the estimate to the room occupancy limit was a little better, although it was subject to more error because that approach required a judgment about how full the room was as a percentage of maximum occupancy, which is an opportunity for subjectivity or bias to contaminate the estimate. 

**Chapter 7 Count, Compute, Judge 89** 

Historical data combined with computation is remarkably free from the biases that can undermine more judgment-based estimates. Avoid the temptation to tweak computed estimates to conform to your expert judgment. When I wrote the second edition of _Code Complete_ (McConnell 2004a), I had a team that formally inspected the entire first edition—all 900 pages of it. During our first inspection meeting, our inspection rate averaged 3 minutes per page. Realizing that 3 minutes per page implied 45 hours of inspection meetings, I commented after the first meeting that I thought we were just beginning to gel as a team, and, in my judgment, we would speed up in future meetings. I suggested using a working number of 2 or 2.5 minutes per page instead of 3 minutes to plan future meetings. The project manager responded that, because we had only one meeting’s worth of data, we should use that meeting’s number of 3 minutes per page as a guide for planning the next few meetings. We could adjust our plans later based on different data from later meetings, if we needed to. 

Nine hundred pages later, how many minutes per page do you think we averaged for the entire book? If you guessed 3 minutes per page, you’re right! 

**Tip #34** Avoid using expert judgment to tweak an estimate that has been derived through computation. Such “expert judgment” usually degrades the estimate’s accuracy. 

## **Additional Resources** 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: AddisonWesley, 2000. Boehm provides a brief description of Object Points. 

Lorenz, Mark and Jeff Kidd. _Object-Oriented Software Metrics_ . Upper Saddle River, NJ: PTR Prentice Hall, 1994. Lorenz and Kidd present numerous suggestions of quantities that can be counted in object-oriented programs. 

## Chapter 8 

## **Calibration and Historical Data** 

## **Applicability of Techniques in This Chapter** 

||**Calibration with**|**Calibration with**|**Calibration with**|
|---|---|---|---|
||**Industry-Average Data**|**Organizational Data**|**Project-Specific Data**|
|**What’s estimated**|Size, Effort, Schedule,|Size, Effort, Schedule,|Size, Effort, Schedule,|
||Features|Features|Features|
|**Size of project**|S M L|S M L|S M L|
|**Development stage**|Early–Middle|Early–Middle|Middle–Late|
|**Iterative or sequential**|Both|Both|Both|
|**Accuracy possible**|Low–Medium|Medium–High|High|



Calibration is used to convert counts to estimates—lines of code to effort, user stories to calendar time, requirements to number of test cases, and so on. Estimates always involve some sort of calibration, whether explicit or implicit. Calibration using various kinds of data makes up the second piece of the “count, then compute” approach described in Chapter 7, “Count, Compute, Judge.” 

Your estimates can be calibrated using any of three kinds of data: 

- _Industry data_ , which refers to data from other organizations that develop the same basic kind of software as the software that’s being estimated 

- _Historical data_ , which in this book refers to data from the organization that will conduct the project being estimated 

- _Project data_ , which refers to data generated earlier in the same project that’s being estimated 

Historical data and project data are both tremendously useful and can support creation of highly accurate estimates. Industry data is a temporary backup that can be useful when you don’t have historical data or project data. 

## **8.1 Improved Accuracy and Other Benefits of Historical Data** 

The most important reason to use historical data from your own organization is that it improves estimation accuracy. The use of historical data, or “documented facts,” is negatively correlated with cost and schedule overruns—that is, projects that have 

**91** 

**92** 

**Part II Fundamental Estimation Techniques** 

been estimated using historical data tend not to have overruns (Lederer and Prasad 1992). 

The following sections discuss some of the reasons that historical data improves accuracy. 

## **Accounts for Organizational Influences** 

First and foremost, use of historical data accounts for a raft of organizational influences that affect project outcomes. For very small projects, individual capabilities dictate the project outcome. As project size increases, talented individuals still matter, but their efforts are either supported or undermined by organizational influences. For medium and large projects, organizational characteristics start to matter as much as or more than individual capabilities. 

Here are some of the organizational influences that affect project outcomes: 

- How complex is the software, what is the execution time constraint, what reliability is required, how much documentation is required, how precedented is the application—that is, how does the project stack up against the Cocomo II factors related to the kind of software being developed (as discussed in Chapter 5, “Estimate Influences”)? 

- Can the organization commit to stable requirements, or must the project team deal with volatile requirements throughout the project? 

- Is the project manager free to remove a problem team member from the project, or do the organization’s Human Resources policies make it difficult or impossible to remove a problem employee? 

- Is the team free to concentrate on the current project, or are team members frequently interrupted with calls to support production releases of previous projects? 

- Can the organization add team members to the new project as planned, or does it refuse to pull people off other projects before those projects have been completed? 

- Does the organization support the use of effective design, construction, quality assurance, and testing practices? 

- Does the organization operate in a regulated environment (for example, under FAA or FDA regulations) in which certain practices are dictated? 

- Can the project manager depend on team members staying until the project is complete, or does the organization have high turnover? 

Accounting for each of these influences in an estimate one by one is difficult and error-prone. But historical data adjusts for all these factors, whether you’re aware of the specifics or not. 

**93** 

**Chapter 8 Calibration and Historical Data** 

## **Avoids Subjectivity and Unfounded Optimism** 

One way that subjectivity creeps into estimates is that project managers or estimators look at a new project, compare it with an old project, observe numerous differences between the two projects, and then conclude that the new project will go better than the old one did. They say, “We had a lot of turnover on the last project. That won’t happen this time, so we’ll be more productive. Also, people kept getting called back to support the previous version, and we’ll make sure that that doesn’t happen this time either. We also had a lot of late-breaking requirements from marketing. We’ll do a better job on that, too. Plus we’re working with better technology this time and newer, more effective development methods. With all those improvements, we should be able to be _way_ more productive.” 

It’s easy to identify with the optimism in these lines of reasoning. But the factors listed are controlled more by the organization than by the specific project manager, so most of these factors tend to be difficult to control for one specific project. The other factors tend to be interpreted optimistically, which introduces bias into the estimate. 

With historical data, you use a simplifying assumption that the next project will go about the same as the last project did. This is a reasonable assumption. As estimation guru Lawrence Putnam says, productivity is an organizational attribute that cannot easily be varied from project to project (Putnam and Myers 1992, Putnam and Myers 2003). The same concept shows up in Extreme Programming as “Yesterday’s Weather”: the weather today won’t always be the same as it was yesterday, but it’s more likely to be like yesterday’s weather than like anything else (Beck and Fowler 2001). 

**Tip #35** Use historical data as the basis for your productivity assumptions. Unlike mutual fund disclosures, your organization’s past performance really is your best indicator of future performance. 

## **Reduces Estimation Politics** 

One of the traps in estimation models that include a lot of control knobs is that many of the higher-leverage knobs are related to personnel. Cocomo II, for example, requires you to make assessments of your requirements analysts’ and programmers’ capabilities, along with several less subjective personnel factors related to experience. Cocomo requires the estimator to rate the programmers as 90th percentile, 75th percentile, 55th percentile, 35th percentile, or 15th percentile. (All these percentiles are industrywide.) 

**94** 

**Part II Fundamental Estimation Techniques** 

Suppose a manager takes a Cocomo II estimate into a meeting with an executive and the meeting agenda is to look for fat in the manager’s estimate. It’s easy to imagine the conversation going like this: 

_MANAGER: I know we had a goal of finishing this release in 12 weeks, but my estimates indicate that it will take 16 weeks. Let’s walk through the estimate using this software estimation tool. Here are the assumptions I made. First, I had to calibrate the estimation model. For the “programmer capability” factor, I assumed our programmers are 35th percentile—_ 

_EXECUTIVE: What?! No one on our staff is below average! You need to have more confidence in your staff! What kind of manager are you? Well, maybe we’ve got a few people who aren’t quite as good as the rest, but the overall team can’t be that bad. Let’s assume they’re at least average, right? Can you enter that into the software?_ 

_MANAGER: Well, OK. Now, the next factor is the capability of the requirements engineers. We’ve never focused on recruiting good requirements engineers or developing those skills in our engineers, so I assumed they were 15th percentile—_ 

_EXECUTIVE: Hold on! 15th percentile? These people are very talented, even if they haven’t had formal training in requirements engineering. They’ve got to be at least average. Can we change that factor to average?_ 

_MANAGER: I can’t justify making them average. We really don’t even have any staff we can call requirements specialists._ 

_EXECUTIVE: Fine. Let’s compromise and change the factor to 35th percentile then._ 

_MANAGER: OK (sigh)._ 

In this interaction, if the manager was using the Cocomo II adjustment factors, his estimate of effort required was just reduced by 23%. If the executive had succeeded in talking the manager into rating the requirements engineers as average rather than 35th percentile, the estimate would be reduced by 39%. In either case, a single conversation would result in a significant difference. 

A manager who calibrates the estimate with historical data sidesteps the whole issue of whether the programmers are above average or below average. Productivity is whatever the data says it is. It’s difficult for a non-technical stakeholder to argue with a statement like this one: “We’ve averaged 300 to 450 delivered lines of code per staff month, so we’ve calibrated the model with an assumption of 400 lines of code per staff month, which we believe is a little on the optimistic side but within a prudent planning range.” 

**95** 

**Chapter 8 Calibration and Historical Data** 

Clearly, half the programmers in the industry are below average, but I rarely meet project managers or executives who believe _their_ programmers are the people who are below average. 

- **Tip #36** Use historical data to help avoid politically charged estimation discussions arising from assumptions like “My team is below average.” 

## **8.2 Data to Collect** 

If you’re not already collecting historical data, you can start with a very small set of data: 

- Size (lines of code or something else you can count after the software has been released) 

- Effort (staff months) 

- Time (calendar months) 

- Defects (classified by severity) 

This small amount of data, even if you collect it only at the completion of two or three projects, will give you enough data to calibrate any of several commercial software estimation tools. It will also allow you to compute simple ratios such as lines of code per staff month. 

In addition to the fact that these four kinds of data are sufficient to calibrate estimation models, most experts recommend starting small so that you understand what you’re collecting (Pietrasanta 1990, NASA SEL 1995). If you don’t start small, you can end up with data that’s defined inconsistently across projects, which makes the data meaningless. Depending on how you define these four kinds of data, the numbers you come up with for each can vary by a factor of 2 or more. 

## **Issues Related to Size Measures** 

You can measure the size of completed projects in Function Points, stories, Web pages, database tables, and numerous other ways, but most organizations eventually settle on capturing size-related historical data in terms of lines of code. (More details on the strengths and weaknesses of using LOC measurements are discussed in Section 18.1, “Challenges with Estimating Size.”) 

For size in lines of code, you’ll need to define several issues, including the following: 

- Do you count all code or only code that’s included in the released software? (For example, do you count scaffolding code, mock object code, unit test code, and system test code?) 

**96** 

**Part II Fundamental Estimation Techniques** 

- How do you count code that’s reused from previous versions? 

- How do you count open source code or third-party library code? 

- Do you count blank lines and comments, or only non-blank, non-comment source lines? 

- Do you count class interfaces? 

- Do you count data declarations? 

- How do you count lines that make up one logical line of code but that are broken across multiple lines for the sake of readability? 

There isn’t any industry standard on this topic, and it doesn’t particularly matter how you answer these questions.[1] What does matter is that you answer these questions consistently across projects so that whatever assumptions are baked into the data you collected is _consciously_ projected forward in your estimates. 

## **Issues Related to Effort Measures** 

Similar cautions apply to collecting effort data: 

- Do you count time in hours, days, or some other unit? 

- How many hours per day do you count? Standard 8 hours or actual hours applied to the specific project? 

- Do you count unpaid overtime? 

- Do you count holidays, vacation, and training? 

- Do you make allowances for all-company meetings? 

- What kinds of effort do you count? Testing? First-level management? Documentation? Requirements? Design? Research? 

- How do you count time that’s divided across multiple projects? 

- How do you count time spent supporting previous releases of the same software? 

- How do you count time spent supporting sales calls, trade shows, and so on? 

- How do you count travel time? 

- How do you count fuzzy front-end time—the time spent firming up the software concept before the project is fully defined? 

> 1 The closest the software industry has to a standard definition is a non-blank, non-comment, deliverable source statement that includes interfaces and data declarations. That definition still leaves a few of the questions unanswered, such as how to count code reused from previous projects. 

**Chapter 8 Calibration and Historical Data 97** 

Again, the main goal here is to define the data you’re collecting well enough so that you know what you’re estimating. If your data from past projects includes a high percentage of unpaid overtime and you use that historical data to estimate a future project, guess what? You’ve just calibrated a high percentage of overtime into your future project. 

## **Issues Related to Calendar Time Measures** 

It’s surprisingly difficult in many organizations to determine how long a particular project lasted. 

- When does the project start? Does it start when it gets formal budget approval? Does it start when initial discussions about the project begin? Does it start when it’s fully staffed? Capers Jones reports that fewer than 1% of projects have a clearly defined starting point (Jones 1997). 

- When does the project end? Does it end when the software is released to the customer? When the final release candidate is delivered to testing? What if most programmers have rolled off the project a month before the official release? Jones reports that 15% of projects have ambiguous end times (Jones 1997). 

In this area, it’s very helpful if the organization has well-defined project launch and project completion milestones. The main goal, again, is simply to understand the data you’re collecting. 

## **Issues Related to Defect Measures** 

Finally, defect measures also vary by a factor of 2 or 3 depending on what’s counted as a defect: 

- Do you count all change requests as defects, or only those that are ultimately classified as defects rather than feature requests? 

- Do you count multiple reports of the same defect as a single defect or as multiple defects? 

- Do you count defects that are detected by developers, or only those detected by testers? 

- Do you count requirements and design defects that are found prior to the beginning of system testing? 

- Do you count coding defects that are found prior to the beginning of alpha or beta testing? 

- Do you count defects reported by users after the software has been released? 

**98 Part II Fundamental Estimation Techniques** 

## **Tip #37** 

In collecting historical data to use for estimation, start small, be sure you understand what you’re collecting, and collect the data consistently. 

## **Other Data Collection Issues** 

Historical data tends to be easiest to collect if it’s collected while the project is underway. It’s difficult to go back six months after a project has been completed and reconstruct the “fuzzy front end” of the project to determine when the project began. It’s also easy to forget how much overtime people worked at the end of the project. 

## **Tip #38** Collect a project’s historical data _as soon as possible_ after the end of the project. 

While it’s useful to collect data at the end of a project, it’s even more useful to collect snapshots of a project as it’s underway. Collecting data on size, effort, and defects every 1 to 2 weeks can provide valuable insight into your project’s dynamics. 

For example, collecting a snapshot of reported defects can help you predict the rate at which defects will be discovered and will need to be fixed on future projects. Collecting data on effort over time can help you understand your organization’s ability to mobilize staff to support a project. If one project staffs up more slowly than desired, it might be a fluke. If your historical data says that the last three projects have each staffed up at about the same rate, that suggests that you’re facing an organizational influence that can’t easily be changed on the next project. 

**Tip #39** As a project is underway, collect historical data on a periodic basis so that you can build a data-based profile of how your projects run. 

## **8.3 How to Calibrate** 

The ultimate goal of collecting data is to convert the data to a model that you can use for estimation. Here are some examples of models you could create: 

- Our developers average _X_ lines of code per staff month. 

- A 3-person team can deliver _X_ stories per calendar month. 

- Our team is averaging _X_ staff hours per use case to create the use case, and _Y_ hours per use case to construct and deliver the use case. 

- Our testers create test cases at a rate of _X_ hours per test case. 

- In our environment, we average _X_ lines of code per function point in C# and _Y_ lines of code per function point in Python. 

- On this project so far, defect correction work has averaged _X_ hours per defect. 

**99** 

**Chapter 8 Calibration and Historical Data** 

These are just examples to illustrate the kinds of models you can build using historical data. Table 7-1 in the previous chapter listed many more examples. 

One characteristic these models have in common is that they are all linear. The math works the same whether you’re building a 10,000-LOC system or a 1,000,000-LOC system. But because of software’s diseconomies of scale, some models will need to be adjusted for different size ranges.You could try to handle the size differentiation informally. Table 8-1 shows one example of how you might do that. 

**Table 8-1 Example of Accounting for Diseconomies of Scale Informally—For Purposes of Illustration Only** 

|**Team Size**|**Average Stories Delivered per Calendar Month**|
|---|---|
|1|5|
|2–3|12|
|4–5|22|
|6–7|31|
|8|No data for projects of this size|



This approach is valid when you have small variations in project size. To account for larger variations in project size, see Section 5.1, “Project Size,” and Section 5.6, “Diseconomies of Scale Revisited.” 

## **8.4 Using Project Data to Refine Your Estimates** 

Earlier in this chapter, I pointed out that historical data is useful because it accounts for organizational influences—both recognized and unrecognized. The same idea applies to the use of historical data within a specific project (Gilb 1988, Cohn 2006). Individual projects have dynamics that will vary somewhat from the dynamics of their surrounding organizations. Using data from the project itself will account for the influences that are unique to that specific project. The sooner on a project you can begin basing your estimates on data from the project itself, the sooner your estimates will become truly accurate. 

**Tip #40** Use data from your current project (project data) to create highly accurate estimates for the remainder of the project. 

Even if you don’t have historical data from past projects, you can collect data from your current project and use that as a basis for estimating the remainder of your project. Your goal should be to switch from using organizational data or industryaverage data to project data as soon as you can. The more iterative your project is, the sooner you’ll be able to do this. 

**100 Part II Fundamental Estimation Techniques** 

Collecting and using data from your own project will be discussed in more detail in Section 16.4, “Estimate Refinement.” Section 12.3, “Story Points,” presents a specific example of using project data to refine your estimates. 

## **8.5 Calibration with Industry Average Data** 

If you don’t have your own historical data, you have little choice but to use industryaverage data, which is adequate but no better. As Table 5-2 illustrated, the productivity rates for different organizations within the same industries typically vary by a factor of 10. If you use the average productivity for your industry, you won’t be accounting for the possibility that your organization might be at the top end of the productivity range or at the bottom. 

Figure 8-1 shows an example of an estimate created using industry-average data. Each point in the graph represents a possible project outcome created using a statistical technique known as a Monte Carlo simulation. The solid black lines represent the median effort and schedule found during the simulation. The dashed black lines represent the 25th and 75th percentiles for effort and schedule. 

## **Schedule and Effort Simulation** 

**==> picture [338 x 221] intentionally omitted <==**

**----- Start of picture text -----**<br>
250<br>225<br>200<br>175<br>150<br>Effort<br>(staff 125<br>months)<br>100<br>75<br>50<br>25<br>0<br>10 12 14 16 18 20 22 24 26 28 30 32<br>Schedule (months)<br>**----- End of picture text -----**<br>


_Source: Estimated prepared using Construx Estimate, available at_ www.construx.com/estimate. 

**Figure 8-1** An example of estimated outcomes for an estimate calibrated using industryaverage data. Total variation in the effort estimates is about a factor of 10 (from about 25 staff months to about 250 staff months). 

**Chapter 8 Calibration and Historical Data 101** 

Figure 8-2 shows an example of a comparable estimate calibrated using historical data from one of my clients. 

## **Schedule and Effort Simulation** 

**==> picture [344 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
120<br>110<br>100<br>90<br>80<br>Effort<br>(staff 70<br>months)<br>60<br>50<br>40<br>30<br>20<br>14 15 16 17 18 19 20 21 22<br>Schedule (months)<br>**----- End of picture text -----**<br>


**Figure 8-2** An estimate calibrated using historical productivity data. The effort estimates vary by only about a factor of 4 (from about 30 staff months to about 120 staff months). 

The sizes and nominal productivity rates of the two projects are identical, but the amount of variability in the two estimates is dramatically different. Because the industry-average estimate must account for factor-of-10 differences in productivity, the standard deviation on the effort estimate created using industry-average data is about 100%! If you wanted to give your boss an estimate that ranged from 25% confident to 75% confident using industry-average data, in this case you’d need to quote a range of 50 to 160 staff months—a factor of 3 difference! 

If you could use historical data instead of industry-average data, you could quote a range of 70 to 95 staff months—a factor of only 1.4 from the top end of the range to the bottom. The standard deviation in the estimate created using historical data is only about 25%. 

A review of studies on estimation accuracy found that in studies in which estimation models were not calibrated to the estimation environment, expert estimates were more accurate than the models. But the studies that used models calibrated with historical data found that the models were as good as or better than expert estimates (Jørgensen 2002). 

**102 Part II Fundamental Estimation Techniques** 

**Tip #41** Use project data or historical data rather than industry-average data to calibrate your estimates whenever possible. In addition to making your estimates more accurate, historical data will reduce variability in your estimate arising from uncertainty in the productivity assumptions. 

## **8.6 Summary** 

If you haven’t previously been exposed to the power of historical data, you can be excused for not currently having any data to use for your estimates. But now that you know how valuable historical data is, you don’t have any excuse not to collect it. Be sure that when you reread this chapter next year you’re not still saying, “I wish I had some historical data!” 

**Tip #42** If you don’t currently have historical data, begin collecting it as soon as possible. 

## **Additional Resources** 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: AddisonWesley, 2000. Appendix E of Boehm’s book contains a checklist that’s useful for precisely defining what constitutes a “line of code.” 

Gilb, Tom. _Principles of Software Engineering Management_ . Wokingham, England: Addison-Wesley, 1988. Section 7.14 of Gilb’s book describes using project-specific data to refine estimates. The description of evolutionary delivery throughout the book is based on the expectation that projects will build feedback loops allowing them to be estimated, planned, and managed in a way that allows the projects to be self-correcting. 

Grady, Robert B. and Deborah L. Caswell. _Software Metrics: Establishing a CompanyWide Program_ . Englewood Cliffs, NJ: Prentice Hall, 1987. This book and the following one describe Grady’s experiences setting up a measurement program at HewlettPackard. The books contain many hard-won insights into the pitfalls of setting up a measurement program plus some interesting examples of the useful data you can ultimately obtain. 

Grady, Robert B. _Practical Software Metrics for Project Management and Process Improvement_ . Englewood Cliffs, NJ: PTR Prentice Hall, 1992. 

Jones, Capers. _Applied Software Measurement: Assuring Productivity and Quality, 2d Ed._ New York, NY: McGraw-Hill, 1997. Chapter 3 of this book presents an excellent discussion of the sources of errors in size, effort, and quality measurements. 

**103** 

**Chapter 8 Calibration and Historical Data** 

Putnam, Lawrence H. and Ware Myers. _Five Core Metrics_ . New York, NY: Dorset House, 2003. This book presents a compelling argument for collecting data on the five core metrics of size, productivity, time, effort, and reliability. 

Software Engineering Institute’s _Software Engineering Measurement and Analysis (SEMA)_ Web site: _www.sei.cmu.edu/sema/_ . This comprehensive Web site helps organizations create data collection (measurement) practices and use the data they collect. 

## Chapter 9 **Individual Expert Judgment** 

## **Applicability of Techniques in This Chapter** 

||**Use of**|||**Comparing**|
|---|---|---|---|---|
||**Structured**|**Use of Estimation**|**Estimating Task**|**Task Estimates**|
||**Process**|**Checklist**|**Effort in Ranges**|**to Actuals**|
|**What’s estimated**|Effort,|Effort, Schedule,|Size, Effort,|Size, Effort,|
||Schedule,|Features|Schedule,|Schedule,|
||Features||Features|Features|
|**Size of project**|S M L|S M L|S M L|S M L|
|**Development stage**|Early–Late|Early–Late|Early–Late|Middle–Late|
|**Iterative or sequential**|Both|Both|Both|Both|
|**Accuracy possible**|High|High|High|N/A|



Individual expert judgment is by far the most common estimation approach used in practice (Jørgensen 2002). Hihn and Habib-agahi found that 83% of estimators used “informal analogy” as their primary estimation technique (Hihn and Habib-agahi 1991). A New Zealand survey found that 86% of software organizations used “expert estimation” (Paynter 1996). Barbara Kitchenham and her colleagues found that 72% of project estimates were based on “expert opinion” (Kitchenham et al. 2002). 

Expert-judgment estimates of individual tasks form the foundation for bottom-up estimation, but not all expert judgments are equal. Indeed, as Chapter 7, “Count, Compute, Judge,” indicated, judgment is the most hazardous kind of estimation. 

When discussing “expert judgment,” we need first to ask “expert in what?” Being expert in the technology or development practices that will be employed does not make someone an expert in estimation. Magne Jørgensen reports that increased experience in the activity being estimated does not lead to increased accuracy in the estimates for the activity (Jørgensen 2002). Other studies have found that “experts” tend to use simple estimation strategies, even when their level of expertise in the subject being estimated is high (Josephs and Hahn 1995, Todd and Benbasat 2000). 

This chapter describes how to ensure that, when you use expert judgment, the judgment is effective. The discussion in this chapter is closely related to the discussion in 

**105** 

**106 Part II Fundamental Estimation Techniques** 

Chapter 10, “Decomposition and Recomposition,” which explains how to combine the individual estimates accurately. 

## **9.1 Structured Expert Judgment** 

Individual expert judgment does not have to be informal or intuitive. Researchers have found significant accuracy differences between “intuitive expert judgment,” which tends to be inaccurate (Lederer and Prasad 1992) and “structured expert judgment,” which can produce estimates that are about as accurate as model-based estimates (Jørgensen 2002). 

## **Who Creates the Estimates?** 

For the estimation of specific tasks—such as the time needed to code and debug a particular feature or to create a specific set of test cases—the people who will actually do the work will create the most accurate estimates. Estimates prepared by people who aren’t doing the work are less accurate (Lederer and Prasad 1992). In addition, separate estimators are more likely to underestimate than estimator-developers are (Lederer and Prasad 1992). 

**Tip #43** To create the task-level estimates, have the people who will actually do the work create the estimates. 

This guideline is for task-level estimates. If your project is still in the wide part of the Cone of Uncertainty (that is, specific tasks haven’t yet been identified or assigned to individuals), the estimate should be created by an expert estimator or by the most expert development, quality assurance, and documentation staff available. 

## **Granularity** 

One of the best ways to improve the accuracy of task-level estimates is to separate large tasks into smaller tasks. When creating estimates, developers, testers, and managers tend to concentrate on the tasks that they understand and deemphasize tasks that are unfamiliar to them. The common result is that a 1-line entry on the schedule, such as “data conversion,” which was supposed to take 2 weeks, instead takes 2 months because no one investigated what was actually involved. 

When estimating at the task level, decompose estimates into tasks that will require no more than about 2 days of effort. Tasks larger than that will contain too many places that unexpected work can hide. Ending up with estimates that are at the 1/4 day, 1/2 day, or full day of granularity is appropriate. 

**Chapter 9 Individual Expert Judgment 107** 

## **Use of Ranges** 

If you ask a developer to estimate a set of features, the developer will often come back with an estimate that looks like Table 9-1. 

**Table 9-1 Example of Developer Single-Point Estimates** 

|**Feature**||**Estimated Days to Complete**|
|---|---|---|
|Feature|1|1.5|
|Feature|2|1.5|
|Feature|3|2.0|
|Feature|4|0.5|
|Feature|5|0.5|
|Feature|6|0.25|
|Feature|7|2.0|
|Feature|8|1.0|
|Feature|9|0.75|
|Feature|10|1.25|
|**TOTAL**||**11.25**|



If you then ask the same developer to reestimate each feature’s best case and worst case, the developer will often return with estimates similar to those in Table 9-2. 

> **Table 9-2 Example of Individual Estimation Using Best Case and Worst Case** 

|**Table 9-2**<br>**Example of Indiv**|**idual Estimation Using Best Case and Worst Case**|
|---|---|
|**Feature**|**Estimated Days to Complete**|
||**Best Case**<br>**Worst Case**|
|Feature 1<br>Feature 2<br>Feature 3<br>Feature 4<br>Feature 5<br>Feature 6<br>Feature 7<br>Feature 8<br>Feature 9<br>Feature 10<br>**TOTAL**|1.25<br>2.0<br>1.5<br>2.5<br>2.0<br>3.0<br>0.75<br>2.0<br>0.5<br>1.25<br>0.25<br>0.5<br>1.5<br>2.5<br>1.0<br>1.5<br>0.5<br>1.0<br>1.25<br>2.0<br>10.51<br>18.25|



> 1 Some statistical anomalies arise when you simply total the Best Case estimates and the Worst Case estimates. Chapter 10 discusses these in detail. 

**108 Part II Fundamental Estimation Techniques** 

When you compare the original single-point estimates to the Best Case and Worst Case estimates, you see that the 11.25 total of the single-point estimates is much closer to the Best Case estimate of 10.5 days than to the Worst Case total of 18.25 days. 

If you examine the estimate for Feature 4, you’ll also notice that both the Best Case and the Worst Case estimates are higher than the original single-point estimate. Thinking through the worst case result sometimes exposes additional work that must be done even in the best case, which can raise the nominal estimate. In thinking through the worst case, I like to ask developers how long the task would take if _everything_ went wrong. People’s worst cases are often optimistic worst cases rather than _true_ worst cases. 

If you’re a manager or a lead, have your developers create a set of single-point estimates. Hide those estimates from them. Then have the developers create a set of Best Case and Worst Case estimates. Have them compare their Best Case and Worst Case estimates to their original single-point estimates. This is often an eye-opening experience. 

This exercise yields two benefits. First, it raises awareness that single-point estimates tend to be akin to Best Case estimates. Second, going through the process of writing down Best Case and Worst Case estimates a few times begins to engrain the habit of thinking through the worst case outcome when estimating. Once you get into the habit of considering both best case and worst case outcomes, you’ll get better at factoring the full range of possible outcomes into your single-point task estimates, regardless of whether you actually write down the best and worst cases. 

**Tip #44** Create both Best Case and Worst Case estimates to stimulate thinking about the full range of possible outcomes. 

## **Formulas** 

Creating the Best Case and the Worst Case estimates is just the first step. You’re still left with the question of which estimate to use. Or maybe you should use the mathematical midpoint instead? The answer is none of the above. In many cases, the Worst Case is much worse than what’s called the Expected Case. Taking the midpoints of the ranges could result in an unnecessarily high estimate. 

A technique called the Program Evaluation and Review Technique (PERT) allows you to compute an Expected Case that might not be exactly in the middle of the range from best case to worst case (Putnam and Myers 1992, Stutzke 2005). To use PERT, you add an additional Most Likely Case to your set of cases. You can estimate the 

**Chapter 9 Individual Expert Judgment 109** 

Most Likely Case using expert judgment. You then calculate the Expected Case using this formula: 

**==> picture [43 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>#1<br>**----- End of picture text -----**<br>


Expected Case = [BestCase + (4 × MostLikelyCase) + WorstCase] / 6 

This formula accounts for the full width of the range as well as the position of the Most Likely Case within the range. Table 9-3 shows the estimates from Table 9-2 with the addition of Most Likely Case and Expected Case. As you can see from the table, the overall estimate of 13.62 is closer to the lower end of the range than the midpoint of 14.4 would have been. 

**Table 9-3 Example of Individual Estimation Using Best Case, Worst Case, and Most Likely Case** 

||||**Estimated Days**|**to Complete**||
|---|---|---|---|---|---|
|**Feature**||**Best Case**|**Most Likely Case**|**Worst Case**|**Expected Case**|
|Feature|1|1.25|1.5|2.0|**1.54**|
|Feature|2|1.5|1.75|2.5|**1.83**|
|Feature|3|2.0|2.25|3.0|**2.33**|
|Feature|4|0.75|1|2.0|**1.13**|
|Feature|5|0.5|0.75|1.25|**0.79**|
|Feature|6|0.25|0.5|0.5|**0.46**|
|Feature|7|1.5|2|2.5|**2.00**|
|Feature|8|1.0|1.25|1.5|**1.25**|
|Feature|9|0.5|0.75|1.0|**0.75**|
|Feature|10|1.25|1.5|2.0|**1.54**|
|**TOTAL**||**10.5**|**13.25**|**18.25**|**13.62**|



As discussed in Chapter 4, “Where Does Estimation Error Come From?” people’s “most likely” estimates tend to be optimistic, which can yield optimistic overall estimates when using this approach. Some estimation experts suggest altering the basic PERT formula to account for a downward bias in the estimates (Stutzke 2005). Here’s the altered formula: 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>Expected Case = [BestCase + (3 × MostLikelyCase) + (2 × WorstCase)] / 6<br>#2<br>**----- End of picture text -----**<br>


This is a reasonable short-term solution to the problem. The long-term solution to this problem is to work with people to make their Most Likely Case estimates more accurate. 

**110 Part II Fundamental Estimation Techniques** 

## **Checklists** 

Even experts occasionally forget to consider everything they should. Studies of forecasting in a variety of disciplines have found that simple checklists help improve accuracy by reminding people of considerations they might otherwise forget (Park 1996, Harvey 2001, Jørgensen 2002). Table 9-4 presents a checklist you might use to improve the accuracy of your estimates. 

## **Table 9-4 Checklist for Individual Estimates** 

1. Is what’s being estimated clearly defined? 

2. Does the estimate include all the _kinds of work_ needed to complete the task? 

3. Does the estimate include all the _functionality areas_ needed to complete the task? 

4. Is the estimate broken down into enough detail to expose hidden work? 

5. Did you look at documented facts (written notes) from past work rather than estimating purely from memory? 

6. Is the estimate approved by the person who will actually do the work? 

7. Is the productivity assumed in the estimate similar to what has been achieved on similar assignments? 

8. Does the estimate include a Best Case, Worst Case, and Most Likely Case? 

9. Is the Worst Case really the worst case? Does it need to be made even worse? 

10. Is the Expected Case computed appropriately from the other cases? 

11. Have the assumptions in the estimate been documented? 

12. Has the situation changed since the estimate was prepared? 

To avoid omitting work from your estimates, you might also review the lists of overlooked activities in Section 4.5, “Omitted Activities.” 

**Tip #45** Use an estimation checklist to improve your individual estimates. Develop and maintain your own personal checklist to improve your estimation accuracy. 

## **9.2 Compare Estimates to Actuals** 

Prying yourself loose from single-point/Best Case estimates is half the battle. The other half is comparing your actual results to your estimated results so that you can refine your personal estimating abilities. 

Keep a list of your estimates, and fill in your actual results when you complete them. Then compute the Magnitude of Relative Error (MRE) of your estimates (Conte, Dunsmore, and Shen 1986). MRE is computed using this formula: 

**Equation #3** 

MRE = AbsoluteValue × [(ActualResult − EstimatedResult) / ActualResult] 

**Chapter 9 Individual Expert Judgment 111** 

Table 9-5 shows how the MRE calculations would work out for the Best Case and Worst Case estimates presented earlier. 

**Table 9-5 Table 9-5 Example of Spreadsheet for Tracking Accuracy of Individual Estimates** 

|**Table 9-5**<br>**Ta**<br>**Estimates**|**ble 9-5 Example of Spreadsheet for Tracking Accuracy of Individual**|
|---|---|
|**Feature**|**Estimated Days to Complete**|
||**Actual**<br>**Outcome**<br>**MRE**<br>**In Range from Best**<br>**Case to Worst Case?**<br>**Best**<br>**Case**<br>**Worst**<br>**Case**<br>**Expected**<br>**Case**|
|Feature 1<br>Feature 2<br>Feature 3<br>Feature 4<br>Feature 5<br>Feature 6<br>Feature 7<br>Feature 8<br>Feature 9<br>Feature 10<br>**TOTAL**<br>**Average**|1.25<br>2<br>1.54<br>2<br>23%<br>Yes<br>1.5<br>2.5<br>1.83<br>2.5<br>27%<br>Yes<br>2<br>3<br>2.33<br>1.25<br>87%<br>No<br>0.75<br>2<br>1.13<br>1.5<br>25%<br>Yes<br>0.5<br>1.25<br>0.79<br>1<br>21%<br>Yes<br>0.25<br>0.5<br>0.46<br>0.5<br>8%<br>Yes<br>1.5<br>2.5<br>2.00<br>3<br>33%<br>No<br>1<br>1.5<br>1.25<br>1.5<br>17%<br>Yes<br>0.5<br>1<br>0.75<br>1<br>25%<br>Yes<br>1.25<br>2<br>1.54<br>2<br>23%<br>Yes<br>**10.50**<br>**18.25**<br>**13.625**<br>**16.25**<br>**80% Yes**<br>**29%**|



In this spreadsheet, the MRE is calculated for each estimate. The average MRE, shown in the bottom row, is 29% for the set of estimates. You can use this average MRE to measure the accuracy of your estimates. As your estimates improve, you should see the MRE decline. The right-most column shows how many estimates are within the best case/worst case range. You should also see the percentage of estimates that fall within the range increase over time. 

**Tip #46** Compare actual performance to estimated performance so that you can improve your individual estimates over time. 

When you compare your actual performance to your estimates, you should try to understand what went right, what went wrong, what you overlooked, and how to avoid making those mistakes in the future. 

Another practice that sets up a feedback loop and encourages accurate estimates is a public estimation review. I’ve worked with companies that have their developers report on their actual results versus their estimates at a Monday morning standup meeting. This reinforces the idea that accurate estimates are an organizational priority. 

**112 Part II Fundamental Estimation Techniques** 

Regardless of how you do it, the key principle is to set up a feedback loop based on actual results so that your estimates improve over time. To be effective, the feedback should be as timely as possible; delay reduces effectiveness of the feedback loop (Jørgensen 2002). 

## **Additional Resources** 

Jørgensen, M. “A Review of Studies on Expert Estimation of Software Development Effort.” 2002. This paper presents a comprehensive review of the research on expert estimation approaches. The author draws numerous conclusions from the common research threads and presents 12 tips for achieving accurate expert estimates. 

Humphrey, Watts S. _A Discipline for Software Engineering_ . Reading, MA: AddisonWesley, 1995. Humphrey lays out a detailed methodology by which developers can collect personal productivity data, compare their planned results to their actual results, and improve over time. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ . Upper Saddle River, NJ: Addison-Wesley, 2005. Chapter 5 of Stutzke’s book discusses judgment-based estimation techniques and provides background on some of the math described in this chapter. 

Chapter 10 

## **Decomposition and Recomposition** 

## **Applicability of Techniques in This Chapter** 

|||**Decomposition by**|**Computing Best and**|
|---|---|---|---|
||**Decomposition by**|**Work Breakdown**|**Worst Cases from**|
||**Feature or Task**|**Structure (WBS)**|**Standard Deviation**|
|**What’s estimated**|Size, Effort, Features|Effort|Effort, Schedule|
|**Size of project**|S M L|- M L|S M L|
|**Development stage**|Early–Late (small projects);|Early–Middle|Early–Late (small projects);|
||Middle–Late (medium||Middle–Late (medium|
||and large projects)||and large projects)|
|**Iterative or sequential**|Both|Both|Both|
|**Accuracy possible**|Medium–High|Medium|Medium|



Decomposition is the practice of separating an estimate into multiple pieces, estimating each piece individually, and then recombining the individual estimates into an aggregate estimate. This estimation approach is also known as “bottom up,” “micro estimation,” “module build up,” “by engineering procedure,” and by many other names (Tockey 2005). 

Decomposition is a cornerstone estimation practice—as long as you watch out for a few pitfalls. This chapter discusses the basic practice in more detail and explains how to avoid such pitfalls. 

## **10.1 Calculating an Accurate Overall Expected Case** 

Scene: The weekly team meeting... 

_YOU: We need to create an estimate for a new project. I want to emphasize how important accurate estimation is to this group, and so I’m betting a pizza lunch that I can create a more accurate estimate for this project than you can. If you win, I’ll buy the pizza. If I win, you’ll buy. Any takers?_ 

_TEAM: You’re on!_ 

_YOU: OK, let’s get started._ 

**113** 

**114 Part II Fundamental Estimation Techniques** 

You look up information about a similar past project, and you find that that project took 18 staff weeks. You estimate that this project is about 20 percent larger than the past project, so you create a total estimate of 22 staff weeks. 

Meanwhile, your team has created a more detailed, feature-by-feature estimate. They come back with the estimate shown in Table 10-1. 

**Table 10-1 Example of Estimation by Decomposition** 

|**Feature**||**Estimated Staff Weeks to Complete**|
|---|---|---|
|Feature|1|1.5|
|Feature|2|4|
|Feature|3|3|
|Feature|4|1|
|Feature|5|4|
|Feature|6|6|
|Feature|7|2|
|Feature|8|1|
|Feature|9|3|
|Feature|10|1.5|
|**TOTAL**||**27**|



_YOU: 27 weeks? Wow, I think your estimate is high, but I guess we’ll find out._ 

A few weeks later… 

_YOU: Now that the project is done, we know that it took a total of 29 staff weeks. It looks like your estimate of 27 staff weeks was optimistic by 2 weeks, which is an error of 7%. My estimate of 22 staff weeks was off by 7 staff weeks, about 24%. It looks like you win, so I’m buying the pizza._ 

_By the way, I want to see which of you good estimators cost me the pizza. Let’s take a look at which detailed estimates were the most accurate._ 

You take a few minutes to compute the magnitude of relative error of each individual estimate and write the results on the whiteboard. Table 10-2 shows the results. 

> **Table 10-2 Example Results of Estimation by Decomposition** 

|||**Estimated Staff**|||**Magnitude of**|
|---|---|---|---|---|---|
|**Feature**||**Weeks to Complete**|**Actual Effort**|**Raw Error**|**Relative Error**|
|Feature|1|1.5|3.0|–1.5|50%|
|Feature|2|4.5|2.5|2.0|80%|
|Feature|3|3|1.5|1.5|100%|
|Feature|4|1|2.5|–1.5|60%|



**Chapter 10 Decomposition and Recomposition 115** 

> **Table 10-2 Example Results of Estimation by Decomposition** 

|**Table 10-2**<br>**Ex**|**ample Results of Estim**|**ation by Decom**|**position**||
|---|---|---|---|---|
||**Estimated Staff**|||**Magnitude of**|
|**Feature**|**Weeks to Complete**|**Actual Effort**|**Raw Error**|**Relative Error**|
|Feature 5|4|4.5|–0.5|11%|
|Feature 6|6|4.5|1.5|33%|
|Feature 7|2|3.0|–1.0|33%|
|Feature 8|1|1.5|–0.5|33%|
|Feature 9|3|2.5|0.5|20%|
|Feature 10|1.5|3.5|–2.0|57%|
|**TOTAL**|**27**|**29**|**–2**|**-**|
|**Average**|**-**|**-**|**–7%**|**46%**|



_TEAM: Wow, that’s interesting. Most of our individual estimates weren’t any more accurate than yours. Our estimates were nearly all wrong by 30% to 50% or more. Our average error was 46%—which is way higher than your error. But our overall error was still only 7% and yours was 24%._ 

_But the joke is on you. Even though our estimates were worse than yours, you’re still buying the pizza!_ 

Somehow the team’s estimate was more accurate than your estimate even though their individual feature estimates were worse. How is that possible? 

## **The Law of Large Numbers** 

The team’s estimate benefited from a statistical property called the Law of Large Numbers. The gist of this law is that if you create one big estimate, the estimate’s error tendency will be completely on the high side or completely on the low side. But if you create several smaller estimates, some of the estimation errors will be on the high side, and some will be on the low side. The errors will tend to cancel each other out to some degree. Your team underestimated in some cases, but it also overestimated in some cases, so the error in the aggregate estimate is only 7%. In your estimate, all 24% of the error was on the same side. 

This approach should work in theory, and research says that it also works in practice. Lederer and Prasad found that summing task durations was negatively correlated with cost and schedule overruns (Lederer and Prasad 1992). 

**Tip #47** Decompose large estimates into small pieces so that you can take advantage of the Law of Large Numbers: the errors on the high side and the errors on the low side cancel each other out to some degree. 

**116 Part II Fundamental Estimation Techniques** 

## **How Small Should the Estimated Pieces Be?** 

Seen from the perspective shown in Figure 10-1, software development is a process of making larger numbers of steadily smaller decisions. At the beginning of the project, you make such decisions as “What major _areas_ should this software contain?” A simple decision to include or exclude an area can significantly swing total project effort and schedule in one direction or another. As you approach top-level requirements, you make a larger number of decisions about which features should be in or out, but each of those decisions on average exerts a smaller impact on the overall project outcome. As you approach detailed requirements, you typically make hundreds of decisions, some with larger implications and some with smaller implications, but on average the impact of these decisions is far smaller than the impact of the decisions made earlier in the project. 

**==> picture [297 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
Construction—thousands of<br>low-leverage decisions<br>(and some high-leverage decisions)<br>Scope<br>Detailed Requirements—far more<br>lower-leverage decisions<br>Top-Level Requirements—more high-leverage decisions<br>Software Concept—few very high-impact decisions<br>**----- End of picture text -----**<br>


Time 

**Figure 10-1** Software projects tend to progress from large-grain focus at the beginning to fine-grain focus at the end. This progression supports increasing the use of estimation by decomposition as a project progresses. 

By the time you focus on software construction, the granularity of the decisions you make is tiny: “How should I design this class interface? How should I name this variable? How should I structure this loop?” And so on. These decisions are still important, but the effect of any single decision tends to be localized compared with the big decisions that were made at the initial, software-concept level. 

The implication of software development being a process of steady refinement is that the further into the project you are, the finer-grained your decomposed estimates can be. Early in the project, you might base a bottom-up estimate on feature areas. Later, you might base the estimate on marketing requirements. Still later, you might use detailed requirements or engineering requirements. In the project’s endgame, you might use developer and tester task-based estimates. 

**Chapter 10 Decomposition and Recomposition 117** 

The limits on the number of items to estimate are more practical than theoretical. Very early in a project, it can be a struggle to get enough detailed information to create a decomposed estimate. Later in the project, you might have too much detail. You need 5 to 10 individual items before you get much benefit from the Law of Large Numbers, but even 5 items are better than 1. 

## **10.2 Decomposition via an Activity-Based Work Breakdown Structure** 

Sometimes unseen work hides in the form of forgotten features. Sometimes it hides in the form of forgotten tasks. Decomposing a project via an activity-based work breakdown structure (WBS) helps you avoid forgetting tasks. It also helps fine-tune thinking about whether the project you’re estimating is bigger or smaller than similar past projects. Comparing the new project to the old project in each WBS category can sharpen your assessment of which parts are bigger and which are smaller. 

Table 10-3 shows a generic, activity-based WBS for a small-to-medium-sized software project. The left column lists the category of activities such as Planning, Requirements, Coding, and so on. The other columns list the kinds of work within each categories, such as Creating, Planning, Reviewing, and so on. 

**Table 10-3 Generic Work Breakdown Structure for a Small-to-Medium-Sized Software Project** 

|**Table 10-3**<br>**Generic Work Bre**<br>**Software Project**|**akdown St**|**ructur**|**e for a Sm**|**all-to-Me**|**dium-Si**|**zed**|
|---|---|---|---|---|---|---|
||**Create/**|||||**Report**|
|**Category**|**Do**|**Plan**|**Manage**|**Review**|**Rework**|**Defects**|
|General management|●|●|●|●|||
|Planning|●||●|●|●||
|Corporate activities (meetings,|●||||||
|vacation, holidays, and so on)|||||||
|Hardware setup/Software|●|●|●|●|●|●|
|setup/Maintenance|||||||
|Staff preparation|●|●|●|●|||
|Technical Processes/Practices|●|●|●|●|●|●|
|Requirements work|●|●|●|●|●|●|
|Coordinate with other projects|●|●|●|●|||
|Change management|●|●|●|●|●|●|
|User-interface prototyping|●|●|●|●|●|●|
|Architecture work|●|●|●|●|●|●|
|Detailed designing|●|●|●|●|●|●|
|Coding|●|●|●|●|●|●|
|Component acquisition|●|●|●|●|●|●|
|Automated build|●|●|●|●|●|●|



**118 Part II Fundamental Estimation Techniques** 

**Table 10-3 Generic Work Breakdown Structure for a Small-to-Medium-Sized Software Project** 

|**Table 10-3**<br>**Generic Work Brea**<br>**Software Project**|**kdown St**|**ructur**|**e for a Sm**|**all-to-Me**|**dium-Si**|**zed**|
|---|---|---|---|---|---|---|
||**Create/**|||||**Report**|
|**Category**|**Do**|**Plan**|**Manage**|**Review**|**Rework**|**Defects**|
|Integration|●|●|●|●|●|●|
|Manual system tests|●|●|●|●|●|●|
|Automated system tests|●|●|●|●|●|●|
|Software release (interim, alpha,|●|●|●|●|●|●|
|beta, and final releases)|||||||
|Documents (user docs, technical|●|●|●|●|●|●|
|docs)|||||||



To use the generic WBS, you combine the column descriptions with the categories— for example, Create/Do Planning, Manage Planning, Review Planning, Create/Do Requirements Work, Manage Requirements Work, Review Requirements Work, Create/Do Coding, Manage Coding, Review Coding, and so on. The dots in the table represent the most common combinations. 

This WBS presents an extensive list of the kinds of activities that you might consider when creating an estimate. You will probably need to extend the list to include at least a few additional entries related to specifics of your organization’s softwaredevelopment approach. You might also decide to exclude some of this WBS’s categories, which will be fine as long as that’s a conscious decision. 

**Tip #48** Use a generic software-project work breakdown structure (WBS) to avoid omitting common activities. 

## **10.3 Hazards of Adding Up Best Case and Worst Case Estimates** 

Have you ever had the following experience? You put together a detailed task list. You carefully estimate each of the tasks on the list, thinking, “We can pull this off if we try hard enough.” After you go through meticulous planning, you work hard on the first task and deliver it on time. The second task turns up some unexpected problems, but you work late and get it done on schedule. The third task turns up a few more problems, and you leave it unfinished at the end of the day, thinking you’ll polish it off the next morning. By the end of the next day, you’ve barely finished that task, and haven’t yet started the task you were supposed to do that day. By the end of the week, you’re more than a full task behind schedule. 

How did that happen? Were your estimates wrong, or did you just not perform very well? 

**Chapter 10 Decomposition and Recomposition 119** 

## **Warning: Math Ahead!** 

The answer lies in some of the statistical subtleties involved in combining individual estimates. _Statistical subtleties?_ Yes, for better or worse, this is an area in which we must dig into the mathematics a little to understand how to avoid common problems associated with building up an estimate from decomposed task or feature estimates. 

## **What Went Wrong?** 

To see what happened in the preceding scenario, let’s take another look at the case study from the beginning of the chapter. The team in the case study produced an accurate estimate. But the accuracy of their single-point estimates was unusual. A more common attempt to produce an estimate by decomposition would not produce the estimates listed in Table 10-1; it would be much more likely to produce estimates such as those shown in Table 10-4. 

**Table 10-4 Example of More Typical, Error-Prone Attempt to Estimate by Decomposition** 

|**Feature**||**Estimated Staff Weeks to Complete**|**Actual Effort**|
|---|---|---|---|
|Feature|1|1.6|3.0|
|Feature|2|1.8|2.5|
|Feature|3|2.0|1.5|
|Feature|4|0.8|2.5|
|Feature|5|3.8|4.5|
|Feature|6|3.8|4.5|
|Feature|7|2.2|3.0|
|Feature|8|0.8|1.5|
|Feature|9|1.6|2.5|
|Feature|10|1.6|3.5|
|**TOTAL**||**20.0**|**29.0**|



In this example, the accuracy of the 20-staff-week estimate obtained through a simple summation of decomposed, single-point estimates is actually worse than the aggregate estimate of 22 staff weeks that you provided earlier in the case study. How can this be? 

The root cause is a combination of the “90% confident” problem that that was discussed in Chapter 1 (“What Is an ‘Estimate’?”) and the optimism problem discussed in Chapter 4 (“Where Does Estimation Error Come From?”). When developers are asked to provide single-point estimates, they often unconsciously present Best Case estimates. Let’s say that each of the individual Best Case estimates is 25% likely, meaning that you have only a 25% chance of doing as well or better than the estimate. The odds of delivering any individual task according to a Best Case estimate 

**120 Part II Fundamental Estimation Techniques** 

are not great: only 1 in 4 (25%). But the odds of delivering _all_ the tasks are vanishingly small. To deliver both the first task and the second task on time, you have to beat 1 in 4 odds for the first task and 1 in 4 odds for the second task. Statistically, those odds are multiplied together, so the odds of completing both tasks on time is only 1 in 16. To complete all 10 tasks on time you have to multiply the 1/4s 10 times, which gives you odds of only about 1 in 1,000,000, or 0.000095%. The odds of 1 in 4 might not seem so bad at the individual task level, but the combined odds kill software schedules. The statistics of combining a set of Worst Case estimates work similarly. 

These statistical anomalies are another reason to create Best Case, Worst Case, Most Likely Case, and Expected Case estimates, as described in Chapter 9, “Individual Expert Judgment.” Table 10-5 shows how that might work out if the developers who produced the estimates in Table 10-4 were asked to produce Best Case, Worst Case, and Most Likely Case estimates, and if the Expected Case estimates were computed from those. 

**Table 10-5 Example of Estimation by Decomposition Using Best Case, Expected Case, and Worst Case Estimates** 

||||**Weeks to Complete**|**Weeks to Complete**||
|---|---|---|---|---|---|
|||**Best Case**|**Most Likely**|**Worst Case**|**Expected Case**|
|**Feature**||**(25% Likely)**|**Case**|**(75% Likely)**|**(50% Likely)**|
|Feature|1|1.6|2.0|3.0|2.10|
|Feature|2|1.8|2.5|4.0|2.63|
|Feature|3|2.0|3.0|4.2|3.03|
|Feature|4|0.8|1.2|1.6|1.20|
|Feature|5|3.8|4.5|5.2|4.50|
|Feature|6|3.8|5.0|6.0|4.97|
|Feature|7|2.2|2.4|3.4|2.53|
|Feature|8|0.8|1.2|2.2|1.30|
|Feature|9|1.6|2.5|3.0|2.43|
|Feature|10|1.6|4.0|6.0|3.93|
|**TOTAL**||**20.0**|**28.3**|**38.6**|**28.62**|



As usual, it turns out that the developers’ single-point estimates in Table 10-4 were actually their Best Case estimates. 

## **10.4 Creating Meaningful Overall Best Case and Worst Case Estimates** 

If you can’t use the sum of the best cases and worst cases to produce overall Best Case and Worst Case estimates, what do you do? A common approximation in statistics is to assume that 1/6 of the range between a minimum and a maximum approximately equals one standard deviation. This is based on the assumption that the minimum is 

**121** 

**Chapter 10 Decomposition and Recomposition** 

only 0.135% likely and the assumption that the maximum includes 99.86% of all possible values. 

## **Computing Aggregate Best and Worst Cases for Small Numbers of Tasks (Simple Standard Deviation Formula)** 

For a small number of tasks (about 10 or fewer), you can base the best and worst cases on a simple standard deviation calculation. First, you add the best cases together and add the worst cases together. Then you compute the standard deviation using this formula: 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StandardDeviation = (SumOfWorstCaseEstimates − SumOfBestCaseEstimates) / 6<br>#4<br>**----- End of picture text -----**<br>


If you take 1/6 of the range between 20.0 and 38.6 in Table 10-5, that will be 1 standard deviation of the distribution of project outcomes for that project. One-sixth of that difference is 3.1. You can then use a table of standard deviations to compute a percentage likelihood. In a business context, this is often referred to as _percentage confident_ . Table 10-6 provides the standard deviation numbers. 

**Table 10-6 Percentage Confident Based on Use of Standard Deviation** 

|**Table 10-6**<br>**P**|**ercentage Confident Based on Use of Standard Deviation**|
|---|---|
|**Percentage**||
|**Confident**|**Calculation**|
|2%|Expected case – (2 x StandardDeviation)|
|10%|Expected case – (1.28 x StandardDeviation)|
|16%|Expected case – (1 x StandardDeviation)|
|20%|Expected case – (0.84 x StandardDeviation)|
|25%|Expected case – (0.67 x StandardDeviation)|
|30%|Expected case – (0.52 x StandardDeviation)|
|40%|Expected case – (0.25 x StandardDeviation)|
|50%|Expected case|
|60%|Expected case + (0.25 x StandardDeviation)|
|70%|Expected case + (0.52 x StandardDeviation)|
|75%|Expected case + (0.67 x StandardDeviation)|
|80%|Expected case + (0.84 x StandardDeviation)|
|84%|Expected case + (1 x StandardDeviation)|
|90%|Expected case + (1.28 x StandardDeviation)|
|98%|Expected case + (2 x StandardDeviation)|



Using this approach, a statistically valid 75%-likely estimate would be the _Expected case_ (29 weeks) plus 0.67 x _StandardDeviation_ , which is 29 + (0.67 x 3.1), which equals 31 weeks. 

**122** 

**Part II Fundamental Estimation Techniques** 

Why do I say the answer is 31 weeks instead of 31.1? Because the garbage in, garbage out principle applies. The underlying task estimates are not accurate to more than 2 significant digits, much less 3, so be humble about the results. In this example, presenting an estimate of 31 weeks probably overstates the accuracy of the result, and 30 might be a more meaningful number. 

**Tip #49** Use the simple standard deviation formula to compute meaningful aggregate Best Case and Worst Case estimates for estimates containing 10 tasks or fewer. 

## **Computing Aggregate Best and Worst Cases for Large Numbers of Tasks (Complex Standard Deviation Formula)** 

If you have more than about 10 tasks, the formula for standard deviation in the previous section isn’t valid, and you have to use a more complicated approach. A scienceof-estimation approach begins by applying the standard deviation formula to each of the individual estimates (Stutzke 2005): 

**Equation** IndividualStandardDeviation = **#5** (IndividualWorstCaseEstimate − IndividualBestCaseEstimate) / 6 

You use this formula to compute the Standard Deviation column in Table 10-7. You then go through some fairly complicated math to compute the standard deviation of the aggregate estimate. 

**1.** Compute the standard deviation of each task or feature using the preceding formula. 

**2.** Compute the square of each task’s standard deviation, which is known as the _variance_ . This is shown in the right-most column of Table 10-7. 

**3.** Total the variances. 

**4.** Take the square root of the total. 

In the table, the sum of the variances is 1.22, and the square root of that is 1.1, so that’s the standard deviation of the aggregate estimate. 

**Table 10-7 Example of Complex Standard Deviation Calculations** 

|**Table 10-7**<br>**Example o**|**f Complex Standard Deviation Calculations**|
|---|---|
|**Feature**|**Weeks to Complete**|
||**Best Case**<br>**Worst Case**<br>**Standard**<br>**Deviation**<br>**Variance (Standard**<br>**Deviation Squared)**|
|Feature 1<br>Feature 2<br>Feature 3|1.6<br>3.0<br>0.233<br>0.054<br>1.8<br>4.0<br>0.367<br>0.134<br>2.0<br>4.2<br>0.367<br>0.134|



**Chapter 10 Decomposition and Recomposition 123** 

> **Table 10-7 Example of Complex Standard Deviation Calculations** 

|**Table 10-7**<br>**Example o**|**f Complex Standard Deviation Calculations**|
|---|---|
|**Feature**|**Weeks to Complete**|
||**Best Case**<br>**Worst Case**<br>**Standard**<br>**Deviation**<br>**Variance (Standard**<br>**Deviation Squared)**|
|Feature 4<br>Feature 5<br>Feature 6<br>Feature 7<br>Feature 8<br>Feature 9<br>Feature 10<br>**TOTAL**<br>**Standard Deviation**|0.8<br>1.6<br>0.133<br>0.018<br>3.8<br>5.2<br>0.233<br>0.054<br>3.8<br>6.0<br>0.367<br>0.134<br>2.2<br>3.4<br>0.200<br>0.040<br>0.8<br>2.2<br>0.233<br>0.054<br>1.6<br>3.0<br>0.233<br>0.054<br>1.6<br>6.0<br>0.733<br>0.538<br>**20.0**<br>**38.6**<br>**-**<br>**1.22**<br>**-**<br>**-**<br>**-**<br>**1.1**|



**Tip #50** Use the complex standard deviation formula to compute meaningful aggregate Best Case and Worst Case estimates when you have about 10 tasks or more. 

If you recall that the standard deviation produced by the preceding approach was 3.1, you’ll realize that this approach produces an answer of 1.10 from the same data, which is quite a discrepancy! How can that be? 

This turns out to be a case of the difference between precision and accuracy. The problem with using the formula _(WorstCaseEstimate – BestCaseEstimate) / 6_ , is that, statistically speaking, you’re assuming that the person who created the Best Case and Worst Case estimates included a 6 standard deviation range from best case to worst case. For that to be true, the estimation range would have to account for 99.7% of all possible outcomes. In other words, out of 1000 estimates, only 3 actual outcomes could fall outside their estimated ranges! 

Of course, this is a ridiculous assumption. In the example, 2 outcomes out of 10 fell outside the estimation range. As Chapter 1 illustrated, most people’s sense of 90% confident is really closer to 30% confident. With practice, people might be able to estimate an all-inclusive range 70% of the time, but estimators don’t have a ghost of a chance of estimating a 99.7% confidence interval. 

A realistic approach to computing standard deviation from best and worst cases is to divide each individual range by a number that’s closer to 2 than 6. Statistically, dividing by 2 implies that the estimator’s ranges will include the actual outcome 68% of the time, which is a goal that can be achieved with practice. 

Table 10-8 lists the number you should divide by based on the percentage of your actual outcomes that are falling within your estimated ranges. 

**124 Part II Fundamental Estimation Techniques** 

**Table 10-8 Divisor to Use for the Complex Standard Deviation Calculation** 

|**Table 10-8**<br>**Divisor to Use for the C**|**omplex Standard Deviation Calculation**|
|---|---|
|**If this percentage of your actual**|**…use this number as the divisor in the**|
|**outcomes fall within your**|**standard deviation calculation for individual**|
|**estimation range…**|**estimates**|
|10%|0.25|
|20%|0.51|
|30%|0.77|
|40%|1.0|
|50%|1.4|
|60%|1.7|
|70%|2.1|
|80%|2.6|
|90%|3.3|
|99.7%|6.0|



You would then plug the appropriate number from this table into the complex standard deviation formula: 

**Equation** IndividualStandardDeviation = **#6** (IndividualWorstCaseEstimate − Individual BestCaseEstimate) / DivisorFromTable10-8 

**Tip #51** Don’t divide the range from best case to worst case by 6 to obtain standard deviations for individual task estimates. Choose a divisor based on the accuracy of your estimation ranges. 

## **Creating the Aggregate Best and Worst Case Estimates** 

In the case study, the team’s actual results fell within its best case–worst case ranges 8 out of 10 times. Table 10-8 indicates that teams hitting the actual result 80% of the time should use a divisor of 2.6. Table 10-9 shows the results of recomputing the standard deviations, variances, and aggregate standard deviation based on dividing the ranges by 2.6 instead of 6. 

**Table 10-9 Example of Computing Standard Deviation Using a Divisor Other Than 6** 

|**Table 10-9**<br>**Examp**|**le of Computing Standard Deviation Using a Divisor Other Than 6**|
|---|---|
|**Feature**|**Weeks to Complete**|
||**Best Case**<br>**Worst Case**<br>**Standard**<br>**Deviation**<br>**Variance (Standard**<br>**Deviation Squared)**|
|Feature 1<br>Feature 2<br>Feature 3|1.6<br>3.0<br>0.538<br>0.290<br>1.8<br>4.0<br>0.846<br>0.716<br>2.0<br>4.2<br>0.846<br>0.716|



**Chapter 10 Decomposition and Recomposition 125** 

> **Table 10-9 Example of Computing Standard Deviation Using a Divisor Other Than 6** 

|**Table 10-9**<br>**Examp**|**le of Computing Standard Deviation Using a Divisor Other Than 6**|
|---|---|
|**Feature**|**Weeks to Complete**|
||**Best Case**<br>**Worst Case**<br>**Standard**<br>**Deviation**<br>**Variance (Standard**<br>**Deviation Squared)**|
|Feature 4<br>Feature 5<br>Feature 6<br>Feature 7<br>Feature 8<br>Feature 9<br>Feature 10<br>**TOTAL**<br>**Standard**<br>**Deviation**|0.8<br>1.6<br>0.308<br>0.095<br>3.8<br>5.2<br>0.538<br>0.290<br>3.8<br>6.0<br>0.846<br>0.716<br>2.2<br>3.4<br>0.462<br>0.213<br>0.8<br>2.2<br>0.538<br>0.290<br>1.6<br>3.0<br>0.538<br>0.290<br>1.6<br>6.0<br>1.692<br>2.864<br>**20.0**<br>**38.6**<br>**-**<br>**6.48**<br>**-**<br>**-**<br>**-**<br>**2.55**|



This approach produces a standard deviation for the aggregate estimate of 2.55 weeks. To compute percentage-confident estimates, you would then use the Expected Case estimate of 28.6 weeks from Table 10-5 and the multipliers from Table 10-6. This would produce a set of percentage-confident estimates such as the ones shown in Table 10-10. 

> **Table 10-10 Example of Percentage-Confident Estimates Computed From Standard Deviation** 

|**Table 10-10**<br>**Example of Perce**<br>**Standard Deviation**|**ntage-Confident Estimates Computed From**|
|---|---|
|**Percentage Confident**|**Effort Estimate**|
|2%|23.5|
|10%|25.4|
|16%|26.1|
|20%|26.5|
|25%|26.9|
|30%|27.3|
|40%|28.0|
|50%|28.6|
|60%|29.3|
|70%|30.0|
|75%|30.3|
|80%|30.8|
|84%|31.2|
|90%|31.8|
|98%|33.7|



Depending on the audience for these estimates, you might heavily edit the entries in this table before you present them. In some circumstances, however, it might be quite useful to point out that although totaling the Best Case estimates yields 

**126 Part II Fundamental Estimation Techniques** 

a total of 20 staff weeks, it’s only 2% likely that you’ll beat 23.5 weeks and only 25% likely that you’ll beat 26.9 weeks. 

As always, you should consider the precision of the estimates before you present them—I would normally present 24 weeks instead of 23.5 and 27 weeks instead of 26.9. 

## **Cautions About Percentage Confident Estimates** 

One general pitfall with the approach I just described is that the Expected Case estimates need to be accurate—that is, they need to be truly 50% likely. You should underrun those estimates just as often as you overrun them. If you find that you’re overrunning them more often than you’re underrunning them, they aren’t really 50% likely and you shouldn’t use them as your expected cases. If the expected cases aren’t accurate, then the sum of the expected cases won’t be accurate either. 

Chapter 9 provides suggestions for making the individual estimates more accurate. 

**Tip #52** 

Focus on making your Expected Case estimates accurate. If the individual estimates are accurate, aggregation will not create problems. If the individual estimates are not accurate, aggregation will be problematic until you find a way to make them accurate. 

## **Additional Resources** 

Humphrey, Watts S. _A Discipline for Software Engineering_ . Reading, MA: AddisonWesley, 1995. Appendix A of Humphrey’s book contains a short, readable summary of statistical techniques that are useful for software estimation. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ , Upper Saddle River, NJ: Addison-Wesley, 2005. Chapter 5 of Stutzke’s book goes into more detail on some of the statistics presented in this chapter. Chapter 20 describes how to create a WBS. 

Gonick, Larry and Woollcott Smith. _The Cartoon Guide to Statistics_ . New York, NY: Harper Collins, 1993. Despite the silly title, this is a respectable (and fun) introduction to statistical techniques. Many readers will find the extensive illustrations help them learn the statistical concepts. Some readers might find that the focus on pictures rather than text makes the concepts harder to understand. 

Larsen, Richard J. and Morris L. Marx. _An Introduction to Mathematical Statistics and Its Applications, Third Edition_ . Upper Saddle River, NJ: Prentice Hall, 2001. This book is a fairly readable, traditional introduction to mathematical statistics; at least it’s readable when you consider the subject matter. It’s an unavoidable fact that if you want to use statistical techniques, sooner or later you’ll have to do some math! 

Chapter 11 **Estimation by Analogy** 

## **Applicability of Techniques in This Chapter** 

||**Estimation by Analogy**|
|---|---|
|**What’s estimated**|Size, Effort, Schedule, Features|
|**Size of project**|S M L|
|**Development stage**|Early–Late|
|**Iterative or sequential**|Both|
|**Accuracy possible**|Medium|



Gigacorp (a fictional corporation) was about to begin work on Triad 1.0, a companion product to its successful AccSellerator 1.0 sales-presentation software. Mike had been appointed project manager of Triad 1.0, and he needed a ballpark estimate for an upcoming sales planning meeting. He called his staff meeting to order. 

“As you know, we’re embarking on development of Triad 1.0,” he said. “The technical work is very similar to AccSellerator 1.0. I see this project as being a little bigger overall than AccSellerator 1.0, but not much bigger.” 

“The database is going to be quite a bit bigger,” Jennifer volunteered. “But the user interface should be about the same size.” 

“It will have a lot more graphs and reports than AccSellerator 1.0 had, too, but the foundation classes should be very similar; I think we’ll end up with the same number of classes.” Joe said. 

“That all sounds right to me,” Mike said. “I think this gives me enough to do a backof-the-envelope calculation of project effort. My notes indicate that the total effort for the last system was 30 staff months. What do you think is a reasonable ballpark estimate for the effort of the new system?” 

What do _you_ think is a reasonable ballpark estimate for the effort of the new system? 

## **11.1 Basic Approach to Estimating by Analogy** 

The basic approach that Mike is using in this example is estimation by analogy, which is the simple idea that you can create accurate estimates for a new project by comparing the new project to a similar past project. 

**127** 

**128** 

**Part II Fundamental Estimation Techniques** 

I’ve had several hundred estimators create estimates for the Triad project. Using the approach implied in the example, their estimates have ranged from 30 to 144 staff months, with an average of 53 staff months. The standard deviation of their estimates is 24, or 46% of the average answer. That is not very good! A little bit of structure on the process helps a lot. 

Here is a basic estimation by analogy process that will produce better results: 

   **1.** Get detailed size, effort, and cost results for a similar previous project. If possible, get the information decomposed by feature area, by work breakdown structure (WBS) category, or by some other decomposition scheme. 

   **2.** Compare the size of the new project piece-by-piece to the old project. 

   **3.** Build up the estimate for the new project’s size as a percentage of the old project’s size. 

   **4.** Create an effort estimate based on the size of the new project compared to the size of the previous project. 

   **5.** Check for consistent assumptions across the old and new projects. 

- **Tip #53** Estimate new projects by comparing them to similar past projects, preferably decomposing the estimate into at least five pieces. 

Let’s continue using the Triad case study to examine these steps. 

## **Step 1: Get Detailed Size, Effort, and Cost Results for a Similar Previous Project** 

After the first meeting, Mike asked the Triad staff to gather more specific information about the sizes of the old system and the relative amount of functionality in the old and new systems. When their work was completed, Mike asked how they had done. “Did you get the data on the project I outlined last week?” he asked. 

“Sure, Mike,” Jennifer replied. “AccSellerator 1.0 had 5 subsystems. They stacked up like this: 

|Database|5,000 lines of code (LOC)|
|---|---|
|User interface|14,000 LOC|
|Graphs and reports|9,000 LOC|
|Foundation classes|4,500 LOC|
|Business rules|11,000 LOC|
|**TOTAL**|**43,500 LOC**|



**Chapter 11 Estimation by Analogy 129** 

“We also got some general information about the number of elements in each subsystem. Here’s what we found: 

|Database|10 tables|
|---|---|
|User interface|14 Web pages|
|Graphs and reports|10 graphs + 8 reports|
|Foundation classes|15 classes|
|Business rules|???|



“We’ve done a fair amount of work to scope out the new system. It looks like this: 

|Database|14 tables|
|---|---|
|User interface|19 Web pages|
|Graphs and reports|14 graphs + 16 reports|
|Foundation classes|15 classes|
|Business rules|???|



“The comparison to most of the old system is pretty straightforward, but the business rules part is a little tough,” Jennifer said. “We think it’s going to be more complicated than the old system, but we’re not sure how to put a number on it. We’ve talked it over, and our feeling is that it’s at least 50% more complicated than the old system.” 

“That’s great work,” Mike said. “This gives me what I need to compute an estimate for my sales meeting. I’ll crunch some numbers this afternoon and run them by you before the meeting.” 

## **Step 2: Compare the Size of the New Project to a Similar Past Project** 

The Triad details give us what we need to create a meaningful estimate by analogy. The Triad team has already performed Step 1, “Get detailed size, effort, cost results for a similar previous project.” We can perform Step 2, “Compare the size of the new project piece-by-piece to the old project.” Table 11-1 shows that detailed comparison. 

**Table 11-1 Detailed Size Comparison Between AccSellerator 1.0 and Triad 1.0** 

|**Table 11-1**<br>**Detailed**|**Size Comparison Betwe**|**en AccSellerator 1.0 an**|**d Triad 1.0**|
|---|---|---|---|
||**Actual Size of**|**Estimated Size of**|**Multiplication**|
|**Subsystem**|**AccSellerator 1.0**|**Triad 1.0**|**Factor**|
|Database|10 tables|14 tables|1.4|
|User interface|14 Web pages|19 Web pages|1.4|
|Graphs and reports|10 graphs + 8 reports|14 graphs + 16 reports|1.7|
|Foundation classes|15 classes|15 classes|1.0|
|Business rules|???|???|1.5|



**130 Part II Fundamental Estimation Techniques** 

Writing down the numbers in columns 2 and 3 is the easy part. The tricky part is what to do in the Multiplication Factor entry in column 4. The main principle here is the Count, Compute, Judge principle. If we can find something to count, we’re better off than if we insert subjective judgment. 

The factors of 1.4 for database, 1.4 for user interface, and 1.0 for foundation classes seem straightforward. 

The factor of 1.7 for graphs and reports is a little tricky. Should graphs be weighted the same as reports? Maybe. Graphs might require more work than reports, or vice versa. If we had access to the code base for AccSellerator 1.0, we could check whether graphs and reports should be weighted equally or whether one should be weighted more heavily than the other. In this case, we’ll just assume they’re weighted equally. We should document this assumption so that we can retrace our steps later, if we need to. 

The business rules entry is also problematic. The team in the case study didn’t find anything they could count, so our estimate is on shakier ground in that area than in the other areas. For sake of the example, we’ll just accept their claim that the business rules for Triad will be about 50% more complicated than the business rules were in AccSellerator. 

## **Step 3: Build Up the Estimate for the New Project’s Size as a Percentage of the Old Project’s Size** 

In Step 3, we convert the size measures from the different areas to a common unit of measure, in this case, lines of code. This will allow us to perform a whole-system size comparison between AccSellerator and Triad. Table 11-2 shows how this works. 

**Table 11-2 Computing Size of Triad 1.0 Based on Comparison to AccSellerator 1.0** 

|**Table 11-2**<br>**Computi**|**ng Size of Triad 1.0 Bas**|**ed on Comparison**|**to AccSellerator 1.0**|
|---|---|---|---|
||**Code Size of**|**Multiplication**|**Estimated Code**|
|**Subsystem**|**AccSellerator 1.0**|**Factor**|**Size of Triad 1.0**|
|Database|5,000|1.4|7,000|
|User interface|14,000|1.4|19,600|
|Graphs and reports|9,000|1.7|15,300|
|Foundation classes|4,500|1.0|4,500|
|Business rules|11,000|1.5|16,500|
|**TOTAL**|**43,500**|**-**|**62,900**|



The code sizes for AccSellerator are carried down from the information that was generated in Step 1. The multiplication factors are carried down from the work we did in Step 2. The estimated code size for Triad is simply AccSellerator’s code size multiplied by the multiplication factors. The total size in lines of code becomes the basis 

**Chapter 11 Estimation by Analogy 131** 

for our effort estimate, which will in turn become the basis for schedule and cost estimates. 

## **Step 4: Create an Effort Estimate Based on the Size of the New Project Compared to the Previous Project** 

We now have enough background to compute an effort estimate, which is shown in Table 11-3. 

**Table 11-3 Final Computation of Effort for Triad 1.0** 

|**Table 11-3**<br>**Final Computation**|**of Effort for Triad 1.0**|
|---|---|
|**Term**|**Value**|
|Size of Triad 1.0|62,900 LOC|
|Size of AccSellerator 1.0|÷43,500 LOC|
|Size ratio|= 1.45|
|Effort for AccSellerator 1.0|×30 staff months|
|Estimated effort for Triad 1.0|= 44 staff months|



Dividing the size of Triad by the size of AccSellerator gives us a ratio of the sizes of the two systems. We can multiply that by AccSellerator’s actual effort, and that gives us the estimate for Triad of 44 staff months. 

The estimate you compute and the estimate you present are two different matters. In this computation, you ended up with a single-point estimate. When you present the estimate, you might well decide to present it as a range, as discussed in Chapter 22, “Estimate Presentation Styles.” 

I’ve had the same several hundred estimators who created the original rolled-up estimates for Triad follow this approach, and their results are more accurate and consistent. The standard deviation of their results is only 7% rather than the 46%, even with the uncertainty surrounding graphs, reports, and business rules. 

## **Step 5: Check for Consistent Assumptions Across the Old and New Projects** 

You should be checking your assumptions at each step. Some assumptions aren’t completely checkable until you’ve computed the estimate. Look for the following major sources of inconsistency: 

- Significantly different sizes between the old and new projects—that is, more than the factor of 3 difference described in Section 5.1, “Project Size.” In this case, the sizes are different, but only by a factor of 1.45, which is not enough of a difference to cause any worry about diseconomies of scale. 

**132 Part II Fundamental Estimation Techniques** 

- Different technologies (for example, one project in C# and the other in Java). 

- Significantly different team members (for small teams) or team capabilities (for large teams). Small differences are OK and often unavoidable. 

- Significantly different kinds of software. For example, an old system that was an internal intranet system and a new system that’s a life-critical embedded system would not be comparable. 

## **11.2 Comments on Uncertainty in the Triad Estimate** 

The information available to create the business rules estimate was pretty fuzzy. Should we fudge the business rules number upward to be conservative in our estimate? For estimation purposes, the answer is no. The focus of the estimate should be on _accuracy_ , not conservatism. Once you move the estimate’s focus away from accuracy, bias can creep in from many different sources and the value of the estimate will be reduced. The best estimation response to uncertainty is not to bias the estimate but to be sure that the estimate accurately expresses any underlying uncertainty. If you were completely confident in the business rules number, you might consider the effort estimate to be accurate to ±10%. Considering the uncertainty in the business rules, perhaps you would fudge the uncertainty number to something like +25%, –10%. 

A better way to address the uncertainty arising from the business rules part of the estimate could be to carry a range for the business rules factor through your computations rather than using a single number. You might estimate the factor with a 50% variation (in other words, a range of 0.75 to 2.25) instead of using a single point factor of 1.5. That would produce an effort range of 38 to 49 staff months rather than the single-point estimate of 44 staff months. 

One contrast between the estimate created using this approach and the estimate created using a rolled-up (undecomposed) approach is that, in the rolled-up approach, uncertainty in one area can spread to other areas. If there is a 50% uncertainty in the business rules, the estimator might apply that uncertainty to the whole estimate, rather than just to the quarter of the estimate related to business rules. If you applied that same 50% variation to the whole estimate, the estimate would range from 22 to 66 staff months rather than from 38 to 49 staff months. Identifying what specifically is uncertain and how much effect that should have on the estimate helps narrow the overall estimation range. 

## **Tip #54** 

Do not address estimation uncertainty by biasing the estimate. Address uncertainty by expressing the estimate in uncertain terms. 

**Chapter 11 Estimation by Analogy 133** 

## **Estimation Uncertainty, Plans, and Commitments** 

Ultimately, the impact of uncertainty in the estimate will flow through to the project _plans_ and _commitments_ . Because the focus of plans and commitments is on maximizing performance rather than on accuracy, it is appropriate to adjust your commitments in a conservative direction, based on uncertainty in the underlying estimate. 

## Chapter 12 **Proxy-Based Estimates** 

## **Applicability of Techniques in This Chapter** 

|||**Standard**|||
|---|---|---|---|---|
||**Fuzzy Logic**|**Components**|**Story Points**|**T-Shirt Sizing**|
|**What’s estimated**|Size, Features|Size, Effort|Size, Effort,|Effort, Cost,|
||||Schedule,|Schedule,|
||||Features|Features|
|**Size of project**|- M L|S M L|S M L|- M L|
|**Development stage**|Early|Early–Middle|Early–Middle|Early|
|**Iterative or sequential**|Sequential|Both|Both|Sequential|
|**Accuracy possible**|Medium|Medium|Medium–High|N/A|



Most estimators can’t look at a feature description and accurately estimate, “That feature will require exactly 253 lines of code.” Similarly, it’s difficult to directly estimate how many test cases your project will need, how many defects to expect, how many classes you’ll end up with, and so on. 

A family of estimation techniques known as proxy-based techniques helps to overcome these challenges. In proxy-based estimation, you first identify a _proxy_ that is correlated with what you really want to estimate and that is easier to estimate or count (or available earlier in the project) than the quantity you’re ultimately interested in. If you want to estimate a number of test cases, you might find that the count of the number of requirements is correlated with the number of test cases. If you want to estimate size in lines of code (LOC), you might find that a feature count— stratified by size category—is correlated with size in lines of code. 

Once you’ve found your proxy, you estimate or count the number of proxy items and then use a calculation based on historical data to convert from the proxy count to the estimate that you really want. 

This chapter discusses some of the most useful proxy-based techniques. The point of each of these techniques is that the whole has a greater validity than the individual parts. Thus, these techniques are useful for creating whole-project or whole-iteration estimates and for providing whole-project or whole-iteration insights, but not for creating detailed task-by-task or feature-by-feature estimates. 

**135** 

**136 Part II Fundamental Estimation Techniques** 

## **12.1 Fuzzy Logic** 

You can use an approach known as _fuzzy logic_ to estimate a project’s size in lines of code (Putnam and Myers 1992, Humphrey 1995). Estimators are usually capable of classifying features as Very Small, Small, Medium, Large, and Very Large. We can then use historical data about how many lines of code the average Very Small feature requires, how many lines of code the average Small feature requires, and so on to compute the total lines of code. Table 12-1 shows an example of how such an estimate might be created. 

**Table 12-1 Example of Using Fuzzy Logic to Estimate a Program’s Size** 

|**Table 12-1**<br>**Exam**|**ple of Using Fuzzy Log**|**ic to Estimate a Progra**|**m’s Size**|
|---|---|---|---|
||**Average Lines of**||**Estimated Lines**|
|**Feature Size**|**Code per Feature**|**Number of Features**|**of Code**|
|Very Small|127|22|2,794|
|Small|253|15|3,795|
|Medium|500|10|5,000|
|Large|1,014|30|30,420|
|Very Large|1,998|27|53,946|
|**TOTAL**|**-**|**104**|**95,955**|



The entries in the Average Lines of Code per Feature column in the table should be based on your organization’s historical data and are fixed before the estimation begins. The Number of Features column is a count of how many features you have classified into each size category. The Estimated Lines of Code column is computed from the other two columns. As shown, the estimate has 5 significant digits, which is well beyond the accuracy of the underlying numbers. If I were presenting this estimate, I would present it as “96,000 lines of code” or even “100,000 lines of code” (that is, to one or two significant digits) to avoid using too much precision and conveying a false sense of accuracy. 

## **How to Get the Average Size Numbers** 

Fuzzy logic works best when the sizes are calibrated from your organization’s historical data. As a rule of thumb, the differences in size between adjacent categories should be at least a factor of 2. Some experts recommend a factor of 4 difference (Putnam and Meyers 1992). 

You should create the initial size averages by classifying completed work from one or more completed systems. Go through the past system and classify each feature as Very Small, Small, Medium, Large, or Very Large. Then count the total number of lines of code for the features in each classification and divide that by the number of features to arrive at the average lines of code for each feature classification. Table 122 shows an example of how this might work out. 

**Chapter 12 Proxy-Based Estimates 137** 

**Table 12-2 Example of Creating Average LOC Numbers** 

|**Table 12-2**<br>**Exa**|**mple of Creating Average**|**LOC Numbers**||
|---|---|---|---|
|**Size**|**Number of Features**|**Count of Total LOC**|**Average LOC**|
|Very Small|117|14,859|127|
|Small|71|17,963|253|
|Medium|56|28,000|500|
|Large|169|171,366|1,014|
|Very Large|119|237,762|1,998|



The numbers in this table are purely for purposes of illustration. You should work out your own numbers by using your own organization’s historical data. 

**Tip #55** Use fuzzy logic to estimate program size in lines of code. 

## **How to Classify New Functionality** 

When assigning new functionality to size categories, it’s important that the assumptions about what constitutes a Very Small, Small, Medium, Large, or Very Large feature in the estimate are the same as the assumptions that went into creating the average sizes in the first place. You can accomplish this in any of three ways: 

- Have the same people who are going to create the estimate create the original numbers for the sizes. 

- Train the estimators so that they classify features accurately. 

- Document the specific criteria for Very Small, Small, Medium, Large, and Very Large so that estimators can apply the size categories consistently. 

## **How Not to Use Fuzzy Logic** 

One interesting aspect of statistics is that statistical summaries can have more validity than any of the individual data points that make up the summary. As discussed in Chapter 10, “Decomposition and Recomposition,” the Law of Large Numbers gives the rolled-up estimate an accuracy above and beyond the accuracy of the individual estimates. The whole is truly greater than the sum of its parts. 

When using fuzzy logic, it’s important to remember this phenomenon, that the rolled-up number has a validity that the underlying numbers do not have. The reason fuzzy logic works is that we can safely assume that if 71 small features required an average of 253 lines of code in the past, 15 small features will each probably require approximately 253 lines of code in the future. However, the fact that the average is 253 lines of code _does not_ mean that any specific feature will actually consist of 253 lines of code. The sizes of individual Small features could range from 50 lines of 

**138 Part II Fundamental Estimation Techniques** 

code to 1,000 lines of code. So, although the rolled-up estimate produced by fuzzy logic can be surprisingly accurate, you should not overextend the technique to make estimates of sizes of specific features. 

By the same token, the fuzzy logic approach works well when you have about 20 features or more. If you don’t have at least 20 total features to estimate, the statistics of this approach won’t work properly, and you should look for another method. 

## **Extensions of Fuzzy Logic** 

Fuzzy logic can also be used to estimate effort if you have the underlying data to support it. Table 12-3 shows an example of how that would work. 

**Table 12-3 Example of Using Fuzzy Logic to Estimate Effort** 

|**Table 12-3**<br>**Exa**|**mple of Using Fuzzy Logi**|**c to Estimate Effort**||
|---|---|---|---|
||**Average Staff Days**||**Estimated Effort**|
|**Size**|**per Feature**|**Number of Features**|**(Staff Days)**|
|Very Small|4.2|22|92.4|
|Small|8.4|15|126|
|Medium|17|10|170|
|Large|34|30|1,020|
|Very Large|67|27|1,809|
|**TOTAL**|**-**|**104**|**3,217**|



The numbers shown in the table are purely for purposes of illustration, and you would need to derive your own Average Staff Days per Feature from your organization’s historical data. 

The final estimate of 3,217 staff days is again too precise. You could simplify it to 3,200 staff days, 3,000 staff days, or 13 staff years (assuming 250 staff days per year). You can also always consider presenting the number as a range, such as 10 to 15 staff years, which would communicate an entirely different accuracy than would 3,217 staff days. 

## **12.2 Standard Components** 

If you develop many programs that are architecturally similar to each other, you can use the _standard components_ approach to estimate size. You first need to find relevant elements to count in your previous systems. The specifics will vary depending on the kind of work you do. Typical systems might include dynamic Web pages, static Web pages, files, database tables, business rules, graphics, screens, dialogs, reports, and so on. After you’ve identified what the standard components are, you compute the average lines of code per component for your past systems. Table 12-4 shows an example of historical data for standard components. 

**Chapter 12 Proxy-Based Estimates 139** 

**Table 12-4 Example of Historical Data on Lines of Code per Standard Component** 

|**Table 12-4**<br>**Example of Hi**|**storical Data on Lines of Code per Standard Component**|
|---|---|
|**Standard Component**|**LOC per Component**|
|Dynamic Web pages|487|
|Static Web pages|58|
|Database tables|2,437|
|Reports|288|
|Business rules|8,327|



Once you have your historical data, you estimate the number of standard components you’ll have in the new program, and you compute the size of the new program based on past sizes. Table 12-5 shows one example. 

> **Table 12-5 Example of Using Standard Components to Create a Size Estimate** 

|**Table 12-5**<br>**Exa**|**mple of Usin**|**g Standard**|**Compone**|**nts to Creat**|**e a Size Est**|**imate**|
|---|---|---|---|---|---|---|
|||**Minimum**|**Most**|**Maximum**|||
|**Standard**|**LOC per**|**Possible**|**Likely**|**Possible**|**Estimated**|**Estimated**|
|**Component**|**Component**|**Number**|**Number**|**Number**|**Number**|**LOC**|
|Dynamic Web|487|11|25|50|26.8|13,052|
|pages|||||||
|Static Web|58|20|35|40|33.3|1,931|
|pages|||||||
|Database|2,437|12|15|20|15.3|37,286|
|tables|||||||
|Reports|288|8|12|20|12.7|3,658|
|Business rules|8,327|-|1|-|1|8,327|
|**TOTAL**|**-**|**-**|**-**|**-**|**-**|**64,254**|



In this table, you enter your estimated counts in columns 3 through 5. In column 3, you enter the minimum number of components you can possibly imagine the project having. For the dynamic Web pages component in this example, that number is 11. In the next column, you enter the number you think is the most likely—25 for dynamic Web pages. Then, in the fifth column, you enter the maximum number of components you can imagine—in this case, 50. The estimated number in column 6 is then computed using the Program Evaluation and Review Technique (PERT) formula that was discussed in Chapter 9, “Individual Expert Judgment.” Here's that formula adapted to estimate number of components: 

**==> picture [43 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>#7<br>**----- End of picture text -----**<br>


EstimatedNumberOfComponents = [MinimumPossible + (4 × MostLikely) + MaximumPossible] / 6 

**140 Part II Fundamental Estimation Techniques** 

In this example, the estimated number of dynamic Web pages works out to [11 + (4 x 25) + 50] / 6 = 26.8.[1] 

Once again, the numbers in this table are for purposes of illustration only, and you should derive your own numbers from your own historical data. 

## **Using Standard Components with Percentiles** 

A variation on this approach is based on the use of percentiles rather than estimated number of components. In this approach, you again need to have enough historical projects to compute meaningful percentiles (in other words, at least 10 historical projects, and, ideally, closer to 20). But if you have that much historical data, rather than estimating a number, you can estimate how much different from average you believe each component will be. Table 12-6 provides an example of a reference table you could construct. 

**Table 12-6 Example of Reference Table for Standard Components** 

|**Table 12-6**<br>**Exam**|**ple of Referen**|**ce Table for Standard C**|**ce Table for Standard C**|**omponents**||
|---|---|---|---|---|---|
|||**LOC per Component**||**(Percentile)**||
|**Standard**|**Very Small**||**Average**||**Very Large**|
|**Components**|**(10th)**|**Small (25th)**|**(50th)**|**Large (75th)**|**(90th)**|
|Dynamic Web|5,105|6,037|12,123|24,030|35,702|
|pages||||||
|Static Web pages|1,511|1,751|2,111|2,723|3,487|
|Database tables|22,498|30,020|40,027|45,776|47,002|
|Reports|1,518|2,518|3,530|5,833|5,533|
|Business rules|7,007|7,534|8,509|10,663|12,111|



The entries in this table give the size of the standard components relative to other projects your organization has done. According to this table, 10% of the organization’s projects had 5,105 lines of code or fewer for their dynamic Web pages, 50% of projects had 2,111 lines of code or fewer for their static Web pages, 75% of projects had 10,663 lines of code or fewer for their business rules, and so on. 

> 1 Sometimes people are confused by whether they should be dividing by 6 or some other number. The discussion in Chapter 10 about not dividing by 6 applied to computation of standard deviations. This formula computes the expected value, not the standard deviation, so the caution about not dividing by 6 doesn’t apply here. 

**Chapter 12 Proxy-Based Estimates 141** 

Once you have a reference table, you can classify the size you expect in each standard component area and look up the lines of code estimated for each component in Table 12-6. Table 12-7 shows an example. 

**Table 12-7 Example of Using Standard Components to Create a Size Estimate** 

|**Table 12-7**<br>**Example of U**|**sing Standard Component**|**s to Create a Size Estimate**|
|---|---|---|
|||**Estimated LOC**|
|**Standard Component**|**Size Classification**|**(from Table 12-6)**|
|Dynamic Web pages|Average|12,123|
|Static Web pages|Large|2,723|
|Database tables|Small|30,020|
|Reports|Very Small|1,518|
|Business rules|Average|8,509|
|**TOTAL**|**-**|**54,893**|



The entries in this table imply that you expect the project you’re estimating to have an average number of dynamic Web pages compared to other projects your organization has done, a larger than average number of static Web pages, a smaller than average number of database tables, and so on. 

This approach yields a size estimate of 54,893 lines of code. When presenting that number, it would once again be accurate to simplify it to 55,000 or 60,000 LOC (that is, 1 or 2 significant digits). 

## **Limitations of Standard Components** 

The standard components approach has the advantage of requiring very little effort other than using your instincts to assess the sizes that the standard components will be in the new system and looking up the corresponding entries in the reference table. It will take some effort to construct and maintain a reference table similar to Table 12-4 or Table 12-6. 

The practice of standard components is not based on counting, and so it violates the general principle of _count, compute, judge_ . It does, however, tie estimates back to something familiar, and so it can be useful at times. 

Overall, while the use of standard components is probably not the best technique to use later in a project, it can support the goal of minimizing the effort to create an early-in-the-project estimate that is subject to a high degree of inaccuracy anyway because of the Cone of Uncertainty. 

Consider using standard components as a low-effort technique to estimate size in a project’s early stages. 

**Tip #56** 

**142 Part II Fundamental Estimation Techniques** 

## **12.3 Story Points** 

Another variation on fuzzy logic is _story points_ , which were originally associated with Extreme Programming (Cohn 2006). The technique is similar to fuzzy logic, but there are some interesting and useful variations that make story points worth discussing separately. 

When using story points, the team reviews the list of stories (or requirements or features) it is considering building and assigns a size to each story. In this sense, story points are similar to fuzzy logic, except that the stories are normally assigned a numeric value from one of the scales shown in Table 12-8. 

**Table 12-8 Most Common Story Point Scales** 

|**Table 12-8**<br>**Most Com**|**mon Story Point Scales**|
|---|---|
|**Story Point Scale**|**Specific Points on the Scale**|
|Powers of 2|1, 2, 4, 8, 16|
|Fibonacci sequence|1, 2, 3, 5, 8, 13|



The result of this estimation activity is the creation of a list like the one shown in Table 12-9. 

> **Table 12-9 Example of List of Stories and Assigned Story Points** 

|**Table 12-9**<br>**Exam**|**ple of List of Stories and Assigned Story Points**|
|---|---|
|**Story**|**Points**|
|Story 1|2|
|Story 2|1|
|Story 3|4|
|Story 4|8|
|…||
|Story 60|2|
|**TOTAL**|**180**|



At this stage of their use, the story points are not terribly useful because they are a unitless measure—they don’t translate into any specific number of lines of code, number of staff days, or calendar time. The critical idea behind story points is that the team has estimated all the stories at the same time, using the same scale, and in a way that is substantially free from bias. 

Next, the team will plan an iteration, including planning to deliver some number of story points. The plan might be based on an assumption that a story point translates to a specific amount of effort, but that is just an assumption at that early point in the project. 

After the iteration has been completed, the team will be in a position to have some real estimation capability. The team can look at how many story points it delivered, how much effort it expended, and how much calendar time elapsed, and it can then make a preliminary calibration of how story points translate to effort and calendar time. This is often called _velocity_ . Table 12-10 shows an example of this. 

**Chapter 12 Proxy-Based Estimates 143** 

**Table 12-10 Data from Iteration 1 and Initial Calibration** 

## **Data for Iteration 1** 

27 story points delivered 12 staff weeks expended 3 calendar weeks expended 

## **Preliminary Calibration** 

Effort = 27 story points ÷ 12 staff weeks = 2.25 story points/staff week Schedule = 27 story points ÷ 3 calendar weeks = 9 story points/calendar week 

This initial calibration allows the project manager to make a historical-data-based estimate of the remainder of the project, as shown in Table 12-11. 

> **Table 12-11 Initial Projection for Remainder of Project** 

## **Data for Iteration 1** 

## **Assumptions (from Preliminary Calibration)** 

Effort = 2.25 story points/staff week Schedule = 9 story points/calendar week Project size = 180 story points 

## **Preliminary Whole-Project Estimate** 

Effort = 180 story points ÷ 2.25 story points/staff week = 80 staff weeks 

Schedule = 180 story points ÷ 9 story points/calendar week = 20 calendar weeks 

Of course, the computations in Table 12-11 assume that the team will remain the same in future iterations, and the projection doesn’t account for the planning considerations of holidays, vacations, and so on. But on iterative projects, it does provide for very early projections of whole-project outcomes based on historical data from the same project. 

The initial whole-project estimates should be refined based on data from later iterations. The shorter your iterations are, the sooner you’ll have data you can use to estimate the rest of the project and the more confident you can be in those estimates. 

## **Tip #57** 

Use story points to obtain an early estimate of an iterative project’s effort and schedule that is based on data from the same project. 

## **Cautions About Ratings Scales** 

Fuzzy logic uses a verbal scale of Very Small, Small, Medium, Large, and Very Large. Story points use a scale based on powers of 2 or Fibonacci numbers. Which is better? 

On a numeric scale, the ratios between the numbers on the scale suggest that the underlying quantities being measured bear a proportionate relationship. If your story points scale is a Fibonacci sequence, a scale of 1, 2, 3, 5, 8, 13 suggests that a 

**144 Part II Fundamental Estimation Techniques** 

story of 5 points will take 5/3 as much effort as a story of 3 points. It suggests that a story of 13 points will take more than 4 times as much effort as a story of 3 points. 

These relationships turn out to be a double-edged sword. If the necessary care is taken to ensure that stories classified as 13 points really are about 4 times as much effort as stories classified as 3 points, that’s great. That means you can compute an average effort per story point (as described earlier), multiply the total number of story points by the average, and get a meaningful result (also as described earlier). 

Accomplishing this level of accuracy requires that great discipline be exercised in assigning story points to stories. It also requires checking actual project data to ensure that the ratios that are estimated are the ratios actually found in practice. 

If care is not taken to ensure that the underlying numeric ratios implied by the Fibonacci sequence or by the powers of 2 are accurate, numeric story points have the potential to lead to computed results that are less valid than they appear. The use of a numeric scale implies that you can perform numeric operations on the numbers: multiplication, addition, subtraction, and so on. But if the underlying relationships aren’t valid—that is, a story worth 13 points doesn’t really require 13/3 as much effort as a story worth 3 points—then performing numeric operations on the “13” isn’t any more valid than performing a numeric operation on “Large” or “Very Large.” 

Table 12-12 illustrates another way of describing this issue. 

> **Table 12-12 Example of What Can Happen with a Numeric Scale That Isn’t as Numeric as It Appears** 

|**Story Point**|**Number**|**Apparent**|**Intended**|**Actual Ratio**|**Real Story**|
|---|---|---|---|---|---|
|**Classification**|**of Stories**|**Story Points**|**Ratio**|**(from Data)**|**Points**|
|“1”|4|“4”|1|2|4|
|“2”|7|“14”|2|2.5|18|
|“3”|5|“15”|3|3|15|
|“5”|5|“25”|5|7|35|
|“8”|12|“96”|8|11|132|
|“13”|2|“26”|13|17|34|
|**TOTAL**|**43**|**“180”**|**-**|**-**|**238**|



In this example, the misleading numeric scale led us to believe that 180 points was a reasonable approximation of our total effort, but the real effort is about 30% higher. 

**Tip #58** Exercise caution when calculating estimates that use numeric ratings scales. Be sure that the numeric categories in the scale actually work like numbers, not like verbal categories such as small, medium, and large. 

**Chapter 12 Proxy-Based Estimates 145** 

## **12.4 T-Shirt Sizing** 

Nontechnical stakeholders often want (and need) to make decisions about project scope during the wide part of the Cone of Uncertainty. A good estimator will refuse to provide highly precise estimates while the project is still in the wide part of the Cone. Sales and marketing staff will say, “How can I know whether I want that feature if I don’t know how much it costs?” And a good estimator will say, “I can’t tell you what it will cost until we’ve done more detailed requirements work.” It would appear that the two groups are at an impasse. 

This impasse can be broken by realizing that the goal of software estimation is not pinpoint accuracy but estimates that are accurate enough to support effective project control. In this case, nontechnical stakeholders are typically not asking for an estimate in staff hours. They are asking whether a specific feature is a mouse, rabbit, dog, or elephant. This observation leads to a very useful estimation approach called _t-shirt sizing_ . 

In this approach, the developers classify each feature’s size relative to other features as Small, Medium, Large, or Extra Large. In parallel, the customer, marketing, sales, or other nontechnical stakeholders classify each feature’s business value on the same scale. These two sets of entries are then combined, as shown in Table 12-13. 

**Table 12-13 Example of Using T-Shirt Sizing to Classify Features by Business Value and Development Cost** 

|**Feature**|**Business Value**|**Development Cost**|
|---|---|---|
|Feature A|Large|Small|
|Feature B|Small|Large|
|Feature C|Large|Large|
|Feature D|Medium|Medium|
|Feature E|Medium|Large|
|Feature F|Large|Medium|
|Feature G|Small|Small|
|Feature H|Small|Medium|
|…|||
|Feature ZZ|Small|Small|



Creating this sort of relationship between business value and development cost allows the nontechnical stakeholder to say things like, “If the cost of Feature B is Large, I don’t want it, because the value is only Small.” This is a tremendously useful decision to be able to make early in the life cycle of that feature. If you were instead to carry that feature through some amount of detailed requirements, architecture, design, and so on, you would be expending effort on a feature that ultimately isn’t cost justified. In software, a quick "No" answer has great value. T-shirt sizing allows for early-in-the-project decisions to rule out features so that you don't need to carry those features further into the Cone of Uncertainty. 

**146 Part II Fundamental Estimation Techniques** 

The discussion about what to carry and what to cut is easier if the feature list can be sorted into a rough cost/benefit order. Typically, that is done by assigning a _net business value_ number (another unitless measure) based on the combination of development cost and business value. Table 12-14 shows one possible scheme for assigning net business value. You can use this scheme or come up with one that seems to more accurately reflect the values in your environment. 

> **Table 12-14 Net Business Value Based on Ratio of Development Cost to Business Value** 

|**Table 12-14**<br>**Net Bu**<br>**Value**|**siness Value Based**|**on Ratio of Development C**|**on Ratio of Development C**|**ost to Business**|
|---|---|---|---|---|
|||**Development Cost**|||
|**Business Value**|**Extra Large**|**Large**|**Medium**|**Small**|
|Extra Large|0|4|6|7|
|Large|–4|0|2|3|
|Medium|–6|–2|0|1|
|Small|–7|–3|–1|0|



This sort of net business value lookup table allows you to add a third column to the original value/cost table (Table 12-13) and to sort that table by net business value, as shown in Table 12-15. 

> **Table 12-15 Example of Sorting T-Shirt Sizing Estimates by Approximate Net Business Value** 

|**Table 12-15**<br>**Exa**<br>**Business Value**|**mple of Sorting T-Shir**|**t Sizing Estimates by A**|**pproximate Net**|
|---|---|---|---|
||||**Approximate Net**|
|**Feature**|**Business Value**|**Development Cost**|**Business Value**|
|Feature A|L|S|3|
|Feature F|L|M|2|
|Feature C|L|L|0|
|Feature D|M|M|0|
|Feature G|S|S|0|
|Feature ZZ|S|S|0|
|Feature H|S|M|–1|
|Feature E|M|L|–2|
|…||||
|Feature B|S|L|–3|



Remember that the Approximate Net Business Value column is an approximation. I don’t suggest just counting down the list and drawing a line. The value of sorting by approximate business value is that it supports getting some quick “definitely yes” answers for the features at the top of the list and some quick “definitely no” decisions for the features at the bottom. That allows discussion to focus on the middle of the list, which is where the discussion will be most productive anyway. 

**Tip #59** Use t-shirt sizing to help nontechnical stakeholders rule features in or out while the project is in the wide part of the Cone of Uncertainty. 

**Chapter 12 Proxy-Based Estimates 147** 

## **12.5 Other Uses of Proxy-Based Techniques** 

The examples in this chapter have shown how to use proxy-based techniques to estimate lines of code and effort. You could apply the same techniques to estimate test cases, defects, pages of user documentation, or anything else that might be easier to estimate by proxy than to estimate directly. 

**Tip #60** Use proxy-based techniques to estimate test cases, defects, pages of user documentation, and other quantities that are difficult to estimate directly. 

As Chapter 7, “Count, Compute, Judge,” described, there is hardly any limit to what you might be able to count. This chapter has presented just a few specific examples. If you believe you have something else in your environment that would be a better indication of project size than fuzzy logic, standard components, or story points, you should count that instead. 

**Tip #61** Count whatever is easiest to count and provides the most accuracy in your environment, collect calibration data on that, and then use that data to create estimates that are well-suited to your environment. 

## **12.6 Additional Resources** 

Cohn, Mike. _Agile Estimating and Planning_ . Upper Saddle River, NJ: Prentice Hall Professional Technical Reference, 2006. Cohn’s book contains a more extended discussion of story points, including planning considerations as well as estimation techniques. 

Humphrey, Watts S. _A Discipline for Software Engineering_ . Reading, MA: AddisonWesley, 1995. Chapter 5 of Humphrey’s book discusses proxy-based estimation, which he calls the PROBE method, and goes into detail on some supporting statistical techniques. Chapter 5 also discusses fuzzy logic. 

Chapter 13 

## **Expert Judgment in Groups** 

## **Applicability of Techniques in This Chapter** 

||**Group Reviews**|**Wideband Delphi**|
|---|---|---|
|**What’s estimated**|Size, Effort, Schedule, Features|Size, Effort, Schedule, Features|
|**Size of project**|- M L|- M L|
|**Development stage**|Early–Middle|Early|
|**Iterative or sequential**|Both|Sequential|
|**Accuracy possible**|Medium|Medium|



Group expert judgment techniques are useful when estimating early in a project or for estimating large unknowns. This chapter presents an unstructured group judgment technique (group reviews) and a structured technique called Wideband Delphi. 

## **13.1 Group Reviews** 

A simple technique for improving the accuracy of estimates created by individuals is to have a group review the estimates. When I have groups review estimates, I require three simple rules: 

- **Have each team member estimate pieces of the project individually, and then meet to compare your estimates** Discuss differences in the estimates enough to understand the sources of the differences. Work until you reach consensus on high and low ends of estimation ranges. 

- **Don’t just average your estimates and accept that** You can compute the average, but you need to discuss the differences among individual results. Do not just take the calculated average automatically. 

- **Arrive at a consensus estimate that the whole group accepts** If you reach an impasse, you can’t vote. You must discuss differences and obtain buy-in from all group members. 

The improvement in accuracy from this simple technique is significant. Figure 13-1 illustrates the results across 24 groups of estimators I’ve worked with. 

**149** 

**150 Part II Fundamental Estimation Techniques** 

**==> picture [344 x 248] intentionally omitted <==**

**----- Start of picture text -----**<br>
Reviewed<br>100% Estimates<br>Individual<br>80%<br>Estimates<br>60%<br>40%<br>20%<br>Error<br>0%<br>-20%<br>-40%<br>-60%<br>-80%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24<br>Estimation Group<br>**----- End of picture text -----**<br>


**Figure 13-1** A simple review of individually created estimates significantly improves the accuracy of the estimates. 

The individual estimates in Figure 13-1 average a Magnitude of Relative Error of 55%. The group-reviewed estimates average an error of only 30%. In this set of estimates, 92% of the group estimates were more accurate than the individual estimates and, on average, the reviews cut the error magnitude approximately in half. 

## **Tip #62** 

Use group reviews to improve estimation accuracy. 

How many experts are enough? Studies in other fields have found that the use of 3 to 5 experts with different backgrounds seems to be sufficient (Libby and Blashfield 1978, Jørgensen 2002). 

In addition, it’s useful to find experts with different backgrounds, different roles, or who use different techniques (Armstrong 2001, Jørgensen 2002). 

## **13.2 Wideband Delphi** 

Wideband Delphi is a structured group-estimation technique. The original Delphi technique was developed by the Rand Corporation in the late 1940s for use in predicting trends in technology (Boehm 1981). The name Delphi comes from the ancient Greek oracle at Delphi. The basic Delphi technique called for several experts 

**Chapter 13 Expert Judgment in Groups 151** 

to create independent estimates and then to meet for as long as necessary to converge on, or at least agree upon, a single estimate. 

An initial study on the use of Delphi for software estimation found that the basic Delphi technique was no more accurate than a less structured group meeting. Barry Boehm and his colleagues concluded that the generic Delphi meetings were subject to too much political pressure and were also likely to be dominated by the more assertive estimators in the group. Consequently, Boehm and his colleagues extended the basic Delphi technique into what has become known as Wideband Delphi. Table 13-1 describes the basic procedure. 

## **Table 13-1 Wideband Delphi Technique** 

1. The Delphi coordinator presents each estimator with the specification and an estimation form. 

2. Estimators prepare initial estimates individually. (Optionally, this step can be performed after step 3.) 

3. The coordinator calls a group meeting in which the estimators discuss estimation issues related to the project at hand. If the group agrees on a single estimate without much discussion, the coordinator assigns someone to play devil’s advocate. 

4. Estimators give their individual estimates to the coordinator anonymously. 

5. The coordinator prepares a summary of the estimates on an iteration form (shown in Figure 13-2) and presents the iteration form to the estimators so that they can see how their estimates compare with other estimators’ estimates. 

6. The coordinator has estimators meet to discuss variations in their estimates. 

7. Estimators vote anonymously on whether they want to accept the average estimate. If any of the estimators votes “no,” they return to step 3. 

8. The final estimate is the single-point estimate stemming from the Delphi exercise. Or, the final estimate is the range created through the Delphi discussion and the singlepoint Delphi estimate is the expected case. 

Source: Adapted from _Software Engineering Economics_ (Boehm 1981). 

Steps 3 through 7 can be performed either in person, in a group-meeting setting, or electronically via e-mail or chat software. Performing the steps electronically can help preserve anonymity. Iterations of steps 3 through 7 can be performed immediately or they can be performed in batch mode, depending on the time-criticality of the estimate and the availability of the estimators. 

**==> picture [330 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
Average<br>Estimate<br>0 5 10 15 20<br>Staff Months<br>**----- End of picture text -----**<br>


**Figure 13-2** A Wideband Delphi estimating form. 

**152 Part II Fundamental Estimation Techniques** 

The estimating form shown in Figure 13-2 can be a paper form or it can be drawn by the coordinator on a whiteboard. The form shown has a range of 0 to 20 staff months. The range you initially show on the form should be at least triple the range you expect the estimators to come up with so that the estimators don’t feel constrained to a predefined range. 

The coordinator should take care to prevent people with dominant personalities from unduly influencing the estimate. Software developers aren’t known for their assertive personalities, and the most reserved person will sometimes have the best insights into the work being estimated. 

It’s also useful to show all the rounds of estimates on the same scale so that the estimators can observe how their estimates are converging (or, in some cases, diverging). Figure 13-3 gives an example of this. 

**==> picture [319 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
Round 1<br>0 5 10 15 20<br>Round 2<br>0 5 10 15 20<br>Round 3<br>0 5 10 15 20<br>Staff Months<br>**----- End of picture text -----**<br>


**Figure 13-3** A Wideband Delphi estimating form after three rounds of estimates. In this case, after Round 3, the group might decide to settle on a range of 12 to 14 staff months with an expected value of 13 staff months. 

## **Effectiveness of Wideband Delphi** 

I’ve collected data on the use of Wideband Delphi with a very difficult estimation problem. For the first 25 groups I worked with, Figure 13-4 shows the error rate from a simple averaging of their initial estimates compared to the error rate from Wideband Delphi estimating. 

My experience with Wideband Delphi suggests that it cuts estimation error by an average of approximately 40% compared to the initial group average. Of the groups in my study, about two-thirds produced a more accurate answer by using Wideband Delphi than by simply averaging their individual estimates. 

**Chapter 13 Expert Judgment in Groups 153** 

**==> picture [348 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
700% Delphi<br>Estimates<br>600%<br>Group<br>500%<br>Averages<br>400%<br>Error 300%<br>200%<br>100%<br>0%<br>-100%<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25<br>Estimation Group<br>**----- End of picture text -----**<br>


**Figure 13-4** Estimation accuracy of simple averaging compared to Wideband Delphi estimation. Wideband Delphi reduces estimation error in about two-thirds of cases. 

Of the 10 groups I’ve worked with that produced the _worst_ initial estimates (shown in Figure 13-5), Wideband Delphi improved estimation accuracy in 8 out of 10 cases, with an average error reduction of about 60%. 

**==> picture [338 x 213] intentionally omitted <==**

**----- Start of picture text -----**<br>
1200%<br>1100% Delphi Estimates<br>1000% Group Averages<br>900%<br>800%<br>700%<br>Error 600%<br>500%<br>400%<br>300%<br>200%<br>100%<br>0%<br>1 2 3 4 5 6 7 8 9 10<br>Estimation Group<br>**----- End of picture text -----**<br>


**Figure 13-5** Wideband Delphi when applied to terrible initial estimates. In this data set, Wideband Delphi improved results in 8 out of 10 cases. 

From this data, I conclude that Wideband Delphi improves accuracy in most cases, and it is especially useful in avoiding wildly erroneous results. 

**154 Part II Fundamental Estimation Techniques** 

## **“The Truth Is Out There”** 

Implicit in estimation techniques that rely on averaging individual estimates is the idea that the correct answer lies somewhere in the range between the lowest estimate and the highest. In my Wideband Delphi data, however, 20% of the groups’ initial estimation ranges do not include the correct answer. This means that averaging their initial estimates cannot possibly produce an accurate result. 

Perhaps the most interesting phenomenon associated with Wideband Delphi is that one-third of the groups whose initial range does not include the correct answer ultimately settle on an estimate that is outside their initial range and closer to the correct answer. In other words, for these groups, the Wideband Delphi estimate turns out to be better than the best individual estimate. Figure 13-6 illustrates this dynamic. Notice that none of the groups settled on a final estimate that was worse than the worst individual estimate. 

Correct Answer � In none of the observed cases Range of initial In one third of cases, the final did the final Wideband Delphi individual estimates Wideband Delphi estimate moved estimate move in this direction into this range (that is, out (that is, out of the initial range, of the original range, toward the away from the correct answer) correct answer) 

**Figure 13-6** In about one-third of cases, Wideband Delphi helps groups that don’t initially include the correct answer to move outside their initial range and closer to the correct answer. 

## **When to Use Wideband Delphi** 

In the difficult group estimation exercise I’ve discussed in this chapter, Wideband Delphi reduced the average estimation error from 290% to 170%. Errors of 290% and 170% are very high, characteristic of estimates created in the wide part of the Cone of Uncertainty. Still, reducing error by 40% is valuable, whether the reduction is from 290% to 170% or from 50% to 30%. 

Although my data seems to endorse the use of Wideband Delphi, industry studies on the question of how to combine estimates created by different estimators have been mixed. Some studies have found that group-based approaches to combining estimates work best, and others have found that simple averaging works best (Jørgensen 2002). 

Because Wideband Delphi requires a meeting, it burns a lot of staff time, making it an expensive way to estimate. It is not appropriate for detailed task estimates. 

**Chapter 13 Expert Judgment in Groups 155** 

Wideband Delphi is useful if you’re estimating work in a new business area, work in a new technology, or work for a brand-new kind of software. It is useful for creating “order of magnitude” estimates at product definition or software concept time, before you’ve pinned down many of the requirements. It’s also useful if a project will draw heavily from diverse specialties, such as a combined need for uncommon usability, algorithmic complexity, exceptional performance, intricate business rules, and so on. It also tends to sharpen the definition of the scope of work, and it's useful for flushing out estimation assumptions. In short, Wideband Delphi is most useful for estimating single, focused items that require input from numerous disciplines in the very wide part of the Cone of Uncertainty. In these uncertain situations, Wideband Delphi can be invaluable. 

**Tip #63** Use Wideband Delphi for early-in-the-project estimates, for unfamiliar systems, and when several diverse disciplines will be involved in the project itself. 

## **Additional Resources** 

Boehm, Barry W. _Software Engineering Economics_ . Englewood Cliffs, NJ: Prentice-Hall, Inc., 1981. Section 22.2 of Boehm’s book describes the original Delphi method and Boehm’s creation of Wideband Delphi. 

NASA, “ISD Wideband Delphi Estimation,” Number 580-PROGRAMMER-016-01, September 1, 2004, _http://software.gsfc.nasa.gov/AssetsApproved/PA1.2.1.2.pdf_ . This document describes a Wideband Delphi technique used by the NASA Goddard Space Flight Center. 

Wiegers, Karl. “Stop Promising Miracles,” _Software Development_ , February 2000. Wiegers’s paper describes a variation on the Wideband Delphi technique. 

Chapter 14 **Software Estimation Tools** 

## **Applicability of Techniques in This Chapter** 

||**Use of Software Estimation Tools**|
|---|---|
|**What’s estimated**|Size, Effort, Schedule, Features|
|**Size of project**|- M L|
|**Development stage**|Early–Middle|
|**Iterative or sequential**|Both|
|**Accuracy possible**|High|



This book focuses on the art of estimation, but sometimes the best support for the art of estimation is the science of estimation—computationally intensive estimation methods that you can’t easily do by hand, even with a good calculator. 

## **14.1 Things You Can Do with Tools That You Can’t Do Manually** 

Software estimation tools allow you to perform several kinds of estimation-related work that you can’t readily perform manually. 

_**Simulating project outcomes**_ Software estimation tools can perform sophisticated statistical simulations, and these simulations can help project stakeholders understand the scope of work. Figure 14-1 shows an example of simulated software project outcomes. 

In the plot, the solid black lines indicate the 50/50, or median, schedule and effort. The dashed black lines represent the 25th percentile and 75th percentile outcomes. 

**157** 

**158 Part II Fundamental Estimation Techniques** 

**==> picture [337 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
60<br>55<br>50<br>45<br>40<br>Effort 35<br>(staff 30<br>months) 25<br>20<br>15<br>10<br>5<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21<br>Schedule (months)<br>**----- End of picture text -----**<br>


**Figure 14-1** A tool-generated simulation of 1,000 project outcomes. Output from Construx Estimate. 

The estimation software accounts for several sources of variability: 

- Variation in productivity 

- Variation in program size, possibly decomposed into multiple modules 

- Variation in rates of staff buildup 

For each simulated outcome, the software uses a statistical technique called Monte Carlo simulation to go through 100-point probability distributions and simulate one possible outcome each for productivity, size, and staff buildup. The software then computes one estimated point in the scatter plot from these three factors. To create the entire scatter plot, the software goes through this cycle 1,000 times. You can see why you wouldn’t want to do this by hand! 

Different tools use different approaches, and some of the tools that are more expensive than Construx Estimate will use more sophisticated techniques. 

_**Probability analysis**_ Chapter 1, “What Is an ‘Estimate’?” explained the fallacies of estimating with terms like “90% confident.” When the estimates are created using judgment, such expressions are inherently error-prone. But when the estimates are generated using an estimation tool calibrated with historical data, numeric percentages are better supported and more meaningful. In Figure 14-1, for example, the effort of 45 staff months is 75% likely, because 75% of simulated projects took less than 45 staff months. 

Table 14-1 shows an example of a tool-calculated probability analysis for project effort. The “nominal” mentioned in the third column refers to the 50% likely estimate of 20 staff months. 

**159** 

**Chapter 14 Software Estimation Tools** 

**Table 14-1 Example of Project Effort Probabilities Computed by Estimation Software** 

||**Effort Will Be Less**|**Difference from Nominal**|
|---|---|---|
|**Probability**|**Than or Equal To**|**Effort Estimate**|
|10%|7|–64%|
|20%|10|–50%|
|30%|13|–37%|
|40%|16|–20%|
|50%|20|0%|
|60%|26|30%|
|70%|37|84%|
|80%|58|189%|
|90%|142|611%|



The most interesting aspects of this table are the very large increases in effort to move from 70% to 80% or 80% to 90% confidence. With judgment-based techniques, very few estimators would multiply their nominal estimate by a factor of 6 to compute the 90% confident estimate, but that is what’s needed in this particular case. (These numbers can’t be used generally; they are computed from the specific assumptions entered into the estimation software.) 

Figure 14-2 shows a graphical depiction of the data in the table. 

**==> picture [352 x 203] intentionally omitted <==**

**----- Start of picture text -----**<br>
100%<br>90%<br>80%<br>70%<br>60%<br>Probability 50%<br>40%<br>30%<br>20%<br>10%<br>0%<br>0 20 40 60 80 100 120 140<br>Effort (staff months)<br>**----- End of picture text -----**<br>


**Figure 14-2** Example of probable project outcomes based on output from estimation software. 

**160 Part II Fundamental Estimation Techniques** 

_**Accounting for diseconomies of scale**_ Estimation tools automatically account for differences in project sizes and the effect of size on productivity. 

_**Accounting for creeping requirements**_ Requirements growth is such a common issue that most commercial estimation tools include an allowance for requirements growth over the course of a project. 

_**Estimation of less common software issues**_ Estimation tools typically support estimating size of requirements documents, size of design documents, number of test cases, number of defects, mean time to failure, and numerous other quantities. 

_**Calculation of planning options and integration with planning tools**_ Some software estimation tools will allow you to allocate effort across requirements, design, construction, test, and debugging activities, and they’ll support dividing the project into as many iterations as you see fit. These sorts of calculations are tedious to perform by hand but easy to do with the right tool support. Some tools also integrate well with Microsoft Project and other project-planning tools. 

_**What-if analysis**_ Estimation tools allow you to quickly revise your estimation assumptions and to see the effect on the estimate. The necessary computations can be performed instantly on a computer but would be time-consuming and errorprone if performed by hand. 

_**Referee for unrealistic project expectations**_ Suppose that your boss has insisted that you complete a project in 50 staff months and 11 calendar months, and suppose that you’ve created the estimate shown in Figure 14-3. The blue rectangle in the lower left corner of the plot shows your boss’s constraints on effort and schedule. The scatter plot of 1,000 simulated project outcomes shows that only 8 of 1,000 project outcomes fall within the specified constraints. This is a visually compelling argument against trying to complete this project within those constraints! 

_**Acting as an objective authority when revising estimation assumptions**_ A common, unhealthy dynamic in software estimation occurs when a stakeholder rejects an initial estimate because it is too high. The stakeholder sometimes proposes a few minor feature cuts and then expects disproportionate reductions in the project’s cost and schedule. A variation on this theme is slightly increasing the team size and then hoping for a large reduction in schedule. 

Estimation software can serve as an impartial third party in arbitrating the effects of such changes. Without the tool, you are the person who must tell the stakeholder that his or her adjustments to the cost and schedule aren’t supported by the feature cuts. With the tool, you can sit down on the same side of the table as the stakeholder and let the tool play the “bad cop” that tells the stakeholder that his or her changes don’t produce as much reduction in the cost and schedule as was hoped for. 

**Chapter 14 Software Estimation Tools 161** 

**==> picture [342 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
250<br>225<br>200<br>175<br>150<br>Effort<br>(staff 125<br>months)<br>100<br>75<br>50<br>25<br>0<br>10 12 14 16 18 20 22 24 26 28 30 32<br>Schedule (months)<br>**----- End of picture text -----**<br>


**Figure 14-3** In this simulation, only 8 of the 1,000 outcomes fall within the desired combination of cost and schedule. 

Figure 14-4 shows an example of the computed tradeoffs between project effort and schedule—that is, the amount of increased staff needed to shorten a schedule, or the savings in effort if the schedule can be lengthened. You might have better luck if the tool says that you need to increase staff from 20 staff months to 26 staff months to achieve a 1-month reduction in schedule than if _you_ simply assert the same thing. 

**==> picture [338 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
30<br>25<br>Effort<br>(staff 20 �<br>months)<br>15<br>10<br>11 12 13 14<br>Schedule (months)<br>**----- End of picture text -----**<br>


**Figure 14-4** Calculated effect of shortening or lengthening a schedule. 

**162 Part II Fundamental Estimation Techniques** 

_**Sanity-checking estimates created with the art of estimation**_ The best estimators use multiple estimation approaches and then look for convergence or spread among the estimates. An estimate created with a commercial tool can provide one of those estimates. 

_**Estimating large projects**_ The larger the project being estimated, the less appropriate it is to rely solely on the art of estimation. Large projects should rely on a commercial software estimation tool to provide at least one of the estimates used to create and compare estimates. 

**Tip #64** Use an estimation software tool to sanity-check estimates created by manual methods. Larger projects should rely more heavily on commercial estimation software. 

## **14.2 Data You’ll Need to Calibrate the Tools** 

You don’t need a lot of data to calibrate estimation tools to use your historical data. If you have data from one or more completed projects, including 

- Effort, in staff months 

- Schedule, in elapsed months 

- Size, in lines of code 

you can calibrate some of the models (including Construx Estimate) to use your historical data instead of industry-average data. Historical data from one project is better than nothing. Historical data from three or more projects is perfectly adequate. 

The more expensive tools described in Section 14.4, “Summary of Available Tools,” tend to use their large databases of historical-project results to justify their high price tags. But if you have historical data from three of your own projects, the estimate you create using your own data will usually be more accurate than an estimate created on the basis of a tool’s generic data. Some of the more expensive tools are worth the money, but not for their large historical databases. 

## **14.3 One Thing You Shouldn’t Do with a Tool Any More than You Should Do Otherwise** 

The fact that an estimate comes out of a software estimation tool doesn’t mean that it’s accurate. The estimate’s assumptions might be incorrect, or the estimate might have been calibrated with inappropriate or flawed calibration data. The tool’s control 

**Chapter 14 Software Estimation Tools 163** 

knobs might have been used to insert bias. The tool’s underlying estimation methodology might be questionable. 

## **Tip #65** 

Don’t treat the output of a software estimation tool as divine revelation. Sanitycheck estimation tool outputs just as you would other estimates. 

## **14.4 Summary of Available Tools** 

Numerous effective software estimation tools are available. Prices range from free to $20,000 per seat per year and up. Here are some of the more popular tools: 

_**Angel, http://dec.bournemouth.ac.uk/ESERG/ANGEL/**_ The Analogy Software Tool is an interesting tool that supports estimating future projects by analogy to past projects. 

_**Construx Estimate, www.construx.com/estimate**_ This is a freeware tool used to generate the estimation tool screen shots shown in this book. The underlying estimation methodology is based on the Putnam Estimation model (Putnam and Myers 1992). The tool also contains some functionality based on Cocomo II. I worked as the lead programmer on the first 2 versions of this tool. 

_**Cocomo II, http://sunset.usc.edu/research/COCOMOII/**_ Several implementations of Cocomo II can be found on the Internet by searching for _Cocomo II_ . The official versions can be found at the University of Southern California Web site listed above and are available for free. 

_**Costar, www.softstarsystems.com**_ Costar is a low-priced, full implementation of Cocomo II offered by Softstar Systems. 

_**KnowledgePLAN, www.spr.com**_ This tool is developed and sold by Software Productivity Research (Capers Jones’s company) and emphasizes a high degree of integration with Microsoft Project. 

_**Price-S, www.pricesystems.com**_ Price-S was originally developed by RCA and now consists of a suite of estimation products. 

_**SEER, www.galorath.com**_ Like Price-S, SEER consists of several related products: SEER-SEM for estimation, planning, and control; SEER-SSM for in-depth software sizing; and SEER-AccuScope for simple software sizing. 

_**SLIM-Estimate and Estimate Express, www.qsm.com**_ Quantitative Software Management’s family of tools includes SLIM-Estimate, which is a full-featured and powerful estimation tool, and Estimate Express, which is less fully featured but still powerful. 

**164 Part II Fundamental Estimation Techniques** 

Both tools are based on the Putnam estimation model. QSM is founded by Lawrence Putnam. 

## **Additional Resources** 

For additional and updated pointers to estimation tools, please see my Web site at _www.construx.com/estimate/_ . 

## Chapter 15 **Use of Multiple Approaches** 

## **Applicability of Techniques in This Chapter** 

||**Use of Multiple Estimation Approaches**|
|---|---|
|**What’s estimated**|Size, Effort, Schedule, Features|
|**Size of project**|S M L|
|**Development stage**|Early–Late|
|**Iterative or sequential**|Both|
|**Accuracy possible**|High|



No single estimation technique is perfect, so using multiple approaches is useful in many contexts. The most sophisticated commercial software producers tend to use at least three different estimating approaches and then look for convergence or spread among their estimates. Convergence among the estimates tells you that you probably have a good estimate. Spread tells you that there are probably factors you have overlooked and need to understand better. This technique applies equally to estimates of size, effort, schedule, and features. 

My first personal exposure to this idea was in creating the estimate for the first edition of my book _Code Complete_ (McConnell 1993). I had spent about 2 years doing background research for the book, writing prototype chapters, and preparing in other ways to write the book. Throughout this 2-year period, I had the idea that I was writing a 250 to 300–page book. That idea didn’t come from any analytical exercise—it was just a length that I had gotten stuck in my head. 

Since I hadn’t published a book before, I thought I should present a proposal to the publisher that made it look like I might be capable of actually finishing the book. So as I was nearing the completion of my proposal for the book, I created my first estimate by decomposition. I went through the detailed outline I’d planned for the book and estimated the length of each section individually. Table 15-1 shows what that estimate looked like. 

**165** 

**166 Part II Fundamental Estimation Techniques** 

**Table 15-1 Estimated Draft Pages in** _**Code Complete**_ **Using Expert Judgment with Decomposition** 

|**Table 15-1**<br>**Estimat**<br>**Decomposition**|**ed Draft Pages in****_Code Complet_**|**_e_ Using Expert Judgment with**|
|---|---|---|
||**Estimate #1: Original Whole-**|**Estimate #2: Expert Judgment**|
|**Chapter**|**Book “Gut Feel” Estimate**|**with Decomposition**|
|Preface|-|4|
|Welcome|-|5|
|Metaphors|-|11|
|Prerequisites|-|52|
|…|…|…|
|Character|-|20|
|Review of themes|-|20|
|**TOTAL**|**250–300**|**802**|



Up to this point, I had essentially used two estimation techniques: gut instinct, which led to a 250 to 300–page estimate, and expert judgment with decomposition, which lead to an 802-page estimate. There was enough spread between these two estimates that I needed to understand why the estimates differed so much. 

I was attached to my 250-page preconception of the book’s length, so I thought, “That 802-page estimate can’t possibly be right. I must have made an error in my estimate.” I decided that I would reestimate the book a second time and get the “correct” estimate. 

For the third estimate, I took the number of pages in each of the prototype chapters I’d written and I divided those page counts by the number of points in the outlines for those chapters. I had a ratio of 1.64 pages per outline point. I then went through my detailed outline for the whole book and counted the number of outline points per chapter. I multiplied those by 1.64. Table 15-2 shows the estimate obtained by using this method. 

> **Table 15-2 Estimated Draft Pages in** _**Code Complete**_ **Using Outline Points and Historical Data** 

||**Estimate #1:**|||
|---|---|---|---|
||**Original Whole-**|**Estimate #2:**|**Estimate #3:**|
||**Book “Gut Feel”**|**Expert Judgment**|**Outline Points and**|
|**Chapter**|**Estimate**|**with Decomposition**|**Historical Data**|
|Preface|-|4|4|
|Welcome|-|5|5|
|Metaphors|-|11|11|
|Prerequisites|-|52|52|
|…|…|…|…|
|Life-cycle models|-|20|16|
|Review of themes|-|20|21|
|**TOTAL**|**250–300**|**802**|**759**|



**Chapter 15 Use of Multiple Approaches 167** 

The third estimate of 759 pages was within 5% of the second estimate of 802 pages. Because of the convergence of those two estimates, I had a pretty clear picture that I wasn’t writing a 250 to 300–page book, as I had thought for 2 years. I was writing a 750 to 800–page book. 

My experience was representative of a more general finding: Estimation accuracy improves when results from multiple estimators or results from multiple estimation techniques are combined (Jørgensen 2002, Tockey 2004). 

**Tip #66** Use multiple estimation techniques, and look for convergence or spread among the results. 

The software parallels of my book-related estimating are straightforward. People form ideas about possible project costs, durations, and features that are based on nothing in particular. They will keep those preconceived ideas until someone presents them with enough data to dislodge their preconceptions. Without data, I would not have believed that the scope of my project was three times as large as I had thought. With a little bit of data, I initially still needed more data before I was convinced. 

Another parallel to software is that it’s better to get bad news early than late. I adjusted my expectations about the size of my project at proposal time. I could have chosen to stop at that time. But I looked at the project scope and decided it was worth doing anyway, which gave me a more realistic view of the schedule I was planning and the commitment I was making. 

The fact that two completely different approaches had produced similar estimates increased my confidence in those estimates. In software, be sure to use different kinds of estimation techniques to create your different estimates. For example, you might use estimation by proxy, expert judgment, estimation by analogy, and a software estimation tool. 

Once I accepted the convergence of the estimates, I was suddenly able to see how other data confirmed that ballpark size as well. One of my prototype chapters was 72 pages long. That would have made up 29% of a 250-page book. I never believed that I was 29% done with the project just because I had completed that prototype chapter. Indeed, at the gut-instinct level I knew that chapter was no more than about 10% of the book. After my eyes were opened by the two convergent estimates, I realized that the length of the prototype confirmed that the real scope of the book was in the 750 to 800–page range, not the 250 to 300–page range. 

Project-specific data usually provides the most accurate estimate. I ended up with 749 draft pages, which was only 10 pages (1%) different from the outline points estimate that had been created using historical data from the same project. 

My original gut-instinct estimate was based on looking at other books in the 250 to 300–page range. Because I hadn’t written a book before, I made what turned out to be 

**168** 

**Part II Fundamental Estimation Techniques** 

a naïve assumption that I would need to write 250 to 300 pages to end up with a 250 to 300–page book. But page count from manuscript to published book expands because of blank pages between chapters, blank pages between book parts, the table of contents, perhaps a list of figures, the index, and other front and back matter. Page count is also affected by the choice of typeface, margins, line leading, and so on. All these elements are obvious once someone points them out, but as a rookie author it was easy for me to forget to account for them in my estimate. Even in my decomposed estimate I committed the classic estimating mistake of doing a good job of estimating the things I knew about but forgetting to estimate certain significant parts of the project. 

Finally, my second two estimates converged to within about 5%. I didn’t know it at the time, but that turns out to be a good target for convergence in general. (If you’re in the wide part of the Cone of Uncertainty, you will sometimes need to settle for less convergence.). 

## **Tip #67** 

If different estimation techniques produce different results, try to find the factors that are making the results different. Continue reestimating until the different techniques produce results that converge to within about 5%. 

In a more software-specific context, I was later asked to estimate a project for one of my clients. The crosses in Figure 15-1 show the individual estimates I created for that project. The size of each cross represents the confidence I had in each estimate. The triangle shows my “most accurate estimate” of 75 staff months and 12 calendar months. Although the crosses look somewhat dispersed, the estimates in which I had the most confidence all converged to within 5% of the “most-accurate estimate.” The square shows my client’s business target of 25 staff months and 5 calendar months. 

**==> picture [332 x 200] intentionally omitted <==**

**----- Start of picture text -----**<br>
150<br>Individual Estimates<br>Most Accurate Estimate<br>125<br>Business Target<br>100<br>Effort<br>(staff 75<br>months)<br>50<br>25<br>0<br>0 2 4 6 8 10 12 14 16<br>Schedule (months)<br>**----- End of picture text -----**<br>


**Figure 15-1** An example of multiple estimates for a software project. 

**Chapter 15 Use of Multiple Approaches 169** 

In this particular case, the client chose to proceed on the basis of the business target of 5 calendar months and 25 staff months. This was unfortunate. The project was ultimately delivered after 14 calendar months and about 80 staff months’ effort, and the team delivered far less functionality than originally planned. 

**Tip #68** If multiple estimates agree and the business target disagrees, trust the estimates. 

## **Additional Resources** 

Tockey, Steve. _Return on Software_ . Boston, MA: Addison-Wesley, 2005. Chapter 22 of Tockey’s book discusses estimation with multiple methods, Chapter 23 discusses how to account for inaccuracy in estimates, and Chapters 24 and 25 discuss how to make decisions under conditions of risk and uncertainty. 

## Chapter 16 

## **Flow of Software Estimates on a Well-Estimated Project** 

## **Applicability of Techniques in This Chapter** 

||**Changing to More Accurate Estimation**|**Estimate Refinement Based**|
|---|---|---|
||**Techniques Later in the Project**|**on Project-Specific Data**|
|**What’s estimated**|Size, Effort, Schedule, Features|Size, Effort, Schedule,|
|||Features|
|**Size of project**|- M L|S M L|
|**Development stage**|Early–Late|Early–Late|
|**Iterative or sequential**|Sequential|Both|
|**Accuracy possible**|High|High|



On poorly estimated projects, estimation focuses on directly estimating cost, effort, and schedule, with little or no focus on estimating the size of the software that will be built. Projects are reestimated many times, but usually in response to schedule slippages late in the project. 

In a well-estimated project, the focus of estimation and the points at which the project is reestimated are different. This chapter describes the estimation flow of a well-estimated project. Chapter 17, “Standardized Estimation Procedures,” describes how to create a standardized estimation approach that includes this healthy estimation flow. 

## **16.1 Flow of an Individual Estimate on a Poorly Estimated Project** 

On poorly estimated projects, the creation of the estimate flows as shown in Figure 16-1. 

The inputs, the estimation process, and the outputs are not well defined, and they are open to debate and scrutiny. Scrutinizing the estimation process would be beneficial if the objective were to obtain more accurate results. But the objective of the scrutiny is usually to make the estimate smaller. In other words, the scrutiny tends to put 

**171** 

**172 Part II Fundamental Estimation Techniques** 

downward pressure on the estimate, which is not offset by any corresponding upward pressure. 

**==> picture [205 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
Inputs defined<br>for this specific<br>estimate Ad Hoc Outputs<br>Estimation<br>Process<br>**----- End of picture text -----**<br>


**Figure 16-1** Estimation on a poorly estimated project. Neither the inputs nor the process are well defined, and the inputs, process, and outputs are all open to debate. 

**Tip #69** Don’t debate the output of an estimate. Take the output as a given. Change the output only by changing the inputs and recomputing. 

## **16.2 Flow of an Individual Estimate on a WellEstimated Project** 

If the estimation inputs and process are well-defined, arbitrarily changing the output is not a rational action. Project stakeholders might not like the output, but the appropriate corrective action is to adjust the inputs (for example, reduce the project’s scope) and to recalculate the outputs, not just to change the output to a different answer. 

Figure 16-2 shows the flow of an estimate on a well-estimated project. 

**==> picture [257 x 103] intentionally omitted <==**

**----- Start of picture text -----**<br>
Technical scope Standard Estimated effort<br>Estimation<br>Priorities Procedure Estimated schedule<br>Constraints Estimated cost<br>Estimated features<br>Historical data<br>**----- End of picture text -----**<br>


**Figure 16-2** Estimation on a well-estimated project. The inputs and process are well defined. The process and outputs are not subject to debate; however, the inputs are subject to iteration until acceptable outputs are obtained. 

In a well-estimated project, specific inputs of technical scope, priorities, and constraints are considered. These inputs can all be adjusted until the estimation process produces an acceptable outcome. Historical data is also an input to the estimate and 

**173** 

**Chapter 16 Flow of Software Estimates on a Well-Estimated Project** 

is used to calibrate the productivity assumptions. Historical data is shown entering the bottom of the diagram because it shouldn’t be adjusted in the context of a specific estimate—especially not to make the estimate come out to a specific result. 

The estimation procedure itself is _standardized_ . In other words, it is a procedure that is defined in advance of the need to create any specific estimate. Because it is standardized, it is not adjusted on an estimate-by-estimate basis—again, especially not for the purpose of moving the estimated results closer to the desired results. We’ll discuss specific standardized estimation procedures in Chapter 17. 

The outputs of estimated effort, schedule, cost, and features flow from following a defined process that uses defined inputs. On a well-estimated project, the outputs are not debated or scrutinized per se. 

Differentiating between estimates, targets, and commitments is especially useful in this context. If the estimate is not what is desired, project leadership might nonetheless have good reasons to commit to achieving a target that is more aggressive than the estimate. But that doesn’t change the estimate itself. 

Within the estimation procedure, the only factor that ever needs to be estimated in the traditional sense (that is, by using judgment) is size. And you’ll need to use judgment to estimate size only very early in a project, before you have requirements, stories, use cases, or something else you can count. Effort is computed from the size estimate by using historical productivity data. Schedule, cost, and features are computed from the effort estimate. Figure 16-3 shows this flow. 

**==> picture [151 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
Schedule<br>Size Effort Cost<br>Features<br>**----- End of picture text -----**<br>


**Figure 16-3** Flow of a single estimate on a well-estimated project. Effort, schedule, cost, and features that can be delivered are all computed from the size estimate. 

**Tip #70** Focus on estimating size first. Then compute effort, schedule, cost, and features from the size estimate. 

## **16.3 Chronological Estimation Flow for an Entire Project** 

Because of the Cone of Uncertainty, most projects will benefit from being reestimated several times. Estimates created in the later days of a project can be more accurate than estimates created earlier. Project plans and controls can then be tightened up when the project is reestimated with better accuracy. 

**174 Part II Fundamental Estimation Techniques** 

## **Tip #71** 

## Reestimate. 

Reestimation does not consist of simply doing the same estimation work again. It consists of converting to more accurate approaches as the project progresses. Figure 16-4 summarizes the most useful kinds of techniques for estimating at various points in a project for common kinds of projects. 

**==> picture [354 x 351] intentionally omitted <==**

**----- Start of picture text -----**<br>
Large  Small<br>Sequential Sequential Iterative<br>Project  Project  Project<br>Kind of Technique<br>Computing � � � � � � � �<br>Counting � � � � � � �<br>Historical Data from Organization � � � � �<br>Historical Data from Same Project � � �<br>Decomposition � � � � � � � �<br>Analogy � � � � �<br>Proxy-Based Estimation � � � � � � � �<br>Complex Algorithms � � � � �<br>Automated Estimation Tool � � � � �<br>Expert Judgment � � � � � � �<br>Estimates by Skilled Estimators � � � �<br>Estimates by Contributors � � � � � � � � Primary Technique<br>Bottom-Up, Task-Level Estimation � � � � � �<br>� [Secondary]<br>Group Estimates/Reviews � � � � � Technique<br>Pre-RequirementsDuring RequirementsDuring DesignDuring ConstructionDuring Initial PlanningDuring ConstructionDuring Initial PlanningDuring Construction<br>**----- End of picture text -----**<br>


**Figure 16-4** Summary of applicability of different estimation techniques by kind of project and project phase. 

## **Estimation Flow for Large Projects** 

Very early in a large project, counting won’t be available, so you’ll be using algorithms, software tools, and other macro techniques. You can still improve those early estimates with group reviews and by using multiple approaches. 

**175** 

**Chapter 16 Flow of Software Estimates on a Well-Estimated Project** 

As you move into later stages of a large project, you can move to more accurate, historical-data–based counting approaches and more toward micro techniques such as bottom-up task estimation, which will produce more accurate estimates (Symons 1991). 

**Tip #72** Change from less accurate to more accurate estimation approaches as you work your way through a project. 

## **Estimation Flow for Small Projects** 

Small projects estimate from the beginning the same ways that larger projects estimate at the end. As soon as you know the specific people who will be working on your project and can start handing out specific task assignments (or work packages), it’s time to switch from large-grain algorithmic approaches to bottom-up approaches based on individuals estimating their own assignments. On a small project, that might be on Day 1. On a large project, that can be several months into the project. 

**Tip #73** When you are ready to hand out specific development task assignments, switch to bottom-up estimation. 

## **16.4 Estimate Refinement** 

When you miss a project milestone, there is a question about how to recalibrate the schedule. Suppose that you have a 6-month schedule. You planned to meet your first milestone in 4 weeks, but it actually took 6 weeks. Should you: 

- Assume you can make up the lost two weeks later in the schedule? 

- Add the two weeks to the total schedule? 

- Multiply the whole schedule by the magnitude of the slip, in this case by 50 percent? 

The most common approach is option #1. The reasoning usually goes like this: “Requirements took a little longer than we expected, but now they’re solid, so we’re bound to save time later. We’ll make up the shortfall during coding and testing.” But a 1991 survey of more than 300 projects found that projects hardly ever make up lost time—they tend to get further behind (van Genuchten 1991). Option #1 is seldom the best choice. 

Option #2 assumes that the first milestone took two weeks longer than it should have but that the rest of the project will take the originally estimated amount of time. The Achilles’ heel of option #2 is that estimation errors tend to be inaccurate for 

**176 Part II Fundamental Estimation Techniques** 

systemic reasons that pervade the whole project. It’s unlikely that the whole estimate is accurate, except for the part that you’ve had real experience with. With rare exception, the correct response to actual results that diverge from estimated results is option #3. 

Changing the estimate after missing or beating a milestone isn’t the only option, of course. You can cut features, spend some of your project’s risk buffer, or perform some combination of adjustments. You might also decide to delay and get more data by monitoring how you do meeting the next milestone. But if you’re still off by 50 percent in meeting the next milestone, your corrective actions won’t have as much time to work as they would have had when you first detected the estimation error. 

## **Tip #74** 

When you reestimate in response to a missed deadline, base the new estimate on the project’s actual progress, not on the project’s planned progress. 

## **16.5 How to Present Reestimation to Other Project Stakeholders** 

Estimators on poorly estimated projects allow themselves to be forced into providing a single-point estimate early on. They will then be held accountable for that estimate for the rest of the project. For example, suppose over the course of a project that you provide the set of estimates listed in Table 16-1. 

**Table 16-1 Example of Estimation History of a Project Estimated Using SinglePoint Estimates** 

|**Table 16-1**<br>**Example of Estimation**<br>**Point Estimates**|**istory of a Project Estimated Using Single-**|
|---|---|
|**Point in Project**|**Estimate (Staff Months)**|
|Initial concept|10|
|Approved product definition|10|
|Requirements complete|13|
|User interface design complete|14|
|First interim release|16|
|**FINAL**|**17**|



With this set of estimates, the customer will consider the project to have slipped over budget and behind schedule the first time the estimate increases from 10 staff months to 13 staff months. Each time you reestimate the project after that, the project will seem to be slipping into ever more trouble. That’s unfortunate, because what’s really happening is that the first 10-month estimate was subject to a very high degree of inaccuracy. It’s appropriate to reestimate several times after that. The final 

**Chapter 16 Flow of Software Estimates on a Well-Estimated Project 177** 

tally of 17 staff months might be the result of a well-run project, but the way the estimates were presented makes it seem otherwise. 

Contrast that scenario with one in which you provide estimates in ranges that become narrower as the project progresses, as shown in Table 16-2. 

**Table 16-2 Example of Estimation History of a Project Estimated Using Estimate Ranges** 

|**Table 16-2**<br>**Example of Estimation Hi**<br>**Estimate Ranges**|**story of a Project Estimated Using**|
|---|---|
|**Point in Project**|**Estimate (Staff Months)**|
|Initial concept|3–40|
|Approved product definition|5–20|
|Requirements complete|9–20|
|User interface design complete|12–18|
|First interim release|15–18|
|**FINAL**|**17**|



As you refine each estimate in this case, your customer will consider the project to be staying within expectations. Rather than losing the customer’s confidence by taking one schedule slip after another, you build confidence by consistently meeting the customer’s expectations and by tightening up the ranges as you go. 

Another reason to use ranges rather than single-point estimates is that researchers have found that initial estimates tend to become “anchors” for future estimates, even when the original estimates are not well founded (Lim and O’Connor 1996, Jørgensen 2002). A poor, initial single-point estimate can thus contaminate the estimates for the whole project. Using ranges instead of single-point estimates helps avoid this problem. 

**Tip #75** Present your estimates in a way that allows you to tighten up your estimates as you move further into the project. 

## **When to Present the Reestimates** 

There are no magic times to reestimate. Estimation accuracy improves continuously throughout the project. Projects commonly reestimate at major milestones, upon major releases, or when major project assumptions change, such as when a large influx of requirements changes are made. 

Regardless of how many times you plan to reestimate, communicate your reestimation plan to other project stakeholders in advance. The Cone of Uncertainty frees you from making firm commitments in the early part of the project when you have a poor chance of ultimately meeting those commitments. But it obligates you to update project stakeholders regularly as your view of the project comes into focus. 

**178 Part II Fundamental Estimation Techniques** 

Table 16-3 gives an example of an estimation schedule that you might publish on a sequentially run project. 

**Table 16-3 Example of an Estimation Schedule for a Sequential Project** 

|**Table 16-3**<br>**Example o**|**f an Estimation Sched**|**ule for a Sequential Project**|
|---|---|---|
||**Estimate Accuracy**||
||**(for Remainder**||
|**After Milestone**|**of Project)**|**Comments**|
|Initial concept|–75%, +300%|For internal use only; do not publish|
|||outside of development group.|
|Approved product|–50%, +100%|_Exploratory Estimate._For internal company|
|definition||use only; do not publish externally.|
|Requirements|–20%, +25%|_Budget Estimate._OK to publish the high|
|complete and user||end of the range externally. Do not publish|
|interface design||the lower number or midpoint.|
|complete (UIDC)|||
|First interim release|–10%, +10%|Preliminary estimates fine-tuned with|
|||project data. Do not publish externally;|
|||these are just FYI. Available approximately|
|||UIDC + 45 days.|
|Second interim|–10%, +10%|_Preliminary Commitment Estimate._OK to|
|release||publish the high end of the range exter-|
|||nally. Do not publish the lower number.|
|Third interim release|–10%, +10%|_Final Commitment Estimate._OK to publish|
|||the midpoint number externally.|
|Interim releases_4-X_|–10%, +10%|Estimates updated only when new require-|
|||ments are approved by the Change Board.|
|Code complete|–5%, +5%|Same as above.|



Depending on the needs of your project stakeholders, you might need to provide reestimates more or less frequently than illustrated in the table. You should adjust the details of this table to fit your environment. Chapter 17 extends this example and suggests an additional approach that's well suited to iterative projects. 

**Tip #76** Communicate your plan to reestimate to other project stakeholders _in advance_ . 

## **What If Your Management Won’t Let You Reestimate?** 

Is it really true that your management won’t let you reestimate? I doubt it. Your management might not allow you to change your _commitment_ , but that is different from prohibiting you from reestimating. You should always plan to reestimate periodically, if only for your own internal project planning and project-control purposes, regardless of whether your management or customer will accept the result of the reestimation. 

**Chapter 16 Flow of Software Estimates on a Well-Estimated Project 179** 

Many organizations do plan ahead for reestimation. I’ll discuss that more in Section 17.2, “Fitting Estimation into a Stage-Gate Process.” 

## **16.6 A View of a Well-Estimated Project** 

It’s difficult to know mid-stream how good your estimates are. The accuracy of a project’s estimates is assessable only in hindsight. In hindsight, however, you can tell the difference between a well-estimated project and a poorly estimated one. 

Once the project has been completed, review the project's estimation history to determine whether the project's estimates anticipated the project’s eventual outcome. Figure 16-5 shows an example of a project that was well estimated. 

**==> picture [355 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Release<br>Interim Interim<br>Scope Core Interim Release 2 Release 3<br>Architecture Release 1 Complete Complete<br>Complete Complete<br>Requirements<br>Complete<br>Project<br>Initiation<br>**----- End of picture text -----**<br>


Time 

**Figure 16-5** A well-estimated project. The single-point estimates miss the mark, but the ranges all include the eventual outcome. 

The vertical bars in the figure represent the estimation ranges. The shaded blue dots represent the single-point Expected Case estimates. The solid blue dot represents the actual project outcome. In this project, the single-point estimates were different from the final outcome until the end of the project. But each of the ranges presented throughout the project included the eventual outcome, so I would consider this project to have been well estimated. 

Figure 16-6 shows an example of a project that was systematically underestimated. 

**180 Part II Fundamental Estimation Techniques** 

**==> picture [335 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
Release<br>Interim<br>Interim<br>Release 3<br>Interim Release 2 Complete<br>Release 1 Complete<br>Core<br>Scope Architecture Complete<br>Complete<br>Project Requirements<br>Initiation Complete<br>Time<br>**----- End of picture text -----**<br>


**Figure 16-6** A poorly estimated project. The project is uniformly underestimated, and the estimation ranges are too narrow to encompass the eventual outcome. 

In essence, this project has fallen prey to the same issue we discussed in Chapter 2 (“How Good an Estimator Are You?”) with regard to unrealistically narrow ranges and “90% confident” claims. The project used estimation ranges, which is good, but the ranges were too narrow to include the project’s eventual outcome, which is bad. 

## Chapter 17 **Standardized Estimation Procedures** 

## **Applicability of Techniques in This Chapter** 

||**Standardized Estimation**|**Assessing Effectiveness of an**|
|---|---|---|
||**Procedure**|**Estimation Procedure**|
|What’s estimated|Size, Effort, Schedule, Features|Size, Effort, Schedule, Features|
|Size of project|S M L|S M L|
|Development stage|Early–Late|Late|
|Iterative or sequential|Both|Both|
|Accuracy possible|High|High|



A standardized estimation procedure is a well-defined process for creating estimates that is adopted at the organizational level and that provides guidance at the individual-project level. Standard procedures protect against poor estimation practices such as off-the-cuff estimation and guessing. They protect against changing estimates arbitrarily because a powerful stakeholder doesn’t like a specific result. They encourage consistency of the estimation process. And, in the event of an especially poor estimate, they allow you to retrace your steps so that you can improve the procedure over time. 

Standardized procedures are equally useful for large projects, small projects, iterative projects, and sequential projects, but the specifics will vary across these types of projects. 

## **17.1 Usual Elements of a Standardized Procedure** 

Based on the typical estimation flow described in Chapter 16, “Flow of Software Estimates on a Well-Estimated Project,” a standardized estimation procedure typically does the following: 

- Emphasizes counting and computing when possible, rather than using judgment 

- Calls for use of multiple estimation approaches and comparison of results 

- Communicates a plan to reestimate at predefined points in the project 

**181** 

**182 Part II Fundamental Estimation Techniques** 

- Defines how the required estimation approach changes over the course of a project 

- Contains a clear description of an estimate’s inaccuracy 

- Defines when an estimate can be used as the basis for a project budget 

- Defines when an estimate can be used as the basis for internal and external commitments 

- Calls for archiving estimation data and reviewing effectiveness of the procedure 

For the standardized estimation procedure to do its job, it’s important that the organization treat the procedure as a _standard_ . Deviations from the procedure need to be justified in writing, and they should be rare. 

The procedure itself should be documented in a “Software Engineering Standards” document or a “Standardized Estimation Procedure” document. The procedure itself is then subject to formal change control. The procedure can be changed at the end of a project, motivated by a desire to improve the procedure’s accuracy for future projects. The procedure should not be changed “in flight.” Such changes are too prone to bias that will undermine both the accuracy of the specific estimate in question and the effectiveness of the procedure for future projects. 

## **Tip #77** 

Develop a Standardized Estimation Procedure at the organizational level; use it at the project level. 

## **17.2 Fitting Estimation into a Stage-Gate Process** 

Many large, established organizations have a defined Software Development Life Cycle (SDLC). These life cycles tend to be part of “stage-gate processes,” product lifecycle processes that are defined in terms of several “stages” and “gates” (Cooper 2001). Companies using stage-gate processes include 3M, Agilent, Corning, Exxon, GE, Guinness, Hewlett-Packard, Intel, Kodak, Proctor & Gamble, and many others. 

Figure 17-1 shows a typical stage-gate process. 

**==> picture [356 x 55] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 4<br>0 1 2 5<br>Stage: Discovery Scoping Planning Develop- Testing and Launch<br>ment Validation<br>Gate: 1 2 3 4 5<br>**----- End of picture text -----**<br>


**Figure 17-1** A typical stage-gate product development life cycle. 

The SDLC identifies the software development activities that are normally performed during each stage. It also defines the exit criteria that determine whether the 

**Chapter 17 Standardized Estimation Procedures 183** 

project is allowed to complete one stage and begin the next stage (that is, to proceed through the next gate). Details of SDLCs vary from one organization to another. Table 17-1 summarizes how an SDLC would coordinate with a typical productoriented stage-gate process. 

**Table 17-1 Typical Product-Oriented Stage-Gate SDLC (Abbreviated Version)** 

|**Table 17-1**<br>**Typi**|**cal Product-Oriented Stage-**|**cal Product-Oriented Stage-**|**Gate SD**|**LC (A**|**bbreviated Version)**|
|---|---|---|---|---|---|
||**Major Activities During**|||||
|**Stage**|**Stage**||**Gate**|**Primary Exit Criteria**||
|0. Discovery|■|Identify market|1|■|Approved Preliminary|
|||opportunity|||Business Case|
||■|Assess high-level||||
|||technical feasibility||||
||■|Develop Preliminary||||
|||Business Case||||
|1. Scoping|■|Define Product Vision|2|■|Approved Product Vision|
||■|Develop Marketing||■|Approved Marketing|
|||Requirements|||Requirements|
||■|Validate concept with||||
|||customers||||
|2. Planning|■|Develop detailed|3|■|Approved Software|
|||requirements|||Development Plans|
||■|Develop detailed Soft-||■|Approved Budget|
|||ware Development Plans||■|Approved Final Business|
||■|Develop budget|||Case|
|||estimates||||
||■|Develop Final Business||||
|||Case||||
|3. Development|■|Execute main software|4|■|Approved Software|
|||development life cycle|||Release Plan|
||■|Develop Marketing||■|Approved Marketing|
|||Launch Plan and Opera-|||Launch Plan and|
|||tions Plan|||Operations Plan|
||■|Develop final Test Plan||■|Approved Software Test|
||||||Plan|
|4. Testing and|■|Execute final Test Plan|5|■|Pass release criteria|
|validation|■|Decide to release||||
|5. Launch|■|Execute Marketing|N/A|N/A||
|||Rollout Plan||||
||■|Conduct project||||
|||postmortem||||
||■|Collect customer feed-||||
|||back and defect reports||||
||■|Monitor business results||||



**184 Part II Fundamental Estimation Techniques** 

From an estimation point of view, stage-gate processes present both challenges and opportunities. The challenges tend to arise from the fact that many stage-gate processes were originally developed for hardware products, consumer goods, or other non-software products. While the basic frameworks of those processes are useful, they need to be tailored to software before they will be able to help software projects the way they help other kinds of product development. 

One common challenge is that Development is often listed as a single stage (shown as Stage 3 in Table 17-1). The activities that occur during development represent 75% to 90% of the total work in a software project, and I would normally want to see more interim signs of progress during that stage than are implied by the single-gate review at the end of the stage. This is one situation in which you should feel free to revise your estimates periodically through such a stage to support effective project planning and control regardless of whether the organization encourages reestimation in the middle of the stage. 

A second common issue is that the Scoping and Planning stages defined in Table 17-1 are often combined into a single stage. That essentially means that Gate 3 should occur at the point where the Cone of Uncertainty has narrowed to ±25%, which can be anywhere from 15% to 35% of the calendar time into the project. (Chapter 21, “Estimating Planning Parameters,” discusses these percentages in more detail.) Nontechnical stakeholders often need to be educated about the extent of software development activities that must be completed to support a meaningful “Gate 3” review. The number and depth of activities are often greater than non-technical stakeholders expect. 

Once you’ve educated nontechnical stakeholders about the mapping between the stage-gate process and the software life cycle, an SDLC provides powerful support for a standardized estimation procedure. It becomes natural to attach specific estimation ranges to the various gates of the SDLC, which helps to institutionalize the concept of estimation uncertainty. 

Table 17-2 shows an example of how you might map estimation ranges onto an organization’s SDLC. 

**Table 17-2 Typical Correspondence Between SDLC Gates and Estimates** 

|**SDLC**|**Estimate Accuracy (for**||
|---|---|---|
|**Gate**|**remainder of project)**|**Estimate Usage**|
|1|–75%, +300%|_Vision Estimate_. For internal use only; do not publish|
|||outside of development group.|
|2|–50%, +100%|_Exploratory Estimate._For internal company use only;|
|||do not publish externally.|
|3|–20%, +25%|_Budget Estimate._OK to publish the high end of the|
|||range externally. Do not publish the lower number or|
|||midpoint.|
|4|–10%, +10%|_Final Commitment Estimate._OK to publish the|
|||midpoint number externally.|



**185** 

**Chapter 17 Standardized Estimation Procedures** 

Depending on the organization’s focus, the Estimate Accuracy percentages might refer to variability in cost, effort, or features. 

**Tip #78** Coordinate your Standardized Estimation Procedure with your SDLC. 

The next two sections provide examples of standardized estimation procedures. Section 17.3 provides an example of a procedure for use on sequential projects, and Section 17.4 provides an example of a procedure for iterative projects. 

## **17.3 An Example of a Standardized Estimation Procedure for Sequential Projects** 

Table 17-3 shows an example of a standardized estimation procedure that could be used to estimate sequential software projects. This estimation procedure assumes that the organization’s main priority is the software’s feature set and that the main goal of estimation is to refine the accuracy of the cost and schedule estimates. 

**Table 17-3 Example Standardized Estimation Procedure for Sequential Projects— Emphasis on Estimating Cost and Schedule** 

## **I. Exploratory Estimate (Approved Product Definition)** 

- A. Create at least one estimate using each of the following approaches: 

1. One estimator shall estimate the project bottom-up, using a work breakdown structure. 

2. One estimator shall estimate the project using standard components. 

3. One estimator shall estimate the project top-down, using estimation by analogy with similar past projects. 

- B. Estimators shall use a Wideband Delphi process to converge to a single-point nominal estimate (N). 

- C. Estimates must always be presented as a range from 0.5N to 2.0N (i.e., –50%, +100%). 

1. The single-point nominal developed for use in these calculations should not be presented. 

2. These estimates may not be used for budgeting or external commitments, except to approve budget for completing the Product Design stage. 

## **II. Budget Estimate (Product Design Complete)** 

- A. Create new estimates using two of the approaches from step I: 

1. Estimate the project bottom-up, using a work breakdown structure. 

2. Estimate the project using standard components. 

- B. Create a function points estimate. 

1. Compute function points based on requirements specification. 

2. Calibrate estimation software using historical data from within our organization. 

**186 Part II Fundamental Estimation Techniques** 

## **Table 17-3 Example Standardized Estimation Procedure for Sequential Projects— Emphasis on Estimating Cost and Schedule** 

3. Estimate the nominal effort and schedule using a commercial estimation software package. 

C. Iterate estimates II.A(1), II.A(2), and II.B until the estimates converge to within 5% of each other. Use the average of these estimates as the nominal, N. 

- D. Compute estimate range as 0.8N to 1.25N. 

1. Budget shall be allocated based on 1.0N. 

2. Contingency budget shall be allocated as 0.25N. 

3. Additional contingency may be allocated to allow for organization’s historical rate of requirements growth. 

4. Only the high end of the range (1.25N) should be published. 

5. This estimate shall not be used for external commitments. 

## **III. Preliminary Commitment Estimate (After Second Interim Release)** 

A. Build a bottom-up estimate. 

1. Create a detailed task list. 

(a) Task list shall be reviewed by the development lead, test lead, and documentation lead. 

2. Have each developer, tester, and other individual contributors estimate the effort required to implement the tasks that he or she will be responsible for. 

- (a) Tasks shall be estimated using best case, worst case, and expected case. 

(b) Task nominals should be computed using the formula [BestCase + ( 4 x MostLikelyCase) + WorstCase] / 6. 

3. Add up the individual module nominals. 

B. Compare II.C to III.A(3). Compute a nominal estimate, N, using the following formula: (2 x TheHigherEstimate + TheLowerEstimate) / 3 

- C. Compute estimate ranges as from 1.0 N to 1.1 N. 

1. The high end of the range (1.1N) may be published externally. 

2. External commitments may be made to 1.1N. 

3. The range 1.0N to 1.1N may be published internally. 

## **IV. Final Commitment Estimate (After Third Interim Release)** 

- A. Compare estimated results to actual results from step III. 

1. Compute a revised nominal based on the following formula:   RemainingEffort = PlannedRemainingEffort * (ActualEffortToDate * PlannedEffortToDate) 

2. Add any tasks that were omitted from step III. 

- B. The sum of IV.A.1 and IV.A.2 may be used as the new Nominal Effort, N. 

1. The nominal (1.0N) may be published externally. 

2. External commitments may be made to 1.0N. 

3. The range 0.9N to 1.1N may be published internally. 

## **V. Project Shall Be Reestimated at Any Time in Response to Major Changes in Project Assumptions** 

A. Changes in assumptions include but are not limited to increase in requirements, changes in definitions of major requirements, changes in staff availability, and changes in schedule targets. 

**Chapter 17 Standardized Estimation Procedures 187** 

> **Table 17-3 Example Standardized Estimation Procedure for Sequential Projects— Emphasis on Estimating Cost and Schedule** 

## **VI. Project Completion** 

- A. Collect and archive data on actual project results for future use. 

- B. Review estimate accuracy of each estimate. 

1. Analyze root causes of any major errors. 

2. Assess whether the same accuracy could be produced with less effort. 

3. Propose revisions to the standardized estimation procedure. 

The estimation procedure shown in Table 17-3 illustrates all of the elements commonly found in estimation procedures: 

_**Emphasizes counting and computing when possible, rather than using judgment**_ The estimates created for the Exploratory Estimate (Estimate I in Table 17-3) call for decomposition via a work breakdown structure, estimation by analogy, and estimation using standard components. None of these approaches is terribly accurate, but each involves at least some computation rather than just pure judgment. 

_**Calls for use of multiple estimation approaches and comparison of results**_ The first three estimates (Estimates I, II, and III) call for multiple estimation approaches. More approaches are used early in the project, when computationally based approaches are not as available. 

_**Communicates a plan to reestimate at predefined points in the project**_ The plan calls for Estimates I through V, which indicates an intent to reestimate periodically. Each estimate is linked to specific milestones in the project. 

_**Defines how the required estimation approach changes over the course of a project**_ The details of each step are different, based on the improving project-generated data that becomes available later in the project. Late in the project, historical data from the same project becomes the primary basis for the estimate. 

_**Contains a clear description of an estimate’s inaccuracy**_ Each of the stages in the procedure contains an expression of inaccuracy. Estimate I.C calls for a range of –50% to +100%, narrowing to ±10% in Estimate IV.B. 

_**Defines when an estimate can be used as the basis for a project budget**_ Estimate II is referred to as the “Budget Estimate.” Estimate I states explicitly that it shall not be used becomes the basis for a budget. 

_**Defines when an estimate can be used as the basis for internal and external commitments**_ Estimate III is called the “Preliminary Commitment Estimate,” and Estimate IV is called the “Final Commitment Estimate.” Earlier estimates explicitly state that they shall not be used as the basis for external commitments. 

**188 Part II Fundamental Estimation Techniques** 

## **17.4 An Example of a Standardized Estimation Procedure for Iterative Projects** 

Table 17-4 shows an estimation procedure that’s suitable for iterative software projects. This sort of procedure tends to be most useful in organizations that are on an annual budgeting cycle. The budget is fixed at the beginning of the cycle, which means staffing levels are also fixed. The estimation challenge is thus not to estimate cost (which is fixed by the budget) or schedule (which defaults to a year for annual budgeting cycles). The challenge is estimating the amount of functionality that can be delivered with fixed staff and within a fixed timeframe. 

The procedure defined in Table 17-4 assumes that the iterations are well controlled— that is, that each iteration is brought to a releasable level of quality, “cleanup work” is performed within each release and does not accumulate off-plan, and so on. 

## **Table 17-4 Example Standardized Estimation Procedure for Iterative Projects— Emphasis on Estimating Features** 

## **I. Exploratory Estimate (To Plan First Iteration)** 

- A. Planned feature set shall be estimated using Story Points. 

- B. First iteration shall be planned using the organization’s historical delivery rate. 

1. Iteration shall be no longer than 1 month. 

2. No estimate for the whole project shall be made. 

3. No commitments shall be made. 

## **II. Planning Estimate (To Plan Second and Third Iterations)** 

- A. Average Story Points per staff week shall be calculated (to calibrate effort). 

- B. Average Story Points per calendar week shall be calculated (to calibrate schedule). 

- C. Data from II.A and II.B shall be used to plan the second and third iterations. 

1. Iterations shall be no longer than 1 month each. 

2. A nominal estimate for the whole project shall be made in terms of number of Story Points that can be delivered in the amount of time and staffing level allowed (N). 

- (a) Estimate may be published internally as 0.75N to 1.0N. 

- (b) Estimate shall not be published externally. 

- (c) No commitments shall be made. 

## **III. Commitment Estimate (After Third Iteration)** 

- A. Average story points per staff week shall be calculated based on first three iterations (to calibrate effort). 

- B. Average Story Points per calendar week shall be calculated based on first three iterations (to calibrate schedule). 

- C. Data from III.A and III.B shall be used to plan remainder of project. 

1. A nominal estimate for the whole project shall be made in terms of number of Story Points that can be delivered in amount of time and staffing level allowed (N). 

- (a) Estimate may be published internally as 0.9N to 1.1N. 

**189** 

**Chapter 17 Standardized Estimation Procedures** 

## **Table 17-4 Example Standardized Estimation Procedure for Iterative Projects— Emphasis on Estimating Features** 

- (b) Estimate may be published externally as 0.9N to 1.0N. 

- (c) Commitments may be made based on 0.9N to 1.0N. 

## **IV. Project Shall Be Reestimated at Any Time in Response to Major Changes in Project Assumptions** 

A. At a minimum, project estimation calibrations shall be updated after each third iteration to account for changes in staffing, increased productivity, and other factors. 

## **V. Project Completion** 

- A. Collect and archive data on actual project results for future use. 

- B. Review estimate accuracy of each estimate. 

1. Analyze root causes of any major errors. 

2. Assess whether the same accuracy could be produced with less effort. 

3. Propose revisions to the standardized estimation procedure. 

The procedure shown in Table 17-4 also illustrates many of the elements usually found in estimation procedures: 

_**Emphasizes counting and computing when possible, rather than using judgment**_ In Estimate II, data from the project is fed back into the estimation process so that estimates from that point forward can be computed based on the project’s historical data. 

_**Calls for use of multiple estimation approaches and comparison of results**_ This procedure does not call for multiple approaches. If you were to use this procedure and you found that Story Points were not providing good predictive accuracy, you should amend the procedure to use additional estimation methods. 

_**Communicates a plan to reestimate at predefined points in the project**_ The plan calls for Estimates I through III, which indicates an intent to reestimate periodically. 

_**Defines how the required estimation approach changes over the course of a project**_ As with the sequential procedure, the details of each step in this procedure are different based on the historical data the project has generated. 

_**Contains a clear description of an estimate’s inaccuracy**_ Estimate I simply states that no whole-project estimate shall be made, and Estimate II provides an uncertainty range of 75% of intended functionality to 100% of intended functionality. 

_**Defines when an estimate can be used as the basis for a project budget**_ In this case, the financial budget is assumed. 

_**Defines when an estimate can be used as the basis for internal and external commitments**_ Estimate III is called the “Commitment Estimate.” Earlier estimates explicitly state that they shall not be used as the basis of external commitments. 

**190 Part II Fundamental Estimation Techniques** 

## **17.5 An Example of a Standardized Estimation Procedure from an Advanced Organization** 

Table 17-5 shows the estimation procedure used by the NASA Software Engineering Lab (SEL), one of the world’s most advanced software development organizations. 

**Table 17-5 NASA SEL Estimation Procedure** 

|**Table 17-5**<br>**NAS**|**A SEL Estimati**|**on Procedur**|**e**|||
|---|---|---|---|---|---|
|**Inputs**||**Outputs**||||
||**Input Data**|**Size**|**Effort**|**Schedule**|**Uncertainty**|
|**Project Phase**|**for Estimate**|**Estimate**|**Estimate**|**Estimate**|**Range1**|
|End of require-|Number of|11,000 lines|3,000 hours|Multiply|+75%|
|ments analysis|subsystems.|of code2per|per sub-|number of|–43%|
|||subsystem.|system.|subsystems||
|||||by 83 weeks||
|||||and divide||
|||||by number||
|||||of staff||
|||||members.||
|End of prelimi-|Number of|190 lines of|52 hours per|Multiply|+40%|
|nary design|functions|code per|unit.|number of|–29%|
||and/or rou-|unit.||units by||
||tines (units).|||1.45 weeks||
|||||and divide||
|||||by number||
|||||of staff||
|||||members.||
|End of detailed|Number of|Lines of|0.31 hours|Multiply|+25%|
|design|new and|code = 200 x|per line of|lines of code|–20%|
||extensively|(N + 0.2R)|code.|by 0.0087||
||modified|||weeks and||
||units (N).|||divide by||
||Number of|||number||
||reused and|||of staff||
||slightly mod-|||members.||
||ified units (R)|||||
|End of imple-|Current size|Add 26% to|Add 43% to|Add 54% to|+10%|
|mentation|in lines of|current size|effort|schedule|–9%|
||code.|(for growth|already|already||
||Effort|during|expended|expended.||
||expended to<br>date.|testing).|(to compute<br>effort to|||
||Schedule||complete).|||
||expended to|||||
||date.|||||



**191** 

**Chapter 17 Standardized Estimation Procedures** 

**Table 17-5 NASA SEL Estimation Procedure** 

|**Table 17-5**<br>**NAS**|**A SEL Estimati**|**on Procedu**|**re**|||
|---|---|---|---|---|---|
|**Inputs**||**Outputs**||||
||**Input Data**|**Size**|**Effort**|**Schedule**|**Uncertainty**|
|**Project Phase**|**for Estimate**|**Estimate**|**Estimate**|**Estimate**|**Range1**|
|End of system|Effort|Final soft-|Add 11% to|Add 18% to|+5%|
|testing|expended to|ware size|effort|schedule|–5%|
||date.|has been|already|already||
|||reached.|expended|expended.||
||||(to compute|||
||||effort to|||
||||complete).|||



1. To allow for staff turnover, growth in requirements, and so on, conservative management practice calls for using estimates that lie between the predicted value and the upper bound. 

> 2. “Lines of code” includes all source statements, including comments and blank lines. 

Source: Adapted from _Manager’s Handbook for Software Development, Revision 1_ (NASA SEL 1990). 

The most noteworthy aspect of the NASA SEL’s estimation procedure is that it requires less work to create a more accurate estimate. This is representative of a more general rule that, the more sophisticated your estimates become, the less effort you will need to create accurate estimates. 

The specific numbers in this estimation procedure are specific to the NASA SEL. They have been calibrated through decades of data collection and analysis and are for use by a highly sophisticated development organization. The specific numbers won’t apply to other organizations. 

The differences from the procedures that can be used by less advanced organizations are instructive, as are some of the similarities: 

_**Emphasizes counting and computing when possible, rather than using judgment**_ The NASA SEL procedure is interesting in that even early-in-the-project estimates are based on counting and computing rather than judgment. Effort and schedule are never estimated directly. 

_**Calls for use of multiple estimation approaches and comparison of results**_ This procedure is distinctive in that it does not call for the use of multiple approaches at any one point in time. The NASA SEL has been collecting and analyzing historical data long enough that it can produce accurate estimates with low effort. 

_**Communicates a plan to reestimate at predefined points in the project**_ Table 17-5 indicates several points in the project at which new estimates will be created. 

_**Defines how the required estimation approach changes over the course of a project**_ Each row in the table represents a different estimation approach for a different time in the project. 

**192 Part II Fundamental Estimation Techniques** 

_**Contains a clear description of an estimate’s inaccuracy**_ The right-most column in the table contains the plus and minus qualifiers used to adjust the nominal estimate. The first footnote presents a good general guideline: “Conservative management practice calls for using estimates that lie between the predicted value and the upper bound.” 

_**Defines when an estimate can be used as the basis for a project budget**_ That element is not expressed in this procedure. 

_**Defines when an estimate can be used as the basis for internal and external commitments**_ That element is not directly expressed in this procedure. A noteworthy aspect of the table is that the first row in the table is for “End of requirements analysis.” In the NASA SEL’s terminology, “requirements analysis” is an activity that occurs after “requirements specification.” Thus the table implies that the first time in the project an estimate can even be created is relatively deep into the Cone of Uncertainty. 

## **17.6 Improving Your Standardized Procedure** 

When ad hoc estimation procedures are used, it’s difficult to improve your estimates because you’re never really sure which estimation practices produced the inaccurate estimates. When you use a standardized procedure, you’ll know the steps that produced each estimate so that you can repeat the successes and prevent the failures. 

After each project, you should assess the effectiveness of your estimates in several ways: 

- How accurate were your estimates? Did your ranges include the final result, as discussed in Section 16.6, “A View of a Well-Estimated Project”? 

- Were your ranges wide enough? Could they be made narrower and still account for the variability that you’ve observed? 

- Did your estimates tend to be on the low side or the high side, or was the error tendency neutral? 

- Were there sources of bias that affected the estimate? 

- Which techniques produced the most accurate estimates? Do those techniques generally produce the most accurate estimates, or did they just happen to produce the best estimates in this case? 

- Did you reestimate at the right times? Were there too many reestimates, too few, or the right number? 

- Was the estimation process more elaborate than it needed to be? How could you streamline it without sacrificing accuracy? 

**Chapter 17 Standardized Estimation Procedures 193** 

**Tip #79** Review your projects’ estimates and estimation process so that you can improve the accuracy of your estimates and minimize the effort required to create them. 

## **Additional Resources** 

Boehm, Barry W. _Software Engineering Economics_ . Englewood Cliffs, NJ: Prentice-Hall, Inc., 1981. Chapter 21 describes a seven-step approach to estimating software projects. 

Cooper, Robert G. _Winning at New Products: Accelerating the Process from Idea to Launch_ . New York, NY: Perseus Books Group, 2001. Cooper is the father of stage-gate processes. This book describes how to develop your own stage-gate process. 

McGarry, John, et al. _Practical Software Measurement: Objective Information for Decision Makers_ , Boston, MA: Addison-Wesley, 2002. Section 5.1 discusses considerations to include in an estimation procedure. 

NASA SEL. _Manager’s Handbook for Software Development, Revision 1_ . Document number SEL-84-101. Greenbelt, MD: Goddard Space Flight Center, NASA, 1990. This document describes the NASA SEL’s estimation approach in more detail. 

