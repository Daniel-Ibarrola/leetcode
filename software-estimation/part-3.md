# **Part III Specific Estimation Challenges** 

## Chapter 18 

## **Special Issues in Estimating Size** 

## **Applicability of Techniques in This Chapter** 

||**Function Points**|**Dutch Method**|**GUI Elements**|
|---|---|---|---|
|What’s estimated|Size, Features|Size, Features|Size, Features|
|Size of project|S M L|S M L|S M L|
|Development stage|Early–Middle|Early|Early|
|Iterative or sequential|Sequential|Sequential|Sequential|
|Accuracy possible|High|Low|Low|



Once you move from directly estimating effort and schedule to computing them from historical data, size becomes the most difficult quantity to estimate. Iterative projects might use a size estimate to help determine how many features can be delivered within an iteration, but they usually focus on techniques designed to estimate features more directly. Estimation in the later stages of sequential projects tends to focus on bottom-up effort estimates created by the people who will be doing the work. Estimating size is thus most applicable to the early and middle stages of sequential projects. The purpose of a size estimate is to support long-range predictability in the wide part of the Cone of Uncertainty. 

The common size measures of lines of code and function points have different strengths and weaknesses, as do custom measures defined by organizations for their own use. Creating estimates by using multiple size measures and then looking for convergence or spread tends to produce the most accurate results. 

This chapter describes how to create the size estimate. Chapter 19, “Special Issues in Estimating Effort,” explains how to convert this chapter’s size estimates into an effort estimate, and Chapter 20, “Special Issues in Estimating Schedule,” describes how to convert the effort estimate into a schedule estimate. 

## **18.1 Challenges with Estimating Size** 

Numerous measures of size exist, including the following: 

- Features 

- User stories 

**197** 

**198 Part III Specific Estimation Challenges** 

- Story points 

- Requirements 

- Use cases 

- Function points 

- Web pages 

- GUI components (windows, dialog boxes, reports, and so on) 

- Database tables 

- Interface definitions 

- Classes 

- Functions/subroutines 

- Lines of code 

The lines of code (LOC) measure is the most common size measure used for estimation, so we’ll discuss that first. 

## **Role of Lines of Code in Size Estimation** 

Using lines of code is a mixed blessing for software estimation. On the positive side, lines of code present several advantages: 

- Data on lines of code for past projects is easily collected via tools. 

- Lots of historical data already exists in terms of lines of code in many organizations. 

- Effort per line of code has been found to be roughly constant across programming languages, or close enough for practical purposes. (Effort per line of code is more a function of project size and kind of software than of programming language, as described in Chapter 5, “Estimate Influences.” _What you get_ for each line of code will vary dramatically, depending on the programming language.) 

- Measurements in LOC allow for cross-project comparisons and estimation of future projects based on data from past projects. 

- Most commercial estimation tools ultimately base their effort and schedule estimates on lines of code. 

On the negative side, LOC measures present several difficulties when used to estimate size: 

- Simple models such as “lines of code per staff month” are error-prone because of software’s diseconomy of scale and because of vastly different coding rates for different kinds of software. 

**Chapter 18 Special Issues in Estimating Size 199** 

- LOC can’t be used as a basis for estimating an individual’s task assignments because of the vast differences in productivity between different programmers. 

- A project that requires more code complexity than the projects used to calibrate the productivity assumptions can undermine an estimate’s accuracy. 

- Using the LOC measure as the basis for estimating requirements work, design work, and other activities that precede the creation of the code seems counterintuitive. 

- Lines of code are difficult to estimate directly, and must be estimated by proxy. 

- What exactly constitutes a line of code must be defined carefully to avoid the problems described in “Issues Related to Size Measures” in Section 8.2, “Data to Collect.” 

Some experts have argued against using lines of code as a measure of size because of problems associated with using them to analyze productivity across projects of different sizes, kinds, programming languages, and programmers (Jones 1997). Other experts have pointed out that variations of the same basic issues apply to other size measurements, including function points (Putnam and Myers 2003). 

The underlying issue that’s common to lines of code, function points, and other simple size measures is that measuring anything as multifaceted as software size using a single-dimensional measure will inevitably give rise to anomalies in at least a few circumstances (Gilb 1988, Gilb 2005). 

We don’t use single-dimensional measures to describe the economy or other complex entities. We can’t even use a single measure to determine who the best hitter in baseball is. We consider batting average, home runs, runs batted in, on-base percentage, and other factors—and then we still argue about what the numbers mean. If we can’t measure the best hitter using a simple measure, why would we expect we could measure something as complex as software size using a simple measure? 

My personal conclusion about using lines of code for software estimation is similar to Winston’s Churchill’s conclusion about democracy: The LOC measure is a terrible way to measure software size, except that all the other ways to measure size are worse. For most organizations, despite its problems, the LOC measure is the workhorse technique for measuring size of past projects and for creating early-in-the-project estimates of new projects. The LOC measure is the _lingua franca_ of software estimation, and it is normally a good place to start, as long as you keep its limitations in mind. 

Your environment might be different enough from the common programming environments that lines of code are not highly correlated with project size. If that’s true for you, find something that is more proportional to effort than lines of code, count that, and base your size estimates on that instead, as discussed in Chapter 8, “Calibration and Historical Data.” Try to find something that’s easy to count, highly correlated with effort, and meaningful for use across multiple projects. 

**200 Part III Specific Estimation Challenges** 

## **Tip #80** 

Use lines of code to estimate size, but remember both the general limitations of simple measures and the specific hazards of the LOC measure. 

## **18.2 Function-Point Estimation** 

One alternative to the LOC measure is function points. A function point is a synthetic measure of program size that can be used to estimate size in a project’s early stages (Albrecht 1979). Function points are easier to calculate from a requirements specification than lines of code are, and they provide a basis for computing size in lines of code. Many different methods for counting function points exist. The standard for function-point counting is maintained by the International Function Point Users Group (IFPUG) and can be found on their Web site at _www.ifpug.org_ . 

The number of function points in a program is based on the number and complexity of each of the following items: 

_**External Inputs**_ Screens, forms, dialog boxes, or control signals through which an end user or other program adds, deletes, or changes a program’s data. They include any input that has a unique format or unique processing logic. 

_**External Outputs**_ Screens, reports, graphs, or control signals that the program generates for use by an end user or other program. They include any output that has a different format or requires a different processing logic than other output types. 

_**External Queries**_ Input/output combinations in which an input results in an immediate, simple output. The term originated in the database world and refers to a direct search for specific data, usually using a single key. In modern GUI and Web applications, the line between queries and outputs is blurry, but, generally, queries retrieve data directly from a database and provide only rudimentary formatting, whereas outputs can process, combine, or summarize complex data and can be highly formatted. 

_**Internal Logical Files**_ Major logical groups of end-user data or control information that are completely controlled by the program. A logical file might consist of a single flat file or a single table in a relational database. 

_**External Interface Files**_ Files controlled by other programs with which the program being counted interacts. This includes each major logical group of data or control information that enters or leaves the program. 

Table 18-1 shows how the count of inputs, outputs, and so on gets converted to an Unadjusted Function Point count. You multiply the number of low-complexity inputs by 3, you multiply the number of low-complexity outputs by 4, and so on. The sum of those numbers gives you the Unadjusted Function Point count. 

**Chapter 18 Special Issues in Estimating Size 201** 

**Table 18-1 Multipliers for Computing an Unadjusted Function Point Count** 

||**Function Points**|||
|---|---|---|---|
||**Low**|**Medium**|**High**|
|**Program Characteristic**|**Complexity**|**Complexity**|**Complexity**|
|External Inputs|___ × 3|___ × 4|___ × 6|
|External Outputs|___ × 4|___ × 5|___ × 7|
|External Queries|___ × 3|___ × 4|___ × 6|
|Internal Logical Files|___ × 4|___ × 10|___ × 15|
|External Interface Files|___ × 5|___ × 7|___ × 10|



Source: Adapted from _Applied Software Measurement, Second Edition_ (Jones 1997). 

After you’ve computed the Unadjusted Function Point total, you compute an Influence Multiplier based on the influence that 14 factors have on the program. These factors include data communications, online data entry, processing complexity, and ease of installation. The influence multiplier ranges from 0.65 to 1.35. When you multiply the unadjusted total by the Influence Multiplier, you get an Adjusted Function Point count. 

If you’ve read my earlier comments about “subjective control knobs,” you can probably guess what I think about the Influence Multiplier and its 14 control knobs. Two studies have found that Unadjusted Function Points are more strongly correlated with ultimate size than Adjusted Function Points are (Kemerer 1987, Gaffney and Werling 1991). Some experts also recommend eliminating the “low complexity” and “high complexity” judgments, and classifying all counted items as “medium,” which eliminates another source of subjectivity (Jones 1997). The ISO/IEC 20926:2003 standard is based on Unadjusted Function Points. 

Table 18-2 provides an example of how you would come up with the final Adjusted Function Point total. The specific number of inputs, outputs, queries, logical internal files, and external interface files shown in the table were chosen solely for purposes of illustration. 

