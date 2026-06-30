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

Chapter 22 

## **Estimate Presentation Styles** 

## **Applicability of Techniques in This Chapter** 

||**Matching Presentation Style to Estimate Accuracy**|
|---|---|
|What’s estimated|Size, Effort, Schedule, Features|
|Size of project|S M L|
|Development stage|Early–Late|
|Iterative or sequential|Both|
|Accuracy possible|N/A|



The way you communicate an estimate suggests how accurate the estimate is. If your presentation style implies an unfounded accuracy, you lay the groundwork for a difficult discussion about the estimate itself. This chapter presents several options for presenting estimates. 

## **22.1 Communicating Estimate Assumptions** 

An essential practice in presenting an estimate is to document the assumptions embodied in the estimate. Assumptions fall into several familiar categories: 

- Which features are required 

- Which features are not required 

- How elaborate certain features need to be 

- Availability of key resources 

- Dependencies on third-party performance 

- Major unknowns 

- Major influences and sensitivities of the estimate 

- How good the estimate is 

- What the estimate can be used for 

Figure 22-1 shows an example of an estimate that’s presented with documented assumptions. By documenting and communicating your assumptions, you help to set the expectation that your software project is subject to variability. 

**249** 

**250 Part III Specific Estimation Challenges** 

## **Project Estimate** 

The base schedule estimate is 6 calendar months, which we believe is accurate to within 25%. This estimate can be used as the basis for the project budget but not for making external commitments. The estimate is based on the following assumptions. 

- 1)  The three key technical leaders will be assigned 100% to project on March 15. 

- 2)  All development and test staff will be assigned 100% to this project by April 15. 

- 3)  Graphics-formatting subsystem will be delivered by subcontractor with acceptable quality by August 1. 

- 4)  No updates in the business rules will be required. 

- 5)  Extent of required integration with the FooBar system is unknown. This estimate has allocated 250 staff hours for that integration work. If more work than that is required, the whole-project estimate will need to be increased. 

- 6)  No more than 5 new reports will be required. 

- 7)  New development tools will produce an improvement in productivity of 20% or more compared to past projects. 

- 8)  Staff will use fewer sick days than average because most of the project occurs during the summer months. 

- 9)  After the availability dates listed in (1) and (2), staff will not be called back to support previous versions of the software. 

- 10)  The project will be able to reuse at least 80% of the database code from Version 2.0 without modifications. 

If these assumptions change, this estimate will need to be revised. 

**Figure 22-1** Example of documenting estimate assumptions. 

This approach can also be useful when you’re forced to base an estimate on assumptions that you think are unrealistic (such as assumptions 7 through 9 in Figure 22-1). You can go ahead and make the estimate, but you should also document the assumptions. Then, if the project unfolds in a way that invalidates the assumptions, you can point back to the estimate assumptions as a basis for revising the estimate. 

**Tip #104** 

Document and communicate the assumptions embedded in your estimate. 

**Chapter 22 Estimate Presentation Styles 251** 

## **22.2 Expressing Uncertainty** 

The key issue in estimate presentation is documenting the estimate’s uncertainty in a way that communicates the uncertainty clearly and that also maximizes the chances that the estimate will be used constructively and appropriately. This section describes several ways to communicate uncertainty. 

## **Plus-or-Minus Qualifiers** 

An estimate with a plus-or-minus qualifier is an estimate such as “6 months, ±2 months” or “$600,000, +$200,000, –$100,000.” The plus-or-minus style indicates both the amount and the direction of uncertainty in the estimate. An estimate of 6 months, +1/2 month, –1/2 month says that the estimate is quite accurate and that there’s a good chance of meeting the estimate. An estimate of 6 months, +4 months, –1 month says that the estimate isn’t very accurate and that there is less chance of meeting the estimate. 

When you express an estimate with plus-or-minus qualifiers, consider how large the qualifiers are and what they represent. A typical practice is to make the qualifiers large enough to include one standard deviation on each side of the core estimate. With this approach, you’ll still have a 16% chance that the actual result will come in above the top of your estimate and a 16% chance that it will come in below the bottom. If you need to account for more than the 68% probability in the middle of the one-standarddeviation range, use qualifiers that account for more than one standard deviation of variability. (See Table 10-6, “Percentage Confident Based on Use of Standard Deviation,” on page 121, for a list of standard deviations and associated probabilities.) 

Be sure to consider whether the minus qualifier should be the same as the plus qualifier. If you’re dealing with effort or schedule, typically the minus side will be smaller than the plus side for the reasons discussed in Section 1.4, “Estimates as Probability Statements.” 

A weakness of the plus-or-minus style is that, as the estimate is passed through the organization, it tends to get stripped down to just the core estimate. Occasionally, managers simplify such an estimate out of a desire to ignore the variability implied by the estimate. More often, they simplify the estimate because their manager or their corporate budgeting system can handle only estimates that are expressed as singlepoint numbers. If you use this technique, be sure you can live with the single-point number that’s left after the estimate gets converted to a simplified form. 

## **Risk Quantification** 

