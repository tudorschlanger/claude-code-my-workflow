Getting to know you
Areyoumostinterestedin
- Publicorprivatemarkets?
- Quantorfundamentalresearch?
- Industryoracademia?
- Tradingornon-tradingroles?
- Stocksorotherassetclasses?
1/41

MGMT924StatisticalFoundations
Class 1: Statistics in Asset Management
Topics: Linearregressioninassetmanagement,visualization,programminginR,
programminginpython,courseinformation,andresearchopportunities
TheisIngerslevJensen
YaleSOM
2/41

| Classical | statistics | + Data | = Foresight |
| --------- | ---------- | ------ | ----------- |
3/41

The basic setup
| Collect historical |          | Use statistics | to         | Use prediction  |
| ------------------ | -------- | -------------- | ---------- | --------------- |
| data related       | to a     | build a        | prediction | rule to predict |
| problem of         | interest |                |            |                 |
|                    |          | rule from      | the data   | future data     |
4/41

| Main tool | in this course: | Linear Regression |     |     |
| --------- | --------------- | ----------------- | --- | --- |
- Linearregressionisarguablythemostwidelyusedstatisticaltoolforunderstanding
relationshipsamongvariables
- Itprovidesaconceptuallysimplemethodforinvestigatingtheassociationbetweenan
outcomeofinterest(e.g.,stockreturns)andoneormorefactors(e.g.,GDPgrowth)
- Therelationshipisexpressedintheformofanequationoramodelconnectingthe
outcometothefactors,e.g.,
|                 | stockreturn |                             | GDPgrowth |      |
| --------------- | ----------- | --------------------------- | --------- | ---- |
|                 |             | = β                         | +β        | +ϵ . |
|                 |             | t+1 0                       | 1         | t t  |
| Ifwecanestimate | and         | ,thenwecanpredictthefuture! |           |      |
β β
0 1
5/41

2. Predictionrule
- LinearregressionofstockreturnonGDPgrowth:
|     |     |     |     | stockreturn | =       | +β GDPgrowth | +ϵt , |
| --- | --- | --- | --- | ----------- | ------- | ------------ | ----- |
|     |     |     |     |             | t+1 β 0 | 1            | t     |
givespredictionrule:
|     |     |     |     | stockreturn | =0.13−1.40×GDPgrowth |     |     |
| --- | --- | --- | --- | ----------- | -------------------- | --- | --- |
|     |     |     |     |             | t+1                  |     | t   |
3. Predictingthefuture
- Saythisyear’sGDPgrowthis3%(0.03),thenweexpectnextyear’sstockreturnstobe
stockreturn
t+1 =0.13−1.40×0.03=8.8%
| Lab: Does | GDP growth | predict stock | returns? |     |     |     |     |
| --------- | ---------- | ------------- | -------- | --- | --- | --- | --- |
1. Datacollection
| - StockreturnsfromRobertShiller:https://shillerdata.com |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
- GDPgrowthfromSt.LouisFED:https://fred.stlouisfed.org/series/GDPC1
6/41

3. Predictingthefuture
- Saythisyear’sGDPgrowthis3%(0.03),thenweexpectnextyear’sstockreturnstobe
stockreturn
t+1 =0.13−1.40×0.03=8.8%
| Lab: Does | GDP growth | predict | stock | returns? |     |
| --------- | ---------- | ------- | ----- | -------- | --- |
1. Datacollection
| - StockreturnsfromRobertShiller:https://shillerdata.com |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- |
- GDPgrowthfromSt.LouisFED:https://fred.stlouisfed.org/series/GDPC1
2. Predictionrule
| - LinearregressionofstockreturnonGDPgrowth: |     |             |         |              |       |
| ------------------------------------------- | --- | ----------- | ------- | ------------ | ----- |
|                                             |     | stockreturn | =       | +β GDPgrowth | +ϵt , |
|                                             |     |             | t+1 β 0 | 1            | t     |
givespredictionrule:
|     |     | stockreturn | =0.13−1.40×GDPgrowth |     |     |
| --- | --- | ----------- | -------------------- | --- | --- |
|     |     |             | t+1                  |     | t   |
6/41

| Lab: Does | GDP growth | predict | stock | returns? |     |
| --------- | ---------- | ------- | ----- | -------- | --- |
1. Datacollection
| - StockreturnsfromRobertShiller:https://shillerdata.com |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- |
- GDPgrowthfromSt.LouisFED:https://fred.stlouisfed.org/series/GDPC1
2. Predictionrule
| - LinearregressionofstockreturnonGDPgrowth: |     |             |         |              |       |
| ------------------------------------------- | --- | ----------- | ------- | ------------ | ----- |
|                                             |     | stockreturn | =       | +β GDPgrowth | +ϵt , |
|                                             |     |             | t+1 β 0 | 1            | t     |
givespredictionrule:
|     |     | stockreturn | =0.13−1.40×GDPgrowth |     |     |
| --- | --- | ----------- | -------------------- | --- | --- |
|     |     |             | t+1                  |     | t   |
3. Predictingthefuture
- Saythisyear’sGDPgrowthis3%(0.03),thenweexpectnextyear’sstockreturnstobe
stockreturn
t+1 =0.13−1.40×0.03=8.8%
6/41

Linear Regression in Asset Management
Assetmanagersuselinearregressionto:
- Understandexpectedassetreturns
- Predictearnings(equity)
- Predictprobabilityofdefault(bond)
- PredictGDPgrowth(macro)
- Understandexpectedassetrisk
- Estimatevariancesandcovariances
- Estimatevalue-at-risk
- Performscenarioanalysis
- Understandexpectedtradingcosts
- Predictoptimaltime-of-daytotrade
- Predictpriceimpact
- Predictmarketdepth
Usealloftheabovetobuildtheiroptimalportfolio
7/41