> **Table 18-2 Example of Computing the Number of Function Points** 

|**Table 18-2**<br>**Example of Computin**|**g the Number of Function Points**|
|---|---|
||**Function Points**|
|**Program Characteristic**|**Low Complexity**<br>**Medium**<br>**Complexity**<br>**High**<br>**Complexity**|
|External Inputs<br>External Outputs<br>External Queries<br>Internal Logical Files<br>External Interface Files|_6_<br> × 3 = 18<br> _2_<br> × 4 = 8<br>_3_<br> × 6 = 18<br> _7_<br> × 4 = 28<br> _7_<br> × 5 = 35<br>_0_<br> × 7 = 0<br> _0_<br> × 3 = 0<br> _2_<br> × 4 = 8<br>_4_<br> × 6 = 24<br> _0_<br> × 7 = 0<br> _2_<br> × 10 = 20<br>_3_<br> × 15 = 45<br> _2_<br> × 5 = 10<br> _0_<br> × 7 = 0<br>_7_<br> × 10 = 70|
|**Unadjusted Function Point total**<br>**Influence multiplier**<br>**Adjusted Function Point total**|**284**<br>**1.0**<br>**284**|



**202 Part III Specific Estimation Challenges** 

The example illustrated here works out to a size of 284 function points. You can convert that directly to an effort estimate (described in Chapter 19), or you can convert it first to a lines of code estimate, and then convert that to an effort estimate. 

The terminology in the function-point approach is fairly database-oriented, but IFPUG has steadily updated the rules for counting function points, and the approach works well for all kinds of software. Studies have found that certified function-point counters will usually produce counts that are within about 10% of each other, so function-point counting presents a real possibility of narrowing the scope-related variability in the Cone of Uncertainty early in a project (Stutzke 2005). 

**Tip #81** Count function points to obtain an accurate early-in-the-project size estimate. 

## **Converting from Function Points to Lines of Code** 

If you want to convert to lines of code, Table 18-3 lists the conversion factors between function points and lines of code for several popular languages. 

**Table 18-3 Programming Language Statements per Function Point** 

|**Table 18-3**<br>**Programming L**|**anguage Statements per Function Poi**|**anguage Statements per Function Poi**|**nt**|
|---|---|---|---|
||**Programming Statements per Function**||**Point**|
||**Minimum**|**Mode**|**Maximum**|
||**(Minus 1 Standard**|**(Most Common**|**(Plus 1 Standard**|
|**Language**|**Deviation)**|**Value)**|**Deviation)**|
|Ada 83|45|80|125|
|Ada 95|30|50|70|
|C|60|128|170|
|C#|40|55|80|
|C++|40|55|140|
|Cobol|65|107|150|
|Fortran 90|45|80|125|
|Fortran 95|30|71|100|
|Java|40|55|80|
|Macro Assembly|130|213|300|
|Perl|10|20|30|
|Second generation default|65|107|160|
|(Fortran 77, Cobol, Pascal, etc.)||||
|Smalltalk|10|20|40|
|SQL|7|13|15|
|Third generation default|45|80|125|
|(Fortran 90, Ada 83, etc.)||||
|Microsoft Visual Basic|15|32|41|



Source: Adapted from _Estimating Software Costs_ (Jones 1998), _Software Cost Estimation with Cocomo II_ (Boehm 2000), and _Estimating Software Intensive Systems_ (Stutzke 2005). 

**Chapter 18 Special Issues in Estimating Size 203** 

If your 284-function-point program were to be implemented in Java, you would take the range of 40 to 80 LOC per function point from the table and multiply that by 284 function points to arrive at a size estimate of 11,360 to 22,720 LOC, with an expected value of 55 times 284, or 15,675 LOC. To avoid conveying a false sense of accuracy, you might simplify these numbers to 11,000 to 23,000 LOC with an expected case of 16,000 LOC. 

The conversion factors presented in the table use wide ranges, typically a factor of 2 to 3 between the high and low ends of the ranges. As with many other quantities you estimate, if you can collect historical data about how function points translate into lines of code in your organization, you will be able to estimate more accurately and probably with narrower ranges than if you use industry-average data. 

This section’s description of function-point counting just skims the surface of a sophisticated technique. While expert function-point counters can produce results that are within 10% of each other, counts of inexperienced function-point counters will vary by 20% to 25% (Kemerer and Porter 1992, Stutzke 2005). For more details on the technique, see the “Additional Resources” section at the end of this chapter. 

## **18.3 Simplified Function-Point Techniques** 

Function-point counting requires going through a requirements specification line by line and literally counting each input, output, file, and so on. This can be time consuming. 

Estimation experts have proposed a handful of simplified approaches to counting function points. Considering the other sources of variability that feed into a software project in the early stages when function points are relevant, a focus on minimizing the effort required to obtain a not-very-accurate estimate seems appropriate. 

## **The Dutch Method** 

The Netherlands Software Metrics Association (NESMA) suggests an “Indicative” method for early-in-the-project function-point counting (Stutzke 2005). In its method, rather than counting all inputs, outputs, and queries, only Internal Logical Files and External Interface Files are counted. An Indicative Count is then computed using this equation: 

**Equation #8** IndicativeFunctionPointCount = (35 × InternalLogicalFiles) + (15 × ExternalInterfaceFiles) 

**204 Part III Specific Estimation Challenges** 

The numbers 35 and 15 have been derived through calibration, and you would ultimately want to come up with your own calibrations for use in your environment. 

The function-point counts created using this method will be less accurate than counts created using the full function-point counting technique described in Section 18.2, “Function-Point Estimation.” But the effort required is much lower, and so this sort of approximation can be useful for rough estimates. 

## **Tip #82** 

Use the Dutch Method of counting function points to attain a low-cost ballpark estimate early in the project. 

## **GUI Elements** 

As an alternative to counting function points directly, you might count GUI elements instead. This is an example of proxy-based estimation, as described in Chapter 12, “Proxy-Based Estimates.” The process follows these steps: 

**1.** Count the number of GUI elements according to the categories in Table 18-4. 

**2.** Convert the GUI elements to an approximate function-point count by transferring appropriate entries generated from Table 18-4 to the matrix shown in Table 18-1. 

**3.** Calculate size in lines of code by using the relationships shown in Table 18-3. 

**Table 18-4 Substituting GUI Elements for Function Points** 

|**GUI Element**|**Function-Point Equivalent**|
|---|---|
|Simple Client Window|1 Low Complexity External Input for add, change, and delete (if|
||present), plus 1 Low Complexity External Query|
|Average Client Window|1 Average Complexity External Input for add, change, and delete|
||(if present), plus 1 Average Complexity External Query|
|Complex Client Window|1 High Complexity External Input for add, change, and delete (if|
||present), plus 1 High Complexity External Query|
|Average Report|1 Average Complexity External Output|
|Complex Report|1 High Complexity External Output|
|Any File|1 Low Complexity Internal Logical File|
|Simple Interface|1 Low Complexity External Input if coming in; 1 Low Complexity|
||External Output if going out|
|Average Interface|1 Average Complexity External Input if coming in; 1 Average|
||Complexity External Output if going out|
|Complex Interface|1 High Complexity External Input if coming in; 1 High Complexity|
||External Output if going out|
|Message or Dialog Box|Not counted; are counted as part of the screen they connect to|



**Chapter 18 Special Issues in Estimating Size 205** 

If you use this approach, recognize how much uncertainty is feeding into your estimate. Some uncertainty likely exists in your original counts of the number of GUI elements or your estimates of them. You introduce additional uncertainty when you convert from GUI elements to function points. And you introduce still more uncertainty when you convert from function points to lines of code. 

**Tip #83** Use GUI elements to obtain a low-effort ballpark estimate in the wide part of the Cone of Uncertainty. 

## **18.4 Summary of Techniques for Estimating Size** 

This chapter and other chapters in this book have presented numerous techniques for estimating size, including several techniques that can produce a size estimate in lines of code. Table 18-5 summarizes the techniques that have been presented so far. 

**Table 18-5 Techniques for Estimating Size** 

|**Table 18-5**<br>**Techniques**|**for Estimatin**|**g Size**|
|---|---|---|
|**Technique**|**Chapter**|**Kind of Size That Can Be Estimated**|
|Analogy|11|features, function points, Web pages, GUI com-|
|||ponents, database tables, interface definitions,|
|||lines of code|
|Decomposition|10|features, function points, Web pages, GUI com-|
|||ponents, database tables, interface definitions,|
|||lines of code|
|Dutch Method|18|function points, lines of code|
|Estimation Tools|14|function points, lines of code|
|Function Points|18|function points, lines of code|
|Fuzzy Logic|12|function points, lines of code|
|Group Reviews|13|features, user stories, story points, requirements,|
|||use cases, function points, Web pages, GUI com-|
|||ponents, database tables, interface definitions,|
|||classes, functions/subroutines, lines of code|
|GUI Elements|18|function points, lines of code|
|Standard Components|12|function points, lines of code|
|Story Points|12|story points, lines of code|
|Wideband Delphi|13|features, user stories, story points, requirements,|
|||use cases, function points, Web pages, GUI com-|
|||ponents, database tables, interface definitions,|
|||classes, functions/subroutines, lines of code|