Risk quantification is a combination of plus-or-minus qualifiers and communication of the estimate’s assumptions. With risk quantification, you attach specific impacts to specific risks, as shown in Table 22-1. 

**252 Part III Specific Estimation Challenges** 

**Table 22-1 Example of an Estimate With Risk Quantification** 

|**Table 22-1**<br>**Exa**|**mple of an Estimate With Risk Quantification**|
|---|---|
||**Estimate: 6 months, +5 months, –1 month**|
|**Impact**|**Description of Risk**|
|+1.5 months|This version needs more than 20% new features compared to Version 2.0|
|+1 month|Graphics-formatting subsystem delivered later than planned|
|+1 month|New development tools don’t work as well as planned|
|+1 month|Can’t reuse 80% of the database code from the previous version|
|+0.5 month|Average staff sickness during the summer months instead of less sickness|
|–0.5 month|All developers assigned 100% by April 1|
|–0.5 month|New development tools work better than planned|



This is a comparatively simple example that focuses only on schedule risks. A more full-fledged example might enumerate major risks to effort and features as well as risks to the schedule. Keep in mind that this technique is an estimate _presentation_ technique. The purpose of the technique is to communicate to nontechnical stakeholders that the project presents risks. The point is not to deluge nontechnical stakeholders with detailed risk information. Thus, you should try to focus on rolled-up, large-grained risks. 

When you document the sources of uncertainty this way, you provide your project stakeholders with information they can use to reduce the risks to the project, and you lay the groundwork for explaining estimate changes in case any of the risks materialize. 

If you’re far enough into the project to have made a _commitment_ , the risks listed in Table 22-1 might be risks to meeting the commitment rather than risks to the estimate. 

This example does not present the generic uncertainty in the project that arises from the Cone of Uncertainty. If you haven’t yet made a commitment, you might need to present the Cone-related uncertainty, too. 

**Tip #105** Be sure you understand whether you’re presenting uncertainty in an estimate or uncertainty that affects your ability to meet a commitment. 

## **Confidence Factors** 

One of the questions that people often ask about a schedule is, “What chance do we have of making this date?” If you use the confidence-factor approach, you can answer that question by providing an estimate that looks like the one in Table 22-2. 

**253** 

**Chapter 22 Estimate Presentation Styles** 

> **Table 22-2 Example of a Confidence-Factor Estimate** 

|**Table 22-2**<br>**Exam**|**ple of a Confidence-Factor Estimate**|
|---|---|
|**Delivery Date**|**Probability of Delivering on or Before the Scheduled Date**|
|January 15|20%|
|March 1|50%|
|November 1|80%|



You can approximate these confidence intervals by using your “most likely” estimate and the multipliers from Table 4-1, “Estimation Error by Software-Development Activity,” on page 39, for the appropriate phase of your project. 

As discussed in Chapter 2, “How Good an Estimator Are You?” and throughout the book, avoid presenting highly confident percentages like “90% confident” unless you have a quantitatively derived basis for such a high percentage. 

Also, consider whether you really need to present low probability estimates. The fact that a result is remotely possible doesn’t mean that you have to put it on the table. I doubt that you’re currently presenting the options that are 1% likely or 0.0001% likely. Presenting only those options that are at least 50% likely is a legitimate estimation strategy. 

- **Tip #106** Don’t present project outcomes to other project stakeholders that are only remotely possible. 

Some people more easily understand data presented in a visual form than in a table form, so you might also consider a more visual presentation, such as the one shown in Figure 22-2. 

