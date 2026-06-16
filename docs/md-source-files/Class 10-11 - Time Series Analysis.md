MGMT924StatisticalFoundations
Class 10-11: Time-Series Analysis
Topics: Time-seriesdata,trends,seasonality,autocorrelation,autoregression,random
walks,stationarity,meanreversion,ARCH,movingaveragemodels,GARCH,ARIMA
TheisIngerslevJensen
YaleSOM
SlidesbasedonworkbyDachengXiu
1/81

Time-series data
2/81

Different Data Types
- Cross-sectionaldataaredatacollectedatagivenpointintimefordifferent“units”.
- Time-seriesdataaresimplyacollectionofobservationsgatheredovertime.
- Paneldataaredatacollectedfordifferentindividualsandacrosstime.
3/81

Time-Series Data
Timeseriesdatacananswerquestionsforwhichcross-sectionaldataareinadequate:
- Forecasting: Whatisyourestimateofnextquarter’sGDP,inflationorinterestrate?
- Dynamiccausaleffect: Whatistheeffectontrafficfatalitiesofalawrequiring
passengerstowearseatbelts?
4/81

| Time Series | Data and | Dependence |
| ----------- | -------- | ---------- |
Toemphasizethatthedataaretime-series,weindexobservationsbyt ratherthani. For
| example,supposey | ...y | are |
| ---------------- | ---- | --- |
|                  | 1    | T   |
- AnnualGDP.
- Quarterlyproductionlevels
- Weeklysales.
- Dailytemperature.
- 5minuteStockreturns.
Ineachcase,wemightexpectwhathappensattimet tobecorrelatedwithtimet −1.
5/81

| Time Series | Data and | Dependence |
| ----------- | -------- | ---------- |
- Supposewemeasuretemperaturesdailyforseveralyears.
- Whichwouldworkbetterasanestimatefortoday’stemperature:
| - Theaverageofthetemperaturesfromthepreviousyear? |     |     |
| ------------------------------------------------- | --- | --- |
| - Thetemperatureonthepreviousday?                 |     |     |
HowwouldthischangeifthereadingswereN(µ,σ2)(IID)?
-
- Correlatederrorsrequirefundamentallydifferenttechniques.
6/81

Examples of Time Series Data
- y =averagedailytemperatureatO’HarefromJan-Feb1997
t
0 10 20 30 40 50 60
05
04
03
02
01
0
day
pmet
- Theobservationsare“sticky”;todaytendstobeclosetoyesterday
7/81

Examples of Time Series Data: Dow Jones Industrial Average
- y =pricelevelofDowJonesIndustrialAverage
t
Time
IJD
1940 1960 1980 2000
00041
00001
0006
0002
0
- DJIappearstohaveatrend
8/81

Examples of Time Series Data: Beer Sales
- y =monthlyU.S.beerproduction(inmillionsofbarrels).
t
0 10 20 30 40 50 60 70
07
06
05
04
03
02
01
0
month
reeb
- Thesamepatternrepeatsitselfyearafteryear.
9/81

| Examples     | of Time      | Series Data: | IID | Normals |     |     |
| ------------ | ------------ | ------------ | --- | ------- | --- | --- |
| - y =justiid | N(0,1)draws! |              |     |         |     |     |
t
3
2
1
t_Y
0
1-
2-
3-
|     |     | 0   | 50  | 100 | 150 | 200 |
| --- | --- | --- | --- | --- | --- | --- |
t
- Itistemptingtoseepatternsevenwheretheydon’texist...
10/81