Figureshowsthevalueofa$100,000investmentinRenTechin1987andcomparesthiswiththe
sameinvestmentinthemarketorBerkshireHathawayAshares(WarrenBuffett’sfund)
$lim ni eulav tnemtsevnI Value by 2018: 2081m
1000.0
 100.0
RenTech
|     |     |     |   10.0 |     |     | Value by 2018: 10m |     |
| --- | --- | --- | ------ | --- | --- | ------------------ | --- |
Berkshire Hathaway
Value by 2018: 2m
|     |     |     |    1.0 |     | US stock market |     |     |
| --- | --- | --- | ------ | --- | --------------- | --- | --- |
   0.1
|     |     |     |     | 1988 | 1998 | 2008 | 2018 |
| --- | --- | --- | --- | ---- | ---- | ---- | ---- |
Year
PerformancenumbersforRenTechcomesfromAppendix1of“TheManWhoSolvedtheMarket”byGregoryZuckerman.
TheotherperformancenumbersarefromCRSP
| Have you | heard about | Renaissance | Technologies? |     |     |     |     |
| -------- | ----------- | ----------- | ------------- | --- | --- | --- | --- |
8/41

| Have you | heard about | Renaissance | Technologies? |     |     |
| -------- | ----------- | ----------- | ------------- | --- | --- |
Arguablythegreatestassetmanagerofalltime
Figureshowsthevalueofa$100,000investmentinRenTechin1987andcomparesthiswiththe
sameinvestmentinthemarketorBerkshireHathawayAshares(WarrenBuffett’sfund)
|     | $lim ni eulav tnemtsevnI |     |     | Value by 2018: 2081m |     |
| --- | ------------------------ | --- | --- | -------------------- | --- |
1000.0
 100.0
RenTech
|     |   10.0 |     |     | Value by 2018: 10m |     |
| --- | ------ | --- | --- | ------------------ | --- |
Berkshire Hathaway
Value by 2018: 2m
|     |    1.0 |     | US stock market |     |     |
| --- | ------ | --- | --------------- | --- | --- |
   0.1
|     |     | 1988 | 1998 | 2008 | 2018 |
| --- | --- | ---- | ---- | ---- | ---- |
Year
PerformancenumbersforRenTechcomesfromAppendix1of“TheManWhoSolvedtheMarket”byGregoryZuckerman.
TheotherperformancenumbersarefromCRSP
8/41

| Renaissance | Technologies | uses linear | regression |
| ----------- | ------------ | ----------- | ---------- |
”It’sfunnythatIthinkthemostimportantthingtodoondataanalysisisto
do the simple things right. So, here’s a kind of non-secret about what we did
at Renaissance: In my opinion, our most important statistical tool was simple
regressionwithonetargetandoneindependentvariable”
-NickPatterson,formerseniorstatisticianatRenaissanceTechnologies
| Link to podcast | (quote is from | 30:06 to 31:57) |     |
| --------------- | -------------- | --------------- | --- |
9/41

Renaissance Technologies uses linear regression (full quote)
”It’sfunnythatIthinkthemostimportantthingtodoondataanalysisistodothe
simplethingsright.So,here’sakindofnon-secretaboutwhatwedidatRenaissance:In
myopinion,ourmostimportantstatisticaltoolwassimpleregressionwithonetarget
andoneindependentvariable. It’sthesimpleststatisticalmodelyoucanimagine. Any
reasonablysmarthighschoolstudentcoulddoit. Nowwehavesomeofthesmartest
peoplearound,workinginourhedgefund,wehavestringtheoristswerecruitedfrom
Harvard,andthey’redoingsimpleregression. Isthisstupidandpointless? Shouldwe
behiringstupiderpeopleandpayingthemless? Andtheanswerisno. Andthereason
isnobodytellsyouwhatthevariablesyoushouldberegressing[are].What’sthetarget.
Should you do a nonlinear transform before you regress? What’s the source? Should
youcleanyourdata? Doyounoticewhenyourresultsareobviouslyrubbish? Andso
on.Andthesmarteryouarethelesslikelyyouaretomakeastupidmistake.Andthat’s
whyIthinkyouoftenneedsmartpeoplewhoappeartobedoingsomethingtechnically
veryeasy,butactuallyusuallynotsoeasy”-NickPatterson,formerseniorstatistician
atRenaissanceTechnologies
10/41

| Modern | Statistics | + Big Data | = Extreme | foresight |
| ------ | ---------- | ---------- | --------- | --------- |
Butusingthesetoolandhandlingmassivedatasetrequireprogrammingskills
11/41

YES!
Suppose:
- You’reahedgefundanalysttaskedwithpredictingstockreturns
- Yourfirm’sdatabasecovers5,000stocksonaverageoverthelast50years
Observationsbypredictionfrequency:
|     |     |     | Freq.   | #obs  | Freq.    | #obs    |
| --- | --- | --- | ------- | ----- | -------- | ------- |
|     |     |     | Yearly  | 0.25m | Daily    | 63m     |
|     |     |     | Monthly | 3m    | Hourly   | 410m    |
|     |     |     | Weekly  | 13m   | Minutely | 24,579m |
AndevenifExcelcanhandleyourdata,Riswaaaayfasterandmuchmoreflexible
| Programming | with                    | vs.   |     |     |     |     |
| ----------- | ----------------------- | ----- | --- | --- | --- | --- |
|             | R (orPython/Julia/etc.) | Excel |     |     |     |     |
Bigdatarequiresprogramming:
- Excelhasafixedlimitofaround1mrowsofdata
| - Rhasnolimit. | Itonlydependsonthehardwareofyourcomputer |     |     |     |     |     |
| -------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
Isthisanissueinassetmanagement?
12/41