The entries in the table’s “Kind of Size That Can be Estimated” column really depend on the calibration data you have. The most common kinds of size data—and the most generally usable—are function points and lines of code. 

**206** 

**Part III Specific Estimation Challenges** 

As Chapter 15, “Use of Multiple Approaches,” discussed, the best estimators usually use multiple estimation techniques and then look for convergence or spread among the estimates. The different approaches listed in Table 18-5 provide numerous options for estimating size in different ways and then comparing your estimates. 

**Tip #84** With better estimation methods, the size estimate becomes the foundation of all other estimates. The size of the system you’re building is the single largest cost driver. Use multiple size-estimation techniques to make your size estimate accurate. 

## **Additional Resources** 

Garmus, David and David Herron. _Function Point Analysis: Measurement Practices for Successful Software Projects_ . Boston, MA: Addison-Wesley, 2001. This book describes function-point counting and presents some simplified counting techniques. 

Jones, Capers. _Applied Software Measurement: Assuring Productivity and Quality, 2d Ed_ . New York, NY: McGraw-Hill, 1997. Jones discusses the history of function points in detail and presents the arguments against LOC measures. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ . Upper Saddle River, NJ: Addison-Wesley, 2005. Chapters 8 and 9 describe additional size-estimation techniques, including use case points, application points, Web objects, and simplified function-point techniques. Stutzke also discusses size estimation on COTS (commercial off the shelf) projects. 

_www.construx.com/resources/surveyor/_ . This site provides a free code-counting tool called Construx Surveyor. 

_www.ifpug.org._ The International Function Point Users Group is the definitive source for current function point counting rules. 

_www.nesma.nl_ . The Netherlands Software Metrics Users Association Web site provides information on the Dutch counting method. 

## Chapter 19 **Special Issues in Estimating Effort** 

## **Applicability of Techniques in This Chapter** 

||**Informal**||||
|---|---|---|---|---|
||**Comparison to**|**Estimation**|**Industry-Average**|**ISBSG**|
||**Past Projects**|**Software Tools**|**Effort Graphs**|**Method**|
|What’s estimated|Effort|Effort|Effort|Effort|
|Size of project|S M -|S M L|S M -|S M -|
|Development stage|Early–Middle|Early–Middle|Early|Early|
|Iterative or sequential|Both|Both|Sequential|Sequential|
|Accuracy possible|Medium|High|Low–Medium|Low–Medium|



Most projects eventually estimate effort directly from a detailed task list. But early in a project, effort estimates are most accurate when computed from size estimates. This chapter describes several means of computing those early estimates. 

## **19.1 Influences on Effort** 

The largest influence on a project’s effort is the size of the software being built. The second largest influence is your organization’s productivity. 

Table 19-1 illustrates the ranges of productivities between different software projects. The data in the table illustrates the hazards both of using industry-average data and of not considering the effect of diseconomies of scale. Embedded software projects, such as the Lincoln Continental and IBM Checkout Scanner projects, tend to generate code at a slower rate than shrink-wrapped projects such Microsoft Excel. If you used “average” productivity data from the wrong kind of project, your estimate could be wrong by a factor of 10 or more. 

Within the same industry, productivity can still vary significantly. Microsoft Excel 3.0 produced code at about 10 times the rate that Lotus 123 v.3 did, even though both projects were trying to build similar products and were conducted within the same timeframe. 

**207** 

**208 Part III Specific Estimation Challenges** 

Even within the same organization, productivity can still vary because of diseconomies of scale and other factors. The Microsoft Windows NT project produced code at a much slower rate than other Microsoft projects did, both because it was a systems software project rather than an applications software project and because it was much larger. 

**Table 19-1 Examples of Productivity Variation Among Different Kinds of Software Projects (* = Estimated)** 

