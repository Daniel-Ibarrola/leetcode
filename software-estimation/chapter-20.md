## Chapter 20 **Special Issues in Estimating Schedule** 

## **Applicability of Techniques in This Chapter** 

||||**Jones’s**||
|---|---|---|---|---|
||**The Basic**|**Informal**|**First-Order**||
||**Schedule**|**Comparison to**|**Estimation**|**Estimation**|
||**Equation**|**Past Projects**|**Practice**|**Software Tools**|
|What’s Estimated|Schedule|Schedule|Schedule|Schedule|
|Size of project|- M L|S M L|- M L|- M L|
|Development stage|Early|Early|Early|Early|
|Iterative or sequential|Sequential|Both|Sequential|Both|
|Accuracy possible|Medium|Medium|Low|High|

The need to meet customer deadlines, trade show deadlines, seasonal sales-cycle deadlines, regulatory deadlines, and other calendar-oriented deadlines seems to put much of the estimation pressure on the schedule. The schedule estimate seems to produce most of the heat in estimation discussions. 

Ironically, once you move from intuitive estimation approaches to approaches based on historical data, the schedule estimate becomes a simple computation that flows from the size and effort estimates. If T.S. Eliot had written poems about software, he might have written 

_This is the way the estimate ends This is the way the estimate ends This is the way the estimate ends Not with a bang but a whimper_ 

## **20.1 The Basic Schedule Equation** 

A rule of thumb is that you can estimate schedule early in a project using the Basic Schedule Equation: 

**Equation #17** 

ScheduleInMonths = 3.0 × StaffMonths[1/3] 

**221** 

**222 Part III Specific Estimation Challenges** 

In case your math is a little rusty, the 1/3 exponent in the equation works the same as taking the cube root of _StaffMonths_ . 

Sometimes the 3.0 is a 2.0, 2.5, 3.5, 4.0 or similar number, but the basic idea that schedule is a cube-root function of effort is almost universally accepted by estimation experts. (The specific number is one that can be derived through calibration with your organization’s historical data.) Barry Boehm commented in 1981 that this formula was one of the most replicated results in software engineering (Boehm 1981). Additional analysis over the past few decades has continued to affirm the validity of the schedule equation (Boehm 2000, Stutzke 2005). 

To use the equation, suppose you’ve estimated that you will need 80 staff months to build your project. The schedule computed from this formula ranges from 8.6 to 17.2 months depending on what coefficient from 2.0 to 4.0 is used. The nominal schedule will be (3.0 x 80[1/3] ), which is 12.9 months. (I don’t recommend presenting the schedule estimate with this much precision; I’m including it here to make the calculations easier to follow.) 

**Tip #89** Use the Basic Schedule Equation to estimate schedule early in medium-to-large projects. 

The schedule equation has some interesting implications for the Cone of Uncertainty, as shown by the numbers on the right axis of Figure 20-1. 