AndevenifExcelcanhandleyourdata,Riswaaaayfasterandmuchmoreflexible
| Programming | with                    |     | vs.   |     |
| ----------- | ----------------------- | --- | ----- | --- |
|             | R (orPython/Julia/etc.) |     | Excel |     |
Bigdatarequiresprogramming:
- Excelhasafixedlimitofaround1mrowsofdata
| - Rhasnolimit. | Itonlydependsonthehardwareofyourcomputer |     |     |     |
| -------------- | ---------------------------------------- | --- | --- | --- |
Isthisanissueinassetmanagement?
YES!
Suppose:
- You’reahedgefundanalysttaskedwithpredictingstockreturns
- Yourfirm’sdatabasecovers5,000stocksonaverageoverthelast50years
Observationsbypredictionfrequency:
|     | Freq.   | #obs  | Freq.    | #obs    |
| --- | ------- | ----- | -------- | ------- |
|     | Yearly  | 0.25m | Daily    | 63m     |
|     | Monthly | 3m    | Hourly   | 410m    |
|     | Weekly  | 13m   | Minutely | 24,579m |
12/41

| Programming | with                    |     | vs.   |     |
| ----------- | ----------------------- | --- | ----- | --- |
|             | R (orPython/Julia/etc.) |     | Excel |     |
Bigdatarequiresprogramming:
- Excelhasafixedlimitofaround1mrowsofdata
| - Rhasnolimit. | Itonlydependsonthehardwareofyourcomputer |     |     |     |
| -------------- | ---------------------------------------- | --- | --- | --- |
Isthisanissueinassetmanagement?
YES!
Suppose:
- You’reahedgefundanalysttaskedwithpredictingstockreturns
- Yourfirm’sdatabasecovers5,000stocksonaverageoverthelast50years
Observationsbypredictionfrequency:
|     | Freq.   | #obs  | Freq.    | #obs    |
| --- | ------- | ----- | -------- | ------- |
|     | Yearly  | 0.25m | Daily    | 63m     |
|     | Monthly | 3m    | Hourly   | 410m    |
|     | Weekly  | 13m   | Minutely | 24,579m |
AndevenifExcelcanhandleyourdata,Riswaaaayfasterandmuchmoreflexible
12/41

Programming with
R
Thiscourse
- UseRcodethroughoutthelecturenotes
- GivestipsandtricksforbestpracticesinR
Practicalities
- DownloadRfromr-project.org
- DownloadRStudiofromposit.co/download/rstudio-desktop
ResourcesforlearningR
- Rfordatascience(book):r4ds.hadley.nz
- Datacamp(interactivecourses):app.datacamp.com/
You’lllearnRbydoing,sostartpracticingASAP!
13/41

- Thebiggestgamechanger,however,islargelanguagemodels:
Learning how to program has never been easier
Todayisanamazingtimetolearnhowtoprogram:
- Tonsofonlineintroductionstoprogramming,suchasdatacamp
- TonsofprogrammingQ&Asites,suchasstackoverflow
14/41

Learning how to program has never been easier
Todayisanamazingtimetolearnhowtoprogram:
- Tonsofonlineintroductionstoprogramming,suchasdatacamp
- TonsofprogrammingQ&Asites,suchasstackoverflow
- Thebiggestgamechanger,however,islargelanguagemodels:
14/41

Visualization
Theartofanalyzingdatawithgraphs
15/41

Who cares about visualization?
- Yourcurrentteacher
- Iputapremiumonaprofessionalpresentationofyoursolutionstotheproblemsets
- Thewayyoupresentyoursolutionscountsforupto10points
- Yourfutureemployer
- Timeisprecious,andathoughtfullymadegraphcanconveyyourinsightsmuchquicker
thanalternativemethods
- JohnTukey(famousstatisticiansometimesregardedasthefatherofdatascience)
- “Thesimplegraphhasbroughtmoreinformationtothedataanalyst’smindthananyother
device”
16/41

Visualization with ggplot2
- Rhasarguablythebestpackagefordata
visualization,namelyggplot2
- ggplot2wascreatedbyHadleyWickham,andI
suggestthatyoureadhisbook,RforData
Science,chapters1,2,10,11,and12
- I’mgoingtoshowyousomealternativewaysto
visualizetheRenTech/Berkshire
Hathaway/Marketperformancedatathatwe
lookedatearlier(seepicturetotheright)
17/41

- Alternative1: Comparecumulativeinvestmentvalueovertime
Value by 2018: 2081m
1000.0
100.0
10.0
RenTech
Value by 2018: 10m
Berkshire
Hathaway
Value by 2018: 2m
1.0 US stock market
0.1
1988 1998 2008 2018
Year
Visualization with ggplot2
- Goal: EvaluateRenTechvs. BerkshireHathawayvs. theUSstockmarket
- Tool: Exploratorydataanalysiswithggplot2
$lim
ni
eulav
tnemtsevnI
Linktocode
18/41

Visualization with ggplot2
- Goal: EvaluateRenTechvs. BerkshireHathawayvs. theUSstockmarket
- Tool: Exploratorydataanalysiswithggplot2
- Alternative1: Comparecumulativeinvestmentvalueovertime
Value by 2018: 2081m
1000.0
100.0
10.0
RenTech
Value by 2018: 10m
Berkshire
Hathaway
Value by 2018: 2m
1.0 US stock market
0.1
1988 1998 2008 2018
Year
$lim
ni
eulav
tnemtsevnI
Linktocode
18/41