||**New Lines**|||**Approximate**||**LOC/**|
|---|---|---|---|---|---|---|
||**of Code**|**Staff**|**Year**|**Cost in 2006**||**Staff**|
|**Product**|**Equivalent**|**Years**|**Built**|**Dollars**|**$/LOC**|**Year**|
|IBM Chief Programmer|83,000|9|1968|1,400,000*|$17|9,200|
|Team Project|||||||
|Lincoln Continental|83,000|35|1989|2,900,000|$35|2,400|
|IBM Checkout Scanner|90,000|58|1989|4,900,000|$55|1,600|
|Microsoft Word for|249,000|55|1989|8,500,000*|$34|4,500|
|Windows 1.0|||||||
|NASA SEL Project|249,000|24|2002|3,700,000*|$15|10,000|
|Lotus 123 v. 3|400,000|263|1989|36,000,000|$90|1,500|
|Microsoft Excel 3.0|649,000|50*|1990|7,700,000|$12|13,000|
|Citibank Teller Machine|780,000|150|1989|22,000,000|$28|5,200|
|Windows NT 3.1|2,880,000|2,000*|1994|200,000,000|$70|1,400|
|(first version)|||||||
|Space Shuttle|25,600,000|22,096|1989|2,000,000,000|$77|1,200|



Sources: “Chief Programmer Team Management of Production Programming” (Baker 1972), “Microsoft Corporation: Office Business Unit” (Iansiti 1994), “How to Break the Software Logjam” (Schlender 1989), “Software Engineering Laboratory (SEL) Relationships, Models, and Management Rules” (NASA, 1991), _Microsoft Secrets_ (Cusumano and Selby 1995). 

The lowest rate of productivity in Table 19-1 on a line-of-code-per-staff-year basis is the Space Shuttle software, but it would be a mistake to characterize that development team as unproductive. For projects of that size, the odds of outright failure exceed 50% (Jones 1998). The fact that the project finished at all is a major accomplishment. Its productivity was only 15% less than the Windows NT project even though the Space Shuttle software was 10 times the size of the Windows NT project, which is impressive. 

If you don’t have historical data on your organization’s productivity, you can approximate your productivity by using industry-average figures for different kinds of software: internal business systems, life-critical systems, games, device drivers, and so on. But beware of the factor of 10 differences in productivity for different organizations within the same industry. If you do have data on your organization’s historical productivity, you should use that data to convert your size estimates to effort estimates instead of using industry-average data. 

**Chapter 19 Special Issues in Estimating Effort 209** 

## **19.2 Computing Effort from Size** 

Computing an effort estimate from a size estimate is where we start to run into some of the weaknesses of the art of estimation and need to rely more on the science of estimation. 

## **Computing Effort Estimates by Using Informal Comparison to Past Projects** 

If your historical data is for projects within a narrow size range (say, a factor of 3 difference from smallest to largest), you are probably safe using a linear model to compute the effort estimate for a new project based on the effort results from similar past projects. Table 19-2 shows an example of past-project data that could form the basis for such an estimate. 

**Table 19-2 Example of Past Project Productivities for Use as the Basis of an Effort Estimate** 

|||**Schedule**|**Effort**|**Productivity**||
|---|---|---|---|---|---|
|||**(Calendar**|**(Staff**|**(LOC/Staff**||
|**Project**|**Size (LOC)**|**Months)**|**Months)**|**Month)**|**Comments**|
|Project A|33,842|8.2|21|1,612||
|Project B|97,614|12.5|99|986||
|Project C|7,444|4.7|2|3,722|Not used—too|
||||||small for comparison|
|Project D|54,322|11.3|40|1,358||
|Project E|340,343|24.0|533|639|Not used—too|
||||||large for comparison|



Suppose you’re estimating the effort for a new business system, and you’ve estimated the size of the new software to be 65,000 to 100,000 lines of Java code, with a most likely size of 80,000 lines of code. Project C is too small to use for comparison purposes because it is less than one-third the size of the low end of your range. Project E is too large to use for comparison purposes because it is more than 3 times the top end of your range. Thus your relevant historical productivity range is 986 LOC per staff month (Project B) to 1,612 LOC per staff month (Project A). Dividing the lowest end of your size range by the highest productivity rate gives a low estimate of 40 staff months. Dividing the highest end of your size range by the lowest productivity gives a high estimate of 101 staff months. Your estimated effort is 40 to 101 staff months. 

A good working assumption is that the range includes 68% of the possible outcomes (that is, ±1 standard deviation, unless you have reasons to assume otherwise). You can refer back to Table 10-6, “Percentage Confident Based on Use of Standard Deviation,” to consider other probabilities that the 40 to 101 staff-month range might include. 

**210 Part III Specific Estimation Challenges** 

## **What Kinds of Effort Are Included in This Estimate?** 

Because you’re using historical data to create this estimate, it includes whatever effort is included in the historical data. If the historical data included effort only for development and testing, and only for the part of the project from end of requirements through system testing, that’s what the estimate includes. If the historical data also included effort for requirements, project management, and user documentation, that’s what the estimate includes. 

In principle, estimates that are based on industry-average data usually include all technical work, but not management work, and all development work except requirements. In practice, the data that goes into computing industry-average data doesn’t always follow these assumptions, which is part of why industry-average data varies as much as it does. 

## **19.3 Computing Effort Estimates by Using the Science of Estimation** 

The science of estimation produces somewhat different results than the informal comparison to past projects does. If you plug the same assumptions into Construx Estimate (that is, using the historical data listed to calibrate the estimate), you get an expected result of 80 staff months, which is in the middle of the range produced by the less-formal approach. Construx Estimate gives a Best Case estimate (20% confident) of 65 staff months, and a Worst Case (80% confident) estimate of 94 staff months. 

When Construx Estimate is calibrated with industry-average data instead of historical data, it produces a nominal estimate of 84 staff months and a 20% to 80% range of 47 to 216 staff months, which is a much wider range. This again highlights the benefit of using historical data, whenever possible. 

**Tip #85** Use software tools based on the science of estimation to most accurately compute effort estimates from your size estimates. 

## **19.4 Industry-Average Effort Graphs** 

If you don’t have your own historical data, you can look up a rough estimate of effort by using an effort graph, such as those contained in Figures 19-1 through 19-9. The bold blue lines in the figures represent a project’s total technical effort (including development, quality assurance, and test) at the industry-average productivity level. The upper black line represents a level of effort that is one standard deviation higher than the average effort. I haven’t shown the effort line that is one standard deviation 

**Chapter 19 Special Issues in Estimating Effort 211** 

below the average. If you don’t have your own historical data and are using these graphs, that’s a sign that your development organization is at best average. Prudent estimation practice calls for the assumption of industry-average productivity or worse. 

The graphs show project sizes up to 250,000 lines of code, with maximum efforts on some of the graphs exceeding 10,000 staff months. For projects of that size, recognize that the use of more powerful and accurate estimation practices could easily improve project plans enough to save hundreds of thousands of dollars. Estimation guru Capers Jones has often commented that using manual methods to estimate projects larger than about 1,000 function points or 100,000 lines of code introduces significant error, and failure to use sophisticated estimation software for projects larger than about 5,000 function points or 500,000 lines of code constitutes management malpractice (Jones 1994, Jones 2005). 

The math underlying these graphs is fairly involved, and so this book doesn’t present the underlying formulas. The effort values on the graphs are presented using a logarithmic scale. The first line above 100 represents 200, the second represents 300, the first line above 1,000 represents 2,000, and so on. 

The graphs appear similar to each other, but if you closely examine specific data points, you’ll find they’re quite different. For example, compare both the average and plus-one-standard-deviation values at 100,000 lines of code, and you’ll see that the estimated staff months vary widely. 

**==> picture [355 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
100,000<br>10,000<br>Staff<br>1,000<br>Months<br>100<br>10<br>Lines of Code<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>**----- End of picture text -----**<br>


**Figure 19-1** Industry-average effort for real-time projects. 

**212 Part III Specific Estimation Challenges** 

**==> picture [355 x 495] intentionally omitted <==**

**----- Start of picture text -----**<br>
100,000<br>10,000<br>Staff<br>1,000<br>Months<br>100<br>10<br>Lines of Code<br>Figure 19-2 Industry-average effort for embedded systems projects.<br>10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>**----- End of picture text -----**<br>


**Figure 19-2** Industry-average effort for embedded systems projects. 

**Figure 19-3** Industry-average effort for telecommunications projects. 

**Chapter 19 Special Issues in Estimating Effort 213** 

**==> picture [349 x 496] intentionally omitted <==**

**----- Start of picture text -----**<br>
10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>Figure 19-4 Industry-average effort for systems software and driver projects.<br>10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>**----- End of picture text -----**<br>


**Figure 19-4** Industry-average effort for systems software and driver projects. 

**Figure 19-5** Industry-average effort for scientific systems and engineering research projects. 

**214 Part III Specific Estimation Challenges** 

**==> picture [349 x 495] intentionally omitted <==**

**----- Start of picture text -----**<br>
10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>Figure 19-6 Industry-average effort for shrink-wrap and packaged software projects.<br>10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>**----- End of picture text -----**<br>


**Figure 19-6** Industry-average effort for shrink-wrap and packaged software projects. 

**Figure 19-7** Industry-average effort for public internet systems projects. 

**Chapter 19 Special Issues in Estimating Effort 215** 

**==> picture [349 x 496] intentionally omitted <==**

**----- Start of picture text -----**<br>
1,000<br>100<br>Staff<br>Months<br>10<br>1<br>Lines of Code<br>Figure 19-8 Industry-average effort for internal intranet projects.<br>10,000<br>1,000<br>Staff<br>100<br>Months<br>10<br>1<br>Lines of Code<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>010,00020,00030,00040,00050,00060,00070,00080,00090,000100,000110,000120,000130,000140,000150,000160,000170,000180,000190,000200,000210,000220,000230,000240,000250,000<br>**----- End of picture text -----**<br>


**Figure 19-8** Industry-average effort for internal intranet projects. 

**Figure 19-9** Industry-average effort for business systems projects. 

**216 Part III Specific Estimation Challenges** 

Using the industry-average graphs, we can reestimate the example that began in Section 19.2, “Computing Effort from Size.” That was a business-systems project with a size estimated between 65,000 and 100,000 lines of code. According to Figure 19-9, the average effort for a 65,000-LOC business system would be about 85 staff months. The average effort for a 100,000-LOC system would be about 170 staff months. If we had to use the upper line rather than the average line, the estimate would range from 300 to 600 staff months. 

**Tip #86** Use industry-average effort graphs to obtain rough effort estimates in the wide part of the Cone of Uncertainty. For larger projects, remember that more powerful estimation techniques are easily cost-justified. 

## **19.5 ISBSG Method** 

The International Software Benchmarking Standards Group (ISBSG) has developed an interesting and useful method of computing effort based on three factors: the size of a project in function points, the kind of development environment, and the maximum team size (ISBSG 2005). Presented by project type, the following eight equations are the ones you’d use to estimate effort using this approach. The equations produce an estimate in staff months, assuming 132 project-focused hours per staff month (that is, excluding vacations, holidays, training days, company meetings, and so on). The General formula is a general-purpose formula for use on all project types and is based on calibration data from about 600 projects. The other categories are calibrated with data from 63 to 363 projects. 

## **Kind of project: General** 

**Equation** StaffMonths = 0.512 × FunctionPoints[0.392] × MaximumTeamSize[0.791] **#9** 

## **Kind of project: Mainframe** 

**Equation** StaffMonths = 0.685 × FunctionPoints[0.507] × MaximumTeamSize[0.464] **#10** 

**Chapter 19 Special Issues in Estimating Effort 217** 

## **Kind of project: Mid-Range** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.472 × FunctionPoints [0.375]  × MaximumTeamSize [0.882]<br>#11<br>**----- End of picture text -----**<br>


## **Kind of project: Desktop** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.157 × FunctionPoints [0.591]  × MaximumTeamSize [0.810]<br>#12<br>**----- End of picture text -----**<br>


## **Kind of project: Third Generation Language** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.425 × FunctionPoints [0.488]  × MaximumTeamSize [0.697]<br>#13<br>**----- End of picture text -----**<br>


## **Kind of project: Fourth Generation Language** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.317 × FunctionPoints [0.472]  × MaximumTeamSize [0.784]<br>#14<br>**----- End of picture text -----**<br>


## **Kind of project: Enhancement** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.669 × FunctionPoints [0.338]  × MaximumTeamSize [0.758]<br>#15<br>**----- End of picture text -----**<br>


## **Kind of project: New Development** 

**==> picture [433 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
Equation<br>StaffMonths = 0.520 × FunctionPoints [0.385]  × MaximumTeamSize [0.866]<br>#16<br>**----- End of picture text -----**<br>


**218** 

**Part III Specific Estimation Challenges** 

Suppose you were creating an effort estimate for a desktop business application of 1,450 function points in Java (the same system we’ve been estimating throughout this chapter) and you have a maximum team size of 7 people. The Desktop equation suggests you will have an effort of 56 staff months: 

## 0.157 × 1,450[0.591] × 7[0.810] 

You could also use the Third Generation Language equation to get an estimate of 58 staff months: 

**==> picture [102 x 30] intentionally omitted <==**

An interesting aspect of the ISBSG method is that the formulas for effort depend on the maximum size of the project team, with smaller teams producing smaller total effort estimates. Varying the maximum team size in the example from 5 to 10 people causes the effort estimate to vary from 43 to 75 staff months. From an estimation point of view, this introduces uncertainty. From a _project control_ point of view, this difference might lead you to use a smaller team size rather than a larger one. (This topic is addressed further in “Schedule Compression and Team Size” in Section 20.6, “Tradeoffs Between Schedule and Effort.”) 

**Tip #87** Use the ISBSG method to compute a rough effort estimate. Combine it with other methods, and look for convergence or spread among the different estimates. 

## **19.6 Comparing Effort Estimates** 

To provide a reality check on these estimates, you might compare the four different approaches to effort estimates in this chapter: 

- Doing informal comparisons to past projects 

- Using estimation software 

- Using industry-average graphs 

- Using the ISBSG method 

**Chapter 19 Special Issues in Estimating Effort 219** 

If you graphed the estimate ranges from these techniques, they would look like those shown in Figure 19-10. 

**==> picture [359 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Informal Comparison<br>to Past Projects<br>Contrux Estimate<br>(Historical Data)<br>Industry-Average Graph<br>("Average" Line)<br>ISBSG Method<br>0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170<br>Staff Months<br>**----- End of picture text -----**<br>


**Figure 19-10** Ranges of estimates derived by using the methods discussed in this chapter. The relative dot sizes and line thicknesses represent the weight I would give each of the estimation techniques in this case. 

The graph shows a range of estimates from about 40 to 110 staff months. The ISBSG method and the industry-average graphs are both using industry-average data, so I would weight them less heavily than the methods that are based on historical data. With the informal comparison to past projects, I would weight the projects that are most similar (including closest in size) the most heavily. 

All things considered, in this case I would present a range of 65 to 100 staff months with an expected outcome of 80 staff months. You might think the expected outcome should fall in the middle of the range of 65 to 100, but the effort will often fall toward the low end of the range because of the issues discussed in Section 1.4, “Estimates as Probability Statements.” 

**Tip #88** Not all estimation methods are equal. When looking for convergence or spread among estimates, give more weight to the techniques that tend to produce the most accurate results. 

## **Additional Resources** 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: Addison Wesley, 2000. The Cocomo II estimation model described in this book provides formulas for converting size estimates in lines of code into effort. Keep in mind the warnings about the “control knobs” involved. 

**220 Part III Specific Estimation Challenges** 

ISBSG. _Practical Project Estimation, 2nd Edition: A Toolkit for Estimating Software Development Effort and Duration_ . Victoria, Australia: International Software Benchmarking Standards Group, February 2005. This book contains numerous useful formulas for computing effort estimates from size estimates. The book is refreshingly candid about the accuracy of its formulas; it includes sample size and r-squared values you can use to assess the validity of its formulas. 

Putnam, Lawrence H. and Ware Myers. _Measures for Excellence: Reliable Software On Time, Within Budget_ . Englewood Cliffs, NJ: Yourdon Press, 1992. The Putnam model described in this book converts size estimates in lines of code into effort. 


## Chapter 21 **Estimating Planning Parameters** 

The line between project estimation and project planning is wide and blurry. Numerous planning parameters need to be estimated, including how much effort to allocate to construction, testing, requirements, and design; how many testers to have for each developer; how many effort hours you can expect to apply to a specific project in a calendar week or month; how large the risk buffer should be; and many other figures that are needed for planning purposes. 

When a project gets to the level of planning discussed in this chapter, the goals of planning tend to be antagonistic toward the goals of estimation. For example, once you estimate the amount of risk buffer you need, the purpose of risk management planning from that point forward will be to minimize the amount of the risk buffer that you actually use, essentially invalidating your estimate. 

Estimation of planning parameters is estimation at its least pure _:_ the interplay between fine-grained target setting and fine-grained estimation should be intense and highly iterative. The goal of estimation in this context is to make sure your initial plans are realistic. From that point forward, planning and project control, rather than estimation, should prevail. 

In short, planning addresses “how” to conduct a project, and estimation addresses “how much” of a quantity to plan for, which is the focus of this chapter. 

## **21.1 Estimating Activity Breakdown on a Project** 

One important planning decision is how much effort to allocate to the activities of requirements, architecture, construction, system test, and management. This choice will need to be made regardless of whether the project is sequential or iterative. In other words, the issue is not how much time to allocate to phases, it is how much effort to allocate to activities, whenever they will be performed. 

## **Estimating Allocation of Effort to Different Technical Activities** 

_Please note that the rolled-up (undecomposed) effort estimate described in Chapter 19, “Special Issues in Estimating Effort,” beginning in Section 19.2, “Computing Effort from Size,” forms the basis for the activity allocations made in this section._ 

**233** 

**234 Part III Specific Estimation Challenges** 

Table 21-1 lists the percentages of the total effort estimate that you would allocate to the basic activities of architecture, construction, and system test. ( _KLOC_ stands for “1,000 lines of code.”) Because of the diseconomy of scale described in Chapter 5, “Estimate Influences,” the proportion of effort allocated to each activity depends on the size of the project. Requirements and management work are usually treated as special cases and are discussed later. 

**Table 21-1 Approximate Technical Effort Breakdown for Projects of Different Sizes** 

|**Table 21-1**<br>**Approxima**|**te Technical Effort Breakdown for Projects of Different Sizes**|
|---|---|
|**Size**|**Activity**|
||**Architecture**<br>**Construction**<br>**System Test**|
|1 KLOC<br>25 KLOC<br>125 KLOC<br>500 KLOC|11%<br>70%<br>19%<br>16%<br>57%<br>27%<br>18%<br>53%<br>29%<br>19%<br>44%<br>37%|



Sources: Albrecht 1979; Boehm 1981; Glass 1982; Boehm, Gray, and Seewaldt 1984; Boddie 1987; Card 1987; Grady 1987; McGarry, Waligora, and McDermott 1989; Putnam and Myers 1992; Brooks 1995; Jones 1998; Jones 2000; Boehm et al, 2000; Putnam and Myers 2003; Boehm and Turner 2004; Stutzke 2005. 

The entries listed in Table 21-1 are _approximate_ . They depend on the specific technical practices you use, the life-cycle model you use, effectiveness of your quality assurance work, and many other factors. Ultimately, you should develop your own table based on your organization’s historical data. Until you’ve done that, you can use Table 21-1 as a starting point and then use the factors presented in Table 21-5 to adjust your estimate for the specific type of project you’re estimating. 

## **Estimating Requirements Effort** 

Table 21-1 does not include effort allocated to requirements. If you created your effort estimate using industry-average productivity data, that data is normally assumed not to include requirements activity. (That isn’t always true, which is one reason that industry-average data varies as much as it does.) 

If you create your estimate using your own historical data, your estimate might or might not include requirements data, depending on whether the historical data you use contains requirements data. 

Estimation models, including Cocomo II and the Putnam model, assume that the rolled-up, “main build” estimates they produce do not include requirements work. One reason is that the percentage of requirements effort varies more than the percentages of the other activities do. You can quickly rush through requirements, defining a large requirements set only very loosely, which will then require 

**Chapter 21 Estimating Planning Parameters 235** 

Herculean effort to implement. Or you can invest more time and define a smaller set of high-quality requirements, which will allow a lower effort implementation. 

With these caveats in mind, Table 21-2 lists the approximate proportion of effort you should plan for requirements work on projects of different sizes. You would add the percentage of effort from the table to your base effort estimate to compute total technical effort, including requirements work. 

**Table 21-2 Approximate Requirements-Effort Proportions for Projects of Different Sizes** 

|**Table 21-2**<br>**App**<br>**Different Sizes**|**roximate Requirements-Effort Proportions for Projects of**|
|---|---|
|**Size**|**Amount to Add to Base Effort**|
|1 KLOC|5%|
|25 KLOC|5%|
|125 KLOC|8%|
|500 KLOC|10%|



Sources: same as for Table 21-1. 

## **Estimating Management Effort** 

As with requirements effort, the rolled-up effort estimate won’t include management effort unless you’re using your own historical data and your historical data includes management effort. Table 21-3 lists approximate management effort for projects of different sizes. As with the requirements effort, you add the percentage of effort from the table, including management work, to your base effort estimate to compute total technical effort. 

**Table 21-3 Approximate Management-Effort Proportions for Projects of Different Sizes** 

|**Table 21-3**<br>**App**<br>**Sizes**|**roximate Management-Effort Proportions for Projects of Different**|
|---|---|
||**Amount to Add to Base Effort from Table 21-1 (Not Including**|
|**Size**|**Requirements Effort)**|
|1 KLOC|10%|
|25 KLOC|12%|
|125 KLOC|14%|
|500 KLOC|17%|



Sources: same as for Table 21-1. 

## **Estimating Total Activity** 

For ease of computation, Table 21-4 lists the effort to allocate to requirements, architecture, construction, system test, and management for projects of different sizes. 

**236 Part III Specific Estimation Challenges** 

This table is useful when the data you use to calibrate your rolled-up effort estimate includes both requirements and management effort. 

**Table 21-4 Total Effort Breakdown for Projects of Different Sizes** 

|**Table 21-4**<br>**To**|**tal Effort Breakdown for Projects of Different Sizes**|
|---|---|
|**Size**|**Activity**|
||**Requirements**<br>**Architecture**<br>**and**<br>**Planning**<br>**Construction**<br>**System**<br>**Test**<br>**Management**|
|1 KLOC<br>25 KLOC<br>125 KLOC<br>500 KLOC|4%<br>10%<br>61%<br>16%<br>9%<br>4%<br>14%<br>49%<br>23%<br>10%<br>7%<br>15%<br>44%<br>23%<br>11%<br>8%<br>15%<br>35%<br>29%<br>13%|



Sources: same as for Table 21-1. 

## **Adjustments Due to Project Type** 

As Chapter 5 discussed, the type of project influences the total effort on a project. It also influences the percentage of effort that will be allocated to different kinds of activities. Table 21-5 lists the adjustments you should make to your nominal activitypercentage estimate based on the kind of project you’re working on. 

**Table 21-5 Approximate Adjustments in Activity Proportions Based on Kind of Project** 

|**Table 21-5**<br>**App**<br>**of Project**|**roximate Adjustment**|**s in Activity Proportion**|**s Based on Kind**|
|---|---|---|---|
||||**Shrink-Wrap,**|
|||**Embedded Systems,**|**Scientific Systems,**|
||**Business Systems,**|**Telecommunications,**|**Engineering Systems,**|
||**Internal Intranet**|**Device Drivers,**|**Public Internet**|
|**Activity**|**Systems**|**Systems Software**|**Systems**|
|Requirements|–3%|+20%|–20%|
|Architecture|–7%|+10%|–5%|
|Construction|+5%|–10%|+2%|
|System Test|–7%|+6%|+9%|
|Management|+3%|+3%|–15%|



Sources: Putnam and Myers 1992; Jones 1998; Jones 2000; Boehm et al, 2000; Putnam and Myers 2003; Boehm and Turner 2004; Stutzke 2005. 

**Tip #98** When allocating project effort across different activities, consider project size, project type, and the kinds of effort contained in the calibration data used to create your initial rolled-up estimate. 

**Chapter 21 Estimating Planning Parameters 237** 

## **Example of Allocating Effort to Activities** 

Suppose you’re developing a business system that you’ve estimated will consist of about 80,000 lines of code (1,450 function points) and will require about 80 staff months total effort. The basic technical activity breakdown from Table 21-1 provides percentages for projects of 25 KLOC and 125 KLOC. An 80-KLOC project is about halfway between those two sizes, so we’ll use the average of the table’s 25 KLOC and 125 KLOC entries. Based on those percentages, you’ll need to allocate 17% of your effort to architecture (13.6 staff months), 55% to construction (44.0 staff months), and 28% to system test (22.4 staff months). Table 21-2 suggests that you add 6.5% for requirements work (5.2 staff months), and Table 21-3 suggests you add 13% for project management (10.4 staff months). Table 21-6 then shows how you multiply your base effort allocation by the adjustment factors for business-systems projects to compute a final effort estimate. 

**Table 21-6 Example of Adjusting a Nominal Effort Allocation Based on Project Type** 

|**Table 21-6**<br>**Exa**<br>**Project Type**|**mple of Adjusting a**|**Nominal Effort**|**Allocation Based on**||
|---|---|---|---|---|
||**Nominal Effort**|**Business-**|**Final Effort**||
||**Allocation (Staff**|**Systems**|**Allocation**||
|**Activity**|**Months)**|**Adjustment**|**(Staff Months)**|**Final %**|
|Requirements|5.2|–3%|5.0|4%|
|Architecture|13.6|–7%|12.6|13%|
|Construction|44.0|+5%|46.6|51%|
|System Test|22.4|–7%|20.8|22%|
|Management|10.4|+3%|10.7|10%|
|**TOTAL**|**95.6**|**-**|**95.7**|**100%**|



In this example, the totals for nominal effort estimate and final effort estimate work out to 95.6 and 95.7 staff months. In these calculations, the two totals sometimes don’t work out exactly the same because of rounding errors in the adjustment factors. 

Recognize that these allocations of effort to phases are approximate. They represent useful starting points for planning. Once the estimates get you into the right planning ballpark, detailed planning considerations should take precedence over these initial estimates. 

## **Developer-to-Tester Ratios** 

A common planning question is, “What should the ratio of developers to testers be?” Table 21-7 lists some common ratios. 

**238 Part III Specific Estimation Challenges** 

**Table 21-7 Examples of Developer-to-Tester Ratios** 

|**Table 21-7**<br>**Examples of Developer-to-Tester**|**Ratios**|
|---|---|
||**Commonly Observed Developer-**|
|**Environment**|**to-Tester Ratios**|
|Common business systems (internal intranet,|3:1 to 20:1 (often no test specialists|
|management information systems, and so on)|at all)|
|Common commercial systems (public internet,|1:1 to 5:1|
|shrink wrap, and so on)||
|Scientific and engineering projects|5:1 to 20:1 (often no test specialists|
||at all)|
|Common systems projects|1:1 to 5:1|
|Safety-critical systems|5:1 to 1:2|
|Microsoft Windows 2000|1:2|
|NASA Space Shuttle Flight Control Software|1:10|



The data in this table is based on observations of organizations that my company and I have worked with during the past 10 years. 

As you can see from the data in the table, ratios vary significantly even within specific kinds of software. This is appropriate, because the ratio that will work the best for a specific company or a specific project will depend on the development style of the project, the complexity of the specific software being tested, the ratio of legacy code to new code, the skill of the testers compared to the skill of the developers, the degree of test automation, and numerous other factors. 

Ultimately, the developer-to-tester ratio is settled more by planning than by estimation—that is, it’s determined more by what you think you _should_ do than by what you predict you will do. 

## **21.2 Estimating Schedule for Different Activities** 

Allocating calendar time to different activities and phases on a project tends again to be more a planning-related judgment than an estimate. Table 21-8 lists approximate schedule breakdowns for the core technical activities at different project sizes. It would be convenient if the numbers in the table weren’t expressed as ranges. The schedule for these activities tends to be influenced by when specific people become available, how fragmented their effort is between the project you’re estimating and their other responsibilities, and other factors. The schedule breakdown is thus subject to more variability than the effort breakdown is. 

**239** 

**Chapter 21 Estimating Planning Parameters** 

**Table 21-8 Approximate Schedule Breakdown At Different Project Sizes** 

|**Table 21-8**<br>**Appr**|**oximate Schedule Breakdown At Different Project Sizes**|
|---|---|
|**Size**|**Activity**|
||**Architecture**<br>**Construction**<br>**System Test**|
|1 KLOC<br>25 KLOC<br>125 KLOC<br>500 KLOC|15–25%<br>50–65%<br>15–20%<br>15–30%<br>50–60%<br>20–25%<br>20–35%<br>45–55%<br>20–30%<br>20–40%<br>40–55%<br>20–35%|



Sources: Boehm 1981; Putnam and Myers 1992; Boehm et al, 2000; Putnam and Myers 2003; Stutzke 2005. 

As with effort, the schedule for requirements is typically estimated as an add-on to the base schedule estimate. Table 21-9 lists the amount to add to the base schedule for requirements work. 

> **Table 21-9 Approximate Schedule to Add for Requirements at Different Project Sizes** 

|**Size**|**Amount to Add for Requirements**|
|---|---|
|1 KLOC|10–16%|
|25 KLOC|12–20%|
|125 KLOC|13–22%|
|500 KLOC|24–30%|



Sources: Boehm 1981; Putnam and Myers 1992; Boehm et al, 2000; Putnam and Myers 2003; Stutzke 2005. 

If your project is highly iterative, you’ll be allocating schedule within each iteration. If your project is more sequential, you’ll be allocating schedule within whole-project phases. 

|**Tip #99**|Consider your project’s size, type, and development approach in allocating schedule|
|---|---|
||to different activities.|



As with allocating effort to activities, allocating  schedule to activities is easiest to do when you have your own historical data. 

## **21.3 Converting Estimated Effort (Ideal Effort) to Planned Effort** 

Effort estimates are usually expressed in “staff months,” “staff days,” or similar terms. Such effort estimates represent _ideal_ effort, in which each effort month corresponds to one calendar month. 

**240** 

**Part III Specific Estimation Challenges** 

Mike Cohn describes the difference between ideal time and planned time as akin to the difference between the minutes on the game clock vs. the minutes on the wall clock in an American football game (Cohen 2006). A normal game of American football lasts 60 minutes on the game clock. On the wall clock, a game can last anywhere from 2 to 4 hours. 

Similarly, a software project planner shouldn’t assume that one person can perform one staff month’s worth of work in one calendar month’s time. The “effort month” might be diluted by vacation, holidays, or training; it might be split across multiple projects; or it might be affected by other factors. 

In considering how to convert ideal effort to planned effort, you should consider the following factors: 

- What hours are included in the calibration data you used to create the effort estimate? Do they include management effort, requirements, and test, or just development effort? Do they include overtime? Whatever assumptions were baked into the calibration data will flow into the estimated effort. 

- How many projects will the project’s staff be spread across? If a programmer is divided between two projects, it can take two or more calendar months to accomplish one focused project-month of effort. 

- Does your calibration data account for vacation, holidays, sick days, training time, trade show support, customer support, supporting systems that are in production, and so on? If not, you’ll need to account for those dilutions in the effort as you convert estimated effort to planned effort. 

These factors vary significantly from one organization to the next. If you work in an entrepreneurial organization in which the team can focus on a single project, you might be able to assume 40 to 50 hours per week of focused project time. In the companies I’ve seen achieve this, team members’ internal motivation has been exceptionally strong; team sizes have been small; team members have been young with minimal family obligations; the company has offered significant financial incentives; and the work environment has no red-tape or corporate-overhead activities. 

If you work in a large, established organization in which you have frequent corporateoverhead meetings and most people work about 40 hours per week, you might need to assume only 20 to 30 hours of project-focused time, and those hours might be spread across 2 or more projects. 

Reports of the average time per day that staff are able to focus on a specific project vary. Capers Jones reports that, on average, technical workers apply about 6 hours of focused project time per day to their assigned projects, or 132 hours per month (Jones 1998). The Cocomo II model assumes 152 hours of focused project time per month (Boehm et al 2000). The specific number of hours varies significantly based 

**Chapter 21 Estimating Planning Parameters 241** 

on organizational specifics, so once again you should develop data based on your organization’s track record if at all possible. 

The “Additional Resources” section at the end of this chapter provides pointers to additional information on the planning aspects of this topic. 

## **21.4 Cost Estimates** 

Estimating cost is nominally a straightforward function based on effort. However, numerous factors complicate the derivation of the cost estimate. 

## **Overtime** 

Does your organization allow uncompensated overtime? If so, some percentage of the estimated effort might not contribute toward the cost estimate. Does your organization use hourly staff or contractors who are paid more for overtime hours? If so, some of your estimated effort might contribute more than average toward the cost estimate. 

## **Is the Project Cost Based on Direct Cost, Fully Burdened Cost, or Some Other Variation?** 

Some organizations base their project costs on the employee’s “direct costs,” which are the costs directly attributable to a specific employee (payroll, payroll taxes, benefits, and so on). Other organizations base their project costs on “burdened costs,” which include corporate overhead that isn’t directly attributable to a specific employee (rent, corporate taxes, cost of human resources, sales, marketing, and so on). Depending on the size of the organization, amount of unbillable infrastructure, cost of office space, and other factors, the cost burden as a percentage of the employee’s salary can range from 30% to 125% or higher. 

## **Other Direct Costs** 

Some projects also incur costs for travel, specialized development tools, hardware, and other specific expenses. Those need to be included in the cost estimate as well. 

The “Additional Resources” section at the end of this chapter provides pointers to additional information on this topic. 

## **21.5 Estimating Defect Production and Removal** 

Defect production on a software project is a function of effort and project size, so it’s possible to estimate defect production. Knowing how many defects are likely to be produced is useful information when you are planning how much effort you’ll need to remove the defects. 

**242 Part III Specific Estimation Challenges** 

Capers Jones provides one way of looking at defect production based on a program’s size in function points (Jones 2000). As Table 21-10 indicates, Jones’s data suggests that a typical project produces a total of about 5 defects per function point. This works out to about 50 defects per 1,000 lines of code (depending on the programming language used). 

**Table 21-10 Typical Defect-Production Rates by Activity** 

|**Table 21-10**<br>**Typical**|**Defect-Production Rates by Activity**|
|---|---|
|**Activity**|**Average Defects Created**|
|Requirements|1 defect per function point|
|Architecture|1.25 defects per function point|
|Construction|1.75 defects per function point|
|Documentation|0.60 defects per function point|
|Bad fixes|0.40 defects per function point|
|**TOTAL**|**5.0 defects per function point**|



One factor that contributes to software’s diseconomy of scale is that larger projects tend to produce more defects per line of code, which requires more defect-correction effort, which in turn drives up project costs. Table 21-11 presents a breakdown of defects based on project size. 

> **Table 21-11 Project Size and Error Density** 

|**Table 21-11**<br>**Project Size and Err**|**or Density**|
|---|---|
|**Project Size (in Lines of Code)**|**Typical Error Density**|
|Smaller than 2K|0–25 errors per KLOC|
|2K–16K|0–40 errors per KLOC|
|16K–64K|0.5–50 errors per KLOC|
|64K–512K|2–70 errors per KLOC|
|512K or more|4–100 errors per KLOC|



Source: “Program Quality and Programmer Productivity” (Jones 1977), _Estimating Software Costs_ (Jones 1998). 

The industry-average ranges of defect production vary by more than a factor of 10. Historical data about defect rates on your past projects will support more accurate estimates of defect production. 

**Tip #100** Use industry-average data or your historical data to estimate the number of defects your project will produce. 

## **Estimating Defect Removal** 

Defect production is only part of the planning equation. Defect removal is the other part. The software industry has accumulated a fair amount of data about the defectremoval efficiency of the most common defect-removal techniques. Table 21-12 lists the defect-removal rates for inspections, reviews, unit testing, system testing, and other techniques. 

**Chapter 21 Estimating Planning Parameters 243** 

**Table 21-12 Defect-Removal Rates** 

|**Table 21-12**<br>**Defect-Removal Rates**||||
|---|---|---|---|
|**Removal Step**|**Lowest Rate**|**Modal Rate**|**Highest Rate**|
|Informal design reviews|25%|35%|40%|
|Formal design inspections|45%|55%|65%|
|Informal code reviews|20%|25%|35%|
|Formal code inspections|45%|60%|70%|
|Modeling or prototyping|35%|65%|80%|
|Personal desk checking of code|20%|40%|60%|
|Unit test|15%|30%|50%|
|New function (component) test|20%|30%|35%|
|Integration test|25%|35%|40%|
|Regression test|15%|25%|30%|
|System test|25%|40%|55%|
|Low-volume beta test (<10 sites)|25%|35%|40%|
|High-volume beta test (>1,000 sites)|60%|75%|85%|



Source: Adapted from _Programming Productivity_ (Jones 1986a), “Software Defect-Removal Efficiency” (Jones 1996), and “What We Have Learned About Fighting Defects” (Shull et al 2002). 

The range from lowest rate to highest rate is significant, and, as usual, historical data from your own organization will support more accurate estimates. 

## **An Example of Estimating Defect-Removal Efficiency** 

Combining the information from the defect-production and the defect-removal tables allows you to estimate the number of defects that will remain in your software at release time (and of course helps you assess the steps to take to remove more or less of the defects, depending on your quality goals). 

Suppose you have a 1,000-function-point system. Using Jones’s data from Table 2110, you would estimate that the project would generate a total of 5,000 defects. Table 21-13 shows how those defects would be removed using a typical defect-removal strategy consisting of personal desk checking of code, unit testing, integration testing, system testing, and low-volume beta testing. 

**Table 21-13 Example of Typical Defect Insertion and Defect Removal (Assuming a 1,000-Function-Point System)** 

|||**Total Defects**|**Defects Still**|
|---|---|---|---|
|**Activity**|**Effect on Defects**|**Produced So Far**|**Remaining**|
|Requirements|+1,000 defects|1,000|1,000|
|Architecture|+1,250 defects|2,250|2,250|
|Construction|+1,750 defects|4,000|4,000|
|Personal desk checking|–40%|4,000|2,400|
|of code||||



**244 Part III Specific Estimation Challenges** 

> **Table 21-13 Example of Typical Defect Insertion and Defect Removal (Assuming a 1,000-Function-Point System)** 

|||**Total Defects**|**Defects Still**|
|---|---|---|---|
|**Activity**|**Effect on Defects**|**Produced So Far**|**Remaining**|
|Documentation|+600 defects|4,600|3,000|
|Unit testing|–30%|4,600|2,100|
|Integration testing|–35%|4,600|1,365|
|System test|–40%|4,600|819|
|Bad fixes|+400 defects|5,000|1,219|
|Low-volume beta testing|–35%|5,000|792|
|**Defects remaining at**|**–84%**|**5,000**|**792 (16%)**|
|**release**||||



This typical approach to defect removal is expected to remove only about 84% of defects from the software prior to its release, which is approximately the software industry average (Jones 2000). The specific numbers you obtain using this technique are, as usual, approximate. 

Table 21-14 shows how a best-in-class organization might plan to remove defects. This example assumes the project team will produce the same total number of 5,000 defects. But defect-removal practices will include requirements prototyping, formal design inspections, personal desk-checking of code, unit testing, integration testing, system testing, and high-volume beta testing. As the data in the table shows, this combination of techniques is estimated to remove about 95% of defects prior to the software’s release. 

> **Table 21-14 Example of Best-in-Class Defect Insertion and Defect Removal (Assuming a 1,000-Function-Point System)** 

|||**Total Defects**|**Defects Still**|
|---|---|---|---|
|**Activity**|**Effect on Defects**|**Produced So Far**|**Remaining**|
|Requirements|+1,000 defects|1,000|1,000|
|Requirements prototyping|–65%|1,000|350|
|Architecture|+1,250 defects|2,250|1,600|
|Formal design inspections|–55%|2,250|720|
|Construction|+1,750 defects|4,000|2,470|
|Documentation|+600 defects|4,600|3,070|
|Personal desk checking|–40%|4,600|1,842|
|of code||||
|Unit testing|–30%|4,600|1,289|
|Integration testing|–35%|4,600|838|
|System test|–40%|4,600|503|



**245** 

**Chapter 21 Estimating Planning Parameters** 

> **Table 21-14 Example of Best-in-Class Defect Insertion and Defect Removal (Assuming a 1,000-Function-Point System)** 

|||**Total Defects**|**Defects Still**|
|---|---|---|---|
|**Activity**|**Effect on Defects**|**Produced So Far**|**Remaining**|
|Bad fixes|+400 defects|5,000|903|
|High-volume beta testing|–75%|5,000|226|
|**Defects remaining at release **|**–95%**|**5,000**|**226 (5%)**|



As with the previous example, the specific estimate of 226 defects is more precise than is supported by the underlying data. 

**Tip #101** Use defect-removal-rate data to estimate the number of defects that your quality assurance practices will remove from your software before it is released. 

Lawrence Putnam provides two additional rules of thumb for defect removal. If you want to move from 95% reliability to 99% reliability, you should plan to add 25% to the “main build” part of your schedule. You should plan to add another 25% to your schedule to improve from 99% to 99.9% reliability (Putnam and Myers 2003). (In Putnam’s terminology, “reliability” and “pre-release defect removal” are synonymous.) 

Further estimation of quality attributes can be an involved topic that relies heavily on the science of estimation. The “Additional Resources” section at the end of this chapter describes where to find more information. 

## **21.6 Estimating Risk and Contingency Buffers** 

Intuitively, we all know that high-risk projects should allow larger buffers for risk contingency and low-risk projects can get by with smaller buffers. But how large should you make the buffers? 

Risks are typically analyzed according to their severity (or impact) and probability. Table 21-15 shows an example of a table of risks, including the risks’ probabilities, severities, and risk exposures. 

**Table 21-15 Example of a Risk Lists Table for Project Schedule Risks** 

|**Table 21-15**|**Example of a Ri**|**sk Lists Table for Project**|**Schedule Risks**|
|---|---|---|---|
|**Risk**|**Probability**|**Severity, Schedule**|**Risk Exposure,  Schedule**|
|#1|5%|15 weeks|0.75 weeks|
|#2|25%|2 weeks|0.5 weeks|
|#3|25%|8 weeks|2 weeks|
|#4|50%|2 weeks|1 week|
|**TOTAL RE**||**-**|**4.25 weeks**|



**246** 

**Part III Specific Estimation Challenges** 

The severity of a risk multiplied by its probability is usually referred to as the Risk Exposure, or RE. Statistically, the RE is the risk’s “expected value,” or the amount that the project should _expect_ to add to its schedule because of its risks. For the risks listed in Table 21-15, the project should expect to add 4.25 weeks to its base schedule because of project risks. There is a 50% chance the project will add more than that and a 50% chance the project will add less than that. 

Total RE makes a good place to begin quantitative buffer planning. If you want more certainty that you will deliver on time, you should plan for a buffer that’s larger than the total RE. If you can live with a high risk of overrun, you might plan for a smaller buffer. 

RE tells only part of the story. In Table 21-15, if risk #1 or #3 hits, the project will blow past its 4.25 week expected buffer. That isn’t very likely, but you should consider the effects that specific risks would have before you settle on a final contingency buffer. 

Table 21-15 showed a risk list from the point of view of schedule risks only. Any given risk might also pose a risk to effort, cost, features, quality, or revenue. Table 21-16 shows an example of a risks list table that includes risks to schedule, cost, and revenue. 

**Table 21-16 Example of a Risk Lists Table for Project Schedule Risks** 

||||**Risk**|||||
|---|---|---|---|---|---|---|---|
|||**Severity,**|**Exposure,**||**Risk**||**Risk**|
|||**Schedule**|**Schedule**|**Severity,**|**Exposure,**|**Severity,**|**Exposure,**|
|**Risk**|**Probability**|**(Weeks)**|**(Weeks)**|**Cost**|**Cost**|**Revenue**|**Revenue**|
|#1|5%|15|0.75|$150,000|$7,500|$10,000,000|$500,000|
|#2|25%|2|0.5|$20,000|$5,000|$0|$0|
|#3|25%|8|2|$80,000|$20,000|$500,000|$125,000|
|#4|50%|2|1|$20,000|$10,000|$0|$0|
|**TOTAL RE**||**-**|**4.25**|**-**|**$42,500**|**-**|**$625,000**|



For buffer planning, you’ll need separate buffers for schedule, effort, cost, features, and quality. These buffers are only loosely related to each other. 

Remember that the severities and probabilities are estimated and that the accuracy of the aggregate RE is only as accurate as the data that went into computing it in the first place. 

**Tip #102** Use your project’s total Risk Exposure (RE) as the starting point for buffer planning. Review the details of your project’s specific risks to understand whether you should ultimately plan for a buffer that’s larger or smaller than the total RE. 

**Chapter 21 Estimating Planning Parameters 247** 

The field of risk management is well advanced, and risk management is an area in which the science of estimation can play a significant role. The “Additional Resources” section that closes this chapter describes where to find more information on risk estimation. 

## **21.7 Other Rules of Thumb** 

Here are some other rules of thumb that you can use for other planning issues: 

- For administrative and clerical support, add 5% to 10% to the base effort estimate (Stutzke 2005). 

- For IT support (lab setup, installing new software, and so on), add 2% to 4% to the base effort estimate (Stutzke 2005). 

- For configuration management/build support, add 2% to 8% to the base effort estimate (Stutzke 2005). 

- Allow for 1% to 4% increase in requirements per month (Jones 1998). 

- To go from one-company, one-campus development to multiple-company, multiple-city development, allow for a 25% increase in effort (Boehm et al 2000). 

- To go from one-company, one-campus development to international outsource development, allow for a 40% increase in effort (Boehm et al 2000). 

- For first-time development with new language and tools compared to comparable development with familiar language and tools, allow for a 20% to 40% increase in effort (Boehm et al 2000). 

- For first-time development in a new environment compared to comparable development with a familiar environment, allow for a 20% to 40% increase in effort (Boehm et al 2000). 

## **21.8 Additional Resources** 

Boehm, Barry W. _Software Engineering Economics_ . Englewood Cliffs, NJ: Prentice-Hall, Inc., 1981. Although this edition has been largely superseded by _Software Cost Estimation with Cocomo II_ (below), this edition contains interesting, detailed reference tables for effort and schedule breakdowns across activities. 

Boehm, Barry, et al. _Software Cost Estimation with Cocomo II_ . Reading, MA: AddisonWesley, 2000. Appendix A of Boehm’s book describes effort and schedule breakdowns for waterfall projects, MBASE projects, and Rational Unified Process projects. Table A.10 (which is actually six tables) provides detailed breakdowns of effort and schedule across different activities. 

**248 Part III Specific Estimation Challenges** 

Cohn, Mike. _Agile Estimating and Planning_ . Englewood Cliffs, NJ: Prentice Hall PTR, 2006. Chapter 5 of Cohn’s book contains a nice description of the differences between ideal effort and planned effort. 

DeMarco, Tom and Timothy Lister. _Waltzing with Bears: Managing Risk on Software Projects_ , New York, NY: Dorset House, 2003. This book presents a readable introduction to software risk management. 

Fenton, Norman E. and Shari Lawrence Pfleeger. _Software Metrics: A Rigorous and Practical Approach_ . Boston, MA: PWS Publishing Company, 1997. Chapter 10 contains a detailed discussion of estimating software reliability. If you don’t like equations with symbols like α, β, Ψ, φ, λ, Π, Σ, Γ , and ∫ , this is not the book for you because all these symbols show up in this chapter. 

Jones, Capers. _Estimating Software Costs_ . New York, NY: McGraw-Hill, 1998. Chapter 14 of Jones’s book contains a detailed discussion and examples of how cost buildups can vary between different kinds of organizations. Chapter 21 explains how unpaid overtime affects cost estimates. 

Jones, Capers. _Software Assessments, Benchmarks, and Best Practices_ . Reading, MA: Addison-Wesley, 2000. Jones’s book provides some data that is updated or expanded from the data he presents in _Estimating Software Costs_ . 

Putnam, Lawrence H. and Ware Myers. _Measures for Excellence: Reliable Software On Time, Within Budget_ . Englewood Cliffs, NJ: Yourdon Press, 1992. Putnam and Myers provide numerous useful rules of thumb for planning. The overall context of the book is a detailed, mathematical explanation of Putnam’s estimation model. 

Stutzke, Richard D. _Estimating Software-Intensive Systems_ . Upper Saddle River, NJ: Addison-Wesley, 2005. Chapter 12 describes approaches to effort allocation that are based on Cocomo 81 and Cocomo II. Chapters 15 and 23 focus on detailed cost estimation issues. Cost estimation and other cost-related issues are a major focus of Stutzke’s book, and various cost-related tips are sprinkled throughout. Sections 12.1 and 12.2 discuss the relationships between effort, duration, and staff availability. 

Tockey, Steve. _Return on Software_ . Boston, MA: Addison-Wesley, 2005. Chapter 15 of Tockey’s book contains a good discussion of determining unit cost, including methods of allocating overhead by using different costing methods and hazards associated with some of the methods. 

**Tip #103** Planning and estimation are related, and planning is a much bigger topic than can be addressed in one chapter in a book that focuses on software estimation. Read the literature on planning. 