Checking for Dependence
- Toseeify wouldbeusefulforpredictingy ,justplotthemtogetherandseeifthere
t−1 t
isarelationship.
0 10 20 30 40 50
05
04
03
02
01
0
Daily Temp at O'Hare
temp(t-1)
)t(pmet
Corr = 0.72
- Correlationbetweeny andy iscalledautocorrelation
t t−1
11/81

| Checking for      | Dependence |                                  |                   |     |     |
| ----------------- | ---------- | -------------------------------- | ----------------- | --- | --- |
| - Wecanploty      | againsty   | toseeL-periodlaggedrelationships |                   |     |     |
|                   | t          | t−L                              |                   |     |     |
| 05                |            | 05                               |                   |     |     |
| Lag 2 Corr = 0.46 |            |                                  | Lag 3 Corr = 0.21 |     |     |
| 04                |            | 04                               |                   |     |     |
| 03                |            | 03                               |                   |     |     |
)t(pmet )t(pmet
| 02  |           | 02       |      |           |       |
| --- | --------- | -------- | ---- | --------- | ----- |
| 01  |           | 01       |      |           |       |
| 0   |           | 0        |      |           |       |
| 0   | 10 20     | 30 40 50 | 0 10 | 20 30     | 40 50 |
|     | temp(t-2) |          |      | temp(t-3) |       |
- ItappearsthatthecorrelationisgettingweakerwithincreasingL.
12/81

Autocorrelation
- Tosummarizethedependenceinourtimeseries,
computethelag-l correlationsforl = 1,2,3,....
- Ingeneral,theautocorrelationfunction(ACF)fory is
r(l) = cor(y ,y )
t t−l
- ForourO’Haretemperaturedata:
> print(acf(weather$temp))
Autocorrelations of series ‘weather$temp’, by lag
0 1 2 3 4 5 6 7 8
1.000 0.713 0.443 0.201 0.070 0.092 0.036 -0.007 -0.085
9 10 11 12 13 14 15 16 17
-0.099 -0.067 0.025 0.047 -0.014 -0.064 -0.057 0.004 0.099
13/81

Autocorrelation
- R’sacffunctionprovidesavisualsummaryofthetime-seriesdependence:
0 5 10 15
0.1
8.0
6.0
4.0
2.0
0.0
2.0-
Lag
FCA
Series weather$temp
- Thebluelinesshow95%confidenceintervalforanuncorrelatedseries,soactual
autocorrelationsoutsidethisrangeare“statisticallysignificant”atthe5%level
- TheACFatlag0isalways1. Why?
14/81

Autocorrelation
- TheDJIdatahasaslowdecay
0 20 40 60 80 100
8.0
4.0
0.0
Lag
FCA
Series DJIdata[, 7]
15/81

Autocorrelation
- Thebeerdatashowsanalternatingdependencestructure,whichcausestimeseries
oscillations.
0 5 10 15 20 25 30
0.1
5.0
0.0
5.0-
Lag
FCA
Series beer$prod
16/81

Autocorrelation
- Anacfplotforiid normaldatashowsnosignificantcorrelation
- Suchaseriesissometimescalledwhitenoise
0 10 20 30 40
0.1
8.0
6.0
4.0
2.0
0.0
2.0-
Lag
FCA
Series rnorm(40)
17/81

Time-Series Decomposition
18/81

- Thesuccessoftimeseriesanalysisdependsstronglyuponthesatisfactionoftwo
somewhatindependentconditions:
- Massagethedataintoastationarytimeseries.
- Modelthestationarytimeseriesandestimatemodelparameters.
Decomposing a Time Series
- Itisverycommontoseeatrend,orseasonalityinatime-series
- GDPhasbeenincreasingformanydecades.
- Stockpriceswanderaroundoverashortperiod.
- Temperaturegoesupinsummeranddowninwinter.
- GasconsumptioninNewHavendotheopposite
19/81

Decomposing a Time Series
- Itisverycommontoseeatrend,orseasonalityinatime-series
- GDPhasbeenincreasingformanydecades.
- Stockpriceswanderaroundoverashortperiod.
- Temperaturegoesupinsummeranddowninwinter.
- GasconsumptioninNewHavendotheopposite
- Thesuccessoftimeseriesanalysisdependsstronglyuponthesatisfactionoftwo
somewhatindependentconditions:
- Massagethedataintoastationarytimeseries.
- Modelthestationarytimeseriesandestimatemodelparameters.
19/81

Removing the Trend
- Thisiseasytodealwith: Justput“time”inthemodel.
y = +β t +u
| t   | β 0 1 | t   |
| --- | ----- | --- |
- Anotherwayistoconsiderthedifference:
∆y = −y = (1−B)y
| t y t                                | t−1      | t     |
| ------------------------------------ | -------- | ----- |
| whereB isa“backward”operator,i.e.,By | = y ,Bky | = y . |
|                                      | t t−1    | t t−k |
- Ify isthelogarithmofsomeeconomicvariable(whichmayexhibitexponential
t
growth),then∆y isapproximatelythepercentagechange
t
20/81

Example: DJI Index
> DJIret<-log(DJI[2:length(DJI)])-log(DJI[1:(length(DJI)-1)])
> plot(ts(DJIret,start=c(1929,2),freq=52),type="l",col="red",
ylab="DJI Returns")
Time
snruteR
IJD
1940 1960 1980 2000
1.0
0.0
1.0-
2.0-
> acf(DJIret)
0 5 10 15 20 25 30 35
0.1
8.0
6.0
4.0
2.0
0.0
Lag
FCA
Series DJIret
21/81

| Dealing with                | Seasonality                            |                         |                           |                  |      |              |          |     |
| --------------------------- | -------------------------------------- | ----------------------- | ------------------------- | ---------------- | ---- | ------------ | -------- | --- |
| - Addperiodicfunctions,e.g. |                                        |                         |                           | Periodic-kmodel: |      |              |          |     |
|                             |                                        | y                       | = β                       | +β sin(2πt/k)+β  |      | cos(2πt/k)+u |          |     |
|                             |                                        | t                       | 0                         | 1                |      | 2            |          | t   |
| Choosek                     | tobethenumberof“times”inasingleperiod. |                         |                           |                  |      |              |          |     |
| - Formonthlydata,k          |                                        |                         | =12impliesanannualcycle.  |                  |      |              |          |     |
| - Forquarterlydata,usuallyk |                                        |                         |                           | =4.              |      |              |          |     |
| - Forhourlydata,k           |                                        | =24givesyouadailycycle. |                           |                  |      |              |          |     |
| - Adddummyvariables.        |                                        |                         | Forquarterlydata,howmany? |                  |      |              |          |     |
|                             |                                        | y =                     | +β                        | 1                | +β 1 |              | +β 1     | +Z  |
|                             |                                        | t                       | β 0                       | 1 {t∈Q1}         | 2    | {t∈Q2}       | 3 {t∈Q3} | t   |
| - Differencing!             | ConsiderZ                              |                         | =                         | (1−Bk)y          | .    |              |          |     |
|                             |                                        |                         | t                         |                  | t    |              |          |     |
22/81

Example: Beer Production
> beerret<-beer$pro[13:72]-beer$pro[1:60]
> par(mfrow=c(2,1))
> plot(beerret,type="l")
> acf(beerret)
0 10 20 30 40 50 60
02
01
0
02-
Index
terreeb
0 5 10 15
0.1
6.0
2.0
2.0-
Lag
FCA
Series beerret
23/81

Autoregression
TheAR(1)Model
24/81

Autoregression
- Howdowemodeltheremainderseries? TheresidualsfromtheDJIandbear
productionlooklikewhitenoise.
- FortheDJIcase,suppose
|       |         | y = u         | ,y −y = u | ,y −y = u ,... |
| ----- | ------- | ------------- | --------- | -------------- |
|       |         | 1 1           | 2 1 2     | 3 2 3          |
| Theny | = ∑t u  | = y +u andE[y | ] = y     | .              |
|       | t i=1 i | t−1 t         | t t−1     |                |
- ThisiscalledaRandomWalkmodelfory : theexpectationofwhatwillhappenis
t
alwayswhathappenedmostrecently.
- Eventhoughy isafunctionoferrorsgoingallthewaybacktothebeginning,youcan
t
| writeitasdependingonlyony |     |     | .   |     |
| ------------------------- | --- | --- | --- | --- |
t−1
25/81

Autoregression
- Randomwalksarejustaversionofamoregeneralmodel...
- Theautoregressivemodeloforderoneholdsthat
|     | AR(1): | y t = β 0 | +β 1 y t−1 +u t |
| --- | ------ | --------- | --------------- |
- ThisisjustanSLRmodelofy regressedontolaggedy ,anditassumesallofour
|     | t   |     | t−1 |
| --- | --- | --- | --- |
standardregressionmodelconditions.
| - Theresidualsshouldlookiid | andbeuncorrelatedwithyˆ |     | .   |
| --------------------------- | ----------------------- | --- | --- |
t
- Allofourpreviousdiagnosticsandtransformsstillapply.
26/81

Autoregression
TheAR(1)model
|           |                              | AR(1): | y = +β | y +u    |
| --------- | ---------------------------- | ------ | ------ | ------- |
|           |                              |        | t β 0  | 1 t−1 t |
| - Again,Y | dependsonthepastonlythroughY |        |        | .       |
|           | t                            |        |        | t−1     |
- AR(1)meansthatpreviouslagvalues(y ,y ,...)donothelppredicty ifyoualready
t−2 t−3 t
| knowy | .   |     |     |     |
| ----- | --- | --- | --- | --- |
t−1
- Thinkaboutdailytemperatures:
- IfIwanttoguesstomorrow’stemperature(withoutknowingtheforecast!),Ibasemy
predictionontoday’stemperatureandwillprobablyignoreyesterday’stemperature.
27/81

Autoregression
- FortheO’Haretemperatures,thereisaclearautocorrelation.
- Theautoregressiveterm(βˆ ≈ 0.7)ishighlysignificant!
1
28/81

Autoregression
- Wecancheckresidualsforany“left-over”correlation.
> acf(tempreg$resid)
0 5 10 15
0.1
8.0
6.0
4.0
2.0
0.0
2.0-
Lag
FCA
Series tempreg$residuals
- Itlookslikewe’vegotagoodfit!
29/81

Autoregression
ManydifferenttypesofseriesmaybewrittenasanAR(1).
AR(1): y = β +β y +u
t 0 1 t−1 t
Thevalueof β iskey!
1
- If|β | = 1,wehavearandomwalk.
1
- If|β | > 1,theseriesexplodes.
1
- If|β | < 1,thevaluesaremeanreverting.
1
30/81

Random Walk
Inarandomwalk,theseriesjustwandersaround.
β = 1
1
0 50 100 150 200
01
5
0
Index
klaw.modnar
31/81

Random Walk
Autocorrelationofarandomwalkstayshighforalongtime.
0 5 10 15 20
0.1
8.0
6.0
4.0
2.0
2.0-
Lag
FCA
Series randwalk
32/81

Random Walk
Therandomwalkhassomespecialproperties:
- Thefirstdifferencesatisfies
y −y = β +u,
t t−1 0
where β iscalledthe“driftparameter”.
0
- Theseriesisnonstationary: ithasnoaveragelevelthatitwantstobenear,butrather
justwandersoffintospace.
-
- Therandomwalkwithoutdriftisacommonmodelforsimpleprocesses.
33/81

| Random | Walk Example: |     | DJI |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- |
Sureenough,theregressionfitlookslikearandomwalk(βˆ
- ≈ 1)
1
> summary(ARdj <- lm(log(DJI[2:length(DJI)]) ~ log(DJI[1:(length(DJI)-1)])))
Coefficients:
|     |                        |     |        | Estimate   | Std.      | Error |
| --- | ---------------------- | --- | ------ | ---------- | --------- | ----- |
|     | (Intercept)            |     |        | -0.0001131 | 0.0017492 |       |
|     | log(DJI[1:(length(DJI) |     | - 1)]) | 1.0001419  | 0.0002506 |       |
|     |                        |     |        | t value    | Pr(>|t|)  |       |
|     | (Intercept)            |     |        | -0.065     | 0.948     |       |
|     | log(DJI[1:(length(DJI) |     | - 1)]) | 3991.459   | <2e-16    | ***   |
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
|     | Residual standard                      | error:          | 0.02489 | on 4325    | degrees | of freedom |
| --- | -------------------------------------- | --------------- | ------- | ---------- | ------- | ---------- |
|     | Multiple R-squared:                    | 0.9997,Adjusted |         | R-squared: |         | 0.9997     |
|     | - Thisalsosuggeststakingthedifferencey |                 |         |            | −y      | .          |
|     |                                        |                 |         |            | t       | t−1        |
34/81

| Random | Walk Example: | DJI |     |     |     |
| ------ | ------------- | --- | --- | --- | --- |
- Andnowtheregressionmodelfindsnothingsignificant.
> summary( lm(DJIret[2:(length(DJI)-1)] ~ DJIret[1:(length(DJI)-2)]) )
Coefficients:
|     |                       |     | Estimate      | Std. Error | t value |
| --- | --------------------- | --- | ------------- | ---------- | ------- |
|     | (Intercept)           |     | 0.0008439     | 0.0003786  | 2.229   |
|     | DJIret[1:(length(DJI) | -   | 2)] 0.0099527 | 0.0152070  | 0.654   |
Pr(>|t|)
|     | (Intercept)           |     | 0.0259     | *   |     |
| --- | --------------------- | --- | ---------- | --- | --- |
|     | DJIret[1:(length(DJI) | -   | 2)] 0.5128 |     |     |
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
|                                | Residual standard   | error:             | 0.02489 on  | 4324 degrees | of freedom |
| ------------------------------ | ------------------- | ------------------ | ----------- | ------------ | ---------- |
|                                | Multiple R-squared: | 9.905e-05,Adjusted |             | R-squared:   | -0.0001322 |
| - Thisiscommonwithrandomwalks: |                     |                    | differenceY | −Y           | isiid.     |
|                                |                     |                    |             | t            | t−1        |
35/81

| Exploding Series    |                                        |     |     |     |     |
| ------------------- | -------------------------------------- | --- | --- | --- | --- |
| - ForARterm>        | 1,they valuesmoveexponentiallyfarfromy |     |     | .   |     |
|                     | t                                      |     |     | 1   |     |
| - Theseriesbelowhas | = 1.02:                                |     |     |     |     |
β 1
003
seires.gnidolpxe
002
001
0
|     | 0   | 50  | 100 | 150 | 200 |
| --- | --- | --- | --- | --- | --- |
Index
36/81

Stationary Series
- ForARterm< 1,Y isalwayspulledbacktowardsthemean
t
- Theseriesbelowhas β = 0.8:
1
0 50 100 150 200
4
2
0
2-
4-
6-
Index
seires.yranoitats
37/81

Stationary Series
- Autocorrelationforthestationaryseriesdropsoffrightaway.
0 5 10 15 20
0.1
8.0
6.0
4.0
2.0
0.0
Lag
FCA
Series stationary.series
- Thepastmatters,butwithlimitedhorizon.
38/81

Stationary Series with Negative Autocorrelation
- ItisalsopossibletohavenegativelycorrelatedAR(1)series
- Theseriesbelowhas β = −0.8:
1
0 20 40 60 80 100
6
4
2
0
2-
4-
Index
seires.rocgen
- Verynegativelycorrelatedseriesarerareinpractice,butyousometimesseeweek
negativecorrelations(we’veactuallyseenthisalready,doyourememberwhere?)
39/81

Stationarity
- Aseriesisstationaryifit’sunconditionalstatisticalpropertiesareconstantovertime
- Forexample,astationaryserieshaveaconstantunconditionalmean
- ThisissatisfiedfortheAR(1)processwhen|β | <1
1
- Importantly,thisdoesnotimplythattheconditionalstatisticalproperties,likethe
conditionalmean,areconstant
- Thinkof,say,theunconditionalmeanastheexpectedvalueofy averagedoverall
t
possiblevaluesofy ,andtheconditionalmeanastheexpectedvalueofy giventhe
t−1 t
observedy
t−1
40/81

The long-run mean of the stationary AR1 process
- Callthelong-rununconditionalmeanµ
- Forµtobeconstant,itmustbethat
µ = β +β µ,
0 1
implyingthat
β
µ = 0
(1−β )
1
41/81

- Since|β
1
| <1,y
t
isexpectedtobeclosertoµthany
t−1
Mean Reversion
- Animportantpropertyofstationaryseriesismeanreversion
- Toseethemeanreversion,rewriteµas β = µ(1−β )andplugitintotheAR(1)
0 1
model:
y = µ(1−β)+β y +u
t 1 t−1 t
= µ+β (y −µ)
1 t−1
- Whyisthisseriesmeanreverting?
42/81

Mean Reversion
- Animportantpropertyofstationaryseriesismeanreversion
- Toseethemeanreversion,rewriteµas β = µ(1−β )andplugitintotheAR(1)
0 1
model:
y = µ(1−β)+β y +u
t 1 t−1 t
= µ+β (y −µ)
1 t−1
- Whyisthisseriesmeanreverting?
- Since|β
1
| <1,y
t
isexpectedtobeclosertoµthany
t−1
42/81

Summary of AR(1) Behavior
- Stationaryseries,|β | < 1: Theserieshasameanleveltowhichitreverts. Forpositive
1
β ,theseriestendstowanderaboveorbelowthemeanlevelforawhile. Fornegative
1
β ,theseriestendstoflipbackandfortharoundthemean. Theseriesisstationary,
1
meaningthattheunconditionalmeanleveldoesnotchangeovertime.
- Randomwalks,|β | = 1: Theserieshasnomeanleveland,thus,iscalled
1
nonstationary. Thedriftparameter β isthedirectioninwhichtheserieswanders.
0
- Explodingseries,|β | > 1: Theseriesexplodes,isnonstationary,andprettymuch
1
useless.
43/81

The AR(p) Model
44/81

AR(p) Models
- ItispossibletoexpandtheARideatohigherlags
TheAR(p)model
AR(p): y t = β 0 +β 1 y t−1 +...β p y t−p +u t
- Modelestimationisstraightforwardifp isknown: Runaregressionwithp lagsofy.
- Modelselection(choiceofp)couldbebasedontrain-validation-testsplit
- Alternatively,theappropriatelagcanbechosenbytheAICorBICcriteria,whichwe
won’tcover
- Modelpredictionisslightlydifferent
45/81

| Prediction | based |     | on AR(p) | Models |     |     |     |     |     |
| ---------- | ----- | --- | -------- | ------ | --- | --- | --- | --- | --- |
- Onestepahead:
|                  |     |     | E(y      | |y        |             | )       |       |          |             |
| ---------------- | --- | --- | -------- | --------- | ----------- | ------- | ----- | -------- | ----------- |
|                  |     |     |          | t+1 1     | ,y 2 ,...,y | t       |       |          |             |
|                  |     |     | =E(β     | +β        | y +...β     | y       |       | +u |y ,y | ,...,y )    |
|                  |     |     |          | 0         | 1 t         | p       | t+1−p | t 1      | 2 t         |
|                  |     |     | =β       | +β y      | +...+β      | y       |       |          |             |
|                  |     |     | 0        | 1 t       |             | p       | t+1−p |          |             |
| Soinpractice,yˆ  |     |     | = βˆ     | +βˆ y     | +...βˆ      | y       | .     |          |             |
|                  |     | t+1 | 0        | 1         | t           | p t+1−p |       |          |             |
| - Twostepsahead: |     |     | supposep | ≥         | 2,          |         |       |          |             |
|                  |     |     | E(y      | |y ,...,y | )           |         |       |          |             |
|                  |     |     | t+2      | 1         | t           |         |       |          |             |
|                  |     | =β  | +β       | E(y       | |y ,...,y   | )+...β  |       | E(y      | |y ,...,y ) |
|                  |     |     | 0        | 1 t+1     | 1           | t       |       | p t+2−p  | 1 t         |
|                  |     | βˆ  | +βˆ      | +...βˆ    |             |         |       |          |             |
| Hence,yˆ         | y+2 | =   | yˆ t+1   |           | p y t+2−p   |         |       |          |             |
|                  |     | 0   | 1        |           |             |         |       |          |             |
⇒predictionbecomesanexplanatoryvariable!
46/81

| The partial | autocorrelation |     | function (PACF) |     |     |
| ----------- | --------------- | --- | --------------- | --- | --- |
- Theautocorrelationfunction(ACF)computesthelagbetweeny andy
t t−k
- TheACFplothelpsdetectwhitenoiseanddemonstrateautocorrelations.
- Thepartialautocorrelationfunction(PACF)computesthecorrelationbetweeny t and
| y afterremovingtheeffectofy               |     |     | ,y ,...,y |                 |     |
| ----------------------------------------- | --- | --- | --------- | --------------- | --- |
| t−k                                       |     |     | t−1 t−2   | t−k+1           |     |
| - Concretely,thepartialautocorrelationisβ |     |     |           | intheregression |     |
k
|                                              |     | y = β | +β y +β y | +...+β | y +u    |
| -------------------------------------------- | --- | ----- | --------- | ------ | ------- |
|                                              |     | t 0   | 1 t−1 2   | t−2    | k t−k t |
| - ThePACFplothelpsdeterminethecorrectorderp. |     |       |           |        |         |
47/81

PACF Plot
- WecansimulateaARprocessusingRfunctionarima.sim:
> sim.ar <- arima.sim(list(ar=c(0.4,0.4)),n=500)# y_t=0.4*y_{t-1}+0.4*y_{t-2}+e
> pacf(sim.ar, main="PACF of AR(2)")
0 5 10 15 20 25
6.0
5.0
4.0
3.0
2.0
1.0
0.0
1.0-
Lag
FCA
laitraP
PACF of AR(2)
48/81

AR(2) Estimation
> summary(lm(sim.ar[3:500]~sim.ar[2:499]+sim.ar[1:498]))
Call:
| lm(formula | = sim.ar[3:500] |     | ~   | sim.ar[2:499] | + sim.ar[1:498]) |     |
| ---------- | --------------- | --- | --- | ------------- | ---------------- | --- |
Residuals:
| Min      |          | 1Q Median |         | 3Q      | Max |     |
| -------- | -------- | --------- | ------- | ------- | --- | --- |
| -2.68154 | -0.64516 | 0.05026   | 0.63486 | 3.14059 |     |     |
Coefficients:
|               | Estimate |         | Std. Error | t value | Pr(>|t|) |     |
| ------------- | -------- | ------- | ---------- | ------- | -------- | --- |
| (Intercept)   |          | 0.03586 | 0.04564    | 0.786   | 0.432    |     |
| sim.ar[2:499] |          | 0.37129 | 0.04145    | 8.958   | <2e-16   | *** |
| sim.ar[1:498] |          | 0.38615 | 0.04155    | 9.293   | <2e-16   | *** |
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
| Residual     | standard   | error:          | 1.008   | on 495       | degrees of | freedom |
| ------------ | ---------- | --------------- | ------- | ------------ | ---------- | ------- |
| Multiple     | R-squared: | 0.4596,Adjusted |         | R-squared:   |            | 0.4574  |
| F-statistic: | 210.5      | on 2            | and 495 | DF, p-value: | <          | 2.2e-16 |
49/81

AR(2) Estimation
Alternatively,wecanusetheRfunctionarima()toestimate:
> fit<-arima(sim.ar,order=c(2,0,0))
Call:
| arima(x = sim.ar, | order = c(2, | 0, 0)) |
| ----------------- | ------------ | ------ |
Coefficients:
| ar1         | ar2 intercept |     |
| ----------- | ------------- | --- |
| 0.3706      | 0.3854 0.1658 |     |
| s.e. 0.0412 | 0.0413 0.1824 |     |
sigma^2 estimated as 1.008: log likelihood = -711.96, aic = 1431.92
Thislikelihood-basedestimationmethodworksformoregeneraltimeseriesmodels.
50/81

AR(2) Prediction
WecanusetheRfunctionpredict()topredict:
pred.ar<-predict(fit,n.ahead=8)
plot.ts(sim.ar)
lines(pred.ar$pred,col="red")
lines(pred.ar$pred+2*pred.ar$se,col="red",lty=3)
lines(pred.ar$pred-2*pred.ar$se,col="red",lty=3)
Time
ra.mis
0 100 200 300 400 500
4
3
2
1
0
1-
2-
3-
51/81

| Correlated | errors: | The ARCH | Model |
| ---------- | ------- | -------- | ----- |
52/81

The ARCH Model
- AutoRegressiveConditionalHeteroskedasticity(ARCH)modelwasproposedby
RobertEngle,whowontheNobelPrizeforthisphenomenalwork.
- Thismodelissuitableformodelingstockreturns,exchangerates,ormostfinancial
timeseries.
- ARCHanditsgeneralizationsstillplaysanimportantrolesinthefinancialindustry.
53/81

Heteroskedasticity and Homoskedasticity
- Remember,whenweassumethaterrorsareIID,weassumethaterrors,u are
t
homoskedastic,i.e.,haveaconstantvariance
- Incontrast,ifthevarianceofu variesovertimeitisheteroskedastic
t
- Inclasses7-9,wesawhowtoadjustthestandarderrorsforheteroskedasticity(and
residualdependence)
- Now,we’regoingtomodelthistheheteroskedasticitywiththegoalofpredictingthe
residualvariance
- Whyisitusefultopredictvarianceinfinance?
54/81

ARCH Model: Motivation
- ConsiderweeklyreturnsofDowJonesIndexfromJan2000tillDec2011:
u ≈ log(p )−log(p )
t t t−1
- Wecanthinkofu2 asrealizedvariance
- Oneofthekeystylizedfactsaboutstocksreturnsisthatwetendtoseevolatility
clustering,i.e.,largeu2 tendtoclustertogether
- Volatility(orvariance)clusteringcorrespondstopositiveautocorrelationinu2
- WecancheckforthisbyplottingtheACFplotofu andu2 toseeifthereisany
autocorrelation
> par(mfrow=c(1,2))
> acf(u)
> acf(u^2)
55/81

| Stock returns | exhibit   | volatility | clustering |             |     |
| ------------- | --------- | ---------- | ---------- | ----------- | --- |
|               | Series  u |            |            | Series  u^2 |     |
| 8.0           |           |            | 8.0        |             |     |
| FCA           |           |            | FCA        |             |     |
| 4.0           |           |            | 4.0        |             |     |
0.0
0.0
|     | 0 5 10 | 15 20 | 25  | 0 5 10 | 15 20 25 |
| --- | ------ | ----- | --- | ------ | -------- |
|     |        | Lag   |     |        | Lag      |
56/81

| Stock returns | exhibit volatility | clustering  |             |     |
| ------------- | ------------------ | ----------- | ----------- | --- |
|               | Series  u          |             | Series  u^2 |     |
|               | 50.0               |             | 51.0        |     |
|               | FCA laitraP        | FCA laitraP |             |     |
00.0
50.0
50.0-
01.0-
|     | 0 5 10 | 15 20 25 | 0 5 10 | 15 20 25 |
| --- | ------ | -------- | ------ | -------- |
|     | Lag    |          | Lag    |          |
ThePACFsuggestsanotherARprocessforsquaredreturns.
57/81

ARCH Model
- Letp bethelogprice,andassumethatpricesfollowarandomwalk:
t
|     | p = | p +u |     | (1) |
| --- | --- | ---- | --- | --- |
|     | t   | t−1  | t   |     |
- Then,fromthepropertiesofrandomwalks,returns(u = p −p t−1 )areunpredictable:
t t
| E            | E            |     |                    |     |
| ------------ | ------------ | --- | ------------------ | --- |
| t−1 [u t ] = | t−1 [p t ]−p | t−1 | = p t−1 −p t−1 = 0 |     |
- However,becauseofvolatilityclustering,wemightbeabletopredictu2 usingpast
realizations:
| u2 = | α +α u2 | +···+α | u2 +ϵ   | (2) |
| ---- | ------- | ------ | ------- | --- |
| t    | 0 1 t−1 |        | p t−p t |     |
- ThisisjustanAR(p)modelofsquaredreturns!
⇒Evenifwecan’tpredictreturns,wecanpredictrisk!
58/81

| ARCH Model: | Estimation |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- |
WecanestimatetheARCHmodelusinglm:
> summary(lm(u[4:623]^2~u[3:622]^2+u[2:621]^2+u[1:620]^2))
Call:
lm(formula = u[4:623]^2 ~ u[3:622]^2 + u[2:621]^2 + u[1:620]^2)
Residuals:
| Min       |           | 1Q Median |     | 3Q       | Max      |     |
| --------- | --------- | --------- | --- | -------- | -------- | --- |
| -0.003210 | -0.000592 | -0.000311 |     | 0.000145 | 0.037773 |     |
Coefficients:
|             | Estimate   | Std. | Error     | t value | Pr(>|t|) |     |
| ----------- | ---------- | ---- | --------- | ------- | -------- | --- |
| (Intercept) | 7.113e-04  |      | 8.331e-05 | 8.538   | < 2e-16  | *** |
| u[3:622]    | -1.804e-02 |      | 3.146e-03 | -5.733  | 1.54e-08 | *** |
| u[2:621]    | -1.046e-02 |      | 3.143e-03 | -3.329  | 0.000925 | *** |
| u[1:620]    | -1.092e-02 |      | 3.138e-03 | -3.481  | 0.000535 | *** |
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
59/81

| Moving | average | models |
| ------ | ------- | ------ |
60/81

The MA(1) model
- Sofar,we’vefocusedonautoregressivemodels,butanotheralternativetimeseries
modelisthemovingaveragemodel
- ThesimplestmovingaveragemodelsistheMA(1)model:
TheMA(1)model
|     | MA(1): | y = ψ +ψ | u t−1 +u |
| --- | ------ | -------- | -------- |
|     |        | t 0      | 1 t      |
- InaMA(1)model,ashockhasafinitelifetimeinthesensethatu t−1 affectsy t butnot
y ,y ,...
t+1 t+2
- InanAR(1)model,ashockhasaninfinitelifetimeinthesensethatu t−1 affectsy t ,but
| sincey affectsy | ,andy affectsy | ,andsoon,theshockliveson |     |
| --------------- | -------------- | ------------------------ | --- |
| t               | t+1 t+1        | t+2                      |     |
61/81

- Becausetheexplanatoryvariablesareunobservable
- Therefore,youneedtoresorttootherestimationmethods,likemaximumlikelihood
estimation
- InRyoucanusethearima()function
The MA(q) model
- Again,it’strivialtogeneralizetoanMA(q)process:
TheMA(q)model
MA(q): y t = ψ 0 +ψ 1 u t−1 +···+ψ q u t−q +u t
- TheMA(q)modelcan’tbefittedwithOLS.Why?
62/81

The MA(q) model
- Again,it’strivialtogeneralizetoanMA(q)process:
TheMA(q)model
MA(q): y t = ψ 0 +ψ 1 u t−1 +···+ψ q u t−q +u t
- TheMA(q)modelcan’tbefittedwithOLS.Why?
- Becausetheexplanatoryvariablesareunobservable
- Therefore,youneedtoresorttootherestimationmethods,likemaximumlikelihood
estimation
- InRyoucanusethearima()function
62/81

The ARMA model
- Ofcourse,amodelcouldhavebothautoregressiveandmovingaveragefeatures
resultinginthegeneralARMA(p,q)model:
TheARMA(p,q)model
|          |        | p     | q       |
| -------- | ------ | ----- | ------- |
|          |        | ∑     | ∑       |
| ARMA(q): | y = µ+ | α y + | ψu +u   |
|          | t      | i t−i | j t−j t |
|          |        | i=1   | j=1     |
- Again,wecanestimatethismodelwiththearima()functioninR
- Note,peoplesometimestalkaboutARIMA(p,i,q)model,wherei meanswhetheryou
takethedifferenceoftheseriesornot. Alotoftimes,wewilltakethefirstdifference
beforeanalyzingthedata,whichisequaltoi = 1
63/81

The GARCH model
64/81

The Generalized ARCH model
- TheARCHmodelledtoaNobelprize,buttodayitssuccessor,theGeneralizedARCH
model(Bollerslev,1986),orGARCH,ismuchmorewidelyused
- TounderstandARCH,supposeyouhavethemodel
r = µ +u
t t t
u = σϵ
t t t
where
- r isthereturn
t
- µt istheconditionalexpectedreturn
- σt istheconditionalstandarddeviation
- u
t
isarandomerrorwithconditionalmeanzeroandconditionalvarianceσ
t
2
- ϵt isarandomerrorwithunconditionalmeanzeroandunconditionalvarianceone
- Normally,weassumethatσ isconstant(σ = σ),andfocusonmodellingµ
t t t
- ARCH/GARCHfocusonmodellingσt
65/81

The Generalized ARCH model
- TheGARCH(1,1)modelspecifiesaprocessforσ2:
t
σ2 = ω+α u2 +β σ2 , (3)
t 1 t−1 1 t−1
wherewetypicallyimpose:
- ω >0:toensurethatthelong-runvarianceispositive
- α ≥0,β ≥0:toavoidnegativevarianceforecasts
1 1
- α +β <1:toensurestationarity
1 1
- ThisresemblesanARMA(1,1)modelforvariances(it’sanexactARMA(1,1)foru2)
t
- CanbegeneralizedtoGARCH(p,q)
- ButGARCH(1,1)workswellinpractice(AndersenandBollerslev,1998)
- Toestimatethemodel,makeanassumptionaboutthedistributionofϵ anduse
t
maximumlikelihoodestimation(nextclass)
66/81

GARCH and its cousins
67/81

| Example: | Predicting | Airline | Earnings |
| -------- | ---------- | ------- | -------- |
68/81

Putting it all together: Airline earnings
- y =monthlytotalinternationalairlinepassengers,1949-1960
t
006
005
004
003
002
001
year
sregnessap
ylhtnom
1949 1951 1953 1955 1957 1959 1961
- Weseeanincreasingannualoscillationandpositivelineartrend.
69/81

Air Passengers
- Thedatashowsastrongpersistenceincorrelation.
0 20 40 60 80 100
0.1
8.0
6.0
4.0
2.0
0.0
2.0-
4.0-
Lag
FCA
Series airline$Passengers
- Youcanseeannual(12month)periodicityshowuphereaswell.
70/81

Air Passengers
- Fittingthemodel: first,don’tforgetyourfundamentals!
- Theseriesvarianceisincreasingintime.
- Passengernumbersarelikesalesvolume.
- Weshouldbeworkingonlogscale!
5.6
0.6
5.5
0.5
year
sregnessap
ylhtnom
gol
1949 1951 1953 1955 1957 1959 1961
71/81

Air Passengers
- Theseriesshowsalineartrend,anoscillationofperiod12,andweexpecttofind
autoregressiveerrors.
|       |     |         | (cid:18) | (cid:19) (cid:18) | (cid:19) |       |
| ----- | --- | ------- | -------- | ----------------- | -------- | ----- |
|       |     |         | 2πt      | 2πt               |          |       |
| log(y | ) = | +β t +β | sin      | +β cos            | +β log(y | )+u   |
|       | t   | β 0 1   | 2        | 3                 | 4        | t−1 t |
|       |     |         | 12       | 12                |          |       |
- EstimatingthisregressioninR:
> summary(airlm <- lm(log(Y[t]) ∼ t + sin(2*pi*t/12) + cos(2*pi*t/12) + log(Y[t-1])))
|                | Estimate | Std.Error    | t-value | Pr(>|t|)     |     |     |
| -------------- | -------- | ------------ | ------- | ------------ | --- | --- |
| (Intercept)    |          | 2.532 0.360  | 7.029   | 8.77e-11 *** |     |     |
| t              |          | 0.005 0.0007 | 6.849   | 2.25e-10 *** |     |     |
| sin(2*pi*t/12) |          | 0.004 0.012  | 0.323   | 0.747        |     |     |
| cos(2*pi*t/12) |          | -0.096 0.011 | -8.068  | 3.12e-13 *** |     |     |
| log(Y[t        | - 1])    | 0.474 0.074  | 6.335   | 3.12e-09 *** |     |     |
72/81

Putting it all together: Airline data
- Themodelpredictionslookprettygood!
5.6
0.6
5.5
0.5
year
sregnessap
ylhtnom
gol
data
fitted
1949 1951 1953 1955 1957 1959 1961
- Sinandcosinetrendsseemtocapturetheperiodicity.
73/81

Air Passengers
- However,acloserlookexposesresidualautocorrellation:
1.0
0.0
1.0-
2.0-
residuals in time
year
laudiser
1949 1952 1955 1958 1961 0 5 10 15 20
0.1
6.0
2.0
2.0-
Lag
FCA
Series airlm$resid
- Howcanwefixthis?
74/81

Air Passengers
- Youcanseetherelationshipshowupinmonthlyresiduals
1 2 3 4 5 6 7 8 9 10 11 12
1.0
0.0
1.0-
2.0-
month
slaudiser
- Thisisprobablyduetoholiday/shoulderseasoneffects.
75/81

Air Passengers
- Wecreatesomeusefuldummyvariables:
dec <- airline$Month[t]==12
mar <- airline$Month[t]==3
jan <- airline$Month[t]==1
jun <- airline$Month[t]==6
jul <- airline$Month[t]==7
aug <- airline$Month[t]==8
nov <- airline$Month[t]==11
holidays <- jun|jul|aug|dec|mar
- Thenre-fitthemodelwithholidays,nov,jan,andjul.
- Monthswithholidayshaveanobviouseffect.
- novandjanhavemorevacationdays.
- julisuniqueastheentiremonthisschoolholiday.
76/81

Air Passengers
- Everythingshowsupasbeingverysignificant
77/81

Putting it all together: Airline data
- Theone-step-aheadmodelpredictionslookevenbetter
5.6
0.6
5.5
0.5
year
sregnessap
ylhtnom
gol
data
fitted
1949 1951 1953 1955 1957 1959 1961
- We’renowreallyabletocapturetheannualdynamics.
78/81

Air Passengers
- Theresidualslookniceandindependent.
| residuals in time |     | Series  airlm2$resid |     |
| ----------------- | --- | -------------------- | --- |
0.1
50.0
8.0
6.0
laudiser 00.0
FCA
4.0
| 50.0- |     | 2.0 |     |
| ----- | --- | --- | --- |
01.0-
2.0-
| 1949 1952 1955 | 1958 1961 | 0 5 10 | 15 20 |
| -------------- | --------- | ------ | ----- |
| year           |           | Lag    |       |
- Someleft-over12-monthautocorrelation,butnothingtogetoverlyworriedabout
79/81

Comments
- Analternativewaytoaddperiodicitywouldbetosimplyaddadummyvariablefor
eachmonth(feb, mar, apr, ...).
- Thisachievesbasicallythesamefitasabove,withoutrequiringyoutoaddsinorcosine.
- However,thistakes11periodicparameterswhileweuseonly6(sinandcosine+
holidays,nov,jan,andjun).
- Sincequarterlydatahasaperiodofonly4,itisoftenfinetojustadd“quarter”effects.
80/81

Thank you!
81/81