**==> picture [308 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
90%<br>80%<br>Nov<br>70%<br>Jun<br>60% Apr<br>Confidence 50% Mar<br>Level<br>40% Feb<br>30% Feb<br>20% Jan<br>Jan<br>10%<br>Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec<br>Delivery Date<br>**----- End of picture text -----**<br>


**Figure 22-2** Example of presenting percentage-confident estimates in a form that’s more visually appealing than a table. 

**254 Part III Specific Estimation Challenges** 

**Tip #107** 

Consider graphic presentation of your estimate as an alternative to text presentation. 

## **Case-Based Estimates** 

Case-based estimates are a variation on confidence-factor estimates. Present your estimates for best case, worst case, and current case combined with your commitment, or planned case. You can use the gaps between the planned case and the best and worst cases to communicate the degree of variability in the project and the degree of optimism in the plan. If the planned case is much closer to the best case, that implies an optimistic plan. Table 22-3 shows an example of case-based estimates. 

> **Table 22-3 Example of Case-Based Estimates** 

|**Table 22-3**<br>**Example of Case-B**|**ased Estimates**|
|---|---|
|**Case**|**Estimate/Commitment**|
|Best case (estimate)|January 15|
|Planned case (commitment)|March 1|
|Current case (estimate)|April 1|
|Worst case (estimate)|November 1|



The relationships between these different dates will be interesting. If the planned case and the best case are the same, and the current case and the worst case are the same, your project is in trouble! 

If you use this technique, be prepared to explain to your project’s stakeholders what would have to occur for you to achieve the best case or fall into the worst case. They will want to know about both possibilities. 

Figure 22-3 provides an example of how you might present similar information visually. 

**==> picture [308 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
90% Worst case:<br>November<br>80%<br>Current case<br>70% (50/50):<br>April<br>60%<br>Confidence 50% Commitment: March<br>Level<br>40%<br>30%<br>20% Best case: January<br>10%<br>Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec<br>Delivery Date<br>**----- End of picture text -----**<br>


**Figure 22-3** Example of presenting case-based estimates in a visual form. 

**Chapter 22 Estimate Presentation Styles 255** 

Depending on whether you’re managing more to a schedule or to a feature set, the casebased estimate can be expressed in terms of feature delivery instead of dates. Table 22-4 shows an example of how you might present a case-based estimate for features. 

**Table 22-4 Example of Case-Based Estimates for Features** 

|**Table 22-4**<br>**Example of Case-B**|**ased Estimates for Features**|
|---|---|
|**Case**|**Estimate/Commitment**|
|Best case (estimate)|100% of Level 1 features|
||100% of Level 2 features|
||100% of Level 3 features|
|Planned case (commitment)|100% of Level 1 features|
||100% of Level 2 features|
||50% of Level 3 features|
|Current case (estimate)|100% of Level 1 features|
||80% of Level 2 features|
||0% of Level 3 features|
|Worst case (estimate)|100% of Level 1 features|
||20% of Level 2 features|
||0% of Level 3 features|



## **Coarse Dates and Time Periods** 

Try to present your estimate in units that are consistent with the estimate’s underlying accuracy. If your estimates are rough, use obviously coarse numbers, such as “We can deliver this in second quarter” or “This project will require 10 staff years,” rather than misleadingly precise numbers, such as “We’ll deliver this May 21” or “This project will require 15,388 staff hours.” Consider using the following: 

- Years 

- Quarters 

- Months 

- Weeks 

In addition to expressing the message that the estimate is an approximation, the advantage of coarse numbers is that you don’t lose information when the estimate is simplified. An estimate of “6 months, +3 months, –1 month” can be simplified to “6 months.” An estimate such as “second quarter” is immune to such simplification. 

As you work your way into the Cone of Uncertainty, you should be able to tighten up your time units. Early in the Cone you might present your estimate in quarters. Later, when you’re creating bottom-up estimates based on effort for individual tasks, you can probably switch to months or weeks and eventually to days. 

**256 Part III Specific Estimation Challenges** 

## **22.3 Using Ranges (of Any Kind)** 

As discussed throughout this book, ranges are the most accurate way to reflect the inherent inaccuracy in estimates at various points in the Cone of Uncertainty. You can combine ranges with the other techniques described in this chapter (that is, ranges of coarse time periods, using ranges for a risk-quantified estimate instead of plus-or-minus qualifiers, and so on). 

When you present an estimate as a range, consider the following questions: 

_**What level of probability should your range include?**_ Should it include ±1 standard deviation (68% of possible outcomes), or does the range need to be wider? 

_**How do your company’s budgeting and reporting processes deal with ranges?**_ Be aware that companies’ budgeting and reporting processes often won’t accept ranges. Ranges are often simplified for reasons that have little to do with software estimation, such as “The company budgeting spreadsheet won’t allow me to enter a range.” Be sensitive to the restrictions your manager is working under. 

_**Can you live with the midpoint of the range?**_ Occasionally, a manager will simplify a range by publishing the low end of the range. More often, managers will average the high and low ends and use that if they are not allowed to use a range. 

_**Should you present the full range or only the part of the range from the nominal estimate to the top end of the range?**_ Projects rarely become smaller over time, and estimates tend to err on the low side. Do you really need to present the low end to high end of your estimate, or should you present only the part of the range from the nominal estimate to the high end? 

_**Can you combine the use of ranges with other techniques?**_ You might want to consider presenting your estimate as a range and then listing assumptions or quantified risks. 

**Tip #108** Use an estimate presentation style that reinforces the message you want to communicate about your estimate’s accuracy. 

## **Usefulness of Estimates Presented as Ranges** 

Project stakeholders might think that presenting an estimate as a wide range makes the estimate useless. What’s really happening is that presentation of the estimate as a wide range accurately conveys the fact that the estimate _is_ useless! It isn’t the presentation that makes the estimate useless; it’s the uncertainty in the estimate itself. You can’t remove the uncertainty from an estimate by presenting it without its uncertainty. You can only ignore the uncertainty, and that’s to everyone’s detriment. 

**Chapter 22 Estimate Presentation Styles 257** 

The two largest professional societies for software developers—the IEEE Computer Society and the Association of Computing Machinery—have jointly decided that software developers have a professional responsibility to include uncertainty in their estimates. Item 3.09 in the IEEE-CS/ACM Software Engineering Code of Ethics reads as follows: 

_Software engineers shall ensure that their products and related modifications meet the highest professional standards possible. In particular, software engineers shall, as appropriate:_ 

_3.09 Ensure realistic quantitative estimates of cost, scheduling, personnel, quality and outcomes on any project on which they work or propose to work_ and provide an uncertainty assessment of these estimates _. [emphasis added]_ 

Including uncertainty in your estimates isn’t just a nicety, in other words. It’s part of a software professional’s ethical responsibility. 

## **Ranges and Commitments** 

Sometimes, when stakeholders push back on an estimation range, they’re really pushing back on including a range in the commitment. In that case, you can present a wide estimation range and recommend that too much variability still exists in the estimate to support a meaningful commitment. 

After you’ve reduced uncertainty enough to support a commitment, ranges are generally not an appropriate way to express the commitment. An estimation range illustrates what the nature of the commitment is—more or less risky—but the commitment itself should normally be expressed as a single-point number. 

**Tip #109** Don’t try to express a commitment as a range. A commitment needs to be specific. 

## **Additional Resources** 

Gotterbarn, Don, Keith Miller, and Simon Rogerson. “Computer Society and ACM Approve Software Engineering Code of Ethics,” _IEEE Computer_ , October 1999, pp. 84–88. Available from _www.computer.org/computer/code-of-ethics.pdf_ . This article describes the adoption of the Software Engineering Code of Ethics and provides the full text of the Code. 

## Chapter 23 **Politics, Negotiation, and Problem Solving** 

## **Applicability of Techniques in This Chapter** 

||**Principled Negotiation**|
|---|---|
|What’s Estimated|Size, Effort, Features, Schedule|
|Size of Project|S M L|
|Development Stage|Early–Late|
|Iterative or Sequential|Both|
|Accuracy Possible|N/A|



Philip Metzger observed decades ago that technical staff were fairly good at estimation but were poor at defending their estimates (Metzger 1981), and I haven’t seen much evidence that technical staff have gotten better at defending their estimates in recent years. This chapter describes the reasons for the difficulty of getting an estimate accepted and an approach to help you negotiate estimates successfully. 

## **23.1 Attributes of Executives** 

One issue in estimate negotiations arises from the personalities of the people doing the negotiating. Technical staff tend to be introverts. About three-quarters of technical staff are introverts, compared with about one-third of the general population (McConnell 2004b). Most technical workers get along with other people fine, but the realm of challenging social interactions is just not their strong suit. 

Software negotiations typically occur between technical staff and executives or between technical staff and marketers. Gerald Weinberg points out that marketers and executives are often at least ten years older and more highly placed in the organization than technical staff. Plus, negotiation is part of their job descriptions (Weinberg 1994). In other words, estimate negotiations tend to be between introverted technical staff and seasoned professional negotiators. 

With this as background, it’s little wonder that technical staff look forward to software estimate negotiations about as much as they look forward to getting their 

**259** 

**260 Part III Specific Estimation Challenges** 

wisdom teeth removed without anesthesia. The factors that make negotiating with executives challenging are not likely to change any time soon. Table 23-1 lists some of these factors. 

## **Table 23-1 Ten Key Characteristics of Software Executives** 

1. Executives will always ask for what they want. 

2. Executives will always probe to get what they want if they don’t get it initially. 

3. Executives will tend to probe until they discover your point of discomfort. 

4. Executives won’t always know what’s possible, but they will know what would be good for the business if it were possible. 

5. Executives will be assertive. That’s how they got to be executives in the first place. 

6. Executives will respect you when you are being assertive. In fact, they assume you will be assertive if you need to be. 

7. Executives want you to operate with the organization’s best interests at heart. 

8. Executives will want to explore lots of variations to maximize business value. 

9. Executives know things about the business, the market, and the company that you don’t know, and they may prioritize your project’s goals differently than you would. 

10. Executives will always want visibility and commitment early (which would indeed have great business value, if it were possible). 

For the most part, executives have these characteristics because _it’s healthy for the organization for them to have them_ . Don’t expect these characteristics to change! 

**Tip #110** Understand that executives are assertive by nature and by job description, and plan your estimation discussions accordingly. 

It might well be that estimate negotiations are a part of your job that you don’t like much, but nobody ever said you get to enjoy 100% of your job. I’ve found that simply recognizing that negotiating is not my favorite activity helps me get through the negotiations more constructively. 

## **23.2 Political Influences on Estimates** 

Several nontechnical factors influence management’s response to software estimates. 

## **External Constraints** 

In many cases management is concerned with significant external influences that require the delivery of the software by a specific date or at a certain cost. There might be an external, immovable deadline (such as the Christmas shopping season, a regulatory compliance date, or a trade show). Similarly, the cost of a project might be influenced by a competitive bidding environment in which management believes 

**261** 

**Chapter 23 Politics, Negotiation, and Problem Solving** 

that your company won’t get the work if it submits a bid high enough to cover your estimate. 

The fact that an external requirement exists does not necessarily mean it’s possible to meet that requirement. It does mean that you need to make it perfectly clear to the executives you’re dealing with that you understand the requirement and that you take it seriously. 

**Tip #111** Be aware of external influences on the target. Communicate that you understand the business requirements and their importance. 

## **Budgeting and Dates** 

A consideration for many businesses is that delivery dates tend to be influenced by quarter boundaries. Companies report expenses and revenues based on quarters. Sometimes it’s easier to get a later date accepted than an earlier date because of the pressure to force the earlier date into the previous quarter. If you suggest a delivery date of July 15, you might well encounter pressure to deliver on June 30 instead— that is, in second quarter rather than third quarter. If you suggest a delivery date of September 15, a date deep into the third quarter, you might actually find that it’s easier to get that delivery date approved than it would be to get the July 15 date accepted because there will be less pressure to push the delivery back into the previous quarter. This stickiness will tend to be even stronger for dates that cross fiscal year boundaries. 

## **Negotiating an Estimate vs. Negotiating a Commitment** 

In some circumstances, negotiation is appropriate, and in others, it isn’t. We don’t negotiate questions of fact, such as the surface temperature of the Sun or the total volume of the Great Lakes. We look them up. Similarly, a software estimate is the result of an analytical activity, and it isn’t rational to negotiate the estimate. It _is_ rational to negotiate the commitment that is related to the estimate. Such a discussion might go something like this: 

_TECHNICAL LEAD: Our estimate for this project is that it will take 5 to 7 months. We’re still pretty early in the Cone of Uncertainty, so we can tighten that up as we go._ 

_EXECUTIVE: Five to 7 months is too wide a range. How about if we just use an estimate of 5 months?_ 

_TECHNICAL LEAD: We’ve found it really useful to distinguish between estimates and commitments. I can’t change the estimate, because that’s a result of a lot of computations. But I could possibly have my team commit to a delivery schedule of 5 months if we all agree that we want to take on that level of risk._ 

**262 Part III Specific Estimation Challenges** 

_EXECUTIVE: That seems like semantics to me. What’s the difference?_ 

_TECHNICAL LEAD: Our range of 5 to 7 months includes one standard deviation of variation on each side of our 50/50 estimate of 6 months. That means we have about an 84% chance that we’ll deliver within 7 months. Our estimates suggest that we have only 16% chance of actually meeting a 5-month commitment._ 

_EXECUTIVE: We need more than 50% confidence in the date we commit to, but 84% is more conservative than we need. What would the 75% confident date be?_ 

_TECHNICAL LEAD: According to the probabilities we estimated, that would be about 6.5 months._ 

_EXECUTIVE: Let’s commit to that then._ 

_TECHNICAL LEAD: That sounds good._ 

Many technical personnel view the kind of dialogue described here as a career-limiting move. In my experience, exactly the opposite is true. If you are willing to endure some uncomfortable dialogues—and if you always keep the best interests of your organization in mind—you are engaging in a career- _enhancing_ move. The real career-limiting move is to sign up for unsupported, unrealistic commitments and then fail to deliver. 

**Tip #112** You can negotiate the commitment, but don’t negotiate the estimate. 

## **What to Do if Your Estimate Doesn’t Get Accepted** 

Developers and managers sometimes worry that presenting an estimate that’s too high will cause the project to be rejected. _That’s OK._ Executive management has both the responsibility and the right to decide that a project is not cost-justified. When technical staff low-balls a project estimate, it denies the executives important information they need to make effective decisions, effectively undermining the executive’s decision-making authority. This results in diverting company resources from projects that are cost-justified to projects that aren’t cost-justified. Good projects aren’t supported adequately, and bad projects are supported excessively. The whole scenario is incredibly unhealthy for the business, and it tends to end unpleasantly for the people involved in the projects that should not have been approved in the first place. 

## **Responsibility of Technical Staff to Educate Nontechnical Stakeholders** 

If you want to ensure the success of your software projects, educate your nontechnical project stakeholders about the costs associated with arbitrarily cutting cost and schedule estimates without making corresponding cuts in the work that needs to 

**Chapter 23 Politics, Negotiation, and Problem Solving 263** 

be done. Educate them about the Cone of Uncertainty, and about the differences between estimates, targets, and commitments. In my experience, nontechnical stakeholders tend to be very receptive to these ideas when they’re presented in the context of trying to do what’s best for the organization. 

## **Tip #113** 

## Educate nontechnical stakeholders about effective software estimation practices. 

In addition to educating nontechnical stakeholders about software, educating yourself about your business’s objectives, priorities, and sensitivities will help support the most constructive estimation discussions possible. 

## **23.3 Problem Solving and Principled Negotiation** 

In my 1996 book _Rapid Development_ , I described estimation discussions as negotiations. As the years have gone by, I have become less and less convinced that negotiation is the most constructive way to view the discussions that occur around estimates of cost, schedule, and functionality. 

Negotiation involves parties who have competing interests. The point is to divide a pie between two or more parties. In antagonistic negotiations, each side tries to get as much of the pie as possible, and every bit of pie that one side gets comes at the other side’s expense. In collaborative negotiations, each side looks for ways to make the pie larger, but in the end, the pie still gets divided. 

In software negotiations, there is no pie to divide. When we’re negotiating with sales, marketing, or executives, we’re all sitting on the same side of the table. Far from being a case of “they win and we lose,” it’s a case of “we all win” or “we all lose.” Our interests are the same. We either lay the groundwork for the software project to succeed, which is a success for everyone, or we create the conditions for its failure, which is a failure for everyone. Thus, I can no longer see what is being _negotiated_ in software estimate discussions. 

A better model for the discussions between technical staff, sales, marketing, executives, and other stakeholders is collaborative problem solving. We all work together, share our expertise in different areas, and create a solution that will ultimately work for the best interests of the business. 

**Tip #114** Treat estimation discussions as problem solving, not negotiation. Recognize that all project stakeholders are on the same side of the table. Everyone wins, or everyone loses. 

**264 Part III Specific Estimation Challenges** 

Once we, the technical staff, recognize that we are problem solving, we create a constructive frame of mind in which to have discussions about targets, estimates, and commitments. The trick now becomes how to get the other stakeholders into that frame of mind. 

## **A Problem-Solving Approach to Negotiation** 

Even if we know that we are problem solving, the people we’re discussing the estimate with might think they are negotiating. People negotiate in many different ways. Some strategies are based on strength of bargaining position, intimidation, friendship, or a desire to gain approval or curry favor. And some strategies rely on deception or other skillful psychological maneuvers. 

Because estimation discussions tend to roam between estimates, targets, commitments, and plans, the discussions can’t be tidily pigeonholed as pure negotiation or pure problem solving. You’ll usually find yourself engaging in some elements of both problem solving and negotiation. 

A good strategy that bridges the divide between negotiating and problem solving is the principled-negotiation method described in _Getting to Yes_ (Fisher and Ury 1991). The method is called negotiation, but the participants are viewed as problem solvers. This method doesn’t rely on negotiating tricks, and it explains how to respond to tricks when others use them. It’s based on the idea of creating win-win alternatives. The method works well when only you are using it, and it works even better when the other side is using it too. 

The strategy consists of four parts: 

- Separate the people from the problem. 

- Focus on interests, not positions. 

- Invent options for mutual gain. 

- Insist on using objective criteria. 

Each of these is described in the following sections. 

## **Separate the People from the Problem** 

Estimate discussions involve people first, interests and positions second. When the stakeholders’ personalities are at odds—as, for example, the personalities of technical staff and marketers often are—discussions can get hung up on personality differences. 

Begin by understanding the other side’s position. Managers can be trapped by their organization’s outdated policies. Some organizations fund software projects in ways 

**265** 

**Chapter 23 Politics, Negotiation, and Problem Solving** 

that are essentially incompatible with the way software is developed. They don’t allow managers to ask for funding just to develop the requirements and plans and come up with a good estimate. To get enough funding to do a meaningful estimate, managers have to get funding for the whole project. By the time they get a meaningful estimate, it can be embarrassing or even career-threatening to go back and ask for the right amount of funding. People at the highest levels of such organizations need to better understand software estimation so that they can institute funding practices that support effective software development. 

In these discussions, you might think of yourself as an advisor on software estimation, and thereby avoid slipping into the role of adversary. Keep pulling the focus of the discussion back to what is best for the business. 

It’s also useful to try to take emotions out of the negotiating equation. Sometimes the easiest way to do that is to let the other people blow off steam. Don’t react emotionally to their emotions. Invite them to express themselves fully. Say something like, “I can see that those are all serious concerns, and I want to be sure I understand our company’s position. What else can you tell me about our business situation?” When they are done explaining, acknowledge what they’ve told you and reiterate your commitment to find a solution that’s good for your organization. The other parts of principled negotiation will help you to follow through on that commitment. 

**Tip #115** Attack the problem, not the people. 

## **Focus on Interests, Not Positions** 

Suppose you’re selling your car in order to buy a new boat, and you’ve figured that you need to get $10,000 for your car to buy the boat you want. A prospective buyer approaches you and offers $9,000. You say, “There’s no way I can part with this car for less than $10,000.” The buyer says, “I can go to $9,000, but that’s my limit.” 

When you negotiate in this way, you focus on positions rather than interests. Positions are bargaining statements that are so narrow that in order for one person to win, the other person has to lose. 

Now suppose that the car buyer says, “I really can’t go over $9,000, but I happen to know that you’re in the market for a new boat, and I happen to be the regional distributor for a big boat company. I can get the boat you want for $2,000 less than you can get it from any dealer. Now what do you think about my offer?” Well, now the offer sounds pretty good because it will leave you with $1,000 more than you would have gotten if the buyer had just agreed to the price of your opening position. 

**266 Part III Specific Estimation Challenges** 

Underlying interests are broader than bargaining positions, and focusing on them opens up a world of negotiating possibilities. Consider the following scenario: 

_EXECUTIVE: We need Giga-Blat 4.0 in 6 months._ 

_TECHNICAL LEAD: We’ve estimated the project carefully. Unfortunately, our estimates show that we can’t deliver it in less than 8 months._ 

_EXECUTIVE: That’s not good enough. We really need it in 6 months._ 

_TECHNICAL LEAD: Do we really need all the functionality that’s currently required? If we could cut enough functionality, we could deliver it in 6 months._ 

_EXECUTIVE: We can’t cut functionality. We’ve already cut features to the bone on this release. We need all the features, and we need them within 6 months._ 

_TECHNICAL LEAD: What’s the major factor that’s driving the 6-month schedule? Maybe we can find a creative solution._ 

_EXECUTIVE: The annual trade show for our industry is in 6 months. If we miss the trade show, we’ve missed our chance to demo the software to many of our key accounts. That will effectively push back our sales cycle by a whole year._ 

_TECHNICAL LEAD: I really can’t commit to delivering the final software in time for the trade show. But I can commit to having a beta version ready for the trade show, and I can provide a tester who knows where all the problems are and who can run the software during the show so that it doesn’t break. How does that sound?_ 

_EXECUTIVE: If you can promise the software won’t crash, that will work fine._ 

_TECHNICAL LEAD: No problem._ 

One major difference between typical negotiating and problem solving via discussion of interests is that negotiations tend to get frozen into positions. The turning point in this dialogue came when the technical lead asked, “What’s the major factor that’s driving the six-month schedule?” That switched the dialogue from arguing about positions to trying to understand the company’s interests and solve the underlying business problem.. When you focus on interests, you’re more likely to find a win-win solution. 

## **Invent Options for Mutual Gain** 

Your most powerful negotiating ally in estimate discussions is not your estimate; it’s your ability to generate _planning options_ that nontechnical stakeholders have no way of knowing about. You hold the key to a vault of technical knowledge, and that puts the responsibility for generating creative solutions more on your shoulders than anyone else’s. It’s your role to propose the full range of possibilities and tradeoffs. 

**Chapter 23 Politics, Negotiation, and Problem Solving 267** 

Table 23-2 lists some of the planning options you might suggest to break a logjam in your discussion. 

## **Table 23-2 Planning Options That Might Help Break a Discussion Deadlock** 

## **Feature-Related Options** 

- Move some of the desired functionality into version 2. Few people need all of what they asked for exactly when they asked for it. 

- Use an iterative approach. Deliver the software in versions 0.2, 0.4, 0.6, 0.8, and 1.0, with the most important functionality coming first. 

- Cut features altogether, with an emphasis on cutting the features that are most expensive. 

- Use t-shirt sizing to focus on delivering the features with the highest net business value. 

- Polish some features less. Implement them to some degree, but make them less fancy. 

- Relax the detailed requirements for each feature. Define your mission as getting as close as possible to the requirements through the use of existing components. 

- Build a feature-oriented Cone of Uncertainty. Define some features as “definitely in,” some as “definitely out,” and some as “possible.” Propose a plan for tightening up the Feature Cone of Uncertainty as the project progresses. 

## **Resource-Related Options** 

- Add more developers or testers, if it’s early in the schedule. 

- Add contract staff, if it’s early in the project. 

- Add higher-output technical staff (for example, subject-area experts or more senior developers). 

- Add more administrative support. 

- Increase the degree of developer support. 

- Increase the level of end-user or customer involvement. Devote a full-time end-user to the project who is authorized to make binding decisions about the software’s features. 

- Increase the level of executive involvement to speed decision making. 

- Suggest that another team do part of the work (but watch out for the extra integration issues this will create). 

- Assign resources 100% to the project. Don’t divide their attention between the new project and an old project or between multiple new projects. 

## **Schedule-Related Options** 

- Provide an “estimate road map” that maps out a plan for reestimating and tightening up the estimates. 

- Use estimation ranges or coarse estimates and refine them as the project progresses. 

- Look for ways to plan toward specific cost, schedule, or feature goals as you refine the requirements and plans. 

- Agree to delay making a specific commitment until you complete the next phase of the project (that is, the work required to narrow the Cone of Uncertainty). 

- Do one or two short iterations to calibrate productivity, and then make a commitment based on the team’s actual productivity. 

**268** 

**Part III Specific Estimation Challenges** 

The key is to prevent a shouting match like this one: _I can’t do it_ . “Yes you can.” _No I can’t_ . “Can!” _Can’t!_ Lay out a set of options, and focus your discussion on those options. Don’t include impossible options in the set you present. Avoid saying, “No, I can’t do that”; instead, redirect the discussion toward what you can do. The more options you generate that support doing what’s best for the organization, the easier it will be to show that you’re on the same side of the table as the person you’re problem solving with. 

## **Tip #116** Generate as many planning options as you can to support your organization’s goals. 

One warning: In the cooperative, brainstorming atmosphere that arises from the freewheeling problem-solving discussion, it’s easy to agree to a solution that seems like a good idea at the time but by the next morning seems like a bad deal. The cautions in Section 4.8, “Off-the-Cuff Estimates,” apply to this situation. Don’t make any hard commitments to new options until you’ve had enough time to analyze them quietly by yourself. 

**Tip #117** As you foster an atmosphere of collaborative problem solving, don’t make any commitments based on off-the-cuff estimates. 

## **Insist on Using Objective Criteria** 

One of the oddest aspects of our business is that when careful estimation produces estimates that are notably larger than desired, the customer or manager will often simply disregard the estimate (Jones 1994). He or she might do that even when the estimate comes from an estimation tool or an outside estimation expert and even when the organization has a history of overrunning its estimates. Questioning an estimate is a valid and useful practice. Throwing it out the window and replacing it with wishful thinking is not. 

When principled negotiation is infused with problem solving, you seek “a wise agreement as judged by any objective standard.” You can reason with the other people about which objective standards are most appropriate, and you keep an open mind about standards they suggest. Most important, you don’t yield to pressure, only to principle. To support discussions based on principle, it’s important to recognize who is the most sensible owner for each specific part of the discussion. 

## **Technical Staff and Technical Management Own the** _**Estimate**_ 

You are in the best position to understand the technical scope of work and to create the estimates for it. Therefore, you should be the primary authority on the estimates. 

**269** 

**Chapter 23 Politics, Negotiation, and Problem Solving** 

## **Nontechnical Stakeholders Own the** _**Target**_ 

Executives and sales and marketing people are usually in the best position to understand the needs and priorities of the business. Therefore, they should be the primary authorities on the business targets. 

## **Technical Staff and Nontechnical Staff Jointly Own the** _**Commitment**_ 

The commitment is where the targets and the estimates must ultimately be resolved. If you can reach agreement that you are the authority for the estimate and other stakeholders are the authority for the targets, most of the discussion will then naturally focus on the commitment. The overriding principle should be to reach agreement about what commitment will be best for the organization. 

During these discussions, keep the following points in mind: 

_**Don’t negotiate the estimate itself**_ Clarify the difference between the estimate and the commitment. Keep moving the discussion back toward making a commitment that’s in the organization’s best interests. 

_**Insist that the estimate be prepared by a qualified party**_ The most qualified estimator will often be you. In other cases, the qualified party might be an independent estimation group. Those groups are effective because they do not have a vested interest either in delivering the software in the shortest possible time or in avoiding hard work. If discussions become deadlocked on the topic of the estimate itself, propose submitting the estimate to a third party and pledge to accept the results. Ask other parties in the discussion to agree to do the same. 

A variation on this theme is to bring in a consultant or outside expert to review your schedule. An unfamiliar expert sometimes has more credibility than a familiar one. Some organizations have also had success using software estimation tools. They’ve found that once technical staff calibrate the estimation tool for a specific project, the tool allows them to easily and objectively explore the effects of different options in an unbiased way. 

_**Refer to your organization’s standardized estimation procedure**_ You can avoid arguing about who creates the estimate most of the time if you’ve previously adopted a standardized estimation procedure. It’s then easy to say, “Our procedure doesn’t allow us to negotiate the estimate itself. Let’s talk about the assumptions in the estimate (like project size) and the level of risk that it makes sense for the organization to take on in the commitment for this project.” 

_**Weather the storm**_ Although people have different tolerances for withstanding pressure, if your customers, managers, marketers, or other stakeholders want you to commit to impossible goals, I think the best approach is to politely and firmly 

**270 Part III Specific Estimation Challenges** 

stand by your principles. Batten down the hatches and endure the thunderstorm of an unwelcome estimate early in the project rather than the hurricane of schedule slips and cost overruns later. 

No one really benefits from pretending that impossible goals can be met, even though sometimes people think they do. Improve your credibility by pushing for solutions that respond to the real business needs of your bosses and customers. Provide predictability and improve your organization’s ability to meet its commitments. 

**Tip #118** Resolve discussion deadlocks by returning to the question of, “What will be best for our organization?” 

## **Additional Resources** 

Fisher, Roger, William Ury, and Bruce Patton. _Getting to Yes, Second Edition._ New York, NY: Penguin Books, 1991. This book lays out the details of the principled negotiation strategy described in this chapter. The book is packed with memorable anecdotes and makes for interesting reading even if you’re not very interested in negotiation. 

## Appendix A **Estimate Sanity Check** 

The following sanity check indicates how useful your current project estimate is likely to be in managing your project. For each Yes answer, give the estimate one point. 

**Yes** ____ 1. Was a standardized procedure used to create the estimate? ____ 2. Was the estimation process free from pressure that would bias the results? ____ 3. If the estimate was negotiated, were only the inputs to the estimate negotiated, not the outputs or the estimation process itself? ____ 4. Is the estimate expressed with precision that matches its accuracy? (For example, is the estimate expressed as a range or coarse number if it’s early in the project?) ____ 5. Was the estimate created using multiple techniques that converged to similar results? ____ 6. Is the productivity assumption underlying the estimate comparable to productivity actually experienced on past projects of similar sizes? ____ 7. Is the estimated schedule at least 2.0 x StaffMonths[1/3] ? (That is, is the estimate outside of the Impossible Zone?) ____ 8. Were the people who are going to do the work involved in creating the estimate? ____ 9. Has the estimate been reviewed by an expert estimator? ____ 10. Does the estimate include a nonzero allowance for the impact that project risks will have on effort and schedule? ____ 11. Is the estimate part of a series of estimates that will become more accurate as the project moves into the narrow part of the cone of uncertainty? ____ 12. Are _all_ elements of the project included in the estimate, including creation of setup program, creation of data conversion utilities, cutover from old system to new system, etc.? 

## ____ **TOTAL (see the next page for scoring information)** 

This Estimate Sanity Check is from _Software Estimation_ by Steve McConnell (Microsoft Press, 2006) and is © 2006 Steve McConnell. All Rights Reserved. Permission to copy this quiz is granted provided that this copyright notice is included. 