Notgreat,maybeifwe:
- Connectthepoints
withgeom
line()
- Showthelineatzero
withgeom
hline()
| Alternative | 2.1: Yearly | returns with |     |
| ----------- | ----------- | ------------ | --- |
geom point()
| perf_data          | |>         |               |     |
| ------------------ | ---------- | ------------- | --- |
| ggplot(aes(x=year, | y=net_ret, | colour=name)) | +   |
geom_point()
1.0
name
ter_ten 0.5
RenTech
Berkshire Hathaway
| 0.0  |      | US stock market |     |
| ---- | ---- | --------------- | --- |
| 1990 | 2000 | 2010            |     |
year
19/41

| Alternative | 2.1: Yearly | returns with |     |
| ----------- | ----------- | ------------ | --- |
geom point()
| perf_data          | |>         |               |     |
| ------------------ | ---------- | ------------- | --- |
| ggplot(aes(x=year, | y=net_ret, | colour=name)) | +   |
geom_point()
Notgreat,maybeifwe:
- Connectthepoints
1.0
withgeom
line()
name
ter_ten 0.5 - Showthelineatzero
RenTech
withgeom
hline()
Berkshire Hathaway
| 0.0  |      | US stock market |     |
| ---- | ---- | --------------- | --- |
| 1990 | 2000 | 2010            |     |
year
19/41

Muchbetter! Nowlayout:
- Modifylabelsso
they’remore
informativewith
labs()
- Movelegendstothe
top,andremove
legendtitlewith
theme()
| Alternative           | 2.2: Yearly | returns with  | multiple | geoms |
| --------------------- | ----------- | ------------- | -------- | ----- |
| perf_data             | |>          |               |          |       |
| ggplot(aes(x=year,    | y=net_ret,  | colour=name)) | +        |       |
| geom_point()          | +           |               |          |       |
| geom_line()           | +           |               |          |       |
| geom_hline(yintercept |             | = 0)          |          |       |
1.0
name
ter_ten 0.5
RenTech
Berkshire Hathaway
US stock market
0.0
|     | 1990 2000 | 2010 |     |     |
| --- | --------- | ---- | --- | --- |
year
20/41

| Alternative           | 2.2: | Yearly returns | with          | multiple | geoms |     |
| --------------------- | ---- | -------------- | ------------- | -------- | ----- | --- |
| perf_data             | |>   |                |               |          |       |     |
| ggplot(aes(x=year,    |      | y=net_ret,     | colour=name)) | +        |       |     |
| geom_point()          | +    |                |               |          |       |     |
| geom_line()           | +    |                |               |          |       |     |
| geom_hline(yintercept |      | = 0)           |               |          |       |     |
Muchbetter! Nowlayout:
- Modifylabelsso
1.0
they’remore
informativewith
name
ter_ten 0.5
labs()
RenTech
Berkshire Hathaway
- Movelegendstothe
US stock market
0.0
top,andremove
legendtitlewith
|     | 1990 | 2000 2010 |     |     |     | theme() |
| --- | ---- | --------- | --- | --- | --- | ------- |
year
20/41

Insights:
- BHandRThadsimilar
performancebefore2000
- RTalmostneverhave
negativereturns
- BHlookscorrelatedwith
market
- RTlooksuncorrelated
withmarket
Alternative 2.3: Yearly returns with multiple geoms and nice layout
| perf_data             | |>      |                    |                 |     |
| --------------------- | ------- | ------------------ | --------------- | --- |
| ggplot(aes(x=year,    |         | y=net_ret,         | colour=name))   | +   |
| geom_point()          | +       |                    |                 |     |
| geom_line()           | +       |                    |                 |     |
| geom_hline(yintercept |         | = 0)               | +               |     |
| labs(x="Year",        | y="Net  | return")           | +               |     |
| theme(legend.position |         | = "top",           |                 |     |
| legend.title          |         | = element_blank()) |                 |     |
|                       | RenTech | Berkshire Hathaway | US stock market |     |
1.0
nruter teN
0.5
0.0
|     | 1990 | 2000 | 2010 |     |
| --- | ---- | ---- | ---- | --- |
Year
21/41

Alternative 2.3: Yearly returns with multiple geoms and nice layout
| perf_data             | |>     |                    |               |     |
| --------------------- | ------ | ------------------ | ------------- | --- |
| ggplot(aes(x=year,    |        | y=net_ret,         | colour=name)) | +   |
| geom_point()          | +      |                    |               |     |
| geom_line()           | +      |                    |               |     |
| geom_hline(yintercept |        | = 0)               | +             |     |
| labs(x="Year",        | y="Net | return")           | +             |     |
| theme(legend.position |        | = "top",           |               |     |
| legend.title          |        | = element_blank()) |               |     |
Insights:
|     | RenTech | Berkshire Hathaway | US stock market |     |
| --- | ------- | ------------------ | --------------- | --- |
- BHandRThadsimilar
1.0 performancebefore2000
- RTalmostneverhave
nruter teN
0.5
negativereturns
- BHlookscorrelatedwith
0.0
market
- RTlooksuncorrelated
|     | 1990 | 2000 | 2010 |     |
| --- | ---- | ---- | ---- | --- |
withmarket
Year
21/41

