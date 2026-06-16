MGMT924StatisticalFoundations
Class 2-3: Prediction with Linear Regression
Topics: Buildingapredictionrule,ordinaryleastsquaresestimation,
numericaloptimization,R2,covarianceandcorrelation,
estimatingportfoliorisk,gettinghigh-qualityfinancialdata
TheisIngerslevJensen
YaleSOM
1/67

Linear regression is an invaluable tool for asset managers
Rememberthequotefromclass1?
”It’sfunnythatIthinkthemostimportantthingtodoondataanalysisistodothe
simplethingsright.So,here’sakindofnon-secretaboutwhatwedidatRenaissance:In
myopinion,ourmostimportantstatisticaltoolwassimpleregressionwithonetarget
andoneindependentvariable”
-NickPatterson,formerseniorstatisticianatRenaissanceTechnologies
2/67

| Example: | Predicting | house | prices |
| -------- | ---------- | ----- | ------ |
3/67

Solution
- Gethistoricaldataonhousesaleswhereweknowthepricepaidalongwithsome
housecharacteristics
- Buildapredictionrulethatpredictsthepriceasafunctionoftheobserved
characteristics
Example: Predicting house prices
Problem
- Predictmarketpricebasedonobservedcharacteristics
4/67

Example: Predicting house prices
Problem
- Predictmarketpricebasedonobservedcharacteristics
Solution
- Gethistoricaldataonhousesaleswhereweknowthepricepaidalongwithsome
housecharacteristics
- Buildapredictionrulethatpredictsthepriceasafunctionoftheobserved
characteristics
4/67

Manyfactorsaffectthepriceofahouse:
- Sizeofhouse
- Sizeofland
- Numberofbeds
- Numberofbathrooms
- Location
- Economicconditions(unemployment,interestrate,etc.)
Wecoulduseanyorallofthesetopredictthehouseprice,butwe’lluseavariablethat
reflectsalloftheaboveinasinglenumber,namelythe
- Housevalueasassessedbythetaxauthorities
What characteristics should we use?
5/67

What characteristics should we use?
Manyfactorsaffectthepriceofahouse:
- Sizeofhouse
- Sizeofland
- Numberofbeds
- Numberofbathrooms
- Location
- Economicconditions(unemployment,interestrate,etc.)
Wecoulduseanyorallofthesetopredictthehouseprice,butwe’lluseavariablethat
reflectsalloftheaboveinasinglenumber,namelythe
- Housevalueasassessedbythetaxauthorities
5/67

Note: Thisterminologyisnotuniversallyadopted,sobearthatinmindifother
professors/booksusedifferentnames
Terminology
Terminologyinthiscourse:
- Theoutputvaluethatweseektopredictiscalledthedependentvariable,andit’s
denotedbyy
- Inexample:y =priceofhouse
- Theinputvaluethatweusetoguidethepredictioniscalledtheexplanatory
variable,andit’sdenotedbyx
- Inexample:x =assessedvalueofhouse
6/67

Terminology
Terminologyinthiscourse:
- Theoutputvaluethatweseektopredictiscalledthedependentvariable,andit’s
denotedbyy
- Inexample:y =priceofhouse
- Theinputvaluethatweusetoguidethepredictioniscalledtheexplanatory
variable,andit’sdenotedbyx
- Inexample:x =assessedvalueofhouse
Note: Thisterminologyisnotuniversallyadopted,sobearthatinmindifother
professors/booksusedifferentnames
6/67

| The house price | model |     |     |     |
| --------------- | ----- | --- | --- | --- |
- Sofar,we’vepostulatedthatthereissomerelationshipbetweenthehousepriceand
it’sassessedvalue:
|     | house | price = | f(assessed value) |     |
| --- | ----- | ------- | ----------------- | --- |
- Toestimatetherelationshipempirically,wefollowtherecipefromclass1:
| Collect | historical  | Use statistics | to         | Use prediction  |
| ------- | ----------- | -------------- | ---------- | --------------- |
| related | to a        |                |            |                 |
| data    |             | build a        | prediction | rule to predict |
| problem | of interest | rule from      | the data   |                 |
future data
7/67

House data
Rawdata: AllrealestatesalesinConnecticut(CT),2001-2021,fromdata.ct.gov
Variablesofinterest
- saleamount: Pricethehousewassoldfor
- assessedvalue: Valueofthepropertyusedforlocaltaxassessment.
- Note:InCT,thisvalueissetto70%ofthetruevalueofthehouseasassessedbythetax
authorities(link)
8/67