**==> picture [358 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
4x 1.6x<br>2x 1.25x<br>Variability in 1.5x 1.15x<br>the Estimate 1.25x 1.1x Variability in<br>of Project 1.0x 1.0x the Estimate<br>Scope 0.8x 0.9x of Project<br>(effort, cost, Schedule<br>0.67x 0.85x<br>features)<br>0.5x 0.8x<br>0.25x 0.6x<br>Time<br>**----- End of picture text -----**<br>


**Figure 20-1** The Cone of Uncertainty, including schedule adjustment numbers on the right axis. The schedule variability is much lower than the scope variability because schedule is a cube-root function of scope. 

**Chapter 20 Special Issues in Estimating Schedule 223** 

The schedule equation is the reason that the uncertainty ranges in Figure 20-1 are much broader for efforts than they are for schedules. Effort increases in proportion to scope, whereas schedule increases in proportion to the cube root of effort. 

The schedule equation implicitly assumes that you’re able to adjust the team size to suit the size implied by the equation. If your team size is fixed, the schedule won’t vary in proportion to the cube root of the scope; it will vary more widely based on your team-size constraints. Section 20.7, “Schedule Estimation and Staffing Constraints,” will discuss this issue in more detail. 

The Basic Schedule Equation is also not intended for estimation of small projects or late phases of larger projects. You should switch to some other technique when you know the names of the specific people working on the project. 

## **20.2 Computing Schedule by Using Informal Comparisons to Past Projects** 

William Roetzheim proposes estimating schedules of new projects based on a ratio of schedule and effort from past projects (Roetzheim 1988, Stutzke 2005). We’ll use the same projects that were used in Chapter 19, “Special Issues in Estimating Effort,” which are repeated in Table 20-1 for reference. 

**Table 20-1 Example of Past Project Efforts and Schedules for Estimating Future Schedules** 

|**Table 20-1**<br>**Schedules**|**Example of P**|**ast Project E**|**fforts and S**|**chedules for E**|**stimating Future**|
|---|---|---|---|---|---|
|||**Schedule**|**Effort**|**Productivity**||
|||**(Calendar**|**(Staff**|**(LOC/Staff**||
|**Project**|**Size (LOC)**|**Months)**|**Months)**|**Month)**|**Comments**|
|Project A|33,842|8.2|21|1,612||
|Project B|97,614|12.5|99|986||
|Project C|7,444|4.7|2|3,722|Not used—too small|
||||||for comparison|
|Project D|54,322|11.3|40|1,358||
|Project E|340,343|24.0|533|639|Not used—too large|
||||||for comparison|



Roetzheim suggests estimating schedule in months by using the Informal Comparison to Past Projects formula: 

**==> picture [43 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>#18<br>**----- End of picture text -----**<br>


EstimatedSchedule = PastSchedule × (EstimatedEffort / Past Effort)[1/3] 

The exponent of 1/3 is used for what this book calls medium-to-large projects (more than about 50 staff months). For smaller projects, you should use an exponent of 1/2. 

**224 Part III Specific Estimation Challenges** 

Chapter 19’s effort estimate of 65 to 100 staff months, with a most likely estimate of 80 staff months,gives us the estimated schedules from past projects shown in Table 20-2. 

**Table 20-2 Example of Schedules Estimates Computed Using Informal Comparisons to Past Projects** 

|**Table 20-2**<br>**Example of Schedules Estima**<br>**to Past Projects**|**tes Computed Using Informal Comparisons**|
|---|---|
|**Historical Data**|**Estimates**|
|**Project**<br>**Past**<br>**Schedule**<br>**(Calendar**<br>**Months)**<br>**Past**<br>**Effort**<br>**(Staff**<br>**Months)**|**Low**<br>**Estimate**<br>**(65 Staff**<br>**Months)**<br>**Nominal**<br>**Estimate**<br>**(80 Staff**<br>**Months)**<br>**High**<br>**Estimate**<br>**(100 Staff**<br>**Months)**|
|Project A<br>8.2<br>21<br>Project B<br>12.5<br>99<br>Project D<br>11.3<br>40|12.0<br>12.8<br>13.8<br>10.8<br>11.6<br>12.5<br>13.2<br>14.2<br>15.3|



Roetzheim’s technique produces a best-case to worst-case range of 10.8 to 17.3 months. I would compute the Expected Case by simply averaging the three nominal estimates from the table. I would compute the low and high ends of the range by averaging the low estimates and the high estimates from the table. Those calculations produce a nominal schedule of 12.9 months with a range of 12.0 to 13.9 months. 

**Tip #90** Use the Informal Comparison to Past Projects formula to estimate schedule early in a small-to-large project. 

## **20.3 Jones’s First-Order Estimation Practice** 

If you have a function-point count, you can compute a rough schedule directly from function points by using what Capers Jones has described as the First-Order Estimation Practice (Jones 1996). To use it, take your function-point total and raise it to the appropriate power selected from Table 20-3. The Average exponents in the table are derived from Jones’s analysis of several thousand projects. I’ve added approximate Better and Worse exponents to represent variations in performance. 

**Table 20-3 Exponents for Computing Schedules from Function Points** 

|**Table 20-3**<br>**Exponents for Computing Sch**|**edules from**|**Function Poin**|**ts**|
|---|---|---|---|
|**Kind of software**|**Better**|**Average**|**Worse**|
|Object-oriented software|0.33|0.36|0.39|
|Client-server software|0.34|0.37|0.40|
|Business systems, internal intranet systems|0.36|0.39|0.42|
|Shrink-wrapped, scientific systems,|0.37|0.40|0.43|
|engineering systems, public internet systems||||
|Embedded systems, telecommunications,|0.38|0.41|0.44|
|device drivers, systems software||||



Source: Loosely adapted from “Determining Software Schedules” (Jones 1995c) and _Estimating Software Costs_ (Jones 1996). 

**Chapter 20 Special Issues in Estimating Schedule 225** 

If you estimate your project’s total number of function points to be 1,450, and you’re working in a business-systems organization with average productivity, you will raise 1,450 to the 0.39 power (1,450[0.39] ), for a rough schedule of 17 calendar months. If you are working in a best-in-class business-systems organization, you will raise 1,450 to the 0.36 power, for a schedule of 14 months. If you’re developing an object-oriented business system, the object-oriented software exponents will give you a range of 11 to 17 months. Thus, it appears that the real schedule lies somewhere in the range of 11 to 17 months. 

This practice isn’t a substitute for more careful schedule estimation, but it does provide a simple means of getting a rough schedule estimate that’s better than guessing. It can also provide a quick reality check. If you want to develop a 1,450-functionpoint business system in 9 months, you should think again. The best-in-class schedule would be 11 to 14 months, and most organizations aren’t best in class. Jones’s First-Order Estimation Practice allows you to know early on if you need to adjust your feature set expectations, schedule expectations, or both. 

**Tip #91** Use Jones’s First-Order Estimation Practice to produce a low-accuracy (but very low-effort) schedule estimate early in a project. 

## **20.4 Computing a Schedule Estimate by Using the Science of Estimation** 

In the final analysis, the art of estimation isn’t very well equipped to take the last step in producing an accurate schedule. Schedules vary too much based on too many factors. The easiest and most accurate way to compute a schedule is to use a tool such as Construx Estimate.[1] 

What happens when we use Construx Estimate to compute a schedule estimate for the case study? If we calibrate Construx Estimate with the historical effort and schedule data that was presented in Chapter 19, Construx Estimate calculates a schedule of 12.2 calendar months, with a 20% to 80% likely range of 11.6 to 12.9 months. With industry-average data, the nominal is 15.8 months and the range is 13.2 to 21.5 months! 

The discrepancy between the nominals and ranges computed using historical data and industry-average data once again illustrates the benefits of using historical data. 

1 Construx Estimate can be downloaded for free from _www.construx.com/estimate_ . 

**226 Part III Specific Estimation Challenges** 

## **20.5 Schedule Compression and the Shortest Possible Schedule** 

After the nominal schedule has been computed, the question often arises, “How much can we shorten the schedule if we need to?” The answer depends on whether the feature set is flexible. If features can be cut, the schedule can be shortened as much as you want, subject to your willingness to cut features. This amounts to doing less work in less time, which is reasonable. 

If the feature set is not flexible, shortening the schedule depends on adding staff to do more work in less time, which is also reasonable, up to a point. 

Over the past several decades, numerous estimation researchers have investigated the effects of compressing a nominal schedule. Figure 20-2 summarizes the results of their investigations. 

## Relative Effort 

**==> picture [340 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
(EffortForDesiredSchedule/<br>EffortForNominalSchedule) Jensen Putnam<br>1.4<br>1.3<br>The  DSN<br>1.2 “Impossible<br>Zone”<br>1.1 Webmo<br>Price<br>Cocomo II<br>1.0<br>0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3<br>Relative Schedule<br>0.9<br>(DesiredSchedule/NominalSchedule)<br>0.8<br>Mk II FP<br>estimating<br>method<br>0.7<br>ISBSG<br>**----- End of picture text -----**<br>


_Source: Adapted and extended from_ Software Sizing and Estimating: Mk II _(Symons 1991),_ Software Cost Estimation with Cocomo II _(Boehm et al 2000), “Estimating Web Development Costs: There Are Differences” (Reifer 2002), and_ Practical Project Estimation, 2nd Edition _(ISBSG 2005)._ 

**Figure 20-2** The effects of compressing or extending a nominal schedule and the Impossible Zone. All researchers have found that there is a maximum degree to which a schedule can be compressed. 

**Chapter 20 Special Issues in Estimating Schedule 227** 

The horizontal axis on the graph represents the relationship between the nominal schedule and the compressed schedule. A figure of 0.9 on that axis indicates a compressed schedule that takes 0.9 times as much time as the nominal schedule (that is, 90% of the nominal). The vertical axis represents the total effort required when the schedule is compressed or expanded compared to the effort required when the nominal schedule is used. A value of 1.3 on the vertical axis indicates that the compressed schedule requires 1.3 times as much total effort as the nominal schedule would require. 

Several conclusions can be drawn from the graph in Figure 20-2: 

_**Shortening the nominal schedule increases overall effort**_ All researchers have concluded that shortening the nominal schedule will increase total development effort. If the nominal schedule is 12 months with a team of 7 developers, you can’t just use 12 developers to reduce the schedule to 7 months. 

Shorter schedules require more effort for several reasons: 

- Larger teams require more coordination and management overhead. 

- Larger teams introduce more communication paths, which introduce more chances to miscommunicate, which introduce more errors, which then have to be corrected. Lawrence Putnam has observed that the shortest possible schedule is also the point at which error production is the highest (Putnam and Myers 2003). 

- Shorter schedules require more work to be done in parallel. The more work that overlaps, the higher the chance both that one piece of work will be based on another incomplete or defective piece of work and that later changes will increase the amount of rework that must be performed. 

Expert findings vary in the degree to which schedule reductions increase effort, but the experts all agree that it does. Specific tradeoffs between schedule and effort are discussed in Section 20.6. 

**Tip #92** Do not shorten a schedule estimate without increasing the effort estimate. 

_**There is an Impossible Zone, and you can’t beat it**_ If 8 people can write a program in 10 months, can 80 people write the same program in one month? Can 1,600 people write it in one day? The ineffectiveness of the extreme schedule compression in these examples is obvious. The endpoint—1,600 people working for one day—is absurd and easy to recognize. 

Finding the limits of less-extreme schedule compression is a more subtle problem, but all researchers have concluded that there is an Impossible Zone, a point beyond which a nominal schedule cannot be compressed. The consensus of researchers is that schedule compression of more than 25% from nominal is not possible. 

**228** 

**Part III Specific Estimation Challenges** 

As Figure 20-2 illustrates, for a project of a particular size, there’s a point beyond which the development schedule simply can’t be shortened. Not by working harder. Not by working smarter. And not by finding creative solutions or by making the team larger. It simply can’t be done (Symons 1991, Boehm 2000, Putnam and Myers 2003). 

**Tip #93** Do not shorten a nominal schedule more than 25%. In other words, keep your estimates out of the Impossible Zone. 

_**Extending schedule beyond the nominal schedule usually reduces total effort, if you reduce team size**_ Experts have generally concluded that increasing the schedule beyond the nominal allows for a reduction in overall effort for the same reasons that shortening a schedule increases effort. A longer schedule allows for a smaller team, which reduces communication and coordination problems. It reduces overlap among activities, which allows more defects to be fixed “in phase” before they contaminate other work and cause more rework. 

For an extended schedule to reduce effort, you must actually reduce the team size. If you simply allocate the same people to the same project fractionally instead of reducing the number of people on the team, you’ll likely make matters worse instead of better, because of the issues discussed in Section 3.1, “Is it Better to Overestimate or Underestimate?” 

**Tip #94** Reduce costs by lengthening the schedule and conducting the project with a smaller team. 

## **20.6 Tradeoffs Between Schedule and Effort** 

Lawrence Putnam’s estimation model provides some rules of thumb for schedule compression and expansion, listed in Table 20-4. 

**Table 20-4 Recommended Tradeoffs Between Effort and Schedule** 

|**Table 20-4**<br>**Recommended Tradeoffs**|**Between Effort and Schedule**|
|---|---|
|**Schedule Compression/Expansion**|**Effort Increase/Reduction**|
|–15%|+100%|
|–10%|+50%|
|–5%|+25%|
|Nominal|0%|
|+10%|–30%|
|+20%|–50%|
|+30%|–65%|
|More than +30%|Not practical|



Source: Adapted from data in _Measures for Excellence_ (Putnam and Myers 1992). 

**Chapter 20 Special Issues in Estimating Schedule 229** 

Putnam cautions that extending the schedule more than about 30% is likely to begin introducing different kinds of inefficiencies, which in turn begin increasing costs. 

Some people have criticized Putnam’s model for exaggerating the effect of schedule compression and expansion, but the International Software Benchmarking Standards Group’s 2005 data produces very similar results (ISBSG 2005). 

## **Schedule Compression and Team Size** 

One of the pitfalls of attempting to compress a schedule below the nominal, even if you avoid the Impossible Zone, is that you might increase team size above the economically effective maximum. Lawrence Putnam has conducted fascinating research on the relationship between team size, schedule, and productivity for medium-sized business systems. Figure 20-3 shows his results (Putnam and Myers 2003). 

**==> picture [359 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
50 300<br>45 Schedule<br>250<br>40 Effort<br>35<br>200<br>30<br>Effort<br>Schedule<br>25 150 (staff<br>(months)<br>months)<br>20<br>100<br>15<br>10<br>50<br>5<br>0 0<br>1.5–3 3–5 5–7 9–11 15–20<br>Team Size<br>**----- End of picture text -----**<br>


**Figure 20-3** Relationship between team size, schedule, and effort for business-systems projects of about 57,000 lines of code. For team sizes greater than 5 to 7 people, effort and schedule both increase. 

Putnam reviewed about 500 business projects that were in the range of 35,000 to 95,000 lines of code (LOC) and which averaged 57,000 LOC. He stratified these projects into 5 groups based on the sizes of the development teams. The average sizes of the projects for each team size were within 3,000 LOC of one another. Putnam found that, as team size increased from the 1.5 to 3 range to the 3 to 5 range, the schedule shortened and effort increased, which is what you would expect. As team size increased from 3–5 to 5–7, the schedule again decreased and effort again increased. But when team size increased from 5–7 to 9–11, _both the schedule and effort increased_ . And when team size increased to 15 to 20, schedule stayed flat but effort increased dramatically. 

**230 Part III Specific Estimation Challenges** 

I suspect (based on nothing but my own judgment) that Putnam’s data is showing that software’s diseconomy of scale is not a smooth, incremental function but is more like a step function that has large penalties that kick in at certain sizes. 

Putnam has not yet generalized his findings to other kinds of software or other project sizes, but for the medium-sized business-systems domain, this is an important finding: A team size of 5 to 7 people appears to be economically optimal for medium-sized business-systems projects. For larger team sizes, both schedule and effort degrade. 

## **Tip #95** 

For medium-sized business-systems projects (35,000 to 100,000 lines of code) avoid increasing the team size beyond 7 people. 

## **20.7 Schedule Estimation and Staffing Constraints** 

Nominally, you can compute the average team size by taking the effort estimate and dividing it by the schedule. If you’ve estimated a 12-month schedule for a project of 80 staff months, your average team size is just the staff months divided by the schedule, 80 divided by 12, which is 6 to 7 team members. 

The schedule estimates produced in this chapter produce the nominal schedule for a project at a particular level of effort. These techniques assume that, whatever the nominal schedule is, you’ll be able to adjust your team size to fit the level indicated. If you’re in a position to apply an average of 6 to 7 people to the project estimated in this chapter, you should be able to achieve the combination of 80-staff-month effort and 12-calendar-month schedule that’s been estimated. 

What if you have only 4 people to work on the project? What if you’re already at a point in the project where you’re assigning specific tasks? What if you have 10 people who are each available two-thirds of the time? What if the team is already intact and doesn’t need any ramp-up time? The formulas in this chapter don’t account for such factors: these formulas are macro estimation techniques that are appropriate only in the early stages of medium-to-large projects. 

Medium and large projects typically experience some ramp up of team members from the beginning to the middle of the project, and some ramp down in the final stages. A medium-sized project might average 15 people, but it might start with 5, peak at 20, and end with 10. 

Smaller projects more often use “flat staffing”—the whole team starts on Day 1 and continues through the end of the project. If your schedule estimate is 12 months but your plans show that, based on people’s availability, you will need 15 months to actually apply 80 staff months of effort, your plans should take precedence over the original schedule estimate. 

The purpose of the schedule estimates in this chapter is not to predict your final schedule to the day but to provide a sanity check on your schedule-related plans. 

**231** 

**Chapter 20 Special Issues in Estimating Schedule** 

Once you’ve used schedule estimation to ensure that your plans are reasonable, detailed planning considerations (such as who is available when) will take precedence over the initial schedule estimation described. 

**Tip #96** Use schedule estimation to ensure your plans are plausible. Use detailed planning to produce the final schedule. 

## **20.8 Comparison of Results from Different Methods** 

Here are the five schedule estimation methods we’ve used in this chapter: 

- Basic Schedule Equation 

- The Informal Comparison to Past Projects formula 

- Jones’s First-Order Estimation Practice 

- Software tool calibrated with industry-average data 

- Software tool calibrated with historical data 

Figure 20-4 shows graphically how these different schedule estimates compare. 

**==> picture [316 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Basic Schedule Equation<br>Informal Comparison to Past Projects<br>Jones's First-Order Estimation<br>Construx Estimate (Historical Data)<br>6 7 8 9 10 11 12 13 14 15 16 17 18<br>Calendar Months<br>**----- End of picture text -----**<br>


**Figure 20-4** Ranges of schedule estimates produced by the methods discussed in this chapter. The relative dot sizes and line thicknesses represent the weights I would give each of these estimates. Looking at all the estimates, including those that aren’t well founded, hides the real convergence among these estimates. 

At first glance, the schedule estimates in this example don’t seem to converge very well. One refinement that could be made is based on the Basic Schedule Equation used to generate the top line. The total range shown in Figure 20-4 is for coefficients in the Basic Schedule Equation that range from 2.0 to 4.0. If you review your historical data, you can assess how much that coefficient should actually vary. The past projects’ coefficients in this chapter’s example have ranged only from 2.7 to 3.7, which narrows the schedule range produced by the Basic Schedule Equation to 11.6 to 14.1 months. 

**232** 

**Part III Specific Estimation Challenges** 

In this case, I would again heavily weight the estimate produced with Construx Estimate both because it is an estimation-science approach and, more important, because it’s based on historical data. I would weight the Basic Schedule Equation and the Informal Comparison to Past Projects formulas second. I would not use Jones’s First-Order Estimation Practice approach at all for a situation in which I have better data. 

Figure 20-5 shows the convergence of the schedule estimates when we remove the overly generic data. 

**==> picture [319 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
Basic Schedule Equation<br>Informal Comparison to Past Projects<br>Construx Estimate (Historical Data)<br>6 7 8 9 10 11 12 13 14 15 16 17 18<br>Calendar Months<br>**----- End of picture text -----**<br>


**Figure 20-5** Ranges of schedule estimates produced by the most accurate methods. Once the estimates produced by overly generic methods are eliminated, the convergence of the estimates becomes clear. 

Based on this convergence, I would present a range of 11.5 to 14 months, and I would probably not provide an Expected Case within that range. The schedule techniques in this chapter are all early-in-the-Cone-of-Uncertainty techniques, so not providing a single-point number would normally be acceptable at this early stage of a project. 

**Tip #97** Remove the results of overly generic estimation techniques from your data set before you look for convergence or spread among your estimates. 

## **Additional Resources** 

Putnam, Lawrence H. and Ware Myers. _Five Core Metrics_ . New York, NY: Dorset House, 2003. Chapter 11 goes into detail about the efficiency penalty for exceeding 7 people on a medium-sized business-systems project. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ . Upper Saddle River, NJ: Addison-Wesley, 2005. Stutzke provides several additional methods for estimating schedule, most of which are more mathematically intensive than the techniques described in this chapter. 