| Alternative           | 3.1: Distribution  |                  | of yearly          | return | with            |             |
| --------------------- | ------------------ | ---------------- | ------------------ | ------ | --------------- | ----------- |
|                       |                    |                  |                    |        | geom            | histogram() |
| perf_data             | |>                 |                  |                    |        |                 |             |
| ggplot(aes(x=net_ret, |                    | fill=name))      | +                  |        |                 |             |
| geom_histogram()      | +                  |                  |                    |        |                 |             |
| labs(x="Net           | return             | bin", y="count") | +                  |        |                 |             |
| theme(legend.position |                    | = "top",         |                    |        |                 |             |
| legend.title          | = element_blank()) |                  |                    |        |                 |             |
|                       |                    | RenTech          | Berkshire Hathaway |        | US stock market |             |
10
tnuoc
5
0
|     |     |     | 0.0 | 0.5 |     | 1.0 |
| --- | --- | --- | --- | --- | --- | --- |
Net return bin
Useful,butlet’sseparateeachfundwithfacet wrap()andlowerthenumberofbins
22/41

| Alternative           | 3.2: Distribution |                  | of yearly          | return | with            |              |
| --------------------- | ----------------- | ---------------- | ------------------ | ------ | --------------- | ------------ |
|                       |                   |                  |                    |        |                 | facet wrap() |
| perf_data             | |>                |                  |                    |        |                 |              |
| ggplot(aes(x=net_ret, |                   | fill=name))      | +                  |        |                 |              |
| geom_histogram(bins   |                   | = 15) +          |                    |        |                 |              |
| facet_wrap(∼name,     |                   | ncol=3) +        |                    |        |                 |              |
| labs(x="Net           | return            | bin", y="count") | +                  |        |                 |              |
| theme(legend.position |                   | = "none")        |                    |        |                 |              |
|                       |                   | RenTech          | Berkshire Hathaway |        | US stock market |              |
9
tnuoc
6
3
0
|     | −0.5 | 0.0 0.5 | 1.0−0.5 0.0 | 0.5 1.0−0.5 | 0.0 | 0.5 1.0 |
| --- | ---- | ------- | ----------- | ----------- | --- | ------- |
Net return bin
23/41

| How | correlated | are | RenTech/BH |     |     | with the | market? |     |
| --- | ---------- | --- | ---------- | --- | --- | -------- | ------- | --- |
- ManyinvestmentfundshaveasizableexposuretotheUSstockmarket
- ReturnsfromactivefundssuchasRenTechandBerkshireHathawayare,therefore,
morevaluableiftheyhavealowcorrelationwiththemarket
- Tovisualizethisrelationship,weneedtomodifythedataslightly:
| perf_data_new |                        | <-  | perf_data | |>           |           |             |              |     |
| ------------- | ---------------------- | --- | --------- | ------------ | --------- | ----------- | ------------ | --- |
|               | select(year,           |     | net_ret,  | name)        | |>        |             |              |     |
|               | pivot_wider(names_from |     |           | =            | name,     | values_from | = net_ret)   | |>  |
|               | pivot_longer(cols      |     | =         | c(‘RenTech‘, |           | ‘Berkshire  | Hathaway‘),  |     |
|               |                        |     | names_to  |              | = "name", | values_to   | = "net_ret") |     |
- Transformeddata:
24/41

| Alternative           | 4.1:     | Market             | correlations        |             | with               |      |         |     |
| --------------------- | -------- | ------------------ | ------------------- | ----------- | ------------------ | ---- | ------- | --- |
|                       |          |                    |                     |             |                    | geom | point() |     |
| perf_data_new         | |>       |                    |                     |             |                    |      |         |     |
| ggplot(aes(x=‘US      |          | stock              | market‘, y=net_ret, |             | colour=name))      |      | +       |     |
| geom_point()          | +        |                    |                     |             |                    |      |         |     |
| geom_hline(yintercept |          | =                  | 0, linetype         | = "dotted") |                    | +    |         |     |
| labs(y="Net           | return") | +                  |                     |             |                    |      |         |     |
| theme(legend.position |          | =                  | "top",              |             |                    |      |         |     |
| legend.title          |          | = element_blank()) |                     |             |                    |      |         |     |
|                       |          |                    |                     | RenTech     | Berkshire Hathaway |      |         |     |
1.0
nruter teN
0.5
0.0
|     |     | −0.4 | −0.2 |     | 0.0 |     | 0.2 | 0.4 |
| --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
US stock market
Hhmnotthatconvincing,let’saddaregressionlinewithgeom smooth()
25/41

Thisiscrazy:RenTechdoesbetterwhenthemarketdoesworse!Buffettstillhasalphabtw,but
someofhisreturnsreflectmarketexposure
| Alternative           | 4.2:     | Market |                    | correlations |         | with               |      |          |     |
| --------------------- | -------- | ------ | ------------------ | ------------ | ------- | ------------------ | ---- | -------- | --- |
|                       |          |        |                    |              |         |                    | geom | smooth() |     |
| perf_data_new         | |>       |        |                    |              |         |                    |      |          |     |
| ggplot(aes(x=‘US      |          | stock  | market‘,           | y=net_ret,   |         | colour=name))      |      | +        |     |
| geom_point()          | +        |        |                    |              |         |                    |      |          |     |
| geom_smooth(method    |          |        | = "lm",            | se=F)        | +       |                    |      |          |     |
| geom_hline(yintercept |          |        | = 0,               | linetype     | =       | "dotted")          | +    |          |     |
| labs(y="Net           | return") |        | +                  |              |         |                    |      |          |     |
| theme(legend.position |          |        | = "top",           |              |         |                    |      |          |     |
| legend.title          |          |        | = element_blank()) |              |         |                    |      |          |     |
|                       |          |        |                    |              | RenTech | Berkshire Hathaway |      |          |     |
1.0
nruter teN
0.5
0.0
|     |     |     | −0.4 | −0.2 |     | 0.0 | 0.2 |     | 0.4 |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
US stock market
26/41