- RestrictthesampletosinglefamilyhomeslocatedinNewHaven,listedin2020,and
haveatrueassessedvaluebelow$500,000
filter(town=="New Haven" & listyear==2020 & residentialtype=="Single
Family" & assessedvalue true<500)
- Changetheunitsofassessedvalue trueandsaleamounttothousandsforeasier
visualization,e.g.,
saleamount := saleamount/1000
Data preparation
Topreparethedata,I:
- Createanewvariablethatshowsthetruevalueassessedbythetaxauthorities
assessedvalue true := assessedvalue/0.7
9/67

- Changetheunitsofassessedvalue trueandsaleamounttothousandsforeasier
visualization,e.g.,
saleamount := saleamount/1000
Data preparation
Topreparethedata,I:
- Createanewvariablethatshowsthetruevalueassessedbythetaxauthorities
assessedvalue true := assessedvalue/0.7
- RestrictthesampletosinglefamilyhomeslocatedinNewHaven,listedin2020,and
haveatrueassessedvaluebelow$500,000
filter(town=="New Haven" & listyear==2020 & residentialtype=="Single
Family" & assessedvalue true<500)
9/67

Data preparation
Topreparethedata,I:
- Createanewvariablethatshowsthetruevalueassessedbythetaxauthorities
| assessedvalue | true := assessedvalue/0.7 |     |
| ------------- | ------------------------- | --- |
- RestrictthesampletosinglefamilyhomeslocatedinNewHaven,listedin2020,and
haveatrueassessedvaluebelow$500,000
filter(town=="New Haven" & listyear==2020 & residentialtype=="Single
| Family" | & assessedvalue | true<500) |
| ------- | --------------- | --------- |
- Changetheunitsofassessedvalue trueandsaleamounttothousandsforeasier
visualization,e.g.,
| saleamount | := saleamount/1000 |     |
| ---------- | ------------------ | --- |
9/67

| Step 2: Building   | a prediction | rule           |            |                 |
| ------------------ | ------------ | -------------- | ---------- | --------------- |
| Collect historical |              | Use statistics | to         | Use prediction  |
| data related       | to a         | build a        | prediction | rule to predict |
| problem of         | interest     |                |            |                 |
|                    |              | rule from      | the data   | future data     |
10/67

Visualizing the data
Theis’rulenumber1whenbuildingapredictionrule: Visualizethedata
- Here,Iuseascatterplotwiththedependentvariable,thehouseprice,onthey-axis
andtheexplanatoryvariable,thehouseassessmentvalue,onthex-axis:
800
600
400
200
0
100 200 300 400 500
assessedvalue_true
tnuomaelas
- Asexpected,actualsalepricesincreaseinassessmentvalue
11/67

- We’llfocusonalinearpredictionruleoftheform
yˆ = f(x) = βˆ +βˆ x
0 1
- Hence,we“buildapredictionrule”bychoosingspecificvaluesfor βˆ and βˆ
0 1
Building a prediction rule
- Apredictionruleisafunctionthattakesx asaninputandoutputsapredictedvalue,
yˆ,whichwewriteasyˆ = f(x)
- Houseexample:Taketheassessedvalueofahouseandpredictitsactualsaleprice
12/67

Building a prediction rule
- Apredictionruleisafunctionthattakesx asaninputandoutputsapredictedvalue,
yˆ,whichwewriteasyˆ = f(x)
- Houseexample:Taketheassessedvalueofahouseandpredictitsactualsaleprice
- We’llfocusonalinearpredictionruleoftheform
yˆ = f(x) = βˆ +βˆ x
0 1
- Hence,we“buildapredictionrule”bychoosingspecificvaluesfor βˆ and βˆ
0 1
12/67

- Anaivepredictionruleisthattheactualhousepriceisequaltotheassessmentvalue,
|     |     |     |     |     |     | whichimplies | βˆ 0and | βˆ 1,suchthatthepredictionruleis |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | -------------------------------- |
|     |     |     |     |     |     |              | =       | =                                |
|     |     |     |     |     |     |              | 0       | 1                                |
saleaˆmountnaive = 0+1×assessedvalue
true
| Building | a prediction | rule for predicting | house | prices |     |     |     |     |
| -------- | ------------ | ------------------- | ----- | ------ | --- | --- | --- | --- |
- Thegeneralpredictionrule:
|     |     | yˆ = | f(x) = βˆ +βˆ x |     |     |     |     |     |
| --- | --- | ---- | --------------- | --- | --- | --- | --- | --- |
|     |     |      | 0 1             |     |     |     |     |     |
- Thehouse-specificpredictionrule:
βˆ +βˆ
|     | saleaˆmount | = f(assessedvalue | true) = | ×assessedvalue | true |     |     |     |
| --- | ----------- | ----------------- | ------- | -------------- | ---- | --- | --- | --- |
0 1
13/67

| Building | a prediction | rule for predicting | house | prices |     |
| -------- | ------------ | ------------------- | ----- | ------ | --- |
- Thegeneralpredictionrule:
|     |     | yˆ = | f(x) = βˆ +βˆ x |     |     |
| --- | --- | ---- | --------------- | --- | --- |
|     |     |      | 0 1             |     |     |
- Thehouse-specificpredictionrule:
βˆ +βˆ
|     | saleaˆmount | = f(assessedvalue | true) = | ×assessedvalue | true |
| --- | ----------- | ----------------- | ------- | -------------- | ---- |
0 1
- Anaivepredictionruleisthattheactualhousepriceisequaltotheassessmentvalue,
| whichimplies | βˆ  | 0and βˆ 1,suchthatthepredictionruleis |     |     |     |
| ------------ | --- | ------------------------------------- | --- | --- | --- |
= =
0 1
|     |     | saleaˆmountnaive | = 0+1×assessedvalue |     |     |
| --- | --- | ---------------- | ------------------- | --- | --- |
true
13/67

| The prediction | rule is | a line |     |     |
| -------------- | ------- | ------ | --- | --- |
- Thelinearpredictionrulewithoneexplanatoryvariableisjusttheequationofaline
| where βˆ istheinterceptand |     | βˆ istheslope: |     |     |
| -------------------------- | --- | -------------- | --- | --- |
| 0                          |     | 1              |     |     |
Y
b
1
Y = b  + b X
0 1
b
0
|     |     | 1   | 2   | X   |
| --- | --- | --- | --- | --- |
14/67

- Thenaivepredictionrulesystematicallyunderpredictthesaleprice,whichis
economicallyinteresting(assessmentvaluesaretoolow)butstatisticallysuboptimal
| A naive | prediction | rule |     |     |     |     |
| ------- | ---------- | ---- | --- | --- | --- | --- |
- Thegraphbelowshowsthenaivepredictionrule,yˆnaive = 0+1x ,byadding
| geom | abline(intercept=0, | slope=1) |     |     |     |     |
| ---- | ------------------- | -------- | --- | --- | --- | --- |
800
|     | tnuomaelas 600 |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
400
200
0
|     |     | 100 | 200 | 300 | 400 | 500 |
| --- | --- | --- | --- | --- | --- | --- |
assessedvalue_true
15/67

| A naive | prediction | rule |     |     |     |     |
| ------- | ---------- | ---- | --- | --- | --- | --- |
- Thegraphbelowshowsthenaivepredictionrule,yˆnaive = 0+1x ,byadding
| geom | abline(intercept=0, | slope=1) |     |     |     |     |
| ---- | ------------------- | -------- | --- | --- | --- | --- |
800
|     | tnuomaelas 600 |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
400
200
0
|     |     | 100 | 200 | 300 | 400 | 500 |
| --- | --- | --- | --- | --- | --- | --- |
assessedvalue_true
- Thenaivepredictionrulesystematicallyunderpredictthesaleprice,whichis
economicallyinteresting(assessmentvaluesaretoolow)butstatisticallysuboptimal
15/67

- Thealgorithm(ormethod)iscalledordinaryleastsquares(OLS)estimation
| The optimal | prediction | rule |
| ----------- | ---------- | ---- |
- Wecouldmanuallychange βˆ and βˆ ,togetabetterpredictionrule
0 1
- However,I’llshowanalgorithmthat,basedonanyy andx inputs,automaticallyfinds
theoptimalparameterestimates(accordingtosomeobjective)
| - Whenyouthinkaboutit,that’sremarkable! |     |     |
| --------------------------------------- | --- | --- |
16/67

| The optimal | prediction | rule |
| ----------- | ---------- | ---- |
- Wecouldmanuallychange βˆ and βˆ ,togetabetterpredictionrule
0 1
- However,I’llshowanalgorithmthat,basedonanyy andx inputs,automaticallyfinds
theoptimalparameterestimates(accordingtosomeobjective)
| - Whenyouthinkaboutit,that’sremarkable! |     |     |
| --------------------------------------- | --- | --- |
- Thealgorithm(ormethod)iscalledordinaryleastsquares(OLS)estimation
16/67

The OLS prediction rule
OLSestimationisextremelyeasyinRviathefunctionlm()(forlinearmodel)
- Inourcase,wecangettheOLSparameterestimatesbythefunctioncall:
lm(formula=saleamount∼assessedvalue_true, data=house_data)
- Theresult:
βˆOLS
= −4.69,
βˆOLS
= 1.37
0 1
leadingtotheOLSpredictionrule
yˆOLS = −4.69+1.37X
17/67

The OLS prediction rule
Inggplot2,youcanaddtheOLSpredictionrulewithgeom smooth(method="lm", se=F)
800
600
400
200
0
100 200 300 400 500
assessedvalue_true
tnuomaelas
Muchbetter. Infact,thefitissurprisinglygood(atleasttome),suggestingthatthe
assessedvalueisagoodpredictorofhowmuchahousewillcostontheopenmarket.
Question: Couldwebuildatradingstrategyfromthispredictionrule?
18/67

The OLS prediction rule
Inggplot2,youcanaddtheOLSpredictionrulewithgeom smooth(method="lm", se=F)
800
600
400
200
0
100 200 300 400 500
assessedvalue_true
tnuomaelas
Question: Couldwebuildatradingstrategyfromthispredictionrule?
Muchbetter. Infact,thefitissurprisinglygood(atleasttome),suggestingthatthe
assessedvalueisagoodpredictorofhowmuchahousewillcostontheopenmarket.
18/67

The OLS prediction rule
Inggplot2,youcanaddtheOLSpredictionrulewithgeom smooth(method="lm", se=F)
800
600
400
200
0
100 200 300 400 500
assessedvalue_true
tnuomaelas
Muchbetter. Infact,thefitissurprisinglygood(atleasttome),suggestingthatthe
assessedvalueisagoodpredictorofhowmuchahousewillcostontheopenmarket.
Question: Couldwebuildatradingstrategyfromthispredictionrule?
18/67

| Ordinary | Least | Squares | Estimation |
| -------- | ----- | ------- | ---------- |
19/67

⇒What’sagoodobjectiveforapredictionrule?
- Anaturalobjectiveismaketotheresidualssmall
| Fitted values | and residuals |     |     |     |
| ------------- | ------------- | --- | --- | --- |
BeforedescribingOLSestimation,wefirstestablishsomenotation:
- Weusei todenoteaspecificobservationandntodenotethetotalnumberof
observations
i = 1,2,...,n
| - Forany | βˆ and βˆ definethefittedvalueforobservationi |     |     | as  |
| -------- | --------------------------------------------- | --- | --- | --- |
0 1
|     |     | yˆi | βˆ +βˆ | xi, |
| --- | --- | --- | ------ | --- |
=
0 1
- Next,definetheresidualforobservationi asthedifferencebetweentheactualyi and
itsfittedvalueyˆi:
|     |     | uˆi = yi −yˆi | = yi −(βˆ | +βˆ xi) |
| --- | --- | ------------- | --------- | ------- |
0 1
20/67

- Anaturalobjectiveismaketotheresidualssmall
| Fitted values | and residuals |     |     |     |
| ------------- | ------------- | --- | --- | --- |
BeforedescribingOLSestimation,wefirstestablishsomenotation:
- Weusei todenoteaspecificobservationandntodenotethetotalnumberof
observations
i = 1,2,...,n
| - Forany | βˆ and βˆ definethefittedvalueforobservationi |     |     | as  |
| -------- | --------------------------------------------- | --- | --- | --- |
0 1
|     |     | yˆi | βˆ +βˆ | xi, |
| --- | --- | --- | ------ | --- |
=
0 1
- Next,definetheresidualforobservationi asthedifferencebetweentheactualyi and
itsfittedvalueyˆi:
|     |     | uˆi = yi −yˆi | = yi −(βˆ | +βˆ xi) |
| --- | --- | ------------- | --------- | ------- |
0 1
⇒What’sagoodobjectiveforapredictionrule?
20/67

| Fitted values | and residuals |     |     |     |
| ------------- | ------------- | --- | --- | --- |
BeforedescribingOLSestimation,wefirstestablishsomenotation:
- Weusei todenoteaspecificobservationandntodenotethetotalnumberof
observations
i = 1,2,...,n
| - Forany | βˆ and βˆ definethefittedvalueforobservationi |     |     | as  |
| -------- | --------------------------------------------- | --- | --- | --- |
0 1
|     |     | yˆi | βˆ +βˆ | xi, |
| --- | --- | --- | ------ | --- |
=
0 1
- Next,definetheresidualforobservationi asthedifferencebetweentheactualyi and
itsfittedvalueyˆi:
|     |     | uˆi = yi −yˆi | = yi −(βˆ | +βˆ xi) |
| --- | --- | ------------- | --------- | ------- |
0 1
⇒What’sagoodobjectiveforapredictionrule?
- Anaturalobjectiveismaketotheresidualssmall
20/67

Moreexplicitly,wecouldwrite:
n
argmin ∑ (yi −[βˆ +βˆ xi])2
0 1
βˆ 0 ,βˆ 1 i=1
tospecifythatOLScanmodify βˆ and βˆ whiley andx arefixed
0 1
The OLS objective
OLSchooses βˆ and βˆ tomakethesumofsquaredresiduals,
0 1
n
∑ uˆ2,
i
i=1
assmallaspossible
21/67

The OLS objective
OLSchooses βˆ and βˆ tomakethesumofsquaredresiduals,
0 1
n
∑ uˆ2,
i
i=1
assmallaspossible
Moreexplicitly,wecouldwrite:
n
argmin ∑ (yi −[βˆ +βˆ xi])2
0 1
βˆ 0 ,βˆ 1 i=1
tospecifythatOLScanmodify βˆ and βˆ whiley andx arefixed
0 1
21/67

- Aside: Solvinganumericalobjectiveisthewayamachine1 learns
- I’llshowyoutwodifferentwaysofsolvingtheobjective:
1. Analyticallybyhand(classicalstatistics)
2. NumericallywithR(computationalstatistics)
The OLS solution
- TogettheOLSestimatesweneedtosolvetheOLSobjective
- Inotherwords,wemustfindthespecificvaluesofβˆ andβˆ thatminimizethesumof
0 1
squaredresiduals
22/67

- I’llshowyoutwodifferentwaysofsolvingtheobjective:
1. Analyticallybyhand(classicalstatistics)
2. NumericallywithR(computationalstatistics)
The OLS solution
- TogettheOLSestimatesweneedtosolvetheOLSobjective
- Inotherwords,wemustfindthespecificvaluesofβˆ andβˆ thatminimizethesumof
0 1
squaredresiduals
- Aside: Solvinganumericalobjectiveisthewayamachine1 learns
1computer
22/67

The OLS solution
- TogettheOLSestimatesweneedtosolvetheOLSobjective
- Inotherwords,wemustfindthespecificvaluesofβˆ andβˆ thatminimizethesumof
0 1
squaredresiduals
- Aside: Solvinganumericalobjectiveisthewayamachine1 learns
- I’llshowyoutwodifferentwaysofsolvingtheobjective:
1. Analyticallybyhand(classicalstatistics)
2. NumericallywithR(computationalstatistics)
1computer
22/67

Deriving the OLS estimates by hand
Asimplifiedguideforfindingtheparametervaluesthatminimizeafunctionbyhand:
1. Definethefunction
2. Findthepartialderivativesofthefunctionwithrespecttoeachparameter
3. Setthepartialderivativestozeroandsolvefortheparametervalues2
2Youmustalsocheck(4.)thatyou’vefoundaminimumand(5.)thatit’stheglobalminimum,butwe’ll
assumethat’sthecasefornow.FormorebackgroundinformationseethisexcellentKhanAcademyarticle
23/67

| Deriving | the OLS | estimates | by hand |     |
| -------- | ------- | --------- | ------- | --- |
Inourcase:
1. ThefunctionwewanttominimizeistheOLSobjective:
n
|     |     | f(βˆ | ,βˆ ∑ (yi −[βˆ | +βˆ xi])2 |
| --- | --- | ---- | -------------- | --------- |
) =
|     |     |     | 0 1 | 0 1 |
| --- | --- | --- | --- | --- |
i=1
2. Usingthechainrule,weget:
|     |     | ∂f(βˆ | ,βˆ ) n        |               |
| --- | --- | ----- | -------------- | ------------- |
|     |     |       | 0 1 = −2 ∑ (yi | −[βˆ +βˆ xi]) |
0 1
∂βˆ
0 i=1
|     |     | ∂f(βˆ | ,βˆ ) n          |               |
| --- | --- | ----- | ---------------- | ------------- |
|     |     |       | 0 1 = −2 ∑ xi(yi | −[βˆ +βˆ xi]) |
0 1
∂βˆ
1 i=1
24/67

| Deriving                                            | the OLS | estimates: | Intercept |      |
| --------------------------------------------------- | ------- | ---------- | --------- | ---- |
| Forstep3,Istartbysolvingfortheinterceptcoefficient, |         |            |           | βˆ : |
0
n
|     |     | 0 = | −2 ∑ (yi −[βˆ +βˆ | xi]) ⇒ |
| --- | --- | --- | ----------------- | ------ |
0 1
i=1
|     |     |      | −βˆ −βˆ   |       |
| --- | --- | ---- | --------- | ----- |
|     |     | 0 =  | −2n(y¯    | x¯) ⇒ |
|     |     |      | 0         | 1     |
|     |     | βˆ = | y¯ −βˆ x¯ |       |
|     |     | 0    | 1         |       |
Wherey¯ andx¯ istheaverageacrossalltheyi’sandxi’s,respectively:
|                      |     | 1                            | n    | 1 n  |
| -------------------- | --- | ---------------------------- | ---- | ---- |
|                      |     |                              | ∑ yi | ∑ xi |
|                      |     | y¯ =                         | &    | x¯ = |
|                      |     | n                            |      | n    |
|                      |     |                              | i=1  | i=1  |
| Therefore,oncewehave |     | βˆ ,it’sstraightforwardtoget |      | βˆ   |
|                      |     | 1                            |      | 0    |
25/67

| Deriving                           | the OLS | estimates: | Slope |     |     |
| ---------------------------------- | ------- | ---------- | ----- | --- | --- |
| Next,Isolvefortheslopecoefficient, |         |            | βˆ :  |     |     |
1
n
|     |     | 0   | = −2 ∑ xi(yi | −[βˆ +βˆ | xi]) |
| --- | --- | --- | ------------ | -------- | ---- |
0 1
i=1
Insertingtheexpressionfor βˆ derivedonthepreviousslidewehave:
0
n
|     |     |     | ∑ xi(yi | −βˆ +βˆ | xi]) |
| --- | --- | --- | ------- | ------- | ---- |
|     |     | 0 = | −2 −[y¯ | x¯      |      |
|     |     |     |         | 1       | 1    |
i=1
whichwecanre-arrangetogive:
|     |     |     | ∑n  | xi(yi −y¯) |     |
| --- | --- | --- | --- | ---------- | --- |
βˆ i=1
1 =
|     |     |     | ∑n  | xi(xi −x¯) |     |
| --- | --- | --- | --- | ---------- | --- |
i=1
26/67

- Yetanotherwaytowrite βˆ is
1
sd(y) (cid:18) s (cid:19)
βˆ = cor(x,y) = r y
1 sd(x) xy
s
x
where
r
isthesamplecorrelationbetweenx andy,and
s
and
s
isthesample
xy y x
standarddeviationofy andx,respectively
Deriving the OLS solution: Slope (continued)
- Itturnsoutthatwecanre-writetheexpressionfor βˆ as
1
∑n (xi −x¯)(yi −y¯)
βˆ = i=1 ,
1 ∑n (xi −x¯)(xi −x¯)
i=1
whichisequalto
cov(x,y) s
βˆ = = xy ,
1 var(x) s2
x
where s isthesamplecovariancebetweeny andx and s2 isthesamplevarianceofx
xy x
27/67

Deriving the OLS solution: Slope (continued)
- Itturnsoutthatwecanre-writetheexpressionfor βˆ as
1
∑n (xi −x¯)(yi −y¯)
βˆ = i=1 ,
1 ∑n (xi −x¯)(xi −x¯)
i=1
whichisequalto
cov(x,y) s
βˆ = = xy ,
1 var(x) s2
x
where s isthesamplecovariancebetweeny andx and s2 isthesamplevarianceofx
xy x
- Yetanotherwaytowrite βˆ is
1
sd(y) (cid:18) s (cid:19)
βˆ = cor(x,y) = r y
1 sd(x) xy
s
x
where
r
isthesamplecorrelationbetweenx andy,and
s
and
s
isthesample
xy y x
standarddeviationofy andx,respectively
27/67

Analytical solution for OLS estimates
Insummary,theestimatesthatminimizetheOLSobjectiveis
(cid:18) (cid:19)
s
βˆ = r y
1 xy
s
x
βˆ = y¯ −βˆ x¯
0 1
Wecanverifythatthissolutioncoincideswiththelmoutputfromthehousepriceexample:
# Inputs
x <- house_data$assessedvalue_true
y <- house_data$saleamount
# Coefficients
b1 <- cor(x,y)*sd(y)/sd(x)
b0 <- mean(y)-b1*mean(x)
whichgives βˆ = −4.69and βˆ = 1.37asexpected
0 1
28/67

Finding the OLS solution with numerical optimization in
R
AsimplifiedguideforfindingtheparametersthatminimizeafunctionnumericallyinR:
1. Definetheobjectivefunction
2. CreatetheobjectivefunctioninR
3. Chooseanoptimizer3
3Again,weneedtoensurethatwe’vefoundaminimumandthatthisminimumisglobaland,again,wejust
assumethat’sthecasefornow
29/67

| Finding | the OLS | solution | with | numerical | optimization | in  |
| ------- | ------- | -------- | ---- | --------- | ------------ | --- |
R
Inourcase:
1. Theobjectivefunctionisthesameasbefore:
n
|     |     |     | f(βˆ | ,βˆ ∑ (yi | −[βˆ +βˆ xi])2 |     |
| --- | --- | --- | ---- | --------- | -------------- | --- |
|     |     |     |      | ) =       |                |     |
|     |     |     | 0    | 1         | 0 1            |     |
i=1
2. IcreatetheobjectivefunctioninRwiththecode:
| objective_fun |     | <- function(b) |     | {   |     |     |
| ------------- | --- | -------------- | --- | --- | --- | --- |
sum((y-(b[1]+b[2]*x))^2)
}
Notethatthefunctionargumentbisavectorwithtwoarguments,wherethefirst
| entryb[1]is |     | βˆ andthesecondb[2]is |     | βˆ  |     |     |
| ----------- | --- | --------------------- | --- | --- | --- | --- |
|             |     | 0                     |     | 1   |     |     |
30/67

- WefoundtheOLSsolutionineffectivelytwolinesofcode!
| OLS | solution | with numerical | optimization |     | in  |
| --- | -------- | -------------- | ------------ | --- | --- |
R
- Forstep3,Iusetheoptim()functionwiththe”BFGS”method,andinitialparameter
| valuesof |     | βˆ = βˆ = 0: |     |     |     |
| -------- | --- | ------------ | --- | --- | --- |
|          |     | 0 1          |     |     |     |
optim(
|     | method | = "BFGS",     | # Optimization | method     |             |
| --- | ------ | ------------- | -------------- | ---------- | ----------- |
|     | par    | = c(0, 0),    | # Initial      | parameters |             |
|     | fn =   | objective_fun | # Objective    | function   | to minimize |
)
whichgivesthesolution βˆ = −4.69and βˆ = 1.37. Thissolutionalignswiththe
|     |     |     | 0   | 1   |     |
| --- | --- | --- | --- | --- | --- |
analyticalsolutionuptothethirddecimalplace.
31/67

| OLS | solution | with numerical | optimization |     | in  |
| --- | -------- | -------------- | ------------ | --- | --- |
R
- Forstep3,Iusetheoptim()functionwiththe”BFGS”method,andinitialparameter
| valuesof |     | βˆ = βˆ = 0: |     |     |     |
| -------- | --- | ------------ | --- | --- | --- |
|          |     | 0 1          |     |     |     |
optim(
|     | method | = "BFGS",     | # Optimization | method     |             |
| --- | ------ | ------------- | -------------- | ---------- | ----------- |
|     | par    | = c(0, 0),    | # Initial      | parameters |             |
|     | fn =   | objective_fun | # Objective    | function   | to minimize |
)
whichgivesthesolution βˆ = −4.69and βˆ = 1.37. Thissolutionalignswiththe
|     |     |     | 0   | 1   |     |
| --- | --- | --- | --- | --- | --- |
analyticalsolutionuptothethirddecimalplace.
- WefoundtheOLSsolutionineffectivelytwolinesofcode!
31/67

Derivation vs. Numerical optimization
- Derivationbyhand
- Pros
- Fastertocomputeonceyouhavethesolution
- Easiertounderstand(e.g,thesignofβˆ
1
dependsonrxy )
- Exactestimates
- Cons
- Derivationcanbetime-consuming
- Derivationcanbedifficult
- Derivationcanbeimpossible
- NumericaloptimizationinR
- Pros
- Oftenfasttoimplement
- Ofteneasytoimplement
- Canbeappliedtovirtuallyanyobjective
- Cons
- Slowertocompute
- Hardertounderstand
- Approximateestimates
32/67

| Evaluating | a prediction | rule |
| ---------- | ------------ | ---- |
33/67

| Evaluating | a prediction | rule |     |     |
| ---------- | ------------ | ---- | --- | --- |
- Thepredictionrulewe’veconsideredsofarisoftheform:
|     |     | yˆi = βˆ +βˆ | xi  | (1) |
| --- | --- | ------------ | --- | --- |
0 1
- WealsosawhowtogettheOLSestimate βˆ and βˆ ,which,whenpluggedinto(1),
0 1
givestheOLSpredictionrule
- Next,I’llshowhowtoevaluateanypredictionrulebyitsR2 (pronounced“Rsquared”)
34/67

Decomposing yi
- OLSdecomposeseachyi intoafittedvalueandaresidual: yi yˆi +uˆi
=
- Basedonthisdecomposition,we’lldefinethreemeasuresofvariability
- Thetotalsumofsquaresmeasuresthevariabilityinyi:
n
∑
| SST= | (yi −y¯)2 |     |
| ---- | --------- | --- |
i=1
- Theexplainedsumofsquaresmeasuresthevariabilityinyˆi:
n
∑
| SSE= | (yˆi −y¯)2 |     |
| ---- | ---------- | --- |
i=1
- Theresidualsumofsquaresmeasuresthevariabilityinuˆi:
| n      |            | n     |
| ------ | ---------- | ----- |
| SSR= ∑ | (yˆi −yi)2 | ∑ uˆ2 |
=
i
| i=1 |     | i=1 |
| --- | --- | --- |
35/67

Q:DowewantR2 tobehighorlow?
R2
OLSensuresthatyˆi anduˆi areuncorrelated,sowehavethedecomposition:
| SST = | SSE+SSR, |     |     |
| ----- | -------- | --- | --- |
whichisthebasisoftheR2 metric:
TheR2 metric
R2 istheratioofexplainedtototalvariation,
| SSE  |      | SSR |     |
| ---- | ---- | --- | --- |
| R2 = | = 1− | ,   | (2) |
| SST  |      | SST |     |
soitmeasuresthefractionofthesamplevariationiny thatisexplainedbyyˆ
36/67

R2
OLSensuresthatyˆi anduˆi areuncorrelated,sowehavethedecomposition:
| SST = | SSE+SSR, |     |     |
| ----- | -------- | --- | --- |
whichisthebasisoftheR2 metric:
TheR2 metric
R2 istheratioofexplainedtototalvariation,
| SSE  |      | SSR |     |
| ---- | ---- | --- | --- |
| R2 = | = 1− | ,   | (2) |
| SST  |      | SST |     |
soitmeasuresthefractionofthesamplevariationiny thatisexplainedbyyˆ
Q:DowewantR2 tobehighorlow?
36/67

- A:In-sampleit’s0withOLS,butout-of-sampleitcanbenegative
- Withlinearregressionusingoneexplanatoryvariable(sometimescalledsimplelinear
regression),theR2 isequaltothesquaredsamplecorrelationbetweenx andy:
R2 = cor(x,y)2
SLR
- Note:thisisonlytrueforin-sampleestimation,andwon’tgenerallybetruefor
out-of-sample
Properties of R2
- ThehigherR2 thebetterthefit
- ThehighestpossibleR2 is1
- Q:WhatisthelowestpossibleR2?
37/67

- Withlinearregressionusingoneexplanatoryvariable(sometimescalledsimplelinear
regression),theR2 isequaltothesquaredsamplecorrelationbetweenx andy:
R2 = cor(x,y)2
SLR
- Note:thisisonlytrueforin-sampleestimation,andwon’tgenerallybetruefor
out-of-sample
Properties of R2
- ThehigherR2 thebetterthefit
- ThehighestpossibleR2 is1
- Q:WhatisthelowestpossibleR2?
- A:In-sampleit’s0withOLS,butout-of-sampleitcanbenegative
37/67

Properties of R2
- ThehigherR2 thebetterthefit
- ThehighestpossibleR2 is1
- Q:WhatisthelowestpossibleR2?
- A:In-sampleit’s0withOLS,butout-of-sampleitcanbenegative
- Withlinearregressionusingoneexplanatoryvariable(sometimescalledsimplelinear
regression),theR2 isequaltothesquaredsamplecorrelationbetweenx andy:
R2 = cor(x,y)2
SLR
- Note:thisisonlytrueforin-sampleestimation,andwon’tgenerallybetruefor
out-of-sample
37/67

- A:Itdependsonthepredictioncontext:
- Whenpredictingmonthlystockreturns,anR2 of0.001isconsideredhigh
- Whenpredictingbondyields,anR2 of0.001wouldbeabysmalsincesimplemodelscan
easilyreachR2 >0.3
- Therefore,a“high”R2 suchas0.7impliesthatthepredictionruleexplainsalotofthe
variationiny,butwecannotautomaticallyconcludethatit’sa“good”rule
- Wecan,however,useR2 tocomparetheabilityofdifferentpredictionrulestoexplain
thesamedependentvariable
Interpreting R2
- Q:Whatisa“high”R2?
38/67

Interpreting R2
- Q:Whatisa“high”R2?
- A:Itdependsonthepredictioncontext:
- Whenpredictingmonthlystockreturns,anR2 of0.001isconsideredhigh
- Whenpredictingbondyields,anR2 of0.001wouldbeabysmalsincesimplemodelscan
easilyreachR2 >0.3
- Therefore,a“high”R2 suchas0.7impliesthatthepredictionruleexplainsalotofthe
variationiny,butwecannotautomaticallyconcludethatit’sa“good”rule
- Wecan,however,useR2 tocomparetheabilityofdifferentpredictionrulestoexplain
thesamedependentvariable
38/67

| Example: | Using | R2 to | compare | prediction | rules |
| -------- | ----- | ----- | ------- | ---------- | ----- |
- Let’sreturntoourhousingdataandusetheR2 metrictocomparethenaiveprediction
rule,yˆi = 0+1xi withthesophisticatedOLSpredictionrule,yˆi = −4.69+1.37xi:
| # Get        | predictions           |                           |           |      |     |
| ------------ | --------------------- | ------------------------- | --------- | ---- | --- |
| y_hat_naive  |                       | <- 0 + 1*x                |           |      |     |
| y_hat_ols    | <-                    | b0+b1*x                   |           |      |     |
| ss_tot       | <- sum((y-mean(y))^2) |                           |           |      |     |
| # R2         | of the                | naive prediction          | rule      |      |     |
| ss_res_naive |                       | <- sum((y-y_hat_naive)^2) |           |      |     |
| 1 -          | ss_res_naive          | / ss_tot                  | # Result: | 0.37 |     |
| # R2         | of the                | OLS prediction            | rule      |      |     |
| ss_res_ols   | <-                    | sum((y-y_hat_ols)^2)      |           |      |     |
| 1 -          | ss_res_ols            | / ss_tot                  | # Result: | 0.71 |     |
- Theresult,R2 = 0.37andR2 = 0.71,suggeststhatOLSoutperformsnaive
|     |     | naive | OLS |     |     |
| --- | --- | ----- | --- | --- | --- |
- Wesawthisvisually,butR2 givesusanicequantificationandinterpretation: “TheOLS
predictionruleexplains71%ofthevariabilityinhousepriceswhereasthenaiveprediction
ruleonlyexplains37%”
39/67

Summarizing a regression in R: The function
summary()
> summary(reg)
Call:
lm(formula = saleamount ∼ assessedvalue_true, data = house_data)
Residuals:
Min 1Q Median 3Q Max
-251.263 -37.898 3.782 39.297 271.605
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -4.69322 8.36906 -0.561 0.575
assessedvalue_true 1.37165 0.04121 33.282 <2e-16 ***
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
Residual standard error: 66.3 on 454 degrees of freedom
Multiple R-squared: 0.7093, Adjusted R-squared: 0.7086
F-statistic: 1108 on 1 and 454 DF, p-value: < 2.2e-16
> var(reg$fitted.values)/var(house data$saleamount)
[1] 0.709288
40/67

| Other means | of evaluating | a prediction | rule |
| ----------- | ------------- | ------------ | ---- |
Inmachinelearning,themostcommonmetricsare
1. Meansquarederror(MSE):
n
1 ∑
|     |     | MSE = | (yˆi −yi)2 |
| --- | --- | ----- | ---------- |
n
i
2. Rootmeansquarederror(RMSE)
√
|     |     | RMSE = | MSE |
| --- | --- | ------ | --- |
3. Meanabsoluteerror(MAE)
n
1 ∑
|     |     | MAE = | |yˆi −yi| |
| --- | --- | ----- | --------- |
n
i
41/67

BecauseonlyMSEisaffectedbythepredictionrule(not1,n,andSST)
| MSE/RMSE | gives the | same prediction | rule | ranking as R2 |     |
| -------- | --------- | --------------- | ---- | ------------- | --- |
- Itturnsoutthatthere’sadirectrelationshipbetweentheMSEofapredictionruleand
itsSSR:
n
|     |     | SSR = ∑ | (yˆi −yi)2 |     | (3) |
| --- | --- | ------- | ---------- | --- | --- |
i=1
n
|     |     | 1     | ∑            | 1    |     |
| --- | --- | ----- | ------------ | ---- | --- |
|     |     | MSE = | (yˆi −yi)2 = | ×SSR | (4) |
|     |     | n     |              | n    |     |
i
- LookingatthedefinitionoftheR2:
|     |     |         | SSR n×MSE |     |     |
| --- | --- | ------- | --------- | --- | --- |
|     |     | R2 = 1− | = 1−      | ,   |     |
|     |     |         | SST       | SST |     |
weseethatthepredictionrulewiththehighestR2 willalsohavethelowestMSE
- Why?
42/67

| MSE/RMSE | gives the | same prediction | rule | ranking as R2 |     |
| -------- | --------- | --------------- | ---- | ------------- | --- |
- Itturnsoutthatthere’sadirectrelationshipbetweentheMSEofapredictionruleand
itsSSR:
n
|     |     | SSR = ∑ | (yˆi −yi)2 |     | (3) |
| --- | --- | ------- | ---------- | --- | --- |
i=1
n
|     |     | 1     | ∑            | 1    |     |
| --- | --- | ----- | ------------ | ---- | --- |
|     |     | MSE = | (yˆi −yi)2 = | ×SSR | (4) |
|     |     | n     |              | n    |     |
i
- LookingatthedefinitionoftheR2:
|     |     |         | SSR n×MSE |     |     |
| --- | --- | ------- | --------- | --- | --- |
|     |     | R2 = 1− | = 1−      | ,   |     |
|     |     |         | SST       | SST |     |
weseethatthepredictionrulewiththehighestR2 willalsohavethelowestMSE
- Why? BecauseonlyMSEisaffectedbythepredictionrule(not1,n,andSST)
42/67

Covariance and Correlation
43/67

Covariance
| Cov(x,y) | = E[(x −E[x])(y | −E[y])] |
| -------- | --------------- | ------- |
| 4        | E[X]            |         |
3
2
y
| 1   |     | E[Y] |
| --- | --- | ---- |
0
1-
| 0.0 | 0.2 0.4 0.6 | 0.8 1.0 |
| --- | ----------- | ------- |
x
x andy varywitheachotheraroundtheirmeans
44/67

Correlation
- Correlationisthestandardizedcovariance:
cov(x,y) cov(x,y)
|     | cor(x,y) | = = |
| --- | -------- | --- |
(cid:112)var(x)var(y) sd(x)sd(y)
- Thecorrelationisscale-invariantandtheunitsofmeasurementdon’tmatter: Itis
| alwaystruethat−1 | ≤ cor(x,y) | ≤ 1 |
| ---------------- | ---------- | --- |
- Thisgivesthedirection(−or+)andstrength(0 → 1)ofthelinearrelationship
betweenx andy.
45/67

Correlation
| 3         |         | 3         |            |
| --------- | ------- | --------- | ---------- |
| corr = 1  |         | corr = .5 |            |
| 2         |         | 2         |            |
| 1         |         | 1         |            |
| 0         |         | 0         |            |
| 1-        |         | 1-        |            |
| 2-        |         | 2-        |            |
| 3-        |         | 3-        |            |
| -3 -2 -1  | 0 1 2 3 | -3 -2 -1  | 0 1 2 3    |
| 3         |         | 3         |            |
| corr = .8 |         |           | corr = -.8 |
| 2         |         | 2         |            |
| 1         |         | 1         |            |
| 0         |         | 0         |            |
| 1-        |         | 1-        |            |
| 2-        |         | 2-        |            |
| 3-        |         | 3-        |            |
| -3 -2 -1  | 0 1 2 3 | -3 -2 -1  | 0 1 2 3    |
46/67

Correlation
Onlymeasureslinearrelationships
- cor(x,y) = 0doesnotmeanthevariablesarenotrelated!
- cor(x,y) 0doesnotimplyanycausality!
̸=
| corr = 0.01 |     | corr = 0.72 |     |
| ----------- | --- | ----------- | --- |
02
0
| 2-  | 51  |     |     |
| --- | --- | --- | --- |
01
4-
5
6-
| 8-       | 0     |        |       |
| -------- | ----- | ------ | ----- |
| -3 -2 -1 | 0 1 2 | 0 5 10 | 15 20 |
Alsobecarefulwithinfluentialobservations
47/67

| Estimating | covariance/correlation |     | from actual | data |
| ---------- | ---------------------- | --- | ----------- | ---- |
- Samplecovariance:
|     | ∑n    | (xi −x¯)(yi | −y¯)      |              |
| --- | ----- | ----------- | --------- | ------------ |
|     | = i=1 |             | (inunitsx | timesunitsy) |
s xy
n−1
- Samplestandarddeviation:
(cid:115)
|     |     | ∑n  | (xi −x¯)2 |     |
| --- | --- | --- | --------- | --- |
i=1
|     |     | s = |     | (inunitsx) |
| --- | --- | --- | --- | ---------- |
x n−1
- Samplecorrelation:
|     | s       | 1 n (xi −x¯)(yi | −y¯) |                           |
| --- | ------- | --------------- | ---- | ------------------------- |
|     | = xy =  | ∑               |      |                           |
|     | r xy    |                 |      | (correlationisscalefree!) |
|     | s s n−1 | s               | s    |                           |
|     | x y     | i=1             | x y  |                           |
48/67

| Example: | Predicting | portfolio | risk with | two assets |
| -------- | ---------- | --------- | --------- | ---------- |
Tool: Sample correlation
49/67

- Solution
- Thevarianceσ2 ofaportfoliowithtwoassetsis
p
|     |     |     |     |     | σ 2 =var(w r +w r | )           |           |
| --- | --- | --- | --- | --- | ----------------- | ----------- | --------- |
|     |     |     |     |     | p s s b           | b           |           |
|     |     |     |     |     | 2σ 2+w 2σ 2+2w    | cor(r       |           |
|     |     |     |     |     | =w                | s w b σsσ b | s ,r b ), |
|     |     |     |     |     | s s b b           |             |           |
wherer (σs )andr (σ )isthereturn(standarddeviation)ofstocksandbonds
s b b
- Hence,wemustpredicttwostandarddeviationsandonecorrelation
- Q:Howwouldyouapproachthisproblem?
| Example: | Predicting | stock-bond | portfolio | risk |     |     |     |
| -------- | ---------- | ---------- | --------- | ---- | --- | --- | --- |
- Situation
- You’reaCIOwithaw =60%exposurestocksandaw =40%exposuretobonds
|         |                                         | s   |     | b   |     |     |     |
| ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| - Goal: | Predictthevariance(risk)ofyourportfolio |     |     |     |     |     |     |
50/67

- Q:Howwouldyouapproachthisproblem?
| Example: | Predicting | stock-bond | portfolio | risk |
| -------- | ---------- | ---------- | --------- | ---- |
- Situation
- You’reaCIOwithaw =60%exposurestocksandaw =40%exposuretobonds
|         |                                         | s   |     | b   |
| ------- | --------------------------------------- | --- | --- | --- |
| - Goal: | Predictthevariance(risk)ofyourportfolio |     |     |     |
- Solution
| -   | Thevarianceσ2 | ofaportfoliowithtwoassetsis |     |     |
| --- | ------------- | --------------------------- | --- | --- |
p
|     |     | σ 2 =var(w | r +w r )    |                       |
| --- | --- | ---------- | ----------- | --------------------- |
|     |     | p          | s s b b     |                       |
|     |     | 2σ         | 2+w 2σ 2+2w | cor(r                 |
|     |     | =w         |             | s w b σsσ b s ,r b ), |
s s b b
wherer (σs )andr (σ )isthereturn(standarddeviation)ofstocksandbonds
|     | s                                                         | b b |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- |
| -   | Hence,wemustpredicttwostandarddeviationsandonecorrelation |     |     |     |
50/67

| Example: | Predicting | stock-bond | portfolio | risk |
| -------- | ---------- | ---------- | --------- | ---- |
- Situation
- You’reaCIOwithaw =60%exposurestocksandaw =40%exposuretobonds
|         |                                         | s   |     | b   |
| ------- | --------------------------------------- | --- | --- | --- |
| - Goal: | Predictthevariance(risk)ofyourportfolio |     |     |     |
- Solution
| -   | Thevarianceσ2 | ofaportfoliowithtwoassetsis |     |     |
| --- | ------------- | --------------------------- | --- | --- |
p
|     |     | σ 2 =var(w | r +w r )    |                       |
| --- | --- | ---------- | ----------- | --------------------- |
|     |     | p          | s s b b     |                       |
|     |     | 2σ         | 2+w 2σ 2+2w | cor(r                 |
|     |     | =w         |             | s w b σsσ b s ,r b ), |
s s b b
wherer (σs )andr (σ )isthereturn(standarddeviation)ofstocksandbonds
|     | s                                                         | b b |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- |
| -   | Hence,wemustpredicttwostandarddeviationsandonecorrelation |     |     |     |
- Q:Howwouldyouapproachthisproblem?
50/67

| Example: | Predicting | stock-bond | portfolio | risk |
| -------- | ---------- | ---------- | --------- | ---- |
- Data
- MonthlyreturnsontheUSstockmarketanda10yrtreasurybondfrom1941to2023
- Predictingstandarddeviations
| -   | Thestockmarkethasanannualsamplestandarddeviationof14.8% |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | --- |
| -   | The10yrbondhasanannualsamplestandarddeviationof6.9%     |     |     |     |
we’llassumethatthefutureequalsthepast
- Predictingstock-bondcorrelation
| -   | ...let’sfirstseehowitaffectsportfoliorisk |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- |
51/67

Example: Predicting stock-bond portfolio risk
- Figureshowshowportfoliostandarddeviationdependsonthestock-bondcorrelation
0.12
0.10
0.08
0.06
−1.0 −0.5 0.0 0.5 1.0
Stock−bond correlation
oiloftrop
04−06
fo
DS
- Clearly,portfoliovariabilitydependsheavilyonthestock-bondcorrelation,whichis
whyassetmanagersobsessaboutpredictingit(see,e.g.,here)
52/67

Example: Predicting stock-bond portfolio risk
- Figureshowshowportfoliostandarddeviationdependsonthestock-bondcorrelation
0.12
0.10
0.08
0.06
−1.0 −0.5 0.0 0.5 1.0
Stock−bond correlation
oiloftrop
04−06
fo
DS
- Clearly,portfoliovariabilitydependsheavilyonthestock-bondcorrelation,whichis
whyassetmanagersobsessaboutpredictingit(see,e.g.,here)
52/67

| Example: | Predicting | stock-bond | portfolio | risk |     |
| -------- | ---------- | ---------- | --------- | ---- | --- |
- Sohowcanwepredictthestock-bondcorrelation?
- Oneoptionistopredictthatthefuturestock-bondcorrelationequalsthesample
correlationthefullsamplefrom1941to2022(left)or,alternatively,therecentsample
correlationfrom2000to2023(right)
|     | Cor 1941−2023: 0.09 |     |     | Cor 2000−2023: −0.15 |     |
| --- | ------------------- | --- | --- | -------------------- | --- |
0.1
| nruter kcots ylhtnoM 0.1 |     |     | nruter kcots ylhtnoM |     |     |
| ------------------------ | --- | --- | -------------------- | --- | --- |
| 0.0                      |     |     | 0.0                  |     |     |
−0.1
−0.1
−0.2
−0.2
|     | −0.05               | 0.00 0.05 | 0.10 | −0.05 | 0.00 0.05           |
| --- | ------------------- | --------- | ---- | ----- | ------------------- |
|     | Monthly bond return |           |      |       | Monthly bond return |
53/67

Example: Predicting stock-bond portfolio risk
- Alternatively,wecancomputethecorrelationonarollingbasis,hereusingthepast10
yearsofdata
0.50
0.25
0.00
−0.25
−0.50
1960 1980 2000 2020
Date
noitalerroc
gnillor
raey
01
54/67

| Predicting | stock-bond | risk |     |     |     |
| ---------- | ---------- | ---- | --- | --- | --- |
- Basedonouranalysissofar,thestock-bondcorrelationcouldprobablyrange
between±50%:
0.12
oiloftrop 04−06 fo DS
0.10
High estimate: 0.106
Low estimate: 0.079
0.08
0.06
|     | −1.0 | −0.5 | 0.0 | 0.5 | 1.0 |
| --- | ---- | ---- | --- | --- | --- |
Stock−bond correlation
| That’samassiverange! |     | We’llworkonnarrowingitlaterinthecourse |     |     |     |
| -------------------- | --- | -------------------------------------- | --- | --- | --- |
55/67

| Adventures | in mean-variance | land |
| ---------- | ---------------- | ---- |
with linear regression
56/67

- Thesolutionis:
1
π optimal = Σ−1µ
γ
- Question: Howcanmean-varianceinvestorsuselinearregressiontofind optimal?
π
The mean-variance investor
- Manyinvestorsseemtolikehighportfoliosreturnsanddislikehighportfoliovariance
- Investorswithmean-variancepreferencestrytosolveanobjectivelike:
maxµ ′ π−γπ ′Σ π,
π
where istheinvestor’sriskaversion, isthevectorofexpectedreturns, isthe
γ µ π
vectorofportfolioweights,andΣistheassetvariance-covariancematrix
57/67

- Question: Howcanmean-varianceinvestorsuselinearregressiontofind optimal?
π
The mean-variance investor
- Manyinvestorsseemtolikehighportfoliosreturnsanddislikehighportfoliovariance
- Investorswithmean-variancepreferencestrytosolveanobjectivelike:
maxµ ′ π−γπ ′Σ π,
π
where istheinvestor’sriskaversion, isthevectorofexpectedreturns, isthe
γ µ π
vectorofportfolioweights,andΣistheassetvariance-covariancematrix
- Thesolutionis:
1
π optimal = Σ−1µ
γ
57/67

The mean-variance investor
- Manyinvestorsseemtolikehighportfoliosreturnsanddislikehighportfoliovariance
- Investorswithmean-variancepreferencestrytosolveanobjectivelike:
maxµ ′ π−γπ ′Σ π,
π
where istheinvestor’sriskaversion, isthevectorofexpectedreturns, isthe
γ µ π
vectorofportfolioweights,andΣistheassetvariance-covariancematrix
- Thesolutionis:
1
π optimal = Σ−1µ
γ
- Question: Howcanmean-varianceinvestorsuselinearregressiontofind optimal?
π
57/67

| Predicting | portfolio    | risk with  | many assets |
| ---------- | ------------ | ---------- | ----------- |
|            | Tool: Linear | regression |             |
58/67

- Withk =4assetsit’s
Var(P) =w2σ2+w2σ2+w2σ2+w2σ2
|     |     |     |     |     |     |     |     | 1 1        | 2 2 3 3       | 4 4        |            |            |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ---------- | ---------- | ---------- | --------- |
|     |     |     |     |     |     |     |     | +2[w w     | cor(r ,r )σ σ | +w w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ      |
|     |     |     |     |     |     |     |     | 1 2        | 1 2 1 2       | 1 3        | 1 3 1 3    | 1 4 1      | 4 1 4 (5) |
|     |     |     |     |     |     |     |     | +w w cor(r | ,r )σ σ +w    | w cor(r    | ,r )σ σ    |            |           |
|     |     |     |     |     |     |     |     | 2 3        | 2 3 2 3       | 2 4        | 2 4 2 4    |            |           |
|     |     |     |     |     |     |     |     | +w w cor(r | ,r )σ σ ].    |            |            |            |           |
|     |     |     |     |     |     |     |     | 3 4        | 3 4 3 4       |            |            |            |           |
- Withk >1000,it’s,well,quitecomplex
| Example: | Predicting | portfolio | risk | with many | assets |     |     |     |     |     |     |     |     |
| -------- | ---------- | --------- | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
- Situation: You’reaportfoliomanagerwithk stocksinyourportfolio
| - Goal: | Predictthevarianceofyourportfolio |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
- Answer
| -   | Thevariancewithk | =3assetsis |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ2 =w2σ2+w2σ2+w2σ2
|     |     | p 1 1 2      | 2 3 3      |         |            |            |        |     |     |     |     |     |     |
| --- | --- | ------------ | ---------- | ------- | ---------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
|     |     | +2[w w cor(r | ,r )σ σ +w | w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ ] |     |     |     |     |     |     |
|     |     | 1 2          | 1 2 1 2    | 1 3     | 1 3 1 3    | 2 3 2      | 3 2 3  |     |     |     |     |     |     |
59/67

- Withk >1000,it’s,well,quitecomplex
| Example: | Predicting | portfolio | risk | with many | assets |     |     |
| -------- | ---------- | --------- | ---- | --------- | ------ | --- | --- |
- Situation: You’reaportfoliomanagerwithk stocksinyourportfolio
| - Goal: | Predictthevarianceofyourportfolio |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
- Answer
| -   | Thevariancewithk | =3assetsis |     |     |     |     |     |
| --- | ---------------- | ---------- | --- | --- | --- | --- | --- |
σ2 =w2σ2+w2σ2+w2σ2
|     |       | p 1 1 2      | 2 3 3   |            |            |            |        |
| --- | ----- | ------------ | ------- | ---------- | ---------- | ---------- | ------ |
|     |       | +2[w w cor(r | ,r )σ σ | +w w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ ] |
|     |       | 1 2          | 1 2 1 2 | 1 3        | 1 3 1 3    | 2 3 2      | 3 2 3  |
| -   | Withk | =4assetsit’s |         |            |            |            |        |
Var(P) =w2σ2+w2σ2+w2σ2+w2σ2
|     |     | 1 1        | 2 2 3 3       | 4 4        |            |            |           |
| --- | --- | ---------- | ------------- | ---------- | ---------- | ---------- | --------- |
|     |     | +2[w w     | cor(r ,r )σ σ | +w w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ      |
|     |     | 1 2        | 1 2 1 2       | 1 3        | 1 3 1 3    | 1 4 1      | 4 1 4 (5) |
|     |     | +w w cor(r | ,r )σ σ +w    | w cor(r    | ,r )σ σ    |            |           |
|     |     | 2 3        | 2 3 2 3       | 2 4        | 2 4 2 4    |            |           |
|     |     | +w w cor(r | ,r )σ σ ].    |            |            |            |           |
|     |     | 3 4        | 3 4 3 4       |            |            |            |           |
59/67

| Example: | Predicting | portfolio | risk | with many | assets |     |     |
| -------- | ---------- | --------- | ---- | --------- | ------ | --- | --- |
- Situation: You’reaportfoliomanagerwithk stocksinyourportfolio
| - Goal: | Predictthevarianceofyourportfolio |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
- Answer
| -   | Thevariancewithk | =3assetsis |     |     |     |     |     |
| --- | ---------------- | ---------- | --- | --- | --- | --- | --- |
σ2 =w2σ2+w2σ2+w2σ2
|     |       | p 1 1 2      | 2 3 3   |            |            |            |        |
| --- | ----- | ------------ | ------- | ---------- | ---------- | ---------- | ------ |
|     |       | +2[w w cor(r | ,r )σ σ | +w w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ ] |
|     |       | 1 2          | 1 2 1 2 | 1 3        | 1 3 1 3    | 2 3 2      | 3 2 3  |
| -   | Withk | =4assetsit’s |         |            |            |            |        |
Var(P) =w2σ2+w2σ2+w2σ2+w2σ2
|     |       | 1 1                          | 2 2 3 3       | 4 4        |            |            |           |
| --- | ----- | ---------------------------- | ------------- | ---------- | ---------- | ---------- | --------- |
|     |       | +2[w w                       | cor(r ,r )σ σ | +w w cor(r | ,r )σ σ +w | w cor(r ,r | )σ σ      |
|     |       | 1 2                          | 1 2 1 2       | 1 3        | 1 3 1 3    | 1 4 1      | 4 1 4 (5) |
|     |       | +w w cor(r                   | ,r )σ σ +w    | w cor(r    | ,r )σ σ    |            |           |
|     |       | 2 3                          | 2 3 2 3       | 2 4        | 2 4 2 4    |            |           |
|     |       | +w w cor(r                   | ,r )σ σ ].    |            |            |            |           |
|     |       | 3 4                          | 3 4 3 4       |            |            |            |           |
| -   | Withk | >1000,it’s,well,quitecomplex |               |            |            |            |           |
59/67

Theyuselinearregression
| Example: | Predicting |     | portfolio | risk | with | many |     | assets |
| -------- | ---------- | --- | --------- | ---- | ---- | ---- | --- | ------ |
- Issue: Theno.ofparameterswemustpredictincreasequicklywiththeno.ofassets
|     |     |     | Variances |     | Correlations |     | Totalparameters |     |
| --- | --- | --- | --------- | --- | ------------ | --- | --------------- | --- |
k
|     |     | 1     | 1     |     |         | 0   |     | 1       |
| --- | --- | ----- | ----- | --- | ------- | --- | --- | ------- |
|     |     | 2     | 2     |     |         | 1   |     | 3       |
|     |     | 3     | 3     |     |         | 3   |     | 6       |
|     |     | 4     | 4     |     |         | 6   |     | 10      |
|     |     | 10    | 10    |     |         | 45  |     | 55      |
|     |     | 50    | 50    |     | 1,225   |     |     | 1,275   |
|     |     | 1,000 | 1,000 |     | 499,500 |     |     | 500,500 |
- Estimating,say,1,275parametersintheconventionalwayispracticallyunfeasible
- Howdoassetmanagershandlethisissue?
60/67

| Example: | Predicting |     | portfolio | risk | with | many |     | assets |
| -------- | ---------- | --- | --------- | ---- | ---- | ---- | --- | ------ |
- Issue: Theno.ofparameterswemustpredictincreasequicklywiththeno.ofassets
|     |     |     | Variances |     | Correlations |     | Totalparameters |     |
| --- | --- | --- | --------- | --- | ------------ | --- | --------------- | --- |
k
|     |     | 1     | 1     |     |         | 0   |     | 1       |
| --- | --- | ----- | ----- | --- | ------- | --- | --- | ------- |
|     |     | 2     | 2     |     |         | 1   |     | 3       |
|     |     | 3     | 3     |     |         | 3   |     | 6       |
|     |     | 4     | 4     |     |         | 6   |     | 10      |
|     |     | 10    | 10    |     |         | 45  |     | 55      |
|     |     | 50    | 50    |     | 1,225   |     |     | 1,275   |
|     |     | 1,000 | 1,000 |     | 499,500 |     |     | 500,500 |
- Estimating,say,1,275parametersintheconventionalwayispracticallyunfeasible
| - Howdoassetmanagershandlethisissue? |     |     |     |     |     | Theyuselinearregression |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
60/67

| Example: | Predicting | portfolio | risk with | many assets |
| -------- | ---------- | --------- | --------- | ----------- |
RecipeforpredictingportfolioriskwithSLR:
| 1. Regressthereturneachassetk |     |     | onthemarketreturn: |            |
| ----------------------------- | --- | --- | ------------------ | ---------- |
|                               |     |     | ri = βˆi +βˆi      | rmkt +uˆi, |
|                               |     |     | t 0                | mkt t t    |
whereri andrmkt isthereturnattimet ofasseti andthemarket,respectively
t t
2. Collectmarketbetaestimatesinthevector βˆ [βˆ1 ,βˆ2 ,...,βˆk ]′
=
mkt mkt mkt mkt
3. Calculatethesamplevarianceoftheresiduals,uˆi,foreachoftheassets
t
- Collectvarianceestimatesinthevectorσ2 = [var(uˆ1),var(uˆ2),...,var(uˆk)]′
uˆ
| 4. Calculatethevarianceofthemarketreturn,denoted |     |     |     | σ2  |
| ------------------------------------------------ | --- | --- | --- | --- |
mkt
61/67

- Thenumberofparametersisreducedfromk stockvariancesand(k2−k)/2
correlationstok residualvariancesandk marketbetas,and1marketvariance,by
usinglinearregression
- That’shuge:Withk =50asset,yougofrom1,275parametersto101!
- But,thedownsideisthatweimplicitlyassumethattheresidualsareuncorrelated
| Example: | Predicting | portfolio | risk with | many assets |
| -------- | ---------- | --------- | --------- | ----------- |
- Aftercompletingthesesteps,wecanestimatethevariance-covariancematrixas
|     |     | Σˆ  | = σ2 βˆ βˆ′ | +diag(σ2) |
| --- | --- | --- | ----------- | --------- |
mkt
|     |     |     | mkt | mkt uˆ |
| --- | --- | --- | --- | ------ |
- Andthevarianceofaspecificportfolioas:
|     |     |     | σ2  | w′Σˆw, |
| --- | --- | --- | --- | ------ |
=
p
| wherew | [w1,w2,...,wk]′ | isthevectorofportfolioweights |     |     |
| ------ | --------------- | ----------------------------- | --- | --- |
=
62/67

| Example: | Predicting | portfolio | risk with | many assets |
| -------- | ---------- | --------- | --------- | ----------- |
- Aftercompletingthesesteps,wecanestimatethevariance-covariancematrixas
|     |     | Σˆ  | = σ2 βˆ βˆ′ | +diag(σ2) |
| --- | --- | --- | ----------- | --------- |
mkt
|     |     |     | mkt | mkt uˆ |
| --- | --- | --- | --- | ------ |
- Andthevarianceofaspecificportfolioas:
|     |     |     | σ2  | w′Σˆw, |
| --- | --- | --- | --- | ------ |
=
p
| wherew | [w1,w2,...,wk]′ | isthevectorofportfolioweights |     |     |
| ------ | --------------- | ----------------------------- | --- | --- |
=
- Thenumberofparametersisreducedfromk stockvariancesand(k2−k)/2
correlationstok residualvariancesandk marketbetas,and1marketvariance,by
usinglinearregression
| -   | That’shuge:Withk | =50asset,yougofrom1,275parametersto101! |     |     |
| --- | ---------------- | --------------------------------------- | --- | --- |
- But,thedownsideisthatweimplicitlyassumethattheresidualsareuncorrelated
62/67

Advanced portfolio risk with linear regression
- Theapproachwe’vediscussedresemblestheoneusedbyMSCIBarra(link)andother
riskmodelproviders
- Inpractice,youtypicallyestimatemultiple“factors”usingcross-sectionalregressions,but
theideaisstilltoreducetheparameterdimensionalitywithregressions
- Formoredetails,IsuggestTheElementsofQuantitativeInvesting
63/67

| Lab: Getting | high quality | financial | data |
| ------------ | ------------ | --------- | ---- |
64/67

|     |     |     |     | Collect      |            | Use        | to         | Use prediction |
| --- | --- | --- | --- | ------------ | ---------- | ---------- | ---------- | -------------- |
|     |     |     |     |              | historical | statistics |            |                |
|     |     |     |     | data related | to a       | build a    | prediction | rule to        |
predict
|                |                |                 |     | problem | of interest | rule from | the data | future data |
| -------------- | -------------- | --------------- | --- | ------- | ----------- | --------- | -------- | ----------- |
| Do consumption | growth predict | stocks returns? |     |         |             |           |          |             |
- Rememberthemodelfromclass1?
|     | stockreturni | = +β GDPgrowth | +ϵi. |     |     |     |     |     |
| --- | ------------ | -------------- | ---- | --- | --- | --- | --- | --- |
β 0 1
|     |     | t+1 | t t |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
- Whatdoweneedtoestimateit?
65/67

| Do  | consumption | growth predict | stocks | returns? |     |     |
| --- | ----------- | -------------- | ------ | -------- | --- | --- |
- Rememberthemodelfromclass1?
|     |     | stockreturni | =   | +β GDPgrowth | +ϵi. |     |
| --- | --- | ------------ | --- | ------------ | ---- | --- |
|     |     |              | β   | 0 1          |      |     |
|     |     |              | t+1 |              | t    | t   |
- Whatdoweneedtoestimateit?
|     | Collect      |            | Use        | to         |     | Use prediction |
| --- | ------------ | ---------- | ---------- | ---------- | --- | -------------- |
|     |              | historical | statistics |            |     |                |
|     | data related | to a       | build a    | prediction |     | rule to        |
predict
|     | problem | of interest | rule from | the data |     | future data |
| --- | ------- | ----------- | --------- | -------- | --- | ----------- |
65/67

Getting high quality financial data
- Theinternetisfilledwithmacroandstockdata,butmanyofthesourcesareofpoor
quality
- TheST.LouisFedprovidesadatabasecalledFRED(FederalReserveEconomicData),
whicharearegoldmineformacroeconomicdata: fred.stlouisfed.org
- Togetdataonstandardequityfactors,KennethFrench’swebsiteisoneofthebest
placestogo: mba.tuck.dartmouth.edu/pages/faculty/ken.french/index.html
- Togetdataonmorethan153equityfactorsfromaroundtheworld,Ialongwith
co-authors,haveawebsite: JKPfactors.com
- Anotherpremiersourceoffinancialdata,isWRDS:wrds-www.wharton.upenn.edu/
66/67

| What prediction | rule would | you like | to build? |
| --------------- | ---------- | -------- | --------- |
- Takesometimetothinkaboutaninterestingpredictionrulethatyou’dliketobuild
- Thepredictionruleshouldbeoftheform:
βˆ +βˆ
|     |     | yˆ = | x,  |
| --- | --- | ---- | --- |
0 1
andberelatedtofinancialmarkets
| - Yourjob: choosey | andx |     |     |
| ------------------ | ---- | --- | --- |
67/67

Questions?
1/1
