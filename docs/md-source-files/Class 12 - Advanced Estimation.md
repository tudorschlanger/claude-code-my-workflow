MGMT924StatisticalFoundations
Class 12: Advanced Estimation
Topics: Thelikelihood,maximumlikelihood,statisticalmoments,methodofmoments,
generalizedmethodofmoments
TheisIngerslevJensen
YaleSOM
1/42

OLS estimation
- Sofarinthiscourse,OLShasbeenouronlyestimationtool:
OLSestimatesparametersbyminimizingthesumofsquaredresiduals:
n
argmin = ∑ (yi −f(xi;θˆ))2,
θˆ i=1
where θˆ is the vector of estimated parameters and f(xi;θˆ) is a function of the ex-
planatoryvariablesx thatdependsontheseestimatedparameters.
- Ifwe’reestimatingtheparametersoftheSLRmodel,wewouldhave
θˆ = [βˆ ,βˆ ]′
0 1
and
f(xi;θˆ) = βˆ +βˆ xi
0 1
2/42

| OLS is not | the only | estimation | method |
| ---------- | -------- | ---------- | ------ |
- However,OLSisnottheonlyestimationmethod,andinthisclass,we’regoingto
covertwoofthemostwidelyusedalternatives:
| - Generalizedmethodofmoments(GMM)  |     |     |     |
| ---------------------------------- | --- | --- | --- |
| - Maximumlikelihoodestimation(MLE) |     |     |     |
- GMMisoneofthemostfrequentlyusedestimationtoolsinfinance
- MLEisoneofthemostfrequentlyusedestimationtoolsinstatistics
- IfyouknowOLS,GMM,andMLE,you’rereadytofacemostestimationchallenges
3/42

| Generalized | Method | of Moments |
| ----------- | ------ | ---------- |
4/42

Generalized Method of Moments (GMM)
MotivatingPrinciple
- MLprinciple: Chooseaprobabilitymodelandestimatetheparametervaluesthatare
mostlikelytogeneratetheobserveddata
- GMMstartsfromadifferentprinciple: Setparameterstomatchcertainattributes
(samplemoments)ofthedata
5/42

Raw moments and the mean
- StatisticalmomentsareatthecoreofGMM
- A“moment”isastatisticalmeasurethatdescribessomethingaboutthedistributionof
arandomvariable
- Thekth momentofarandomvariablex isdefinedas
moment (x) = E[xk]
k
- So,forexample,thefirstmomentofx issimplyitsmean:
moment (x) = E[x]
1
6/42