| Alternative           | 4.2:     | Market |                    | correlations |         | with               |      |          |     |
| --------------------- | -------- | ------ | ------------------ | ------------ | ------- | ------------------ | ---- | -------- | --- |
|                       |          |        |                    |              |         |                    | geom | smooth() |     |
| perf_data_new         | |>       |        |                    |              |         |                    |      |          |     |
| ggplot(aes(x=‘US      |          | stock  | market‘,           | y=net_ret,   |         | colour=name))      |      | +        |     |
| geom_point()          | +        |        |                    |              |         |                    |      |          |     |
| geom_smooth(method    |          |        | = "lm",            | se=F)        | +       |                    |      |          |     |
| geom_hline(yintercept |          |        | = 0,               | linetype     | =       | "dotted")          | +    |          |     |
| labs(y="Net           | return") |        | +                  |              |         |                    |      |          |     |
| theme(legend.position |          |        | = "top",           |              |         |                    |      |          |     |
| legend.title          |          |        | = element_blank()) |              |         |                    |      |          |     |
|                       |          |        |                    |              | RenTech | Berkshire Hathaway |      |          |     |
1.0
nruter teN
0.5
0.0
|     |     |     | −0.4 | −0.2 |     | 0.0 | 0.2 |     | 0.4 |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
US stock market
Thisiscrazy:RenTechdoesbetterwhenthemarketdoesworse!Buffettstillhasalphabtw,but
someofhisreturnsreflectmarketexposure 26/41

| “Why | don’t | we use | Python?” |
| ---- | ----- | ------ | -------- |
27/41

- Thatsaid,pythonisalsoagreattool:
- pythonhasanedgeoverRincomputerscience
- Manybooksonmachinelearninghaveexamplesinpython
- Iusepythoninmyownresearch
⇒ Istronglyencourageyoutolearnboth!
- Butifyouwanttostayinpythontranslatingmycodeiseasy
Why I prefer over for this course
R python
- IpreferRforthiscoursebecause:
- Rhasanedgeoverpythonforstatisticsandeconometrics
- ThebooksweusehaveexamplesinR
- IuseRinmyownresearch
28/41

⇒ Istronglyencourageyoutolearnboth!
- Butifyouwanttostayinpythontranslatingmycodeiseasy
Why I prefer over for this course
R python
- IpreferRforthiscoursebecause:
- Rhasanedgeoverpythonforstatisticsandeconometrics
- ThebooksweusehaveexamplesinR
- IuseRinmyownresearch
- Thatsaid,pythonisalsoagreattool:
- pythonhasanedgeoverRincomputerscience
- Manybooksonmachinelearninghaveexamplesinpython
- Iusepythoninmyownresearch
28/41

Why I prefer over for this course
R python
- IpreferRforthiscoursebecause:
- Rhasanedgeoverpythonforstatisticsandeconometrics
- ThebooksweusehaveexamplesinR
- IuseRinmyownresearch
- Thatsaid,pythonisalsoagreattool:
- pythonhasanedgeoverRincomputerscience
- Manybooksonmachinelearninghaveexamplesinpython
- Iusepythoninmyownresearch
⇒ Istronglyencourageyoutolearnboth!
- Butifyouwanttostayinpythontranslatingmycodeiseasy
28/41

| Data wrangling | in rather | than  |
| -------------- | --------- | ----- |
|                | ibis      | dplyr |
- IusetheRpackagedplyrasmyprimarytoolfordatawranglingthroughoutthecourse
- Luckily,thereisapythonequivalenttodplyrcalledibis
- ibiswascreatedbyWesMcKinney—thecreatorofpandas—anditsyntaxisheavily
inspiredbydplyr
- Theyevenhaveatutorialonusingibisasadplyruser:
https://ibis-project.org/tutorials/ibis-for-dplyr-users
29/41

- withtheequivalentibiscode:
|     |     |     |     |     | perf_data_new | = ( |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
perf_data
|     |     |     |     |     |     | .select([’year’,                | ’net_ret’,       | ’name’])               |             |
| --- | --- | --- | --- | --- | --- | ------------------------------- | ---------------- | ---------------------- | ----------- |
|     |     |     |     |     |     | .pivot_wider(names_from=’name’, |                  | values_from=’net_ret’) |             |
|     |     |     |     |     |     | .pivot_longer(col=[’RenTech’,   |                  | ’Berkshire             | Hathaway’], |
|     |     |     |     |     |     |                                 | names_to=’name’, | values_to=’net_ret’)   |             |
)
versus
| ibis | dplyr |     |     |     |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
- Comparedplyrcodefromearlierinthelecture:
| perf_data_new          | <- perf_data | |>           |             |              |     |     |     |     |     |
| ---------------------- | ------------ | ------------ | ----------- | ------------ | --- | --- | --- | --- | --- |
| select(year,           | net_ret,     | name) |>     |             |              |     |     |     |     |     |
| pivot_wider(names_from |              | = name,      | values_from | = net_ret)   | |>  |     |     |     |     |
| pivot_longer(cols      | =            | c(‘RenTech‘, | ‘Berkshire  | Hathaway‘),  |     |     |     |     |     |
|                        | names_to     | = "name",    | values_to   | = "net_ret") |     |     |     |     |     |
30/41

versus
| ibis | dplyr |     |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- | --- | --- |
- Comparedplyrcodefromearlierinthelecture:
| perf_data_new          | <- perf_data |     | |>           |       |             |              |     |
| ---------------------- | ------------ | --- | ------------ | ----- | ----------- | ------------ | --- |
| select(year,           | net_ret,     |     | name)        | |>    |             |              |     |
| pivot_wider(names_from |              |     | =            | name, | values_from | = net_ret)   | |>  |
| pivot_longer(cols      |              | =   | c(‘RenTech‘, |       | ‘Berkshire  | Hathaway‘),  |     |
|                        | names_to     |     | = "name",    |       | values_to   | = "net_ret") |     |
- withtheequivalentibiscode:
| perf_data_new | = ( |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
perf_data
| .select([’year’,                |     | ’net_ret’,       |     | ’name’]) |                        |             |     |
| ------------------------------- | --- | ---------------- | --- | -------- | ---------------------- | ----------- | --- |
| .pivot_wider(names_from=’name’, |     |                  |     |          | values_from=’net_ret’) |             |     |
| .pivot_longer(col=[’RenTech’,   |     |                  |     |          | ’Berkshire             | Hathaway’], |     |
|                                 |     | names_to=’name’, |     |          | values_to=’net_ret’)   |             |     |
)
30/41

“But what if I want to use ?”
pandas
- Shortanswer: pleasedon’t
- Longanswer: tenthingsIhateaboutPandasbyWesMcKinney(thecreatorofpandas
andibis)
- Mylonganswer:
- pandasisafineforsmalldatasetsthatare1/10ththesizeofyourcomputer’sRAM
- ibisisabettertoolforbigdatasetsthatare10timesthesizeofyourcomputer’sRAM
⇒ With16GBofRAM,ibiscangetyouworkingwithseriousAMdata,pandascannot
- Checkoutthisbenchmarkofibisversuspandas:
ibis-project.org/posts/pydata-performance
31/41

Visualization with instead of
plotnine ggplot2
- IusetheRpackageggplot2fordatavisualizationthroughoutthecourse
- Luckily,again,thereisapythonequivalenttoggplot2calledplotnine
- ibiswasinspiredbydplyrbutplotnineisadirecttranslationofggplot2:
“plotnineisanimplementationofagrammarofgraphicsinPythonbasedonggplot2.”
(source:plotnine.org)
32/41

- withtheequivalentplotninecode:
ggplot(perf_data_new, aes(x=’US stock market’, y=’net_ret’, color=’name’)) +
geom_point() +
|     |     |     |     |     | geom_smooth(method=’lm’, | se=False)          | +   |
| --- | --- | --- | --- | --- | ------------------------ | ------------------ | --- |
|     |     |     |     |     | geom_hline(yintercept=0, | linetype="dotted") | +   |
|     |     |     |     |     | labs(y="Net return") +   |                    |     |
theme(legend_position="top",
legend_title=element_blank())
versus
plotnine ggplot2
- Compareggplot2codefromearlierinthelecture:
| perf_data_new |>      |                    |             |               |     |     |     |     |
| --------------------- | ------------------ | ----------- | ------------- | --- | --- | --- | --- |
| ggplot(aes(x=‘US      | stock market‘,     | y=net_ret,  | colour=name)) | +   |     |     |     |
| geom_point() +        |                    |             |               |     |     |     |     |
| geom_smooth(method    | = "lm", se=F)      | +           |               |     |     |     |     |
| geom_hline(yintercept | = 0, linetype      | = "dotted") | +             |     |     |     |     |
| labs(y="Net return")  | +                  |             |               |     |     |     |     |
| theme(legend.position | = "top",           |             |               |     |     |     |     |
| legend.title          | = element_blank()) |             |               |     |     |     |     |
33/41

versus
plotnine ggplot2
- Compareggplot2codefromearlierinthelecture:
| perf_data_new |>      |                    |               |             |               |     |
| --------------------- | ------------------ | ------------- | ----------- | ------------- | --- |
| ggplot(aes(x=‘US      | stock              | market‘,      | y=net_ret,  | colour=name)) | +   |
| geom_point() +        |                    |               |             |               |     |
| geom_smooth(method    | = "lm",            | se=F)         | +           |               |     |
| geom_hline(yintercept |                    | = 0, linetype | = "dotted") | +             |     |
| labs(y="Net return")  | +                  |               |             |               |     |
| theme(legend.position |                    | = "top",      |             |               |     |
| legend.title          | = element_blank()) |               |             |               |     |
- withtheequivalentplotninecode:
ggplot(perf_data_new, aes(x=’US stock market’, y=’net_ret’, color=’name’)) +
| geom_point() +           |     |                    |     |     |     |
| ------------------------ | --- | ------------------ | --- | --- | --- |
| geom_smooth(method=’lm’, |     | se=False)          | +   |     |     |
| geom_hline(yintercept=0, |     | linetype="dotted") |     | +   |     |
| labs(y="Net return")     | +   |                    |     |     |     |
theme(legend_position="top",
legend_title=element_blank())
33/41

| Bottom | line: switching | between | and | is easy |
| ------ | --------------- | ------- | --- | ------- |
R python
- RandPythonarebothgreattoolsfordataanalysis⇒choosewhicheveryouwant
- MostofthecoursematerialwillbeinRbutitshouldbeeasytotranslateintopython
withtoolssuchasChatGPTandpackagessuchasibisandplotnine
- Forthefirstlecture,IpreparedallcodeinbothRandpython,soyoucanseehow
easyitistoswitchbetweenthetwoanduploadedthemtocanvas:
|     | - class1.R  |     |     |     |
| --- | ----------- | --- | --- | --- |
|     | - class1.py |     |     |     |
34/41

Course information
35/41