- Therefore,it’ssometimesmoreinformativetofocusoncentralmoments,whichisjust
themomentofarandomvariablewithitsexpectedvaluesubtracted:
−E[x])k]
|     |     |     | centralmoment | (x) = E[(x |     |
| --- | --- | --- | ------------- | ---------- | --- |
k
- Thesecondcentralmomentisexactlythevarianceofx:
|     |     |     | centralmoment | (x) = E[(x | −E[x])2] |
| --- | --- | --- | ------------- | ---------- | -------- |
2
Central moments: variance
- Thesecondmomentofx is
E[x2],
moment (x) =
2
| whichiskindoflikethevarianceofx | butnotquite. | Why? |     |     |     |
| ------------------------------- | ------------ | ---- | --- | --- | --- |
7/42

| Central moments: variance |     |     |     |
| ------------------------- | --- | --- | --- |
| - Thesecondmomentofx      | is  |     |     |
E[x2],
|     | moment | (x) = |     |
| --- | ------ | ----- | --- |
2
| whichiskindoflikethevarianceofx |     | butnotquite. | Why? |
| ------------------------------- | --- | ------------ | ---- |
- Therefore,it’ssometimesmoreinformativetofocusoncentralmoments,whichisjust
themomentofarandomvariablewithitsexpectedvaluesubtracted:
−E[x])k]
|     | centralmoment | (x) = E[(x |     |
| --- | ------------- | ---------- | --- |
k
- Thesecondcentralmomentisexactlythevarianceofx:
|     | centralmoment | (x) = E[(x | −E[x])2] |
| --- | ------------- | ---------- | -------- |
2
7/42

Standardized central moments: skewness and kurtosis
- Anothertypeofmomentisthestandardizedcentralmoment:
E[(x −E[x])k]
standardizedcentralmoment (x) =
k E[(x −E[x])2]k
2
- Thestandardizationensuresthatthemomentsaredimensionless
- Justlikehowthecorrelationisadimensionlessalternativetothecovariance
- Thethirdstandardizedcentralmomentiscalledtheskewnessofx:
E[(x −E[x])3]
standardizedcentralmoment (x) = ,
3 E[(x −E[x])2]3
2
anditmeasurestheasymmetryofthedistribution
8/42

Standardized central moments: kurtosis
- Thefourthstandardizedcentralmomentisthekurtosisofx:
E[(x −E[x])4]
standardizedcentralmoment (x) =
4 E[(x −E[x])2]4
2
anditmeasurestheheavinessofthetailsofthedistribution
- It’sraretoconsideranythingabovethefourthstandardizedcentralmoment,butin
principle,youcould
9/42

The bottom line: moments tell you useful facts about a distribution
- Momentsmightseemabitabstract,butthey’rejustusefulfactsaboutadistribution
1. IfIknowthemeanofadistribution,Iknowwhereit’scentered
2. IfIknowthevarianceofadistribution,Iknowhowspreadoutitis
3. IfIknowtheskewnessofadistribution,Iknowhowasymmetricitis
4. IfIknowthekurtosisofadistribution,Iknowhowheavythetailsare
10/42

- Thisisexactlythesameconceptasforlinearregression,wherewehavesome
unobservablepopulationparameters, β ,andweuseOLStoestimatetheobservable
j
sampleestimates, βˆ
j
| Population                  | versus sample | moments:          | the sample  | mean |
| --------------------------- | ------------- | ----------------- | ----------- | ---- |
| - Whenwewritethatavariablex |               | hasafirstmomentof |             |      |
|                             |               | moment            | (x) = E[x], |      |
1
werefertoanunobservablepopulationmoment
- Incontrast,ifwehavenobservationsofx,thenwecancomputeit’smean
|     |     |         | 1          | n    |
| --- | --- | ------- | ---------- | ---- |
|     |     | momˆent | (x) = x¯ = | ∑ xi |
1
n
i=1
whichistheequivalentobservablesamplemoment
11/42

| Population                  | versus sample | moments:          | the sample  | mean |
| --------------------------- | ------------- | ----------------- | ----------- | ---- |
| - Whenwewritethatavariablex |               | hasafirstmomentof |             |      |
|                             |               | moment            | (x) = E[x], |      |
1
werefertoanunobservablepopulationmoment
- Incontrast,ifwehavenobservationsofx,thenwecancomputeit’smean
|     |     |         | 1          | n    |
| --- | --- | ------- | ---------- | ---- |
|     |     | momˆent | (x) = x¯ = | ∑ xi |
1
n
i=1
whichistheequivalentobservablesamplemoment
- Thisisexactlythesameconceptasforlinearregression,wherewehavesome
unobservablepopulationparameters, β ,andweuseOLStoestimatetheobservable
j
sampleestimates, βˆ
j
11/42

| Population | versus sample | moments: | the sample | variance |
| ---------- | ------------- | -------- | ---------- | -------- |
- Similarly,wecanestimatethesecondcentralsamplemomentas
1 n
|     | centralmˆ |             |           | ∑ (xi −x¯)2, |
| --- | --------- | ----------- | --------- | ------------ |
|     |           | oment (x) = | vaˆr(x) = |              |
|     |           | 2           | n−1       |              |
i=1
whichisjustthesamplevarianceofx
- Again,wedividebyn−1ratherthannbecausewe’veused1degreeoffreedomto
estimatethemean
12/42

The Method of Moments Idea
- Themethodofmomentsideaistoestimateunknownparametersbyensuringthat
samplemomentsaresetequaltosometheoreticalpopulationmoments
- We’llcometothegeneralizedpartlater,butfirst,we’llusethemethodofmomentsto
estimatetheparametersoftheSLRmodel:
y = β +β x +u
0 1
13/42

| Estimating | the SLR | model with | the method | of moments |
| ---------- | ------- | ---------- | ---------- | ---------- |
- WhenwespecifiedtheSLR,weassumedthattherandomerrorwasmeanzeroand
| meanindependentofx |     | inthepopulation: |     |     |
| ------------------ | --- | ---------------- | --- | --- |
E[u] =
0
E[u|x] E[u]
|                                 |     |          | =                     | = 0  |
| ------------------------------- | --- | -------- | --------------------- | ---- |
| - Thelastassumptionimpliesthatu |     |          | andx areuncorrelated: |      |
|                                 |     | Cov(u,x) | = E[ux]               | = 0, |
(whichisthefirstmomentoftherandomvariableux)
⇒WecanexploitthesetwomomentconditionstoestimatetheSLRparameters!
14/42

Method of Moments
- Wecanestimatethesepopulationmomentsusingtheirsamplecounterparts
Specifically,E[u]
- = 0meansthatpopulationerrorsarezeroofaverage,sowechoose
βˆ and βˆ tomakeoursampleresidualszeroonaverage:
0 1
1 n
| E[u]                                 |       | ∑ −βˆ     | −βˆ                          |
| ------------------------------------ | ----- | --------- | ---------------------------- |
|                                      | = 0 ⇔ | (y        | x ) = 0                      |
|                                      |       | n i       | 0 1 i                        |
| (cid:124)(cid:123)(cid:122)(cid:125) |       | i         |                              |
| populationmoment                     |       | (cid:124) | (cid:123)(cid:122) (cid:125) |
samplemoment
- Simultaneously,u andx areuncorrelatedatthepopulationlevel,E[ux] = 0,sowe
βˆ βˆ
choose and tomakethemuncorrelatedinoursample:
0 1
1 n
| E[ux]                                  |       | ∑      |              |
| -------------------------------------- | ----- | ------ | ------------ |
|                                        | = 0 ⇔ | (y −βˆ | −βˆ x )x = 0 |
|                                        |       | n i    | 0 1 i i      |
| (cid:124) (cid:123)(cid:122) (cid:125) |       |        |              |
i
| populationmoment |     | (cid:124) | (cid:123)(cid:122) (cid:125) |
| ---------------- | --- | --------- | ---------------------------- |
samplemoment
15/42

Method of Moments
Thisgivesustwoequationsintwounknowns(βˆ βˆ
- 0 and 1 ),
1 n
∑ −βˆ −βˆ
| (y    | x ) = 0 |     |
| ----- | ------- | --- |
| n i 0 | 1 i     |     |
i
1 n
∑ −βˆ −βˆ
| (y 0 | 1 x )x = 0, |     |
| ---- | ----------- | --- |
| n i  | i i         |     |
i
whichensuresauniquesolution
- Thefirstequationisequivalentto
−βˆ −βˆ
| y¯  | x¯ = 0, |     |
| --- | ------- | --- |
0 1
whichwecanre-arrangetogive
| βˆ = y¯ −βˆ | x¯  | (1) |
| ----------- | --- | --- |
| 0           | 1   |     |
16/42

Method of Moments
βˆ
- Takingtheexpressionfor 0 from(1)andpluggingitintothesecondequationgives:
1 n
|     | ∑   | −βˆ x¯)−βˆ |           |     |
| --- | --- | ---------- | --------- | --- |
|     | (y  | −(y¯       | x )x = 0, |     |
|     | n i | 1          | 1 i i     |     |
i
| i.e.,oneequationinoneunknown(βˆ |     | )   |     |     |
| ------------------------------- | --- | --- | --- | --- |
1
- Wecanre-arrangethistogive:
|     | n    |             | n       |     |
| --- | ---- | ----------- | ------- | --- |
|     | ∑ (y | −y¯) = βˆ ∑ | (x −x¯) |     |
|     | x i  | i 1         | x i i   |     |
|     | i    |             | i       |     |
- Frombasicpropertiesofthesummationoperator,wehavethat
| n         | n           |          | n         | n          |
| --------- | ----------- | -------- | --------- | ---------- |
| ∑         | ∑           |          | ∑         | ∑          |
| x (y −y¯) | = (x −x¯)(y | −y¯) and | x (x −x¯) | = (x −x¯)2 |
| i i       | i           | i        | i i       | i          |
| i         | i           |          | i         | i          |
17/42

Method of Moments
- Therefore,providedthatthere’ssomedispersionintheexplanatoryvariables:
n
∑ −x¯)2
|     | (x  | > 0, |
| --- | --- | ---- |
i
i
theestimatedslopeis
| ∑n(x | −x¯)(y −y¯) | coˆv(x,y) |
| ---- | ----------- | --------- |
| βˆ = | i i i       | =         |
1
|     | ∑n(x −x¯)2 | vaˆr(x) |
| --- | ---------- | ------- |
i i
- Inotherwords,exactlythesameastheOLSestimator
18/42

The Generalized Method of Moments
- Themethodofmomentsmethodologyworkswhenyouhaveasmanymoment
restrictionsasparameters
- Forexample,forestimatingtheSLRmodel,wehavetwomomentrestrictions(E[u] =0
andE[ux] =0)andtwoparameters(β andβ )
0 1
- Thegeneralizedmethodofmomentsworkswhenyouhavemoremomentsthan
parameters
- Foranexample,supposeyouassumethatx ist distributedwithunknowndegreeof
freedom,ν:
x ∼ t(ν)
andyouwanttoestimateν
19/42

The Generalized Method of Moments
- Thevariance(secondmoment)ofat distributedvariableis
ν
E[x2] = ,
ν−2
andthekurtosis(fourthmoment)is
3ν2
E[x4] =
(ν−2)(ν−4)
- Bothofthesemomentsdependofν,sowehavemoremomentsthanparameters
- TheMMapproachistochooseνtomatchonemomenttoexactly
- TheGMMapproachistochooseνtomatchbothmomentsapproximately
20/42

The Generalized Method of Moments
- Letvaˆr(x)andkuˆrt(x)be,respectively,thesamplevarianceandkurtosisofx
- Next,letg beavectorthatcomputesthedifferencebetweenthesampleand
populationmomentsasafunctionofν:
(cid:34) (cid:35)
vaˆr(x)− ν
g = ν−2
kuˆrt(x)− 3ν2
(ν−2)(ν−4)
- GMMchoosesνtominimizetheweighteddistanceofsampleversuspopulation
momentsusingaweightingmatrixW1:
TheGMMEstimator
ming′Wg
ν
1ThereaaremanywaystochooseW,butasimplechoiceistheidentitymatrix(whichweighmoments
equally)
21/42

| Maximum | Likelihood | Estimation |
| ------- | ---------- | ---------- |
22/42

The maximum likelihood principle
- Maximumlikelihoodprinciple: Picktheparametersthatmaketheobserveddatamost
likelygivenanassumeddistribution(RonaldFisherca.1920’s). Parametersarenot
random(though,ofcourse,estimatesare)
- Thisisclassicalstatistics. ContrastwithBayesianstates,inwhichparametersare
randomvariables,andweseekposteriordistributionsofparameters,“parametersthat
aremostlikely,”giventhedata
23/42

- That’sallfine,buthowcanwecomputethe“likelihood”ofthedata?
| Maximum | Likelihood | Estimation |
| ------- | ---------- | ---------- |
Properties
- Besidesbeingintuitivelyreasonable,themaximumlikelihoodprincipleleadstosome
niceestimatorproperties
- Aslongas
| - Correctlyspecified |     |     |
| -------------------- | --- | --- |
- Likelihoodwellbehaved(continuity,integrabilityofit,andvariousderivatives)
| - Uniquelyidentified |     |     |
| -------------------- | --- | --- |
then:
| 1. Consistency:Thenθˆa |     | → .s. |
| ---------------------- | --- | ----- |
θ 0
Efficiency:ThenθˆachievestheCramer-Raolowerbound–minimumvarianceinclassof
2.
consistentestimators
- FromComputerAgeStatisticalInference: Rouglyspeaking,maximumlikelihood
estimationprovidesnearlyunbiasedestimatesofnearlyminimumvariance
24/42

| Maximum | Likelihood | Estimation |
| ------- | ---------- | ---------- |
Properties
- Besidesbeingintuitivelyreasonable,themaximumlikelihoodprincipleleadstosome
niceestimatorproperties
- Aslongas
| - Correctlyspecified |     |     |
| -------------------- | --- | --- |
- Likelihoodwellbehaved(continuity,integrabilityofit,andvariousderivatives)
| - Uniquelyidentified |     |     |
| -------------------- | --- | --- |
then:
| 1. Consistency:Thenθˆa |     | → .s. |
| ---------------------- | --- | ----- |
θ 0
Efficiency:ThenθˆachievestheCramer-Raolowerbound–minimumvarianceinclassof
2.
consistentestimators
- FromComputerAgeStatisticalInference: Rouglyspeaking,maximumlikelihood
estimationprovidesnearlyunbiasedestimatesofnearlyminimumvariance
- That’sallfine,buthowcanwecomputethe“likelihood”ofthedata?
24/42

|     |     |     | - It’sµ =5!    |                      |     |
| --- | --- | --- | -------------- | -------------------- | --- |
|     |     |     | - Howlikelyisµ | = 4? Lesslikelythanµ | = 5 |
- Howlikelyisµ = 4.5? Lesslikelythanµ = 5,butmorelikelythanµ = 4
- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
| The likelihood | for one data | point |     |     |     |
| -------------- | ------------ | ----- | --- | --- | --- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |     |     |     |
| -------------------- | --- | --------------------------- | --- | --- | --- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
25/42

|     |     |     | - Howlikelyisµ | = 4? Lesslikelythanµ | = 5 |
| --- | --- | --- | -------------- | -------------------- | --- |
- Howlikelyisµ = 4.5? Lesslikelythanµ = 5,butmorelikelythanµ = 4
- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
| The likelihood | for one data | point |     |     |     |
| -------------- | ------------ | ----- | --- | --- | --- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |     |     |     |
| -------------------- | --- | --------------------------- | --- | --- | --- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
| - It’sµ =5! |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
25/42

Lesslikelythanµ = 5
- Howlikelyisµ = 4.5? Lesslikelythanµ = 5,butmorelikelythanµ = 4
- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
| The likelihood | for one data | point |
| -------------- | ------------ | ----- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |
| -------------------- | --- | --------------------------- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
| - It’sµ =5!    |      |     |
| -------------- | ---- | --- |
| - Howlikelyisµ | = 4? |     |
25/42

|     |     |     | Lesslikelythanµ | = 5,butmorelikelythanµ | = 4 |
| --- | --- | --- | --------------- | ---------------------- | --- |
- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
| The likelihood | for one data | point |     |     |     |
| -------------- | ------------ | ----- | --- | --- | --- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |     |     |     |
| -------------------- | --- | --------------------------- | --- | --- | --- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
| - It’sµ =5!    |                      |     |     |     |     |
| -------------- | -------------------- | --- | --- | --- | --- |
| - Howlikelyisµ | = 4? Lesslikelythanµ | = 5 |     |     |     |
| - Howlikelyisµ | = 4.5?               |     |     |     |     |
25/42

- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
| The likelihood | for one data | point |
| -------------- | ------------ | ----- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |
| -------------------- | --- | --------------------------- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
| - It’sµ =5!    |                      |     |
| -------------- | -------------------- | --- |
| - Howlikelyisµ | = 4? Lesslikelythanµ | = 5 |
- Howlikelyisµ = 4.5? Lesslikelythanµ = 5,butmorelikelythanµ = 4
25/42

| The likelihood | for one data | point |
| -------------- | ------------ | ----- |
- Supposethatweobservesomedatafromanormaldistribution,x ∼ N(µ,1),where
| weknowthevariance(σ2 | =   | 1),butwedon’tknowthemean(µ) |
| -------------------- | --- | --------------------------- |
- Supposeyouobserveonedatapoint,x = 5,what’sthemostlikelyvalueofµgiven
1
thisobservation?
| - It’sµ =5!    |                      |     |
| -------------- | -------------------- | --- |
| - Howlikelyisµ | = 4? Lesslikelythanµ | = 5 |
- Howlikelyisµ = 4.5? Lesslikelythanµ = 5,butmorelikelythanµ = 4
- Toquantifythelikelihoodofadatapoint,weuseprobabilitydensityfunctions(PDFs)
25/42

The likelihood for one data point
- You’vealreadyseenseveralexamplesofaprobabilitydensityfunction. Thepicture
belowshowsoneexamplesforN(µ = 5,σ2 = 1):
0.4
0.3
0.2
0.1
0.0
0 1 2 3 4 5 6 7 8 9 10
x
ytisneD
PDF of Normal(5, 1)
- Theheightofthegraphshowsthedensityateachvalueofx,roughlyspeaking,it
measurestherelativeprobabilityofobservingaspecificpoint
- So,arandomobservationfromN(µ =5,σ2 =1)isaroundtwiceaslikelytobex =5as
itistobe,say,x =3.8
- TogettheexactdensityinR,wecanusednorm(),e.g.,dnorm(5, mean=5, sd=1)=0.4
26/42

| The likelihood | for | one data | point |     |     |     |
| -------------- | --- | -------- | ----- | --- | --- | --- |
- Lookingatthedensityofx = 5forµ = 5versusµ = 4capturesourearlierintuition
thattheobservationismorelikelyintheformerdistribution:
|         | PDF of Normal(5, 1) |       |            | PDF of Normal(4, 1) |           |          |
| ------- | ------------------- | ----- | ---------- | ------------------- | --------- | -------- |
|         | 0.4                 |       |            | 0.4                 |           |          |
|         | 0.3                 |       |            | 0.3                 |           |          |
| ytisneD |                     |       |            | ytisneD             |           |          |
|         | 0.2                 |       |            | 0.2                 |           |          |
|         | 0.1                 |       |            | 0.1                 |           |          |
|         | 0.0                 |       |            | 0.0                 |           |          |
|         | 0 1 2               | 3 4 5 | 6 7 8 9 10 | 0 1                 | 2 3 4 5 6 | 7 8 9 10 |
|         |                     | x     |            |                     | x         |          |
- WorkingwithPDFs,wecanquantifytherelativelikelihood:
|     |     | dnorm(5, | mean = | 5, sd = 1) | = 0.40  |     |
| --- | --- | -------- | ------ | ---------- | ------- | --- |
|     |     | dnorm(4, | mean = | 5, sd = 1) | = 0.24, |     |
soobservingx = 5isappromimately1.6timesmorelikelyforµ = 5relativetoµ = 4!
27/42

| The MLE | for one | data point |     |     |     |     |
| ------- | ------- | ---------- | --- | --- | --- | --- |
- Itturnsoutthatifwesearchacrosstherangeofallvaluesforµ,thenµ = 5givesthe
| highestlikelihoodforx |     | = 5 |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
- Therefore,consistentwithoutintuition,µˆ = 5isthemaximumlikelihoodestimatorof
µgiventheobserveddata
|         | PDF of Normal(5, 1) |         |          | PDF of Normal(4, 1) |         |          |
| ------- | ------------------- | ------- | -------- | ------------------- | ------- | -------- |
|         | 0.4                 |         |          | 0.4                 |         |          |
|         | 0.3                 |         |          | 0.3                 |         |          |
| ytisneD |                     |         | ytisneD  |                     |         |          |
|         | 0.2                 |         |          | 0.2                 |         |          |
|         | 0.1                 |         |          | 0.1                 |         |          |
|         | 0.0                 |         |          | 0.0                 |         |          |
|         | 0 1 2               | 3 4 5 6 | 7 8 9 10 | 0 1 2               | 3 4 5 6 | 7 8 9 10 |
|         |                     | x       |          |                     | x       |          |
28/42

- Ofcourse,(2)isexactlywhatyougetfromdnorm():
| The MLE | for one data | point |     |     |     |
| ------- | ------------ | ----- | --- | --- | --- |
- Wecanseethatµ = x forasingledatapointbywritingtheexplicitprobability
i
densityfunctionforthenormaldistribution:
(cid:16)xi−µ(cid:17)2
1 −1
|     |     | d(x,θ) | = √ e | 2 σ | (2) |
| --- | --- | ------ | ----- | --- | --- |
i
σ 2π
- Ifweknowthevariance,σ2,thenthisdensityonlydependsonthedifferencebetween
x andµ,andthatit’smaximizedatµ = x (because−z2 ismaximizedatz = 0)
| i   |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- |
29/42

| The MLE | for one data | point |     |     |     |
| ------- | ------------ | ----- | --- | --- | --- |
- Wecanseethatµ = x forasingledatapointbywritingtheexplicitprobability
i
densityfunctionforthenormaldistribution:
(cid:16)xi−µ(cid:17)2
1 −1
|     |     | d(x,θ) | = √ e | 2 σ | (2) |
| --- | --- | ------ | ----- | --- | --- |
i
σ 2π
- Ifweknowthevariance,σ2,thenthisdensityonlydependsonthedifferencebetween
x andµ,andthatit’smaximizedatµ = x (because−z2 ismaximizedatz = 0)
| i   |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- |
- Ofcourse,(2)isexactlywhatyougetfromdnorm():
29/42

| The likelihood | for many | data points |     |     |
| -------------- | -------- | ----------- | --- | --- |
- Whathappensifweobservemorethanonedatapoint?
- Wemaximizethelikelihoodofalldatapoints!
- Ifthedatapointsareindependent,asintheSLRmodel,wecansimplytakethe
productofthelikelihoodsfortheindividualdatapoints:
|     |     | L = d(x ;θˆ)×d(x | ;θˆ)×···×d(x | ;θˆ), |
| --- | --- | ---------------- | ------------ | ----- |
|     |     | 1                | 2            | n     |
- Inpractice,it’susuallyeasier(andgivesthesameestimates)toworkwiththesumof
theloglikelihoods:
|     | log(L) = | log(d(x ;θˆ))+log(d(x | ;θˆ))+···+log(d(x | ;θˆ)), |
| --- | -------- | --------------------- | ----------------- | ------ |
|     |          | 1                     | 2                 | n      |
30/42

The maximum likelihood estimator
The Maximum Likelihood Estimator: Let x = (x ,...,x ) be a data set with likelihood
1 n
(probabilitydensityfunctions)givenbyL = f(x;θ). Theformoff isknown,butparame-
tersθ areunknown. TheMLEis
θˆ = argmaxL
θ
- TofindtheMLE,you,therefore,needtospecify
1. Data:Theobserveddata(e.g.,x)
2. Distribution:Theprobabilitydensityfunctionofthedata(e.g.,normal)
3. Parameters:Theparametersyouneedtoestimate(e.g.,themean)
- Onceyouhavethose,youcanfindthemaximumlikelihoodestimatorbyanalytical
derivationornumericaloptimization
31/42

| The | maximum | likelihood |     |     | estimator | for | the normal | mean |     |     |
| --- | ------- | ---------- | --- | --- | --------- | --- | ---------- | ---- | --- | --- |
- Continuingourpreviousexamplewithx ∼ N(µ,1),andsupposeweobservedtwo
|     | observations,x                              | 1 =    | 5andx          | 2   | = 4,then |     |     |     |     |     |
| --- | ------------------------------------------- | ------ | -------------- | --- | -------- | --- | --- | --- | --- | --- |
|     | 1. Data:x                                   | =5andx |                | =4  |          |     |     |     |     |     |
|     |                                             | 1      | 2              |     |          |     |     |     |     |     |
|     | 2. Distribution:Normalwithknownvarianceofσ2 |        |                |     |          |     | =1  |     |     |     |
|     | 3. Parameters:                              | µ      | (sinceweknowσ2 |     |          | =1) |     |     |     |     |
- From(2),weknowthatthelikelihoodofthetwodatapointsis:
|     |     |     |             |     |     | 1   | (5−µ)2 | 1   | (4−µ)2 |     |
| --- | --- | --- | ----------- | --- | --- | --- | ------ | --- | ------ | --- |
|     |     | L = | d(x ,θ)×d(x |     | ,θ) | = √ | e−1    | × √ | e−1    | ,   |
|     |     |     | 1           |     | 1   |     | 2      |     | 2      |     |
|     |     |     |             |     |     | 2π  |        | 2π  |        |     |
32/42

| Deriving | the | MLE | of the | normal | mean |     |     |     |     |
| -------- | --- | --- | ------ | ------ | ---- | --- | --- | --- | --- |
- Westartbytakingthelog-likelihoodbecauseit’seasiertoworkwith
|     |        |     | (cid:18)          |            |                 |            | (cid:19)          |                 |          |
| --- | ------ | --- | ----------------- | ---------- | --------------- | ---------- | ----------------- | --------------- | -------- |
|     |        |     | 1                 | e−1 (5−µ)2 | 1               | e−1 (4−µ)2 |                   |                 |          |
|     | log(L) | =   | log √             |            | × √             |            |                   |                 |          |
|     |        |     |                   | 2          |                 | 2          |                   |                 |          |
|     |        |     | 2π                |            |                 | 2π         |                   |                 |          |
|     |        |     | (cid:18)          |            | (cid:19)        | (cid:18)   | (cid:19)          |                 |          |
|     |        |     | 1                 | e−1 (5−µ)2 |                 | 1 e−1      | (4−µ)2            |                 |          |
|     |        | =   | log √             |            | +log            | √          |                   |                 |          |
|     |        |     |                   | 2          |                 |            | 2                 |                 |          |
|     |        |     | 2π                |            |                 | 2π         |                   |                 |          |
|     |        |     | (cid:18)          | (cid:19)   |                 |            | (cid:18) (cid:19) |                 |          |
|     |        |     | 1                 |            | (cid:16) (5−µ)2 | (cid:17)   | 1                 | (cid:16) (4−µ)2 | (cid:17) |
|     |        | =   | log √             | +log       | e−1             | +log       | √ +log            | e−1             |          |
|     |        |     |                   |            | 2               |            |                   | 2               |          |
|     |        |     | 2π                |            |                 |            | 2π                |                 |          |
|     |        |     | 1                 |            | 1               |            |                   |                 |          |
|     |        | =   | c− (5−µ)2−        |            | (4−µ)2,         |            |                   |                 |          |
|     |        |     | 2                 |            | 2               |            |                   |                 |          |
|     |        |     | (cid:16) (cid:17) |            |                 |            |                   |                 |          |
√1
| wherec | =   | 2log | isaconstantthatdoesn’tdependonµ |     |     |     |     |     |     |
| ------ | --- | ---- | ------------------------------- | --- | --- | --- | --- | --- | --- |
2π
33/42

- Alternatively,wecouldhaveusedoptim()inRtofindthevalueofµthatmaximizes
thelog-likelihood
Deriving the MLE of the normal mean
- Differentiatingthelog-likelihoodwithrespecttoµ:
∂log(L)
= (5−µ)+(4−µ)
∂µ
- Settingthistozeroandsolvingforµ,wegetthemaximumlikelihoodestimatorforthe
normalmean:
1
µMLE = (5+4) = 4.5,
2
whichisjustthesamplemeanofx andx !
1 2
34/42

Deriving the MLE of the normal mean
- Differentiatingthelog-likelihoodwithrespecttoµ:
∂log(L)
= (5−µ)+(4−µ)
∂µ
- Settingthistozeroandsolvingforµ,wegetthemaximumlikelihoodestimatorforthe
normalmean:
1
µMLE = (5+4) = 4.5,
2
whichisjustthesamplemeanofx andx !
1 2
- Alternatively,wecouldhaveusedoptim()inRtofindthevalueofµthatmaximizes
thelog-likelihood
34/42

- ThisisthesameassumptionweusedtoderivethesamplingdistributionoftheOLS
estimators,butnowwe’reusingtheassumptionforestimationratherthaninference
| Maximum | likelihood | estimation | of the SLR | model |
| ------- | ---------- | ---------- | ---------- | ----- |
- Next,we’lluseMLEtoestimatetheparametersoftheSLRmodel:
|     |     |     | y = β +β x | +u  |
| --- | --- | --- | ---------- | --- |
|     |     |     | 0 1        |     |
- ToestimateMLE,weneedtoaddmorestructuretotheSLRmodelthanforOLS
estimation;inparticularweneedtomakeanassumptionaboutthedistributionofu
- We’llassumethatu isnormalwithameanof0andanunknownvarianceofσ2:
u ∼ N(0,σ2)
35/42

| Maximum | likelihood | estimation | of the SLR | model |
| ------- | ---------- | ---------- | ---------- | ----- |
- Next,we’lluseMLEtoestimatetheparametersoftheSLRmodel:
|     |     |     | y = β +β x | +u  |
| --- | --- | --- | ---------- | --- |
|     |     |     | 0 1        |     |
- ToestimateMLE,weneedtoaddmorestructuretotheSLRmodelthanforOLS
estimation;inparticularweneedtomakeanassumptionaboutthedistributionofu
- We’llassumethatu isnormalwithameanof0andanunknownvarianceofσ2:
u ∼ N(0,σ2)
- ThisisthesameassumptionweusedtoderivethesamplingdistributionoftheOLS
estimators,butnowwe’reusingtheassumptionforestimationratherthaninference
35/42

| The MLE | estimator | of the SLR | model |     |
| ------- | --------- | ---------- | ----- | --- |
- Withthisassumptionfortheerrorterm,theassumeddistributionofy is
|                                                |     |     | ∼ N(β +β x,σ2), |          |
| ---------------------------------------------- | --- | --- | --------------- | -------- |
|                                                |     |     | y 0 1           |          |
| meaningthatwemustestimatethreeparametersnamely |     |     |                 | , ,andσ2 |
β 0 β 1
- Ifwesolvefortheparametersthatmaximizethelikelihood,we’llfindthatthe
maximumlikelihoodestimatorof and isexactlythesameastheOLSestimator:
β 0 β 1
|     |     | βˆMLE = | βˆOLS and βˆMLE | = βˆOLS |
| --- | --- | ------- | --------------- | ------- |
|     |     | 0       | 0 1             | 1       |
inotherwords,OLScanbethoughtofasthemaximumlikelihoodestimatorwhenthe
errortermisnormallydistributed!
36/42

- Tome,that’sverycool. PeoplehavebeenusingOLSestimationsinceCarlGaussin
1795,anditturnsouttocoincidewithsomethinglikethemaximumlikelihood
estimator,whichdidn’tbecomepopularuntilRonaldFishercarefullyanalyzeditinthe
early1900s,andtodaysomeoftheOLSideasarebeingusedtocreatetechnological
wonderslikeChatGPT
Notice something amazing?
- TheOLSestimatorisnotjusttheestimatorthatminimizesthesumofsquared
residuals,asitisalso:
1. Themaximumlikelihoodestimatorwhenresidualsarenormallydistributed
2. ThemethodofmomentsestimatorwhenthemomentconditionsareE[u] =0andE[ux]
- ItmeansthatyoucanmotivatetheuseofOLSundervariousdifferentassumptions,
whichhascontributedtoitspopularity
37/42

Notice something amazing?
- TheOLSestimatorisnotjusttheestimatorthatminimizesthesumofsquared
residuals,asitisalso:
1. Themaximumlikelihoodestimatorwhenresidualsarenormallydistributed
2. ThemethodofmomentsestimatorwhenthemomentconditionsareE[u] =0andE[ux]
- ItmeansthatyoucanmotivatetheuseofOLSundervariousdifferentassumptions,
whichhascontributedtoitspopularity
- Tome,that’sverycool. PeoplehavebeenusingOLSestimationsinceCarlGaussin
1795,anditturnsouttocoincidewithsomethinglikethemaximumlikelihood
estimator,whichdidn’tbecomepopularuntilRonaldFishercarefullyanalyzeditinthe
early1900s,andtodaysomeoftheOLSideasarebeingusedtocreatetechnological
wonderslikeChatGPT
37/42

Finding the MLE with numerical optimization
- EstimatinganSLRmodelwithnormallydistributederrorisoneoftherarecases
wherewecananalyticallyderivetheMLEestimator
- Ifweinstead,say,assumedthattheerrorwasgammadistributed,thatwouldno
longerbethecase
- However,ifyoucannumericallyoptimize,youcanfindthemaximumlikelihood
estimate
- Justspecifythedistributionofu anduseafunctionlikeoptim()inRtofindthe
parametersthatmaximizesthelikelihood
38/42

GMM vs. MLE
ContrastingGMMandMLEphilosophies
- MLEspecifiesfulllikelihood—andthereforeallmoments—ofthedata
→generallymuchmorestructuredthanGMM
- Benefitofstructure:Efficiency
- Evenifyouareestimatingsomethingsimplelikemeansorvariances,MLEusesotherfeaturesof
thedatadistributiontoinformthoseestimates
- Costofstructure:Misspecification
- Incorrectstructureintroducesbias
Thechoiceofapproachfacesadelicatetradeoff
“Allmodelsarewrong,butsomeauseful”-GeorgeBox
39/42

| Example: | estimating | GARCH(1,1) | with MLE |
| -------- | ---------- | ---------- | -------- |
(iftime)
40/42

1. Specifydistributionofϵ
- E.g.,normal,sor
t
∼N(µ,σ
t
2)
2. Determineparameterstoestimate: µ,ω,α ,β
1 1
3. Estimateparametersbynumericallymaximizingthelog-likelihood
How to estimate GARCH(1,1)
- Supposeyouhavethemodel
r = µ+u ,
t t
u = σϵ
t t t
whereµisconstantandσ istime-varying.
t
- WespecifyaGARCH(1,1)modelforthevolatility:
σ2 = ω+α u2 +β σ2
t 1 t−1 1 t−1
- HowcanweestimatetheparameterswithMLE?
41/42

| How | to estimate | GARCH(1,1) |
| --- | ----------- | ---------- |
- Supposeyouhavethemodel
r = µ+u ,
t t
=
u t σϵ t t
whereµisconstantandσ istime-varying.
t
- WespecifyaGARCH(1,1)modelforthevolatility:
σ2 u2 σ2
= ω+α 1 +β 1
t t−1 t−1
- HowcanweestimatetheparameterswithMLE?
|     | 1. Specifydistributionofϵ |           |
| --- | ------------------------- | --------- |
|     | - E.g.,normal,sor         | ∼N(µ,σ 2) |
t t
|     | 2. Determineparameterstoestimate: | µ,ω,α 1 ,β 1 |
| --- | --------------------------------- | ------------ |
3. Estimateparametersbynumericallymaximizingthelog-likelihood
41/42

Thank you!
42/42