Administrative Details
1. Syllabus
- Lotofinformation!Pleasechecksyllabusbeforeasking
- Detailedcourseoverview
- Suggestedreadingsforcoursematerial
- Academicpolicies
2. GeneralExpectations
- Readthelecturenotes
- Ifsomethingisunclear,supplementwithsuggestedreadings
- Practiceandthinkhard
- Givefeedbackandaskquestions
- Beontimeandonschedule
3. Problemsets
- Threeproblemsets
- Oneweektoproducesolution
- Solveingroupsofmax4(formgroupsinCanvas)
- IMPORTANT:Donotincludeyourcodeunlessexplicitlyspecifiedintheproblemset
36/41

Guidelines for problem sets
Keytake-aways:
- Presentyoursolutionasapro
- Donotincludecode(unlessasked)
- Bebriefandtothepoint
- Describehowyouarrivedatyour
solution
37/41

Course overview
MostclassesareheldMondaysandWednesdaysfrom8:30amto9:50aminEvansHall
2410. Theonlyexceptionisthefirstweek,whereclasseswillbeheldonWednesdayand
Friday,andMonday,September1st,wherewewillnotmeetbecauseofLaborday.
| Class Date | Topic                            | Problemset       |
| ---------- | -------------------------------- | ---------------- |
| 1 Aug.27   | StatisticsinAssetManagement      |                  |
| 2 Aug.29   | PredictionwithLinearRegression   |                  |
| 3 Sep.3    | PredictionwithLinearRegression   | PS1(dueonSep.10) |
| 4 Sep.8    | InferenceforLinearRegression     |                  |
| 5 Sep.10   | InferenceforLinearRegression     |                  |
| 6 Sep.15   | InferenceforLinearRegression     | PS2(dueonSep.22) |
| 7 Sep.17   | AdvancedTopicsinLinearRegression |                  |
| 8 Sep.22   | AdvancedTopicsinLinearRegression |                  |
| 9 Sep.24   | AdvancedTopicsinLinearRegression | PS3(dueonOct.1)  |
| 10 Sep.29  | TimeSeriesAnalysis               |                  |
| 11 Oct.1   | TimeSeriesAnalysis               |                  |
| 12 Oct.6   | AdvancedEstimationMethods        |                  |
| 13 Oct.8   | ReviewofKeyConcepts              |                  |
| Oct.10     |                                  | Finalexam        |
38/41

Suggested Readings
- Thereisnorequiredreading,butherearesomeusefulreferences:
- IntroductoryEconometrics:AModernApproachbyWooldridge
- Iusethe7thedition,butthe6thand5theditionsshouldbefineaswell
- AfreealternativethatalsoincludesRcodeisAModernApproachtoRegressionwithRby
Sheather,availablefromtheYalelibrary(library.yale.edu)
- ComputerAgeStatisticalInferencebyEfronandHastie
- Thebooksisfreelyavailablefromhastie.su.domains/CASI/order.html
- Thesyllabusshowswhichpartsarerelevanttoeachclass.
39/41

Research opportunities
40/41

Research opportunities
- I’llgiveeveryonewith“HighHonors”theopportunityforRAwork
- Lastyear,4AMstudents(FrederikCiupek,JingGao,MiaHua,andVedantSherma)and1
non-AMstudent(DominikFeil)tookuptheoffer
- TheyhelpedmeandLelandBybeefromChicagoBoothonaprojecton“howpeoplevalue
firms,”wheretheyusedLLMstoextractallvaluationssubmittedtotheSECsince2001
- RAworkcanbealongsideyourstudies,and/oraspartofthe“practicalexperience”
requirementforAMstudents
41/41

Questions?
42/41

Appendix
1/2

| Code: Cumulative | return | graph |     |     |     |
| ---------------- | ------ | ----- | --- | --- | --- |
perf_data |>
mutate(
label = if_else(year==2018, paste0("Value by 2018: ", round(inv_value/1e6,0),
| "m"), NA_character_) |                |               |          |     |     |
| -------------------- | -------------- | ------------- | -------- | --- | --- |
| ) |> # Controls      | the order      | of the legend | labels   |     |     |
| ggplot(aes(year,     | inv_value/1e6, | colour        | = name)) | +   |     |
geom_text(aes(label=label), hjust = 1, vjust=0, nudge_y = 0.05, size=3) +
| geom_textline(aes(label=name), |     | hjust | = 0.56) | +   |     |
| ------------------------------ | --- | ----- | ------- | --- | --- |
scale_y_log10(labels = function(x) format(x, scientific = FALSE)) +
| scale_x_continuous(breaks |                 | = seq(1988, | 2018, by  | = 10)) + |     |
| ------------------------- | --------------- | ----------- | --------- | -------- | --- |
| labs(x = "Year",          | y = "Investment | value       | in mil$") | +        |     |
theme(
| legend.position | = "none",         |     |     |     |     |
| --------------- | ----------------- | --- | --- | --- | --- |
| legend.title    | = element_blank() |     |     |     |     |
)
|     |     | $lim ni eulav tnemtsevnI |     | Value by 2018: 2081m |     |
| --- | --- | ------------------------ | --- | -------------------- | --- |
1000.0
 100.0
RenTech
Value by 2018: 10m
|     |     |   10.0 | Berkshire Hathaway |     |     |
| --- | --- | ------ | ------------------ | --- | --- |
Value by 2018: 2m
|     |     |    1.0 | US stock market |     |     |
| --- | --- | ------ | --------------- | --- | --- |
Back
   0.1
|     |     | 1988 | 1998 | 2008 2018 | 2/2 |
| --- | --- | ---- | ---- | --------- | --- |
Year
