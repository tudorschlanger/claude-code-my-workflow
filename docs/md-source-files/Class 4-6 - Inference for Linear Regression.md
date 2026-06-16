MGMT924StatisticalFoundations
Class 4-6: Inference for Linear Regression
Topics: Samplingdistributions,thenormalityassumption,thecentrallimittheorem,
hypothesistesting,t-statistics,p-values,confidenceintervals,predictionintervals,
Bayesianinference
TheisIngerslevJensen
YaleSOM
1/112

Nextcoupleofclasses: Accuracy
- Howaccurateare βˆ and βˆ ?
0 1
- Howaccurateisyˆ ?
i
- HowaccurateistheOLSestimator?
⇒Q:Whydowecareaboutaccuracyinassetmanagement?
| Modelling        | goals:        | Expected | value and | accuracy |     |
| ---------------- | ------------- | -------- | --------- | -------- | --- |
| Previousclasses: | Expectedvalue |          |           |          |     |
- UseOLSestimationtobuildapredictionrule,suchas
|                  |     |              | yˆ = | βˆ +βˆ x, |     |
| ---------------- | --- | ------------ | ---- | --------- | --- |
|                  |     |              | i    | 0 1 i     |     |
| whichdifferfromy |     | byaresidualy | = yˆ | +uˆ       |     |
|                  |     | i            | i i  | i         |     |
- Apredictionruleisaboutexpectedvaluesor“bestguesses”
| -   | βˆ andβˆ isourbestguessaboutthetrueparametersβ |     |     |                   | andβ |
| --- | ---------------------------------------------- | --- | --- | ----------------- | ---- |
|     | 0 1                                            |     |     |                   | 0 1  |
| -   | isourbestguessaboutfuturevaluesofy             |     |     | giventheobservedx |      |
| yˆ  | i                                              |     |     |                   | i    |
2/112

⇒Q:Whydowecareaboutaccuracyinassetmanagement?
| Modelling        | goals:        | Expected | value and | accuracy |     |
| ---------------- | ------------- | -------- | --------- | -------- | --- |
| Previousclasses: | Expectedvalue |          |           |          |     |
- UseOLSestimationtobuildapredictionrule,suchas
|                  |     |              | yˆ = | βˆ +βˆ x, |     |
| ---------------- | --- | ------------ | ---- | --------- | --- |
|                  |     |              | i    | 0 1 i     |     |
| whichdifferfromy |     | byaresidualy | = yˆ | +uˆ       |     |
|                  |     | i            | i i  | i         |     |
- Apredictionruleisaboutexpectedvaluesor“bestguesses”
| -                    | βˆ andβˆ isourbestguessaboutthetrueparametersβ |           |     |                   | andβ |
| -------------------- | ---------------------------------------------- | --------- | --- | ----------------- | ---- |
|                      | 0 1                                            |           |     |                   | 0 1  |
| -                    | isourbestguessaboutfuturevaluesofy             |           |     | giventheobservedx |      |
| yˆ                   | i                                              |           |     |                   | i    |
| Nextcoupleofclasses: |                                                | Accuracy  |     |                   |      |
| - Howaccurateare     |                                                | βˆ and βˆ | ?   |                   |      |
0 1
| - Howaccurateisyˆ |     | ?   |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
i
- HowaccurateistheOLSestimator?
2/112

| Modelling        | goals:        | Expected | value and | accuracy |     |
| ---------------- | ------------- | -------- | --------- | -------- | --- |
| Previousclasses: | Expectedvalue |          |           |          |     |
- UseOLSestimationtobuildapredictionrule,suchas
|                  |     |              | yˆ = | βˆ +βˆ x, |     |
| ---------------- | --- | ------------ | ---- | --------- | --- |
|                  |     |              | i    | 0 1 i     |     |
| whichdifferfromy |     | byaresidualy | = yˆ | +uˆ       |     |
|                  |     | i            | i i  | i         |     |
- Apredictionruleisaboutexpectedvaluesor“bestguesses”
| -                    | βˆ andβˆ isourbestguessaboutthetrueparametersβ |           |     |                   | andβ |
| -------------------- | ---------------------------------------------- | --------- | --- | ----------------- | ---- |
|                      | 0 1                                            |           |     |                   | 0 1  |
| -                    | isourbestguessaboutfuturevaluesofy             |           |     | giventheobservedx |      |
| yˆ                   | i                                              |           |     |                   | i    |
| Nextcoupleofclasses: |                                                | Accuracy  |     |                   |      |
| - Howaccurateare     |                                                | βˆ and βˆ | ?   |                   |      |
0 1
| - Howaccurateisyˆ |     | ?   |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
i
- HowaccurateistheOLSestimator?
⇒Q:Whydowecareaboutaccuracyinassetmanagement?
2/112

- Itturnsoutthatchoosingthebestestimatorisalotlikechoosingthebest
dart-throwingstrategy....
Picking an accurate estimator
- WeuseestimatorssuchasOLStobuildpredictionrulessuchasf(x) = βˆ +βˆ x
0 1
- Butthereareinfinitelymanypotentialestimators,sohowdowechoosethebest
estimator?
3/112

Picking an accurate estimator
- WeuseestimatorssuchasOLStobuildpredictionrulessuchasf(x) = βˆ +βˆ x
0 1
- Butthereareinfinitelymanypotentialestimators,sohowdowechoosethebest
estimator?
- Itturnsoutthatchoosingthebestestimatorisalotlikechoosingthebest
dart-throwingstrategy....
3/112

Choosing the best estimator in darts
- Supposeyourrichuncleoffersyouonedart
throwatatargetwiththreecirclesand
promisesyou$1,000,$2,000,or$3,000,ifyou
hittheouter,middle,orinnercircle,respectively
- You’reconsideringfourdifferentstategiesfor
howtothrowthedartandyouruncleallows
you5practicethrowswitheach
4/112

Choosing the best estimator in darts
- Supposeyourrichuncleoffersyouonedart
throwatatargetwiththreecirclesand
promisesyou$1,000,$2,000,or$3,000,ifyou
hittheouter,middle,orinnercircle,respectively
- You’reconsideringfourdifferentstategiesfor
howtothrowthedartandyouruncleallows
you5practicethrowswitheach
- Yourpracticeshotsareshowntotheright
- Whichstrategydoyouchoose? Why?
4/112

You should choose strategy 1!
- Why?
- It’sunbiased:Theaverageshotisclosetothe
target
- It’saccurate:Allshotsareclosetotheaverage,
i.e.,theyhavealowvariance
5/112

You should choose strategy 1!
- Why?
- It’sunbiased:Theaverageshotisclosetothe
target
- It’saccurate:Allshotsareclosetotheaverage,
i.e.,theyhavealowvariance
- It’sthesamewhenchoosingestimators!
- Welikeestimatorsthathavealowbias
- Welikeestimatorsthathavealowvariance
5/112

You should choose strategy 1!
- Why?
- It’sunbiased:Theaverageshotisclosetothe
target
- It’saccurate:Allshotsareclosetotheaverage,
i.e.,theyhavealowvariance
- It’sthesamewhenchoosingestimators!
- Welikeestimatorsthathavealowbias
- Welikeestimatorsthathavealowvariance
- Butwhat’sthetargetforanestimator?
5/112

⇒Theestimator’stargetisthepopulationparameters,
β
and
β
!
0 1
The simple linear regression model
- Todefineatarget,weassumethatthedataisgeneratedfromsometruemodel
- Thismodeliscalledthepopulationmodel
- Thefirstpopulationmodelwecoveristhesimplelinearregression(SLR)model:
Thesimplelinearregressionmodel
y = β +β x +u (1)
0 1
where
- β isthepopulationintercept
0
- β isthepopulationslope
1
- uisarandomerrorthatismeanzeroandmeanindependentofx,E[u] =E[u|x] =0
6/112

The simple linear regression model
- Todefineatarget,weassumethatthedataisgeneratedfromsometruemodel
- Thismodeliscalledthepopulationmodel
- Thefirstpopulationmodelwecoveristhesimplelinearregression(SLR)model:
Thesimplelinearregressionmodel
y = β +β x +u (1)
0 1
where
- β isthepopulationintercept
0
- β isthepopulationslope
1
- uisarandomerrorthatismeanzeroandmeanindependentofx,E[u] =E[u|x] =0
⇒Theestimator’stargetisthepopulationparameters,
β
and
β
!
0 1
6/112

Butperhapsmostimportantlyit’samodel
- Weassumeitholdsforsomefixedbutunobservablevaluesof β and β
0 1
- Inotherwords,unlikethedartsexamplewecannotseeourtarget
- However,wecanseesomex’sandy’sgeneratedfromthemodel
| What’s important | to understand | about | the SLR model? |
| ---------------- | ------------- | ----- | -------------- |
TheSLRmodelimpliesthat
| - Therelationshipbetweenx |     | andy islinear |     |
| ------------------------- | --- | ------------- | --- |
- Theerrorterm,u,isarandomvariablethatcapturesunobservedfactors
| - Thetrueexpectedvalueofy |     | givenx isE[y|x] | = +β |
| ------------------------- | --- | --------------- | ---- |
β 0 1 x
7/112

| What’s important | to understand | about | the SLR model? |
| ---------------- | ------------- | ----- | -------------- |
TheSLRmodelimpliesthat
| - Therelationshipbetweenx |     | andy islinear |     |
| ------------------------- | --- | ------------- | --- |
- Theerrorterm,u,isarandomvariablethatcapturesunobservedfactors
| - Thetrueexpectedvalueofy |     | givenx isE[y|x] | = +β |
| ------------------------- | --- | --------------- | ---- |
β 0 1 x
Butperhapsmostimportantlyit’samodel
- Weassumeitholdsforsomefixedbutunobservablevaluesof β and β
0 1
- Inotherwords,unlikethedartsexamplewecannotseeourtarget
- However,wecanseesomex’sandy’sgeneratedfromthemodel
7/112

| Estimating | the SLR | model parameters | with OLS |     |     |
| ---------- | ------- | ---------------- | -------- | --- | --- |
- Sayweobservedn = 20pairsofx’sandy’s,{(x ,y ),(x ,y ),...,(x ,y )}
|     |     |     | 1 1 | 2 2 | 20 20 |
| --- | --- | --- | --- | --- | ----- |
- Wethinkoftheseobservationsasarandomsamplefromthepopulationmodel
| - Therandomnesscomesfromu |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- |
- Fromtheobservedsample,weuseOLStoestimate and with βˆ and βˆ
|     |     |     | β 0 | β 1 0 | 1   |
| --- | --- | --- | --- | ----- | --- |
- Dartsanalogy:
| - OLSisourstrategy |                              |     |     |     |     |
| ------------------ | ---------------------------- | --- | --- | --- | --- |
| -                  | andβ arethecenterofthetarget |     |     |     |     |
β
0 1
| - βˆ | andβˆ representsonethroweach,attheirrespectivetargets |     |     |     |     |
| ---- | ----------------------------------------------------- | --- | --- | --- | --- |
0 1
8/112

- Sampleestimatesvary,populationparametersarefixed
- Anysampleisrandom,sothespecificβˆ andβˆ wegetfromonesample,willdifferfrom
0 1
theoneswegetfromanother,evenifβ andβ areconstant
0 1
- Darts:Differentthrowshitdifferentplaces,butthetargetcenterisconstant
Let’strytosimulatethesepropertiesinR
| Sample estimates | differ from | population | parameters |
| ---------------- | ----------- | ---------- | ---------- |
It’scrucialtounderstandthat
- Sampleestimatesarenotthesameaspopulationparameters
| - Inotherwords,βˆ | isnotβ | andβˆ isnotβ | ,thereareonlyestimates |
| ----------------- | ------ | ------------ | ---------------------- |
|                   | 0 0    | 1 1          |                        |
- Darts:Nothrowhitsthetargetcenterexactly
9/112

Let’strytosimulatethesepropertiesinR
| Sample estimates | differ from | population | parameters |
| ---------------- | ----------- | ---------- | ---------- |
It’scrucialtounderstandthat
- Sampleestimatesarenotthesameaspopulationparameters
| - Inotherwords,βˆ | isnotβ | andβˆ isnotβ | ,thereareonlyestimates |
| ----------------- | ------ | ------------ | ---------------------- |
|                   | 0 0    | 1 1          |                        |
- Darts:Nothrowhitsthetargetcenterexactly
- Sampleestimatesvary,populationparametersarefixed
- Anysampleisrandom,sothespecificβˆ andβˆ wegetfromonesample,willdifferfrom
|     |     | 0   | 1   |
| --- | --- | --- | --- |
theoneswegetfromanother,evenifβ andβ areconstant
|     |     | 0   | 1   |
| --- | --- | --- | --- |
- Darts:Differentthrowshitdifferentplaces,butthetargetcenterisconstant
9/112

| Sample estimates | differ from | population | parameters |
| ---------------- | ----------- | ---------- | ---------- |
It’scrucialtounderstandthat
- Sampleestimatesarenotthesameaspopulationparameters
| - Inotherwords,βˆ | isnotβ | andβˆ isnotβ | ,thereareonlyestimates |
| ----------------- | ------ | ------------ | ---------------------- |
|                   | 0 0    | 1 1          |                        |
- Darts:Nothrowhitsthetargetcenterexactly
- Sampleestimatesvary,populationparametersarefixed
- Anysampleisrandom,sothespecificβˆ andβˆ wegetfromonesample,willdifferfrom
|     |     | 0   | 1   |
| --- | --- | --- | --- |
theoneswegetfromanother,evenifβ andβ areconstant
|     |     | 0   | 1   |
| --- | --- | --- | --- |
- Darts:Differentthrowshitdifferentplaces,butthetargetcenterisconstant
Let’strytosimulatethesepropertiesinR
9/112

| Sampling | from | a population |     | model | in  |     |
| -------- | ---- | ------------ | --- | ----- | --- | --- |
R
- It’sstraightforwardtosimulatefromaspecificmodelinR.Forexample,suppose
| -   | Thepopulationmodelisy |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- |
=1+3x+u
| -   | Weobservex | =   | {−2,−1,0,1,2} |     |     |     |
| --- | ---------- | --- | ------------- | --- | --- | --- |
- Tosimulatearandomsamplefromthispopulationmodel,weonlyneedtosimulate
| n = | 5randomerrors,u |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- |
- Rhavemanyfunctionstogeneratepseudo-randomnumbers,suchasrnorm():
| # Always | set | a seed | when | generating | pseudo-random | numbers |
| -------- | --- | ------ | ---- | ---------- | ------------- | ------- |
set.seed(1)
| # 3     | different | pseudo-random |         | numbers |       |     |
| ------- | --------- | ------------- | ------- | ------- | ----- | --- |
| rnorm(n | = 1,      | mean          | = 0, sd | = 5) #  | -3.13 |     |
| rnorm(n | = 1,      | mean          | = 0, sd | = 5) #  | 0.92  |     |
| rnorm(n | = 1,      | mean          | = 0, sd | = 5) #  | -4.28 |     |
10/112

- ComputingtheOLSestimatesfromthissample:
|     |     |     |     |     |     | b1_ols | <- cov(y,x)/var(x)        |                           |      |       |
| --- | --- | --- | --- | --- | --- | ------ | ------------------------- | ------------------------- | ---- | ----- |
|     |     |     |     |     |     | b0_ols | <- mean(y)-mean(x)*b1_ols |                           |      |       |
|     |     |     |     |     |     | gives  | 1.65and                   | 4.66,clearlydifferentfrom | 1and |       |
|     |     |     |     |     |     | βˆ     | =                         | βˆ =                      | β =  | β = 3 |
|     |     |     |     |     |     | 0      |                           | 1                         | 0    | 1     |
- Nowlet’srepeatthisproceduremultipletimesandseehowtheestimatesvary
| Sampling | from | a population | model | in  |     |     |     |     |     |     |
| -------- | ---- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
R
- Onesimulatedsamplefromthepopulationmodel:
| x <- | c(-2,   | -1, 0, | 1, 2)        | # Observed      | x            |     |     |     |     |     |
| ---- | ------- | ------ | ------------ | --------------- | ------------ | --- | --- | --- | --- | --- |
| u <- | rnorm(n | = 5,   | mean = 0, sd | = 5) # Simulate | random error |     |     |     |     |     |
| y <- | 1+3*x+u |        |              | # Observed      | y            |     |     |     |     |     |
11/112

| Sampling |     | from a | population |     | model | in  |     |     |     |     |
| -------- | --- | ------ | ---------- | --- | ----- | --- | --- | --- | --- | --- |
R
- Onesimulatedsamplefromthepopulationmodel:
| x   | <- c(-2,   | -1, | 0, 1,   | 2)  |       |      | # Observed |     | x      |       |
| --- | ---------- | --- | ------- | --- | ----- | ---- | ---------- | --- | ------ | ----- |
| u   | <- rnorm(n | =   | 5, mean | =   | 0, sd | = 5) | # Simulate |     | random | error |
| y   | <- 1+3*x+u |     |         |     |       |      | # Observed |     | y      |       |
- ComputingtheOLSestimatesfromthissample:
| b1_ols |     | <- cov(y,x)/var(x)        |     |                           |     |     |     |     |      |       |
| ------ | --- | ------------------------- | --- | ------------------------- | --- | --- | --- | --- | ---- | ----- |
| b0_ols |     | <- mean(y)-mean(x)*b1_ols |     |                           |     |     |     |     |      |       |
| gives  |     | 1.65and                   |     | 4.66,clearlydifferentfrom |     |     |     |     | 1and |       |
|        | βˆ  | =                         | βˆ  | =                         |     |     |     | β   | =    | β = 3 |
|        | 0   |                           | 1   |                           |     |     |     | 0   |      | 1     |
- Nowlet’srepeatthisproceduremultipletimesandseehowtheestimatesvary
11/112

| Four random | samples | from population  | model:               |          |     |
| ----------- | ------- | ---------------- | -------------------- | -------- | --- |
|             |         |                  |                      | y = 1+3x | +u  |
|             |         | Population model | OLS line from sample |          |     |
Simulation 1: b0=1.65, b1=4.66 Simulation 2: b0=1.68, b1=3.56
10
5
0
−5
−10
y Simulation 3: b0=1.19, b1=1.31 Simulation 4: b0=3.3, b1=4.06
10
5
0
−5
−10
| −2  | −1  | 0 1 | 2 −2 | −1 0 | 1 2 |
| --- | --- | --- | ---- | ---- | --- |
x
12/112

| Accuracy | increases | if we have | observations |     |     |
| -------- | --------- | ---------- | ------------ | --- | --- |
n = 100
|     |     | Population model | OLS line from sample |     |     |
| --- | --- | ---------------- | -------------------- | --- | --- |
Simulation 1: b0=0.88, b1=3.39 Simulation 2: b0=1.13, b1=2.77
10
0
−10
y Simulation 3: b0=1.56, b1=2.11 Simulation 4: b0=0.7, b1=2.79
10
0
−10
|     | −2 −1 | 0 1 | 2 −2 | −1 0 | 1 2 |
| --- | ----- | --- | ---- | ---- | --- |
x
13/112

| Repeating | the                | sample 1,000 | times gives | a distribution     |     |
| --------- | ------------------ | ------------ | ----------- | ------------------ | --- |
|           | n = 100            |              |             |                    |     |
|           | Distribution of b0 |              |             | Distribution of b1 |     |
150
100
tnuoc
50
0
|     | −1 0 1 | 2 3 4 | −1 0 | 1 2 | 3 4 |
| --- | ------ | ----- | ---- | --- | --- |
value
14/112

- So,likethefinaldartschallengeweonlygetonethrow,butunlikethedartsexample
wedon’thavepracticeshots
⇒Statisticalinferenceisaboutusingmathtomakeeducated“guesses”aboutwherethe
practiceshotswouldhit(!)
In reality, we only observe one sample
- Inthesimulationwejustran,weknewthepopulationparameters
- Inreality,wedon’tknowthepopulationparameters,soweonlyseeonespecific
sample(ouractualdataset)
15/112

⇒Statisticalinferenceisaboutusingmathtomakeeducated“guesses”aboutwherethe
practiceshotswouldhit(!)
In reality, we only observe one sample
- Inthesimulationwejustran,weknewthepopulationparameters
- Inreality,wedon’tknowthepopulationparameters,soweonlyseeonespecific
sample(ouractualdataset)
- So,likethefinaldartschallengeweonlygetonethrow,butunlikethedartsexample
wedon’thavepracticeshots
15/112

In reality, we only observe one sample
- Inthesimulationwejustran,weknewthepopulationparameters
- Inreality,wedon’tknowthepopulationparameters,soweonlyseeonespecific
sample(ouractualdataset)
- So,likethefinaldartschallengeweonlygetonethrow,butunlikethedartsexample
wedon’thavepracticeshots
⇒Statisticalinferenceisaboutusingmathtomakeeducated“guesses”aboutwherethe
practiceshotswouldhit(!)
15/112

The sampling distribution
16/112

The sampling distribution
- Thewaywethinkaboutthe“practiceshots”in
statisticalinferenceisintheformofasampling
distribution
- Thesamplingdistributionof,say,theOLS
estimatorstellsushowtheOLSestimatevary
fromsampletosample
- Importantpropertiesofasamplingdistribution:
- Itsbias,i.e.,thedifferencebetweentheaverage
estimateandthepopulationparameter
- Itsvariance
- Itsshape
17/112

Q:Whataresomeinterestingobservationsaboutthissamplingdistribution?
- Bias: Theaveragevalueisclosetopopulationparameters
- Variance: Mostestimatesarewithin1unitofthepopulation
- Shape: It’ssymmetricandcouldbenormallydistributed
| You’ve already | seen a sampling    | distribution |                    |     |
| -------------- | ------------------ | ------------ | ------------------ | --- |
|                | Distribution of b0 |              | Distribution of b1 |     |
150
100
tnuoc
50
0
|     | −1 0 | 1 2 3 | 4 −1 0 | 1 2 3 4 |
| --- | ---- | ----- | ------ | ------- |
value
18/112

- Bias: Theaveragevalueisclosetopopulationparameters
- Variance: Mostestimatesarewithin1unitofthepopulation
- Shape: It’ssymmetricandcouldbenormallydistributed
| You’ve already | seen a sampling    | distribution |                    |     |
| -------------- | ------------------ | ------------ | ------------------ | --- |
|                | Distribution of b0 |              | Distribution of b1 |     |
150
100
tnuoc
50
0
|     | −1 0 | 1 2 3 | 4 −1 0 | 1 2 3 4 |
| --- | ---- | ----- | ------ | ------- |
value
Q:Whataresomeinterestingobservationsaboutthissamplingdistribution?
18/112

| You’ve already | seen a sampling    | distribution |                    |     |
| -------------- | ------------------ | ------------ | ------------------ | --- |
|                | Distribution of b0 |              | Distribution of b1 |     |
150
100
tnuoc
50
0
|     | −1 0 | 1 2 3 | 4 −1 0 | 1 2 3 4 |
| --- | ---- | ----- | ------ | ------- |
value
Q:Whataresomeinterestingobservationsaboutthissamplingdistribution?
- Bias: Theaveragevalueisclosetopopulationparameters
| - Variance: Mostestimatesarewithin1unitofthepopulation |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- |
| - Shape: It’ssymmetricandcouldbenormallydistributed    |     |     |     |     |
18/112

| The sampling | distribution | of the | OLS estimators |
| ------------ | ------------ | ------ | -------------- |
19/112

- ButtoderivetheOLSsamplingdistribution,weneedtomakeanassumptionabout
thedistributionofu
ThenormalityassumptionThepopulationerror,u,isindependentoftheexplanatory
variables and is normally distributed with zero mean and variance σ2, denoted u ∼
N(0,σ2)
The normality assumption
- Sofar,we’vewrittenthepopulationmodelas
y = β +β x +u,
0 1
withoutputtingmuchstructureonu
20/112

ThenormalityassumptionThepopulationerror,u,isindependentoftheexplanatory
variables and is normally distributed with zero mean and variance σ2, denoted u ∼
N(0,σ2)
The normality assumption
- Sofar,we’vewrittenthepopulationmodelas
y = β +β x +u,
0 1
withoutputtingmuchstructureonu
- ButtoderivetheOLSsamplingdistribution,weneedtomakeanassumptionabout
thedistributionofu
20/112

The normality assumption
- Sofar,we’vewrittenthepopulationmodelas
y = β +β x +u,
0 1
withoutputtingmuchstructureonu
- ButtoderivetheOLSsamplingdistribution,weneedtomakeanassumptionabout
thedistributionofu
ThenormalityassumptionThepopulationerror,u,isindependentoftheexplanatory
variables and is normally distributed with zero mean and variance σ2, denoted u ∼
N(0,σ2)
20/112

A quick review of the normal distribution
Thenormaldistribution
- Issymmetric
- Has68.2%,95.4%,and99.7%ofitsvalueswithin1,2,and3standarddeviationsof
themean,respectively
- Values> 3standarddeviationsfromthemeanhappenbutareveryunlikely
21/112

| A quick | review | of the standard | normal distribution |     |
| ------- | ------ | --------------- | ------------------- | --- |
- Arandomvariablehasastandardnormaldistributionifitsdistributionisnormalwitha
meanofzeroandavarianceofone
- Itiscommon,andpracticallyuseful,tostandardizeavariablebysubtractingitsmean
anddividingbyitsstandarddeviation. Ifthevariablehasanormaldistribution,then
thestandardizedvariablehasastandardnormaldistribution
| If  | hasanormaldistributionwithmean |     | andvariance | σ2: |
| --- | ------------------------------ | --- | ----------- | --- |
|     | θ                              |     | µ           |     |
N(µ,σ2),
θ ∼
thenthestandardized ,calledz ,hasastandardnormaldistribution:
|     |     | θ   | θ   |     |
| --- | --- | --- | --- | --- |
θ−µ
z = ∼ N(0,1)
θ
σ
22/112

| I’ve already | used the | normality | assumption |     |
| ------------ | -------- | --------- | ---------- | --- |
- Thernorm()functionthatIusedpreviouslygenerates(pseudo)randomnumbersthat
arenormallydistributed
- Hence,whenIsimulatedfromthepopulationmodel,Iimplicitlyassumedthatthe
| errorwasnormallydistribution,u |     |     | N(0,52) |     |
| ------------------------------ | --- | --- | ------- | --- |
∼
√
- Withrnorm(),youshouldsupplythestandarddeviation, σ2 = σ ,ratherthanthe
variance, σ2,ofthedistributionyouwanttosamplefrom. Theappropriatenotationfor
| thecallrnorm(mean=0, |     | sd=5)is,therefore,u |     | N(0,52) |
| -------------------- | --- | ------------------- | --- | ------- |
∼
- Noticethatthernorm(mean=0, sd=1)defaultgivesyouastandardnormalvariable
23/112

- Animmediateimplicationisthat βˆ isunbiased,E[βˆ ] = β
1 1 1
- That’sgreatnews.Itmeansthatβˆ iscorrectonaverage
1
- Anotherimplicationisthatthestandardized βˆ hasastandardnormaldistribution
1
βˆ −β
1 1 ∼ N(0,1)
sd(βˆ )
1
Sampling distribution of ˆ
β
1
- Thesamplingdistributionof βˆ describeshowitvariesoverdifferentsamples(with
1
thesamex values)
- Itturnsoutthat,whenweassumethatu isnormallydistributed, βˆ isalsonormally
1
distributedwithmean
β
andvariancevar(βˆ ),denoted
1 1
(cid:16) (cid:17)
βˆ ∼ N β ,var(βˆ )
1 1 1
24/112

- Anotherimplicationisthatthestandardized βˆ hasastandardnormaldistribution
1
βˆ −β
1 1 ∼ N(0,1)
sd(βˆ )
1
Sampling distribution of ˆ
β
1
- Thesamplingdistributionof βˆ describeshowitvariesoverdifferentsamples(with
1
thesamex values)
- Itturnsoutthat,whenweassumethatu isnormallydistributed, βˆ isalsonormally
1
distributedwithmean
β
andvariancevar(βˆ ),denoted
1 1
(cid:16) (cid:17)
βˆ ∼ N β ,var(βˆ )
1 1 1
- Animmediateimplicationisthat βˆ isunbiased,E[βˆ ] = β
1 1 1
- That’sgreatnews.Itmeansthatβˆ iscorrectonaverage
1
24/112

Sampling distribution of ˆ
β
1
- Thesamplingdistributionof βˆ describeshowitvariesoverdifferentsamples(with
1
thesamex values)
- Itturnsoutthat,whenweassumethatu isnormallydistributed, βˆ isalsonormally
1
distributedwithmean
β
andvariancevar(βˆ ),denoted
1 1
(cid:16) (cid:17)
βˆ ∼ N β ,var(βˆ )
1 1 1
- Animmediateimplicationisthat βˆ isunbiased,E[βˆ ] = β
1 1 1
- That’sgreatnews.Itmeansthatβˆ iscorrectonaverage
1
- Anotherimplicationisthatthestandardized βˆ hasastandardnormaldistribution
1
βˆ −β
1 1 ∼ N(0,1)
sd(βˆ )
1
24/112

- Q:Whichthreefactorsdeterminethevariance?
1. Theerrorvariance(σ2)
2. Thevarianceofx (s2)
x
3. Thesamplesize(n)
| Sampling | distribution | of ˆ |     |     |
| -------- | ------------ | ---- | --- | --- |
β
1
| - Thevarianceof | βˆ is |     |     |     |
| --------------- | ----- | --- | --- | --- |
1
σ2 σ2
|     |     | var(βˆ ) =    | =       | ,   |
| --- | --- | ------------- | ------- | --- |
|     |     | 1 ∑n (x −x¯)2 | (n−1)s2 |     |
i
i=1 x
| where | s2 isthesamplevarianceofx |     |     |     |
| ----- | ------------------------- | --- | --- | --- |
x
25/112

1. Theerrorvariance(σ2)
2. Thevarianceofx (s2)
x
3. Thesamplesize(n)
| Sampling | distribution | of ˆ |     |     |
| -------- | ------------ | ---- | --- | --- |
β
1
| - Thevarianceof | βˆ is |     |     |     |
| --------------- | ----- | --- | --- | --- |
1
σ2 σ2
|     |     | var(βˆ ) =    | =       | ,   |
| --- | --- | ------------- | ------- | --- |
|     |     | 1 ∑n (x −x¯)2 | (n−1)s2 |     |
i
i=1 x
| where | s2 isthesamplevarianceofx |     |     |     |
| ----- | ------------------------- | --- | --- | --- |
x
- Q:Whichthreefactorsdeterminethevariance?
25/112

| Sampling | distribution | of ˆ |     |     |
| -------- | ------------ | ---- | --- | --- |
β
1
| - Thevarianceof | βˆ is |     |     |     |
| --------------- | ----- | --- | --- | --- |
1
σ2 σ2
|     |     | var(βˆ ) =    | =       | ,   |
| --- | --- | ------------- | ------- | --- |
|     |     | 1 ∑n (x −x¯)2 | (n−1)s2 |     |
i
i=1 x
| where | s2 isthesamplevarianceofx |     |     |     |
| ----- | ------------------------- | --- | --- | --- |
x
- Q:Whichthreefactorsdeterminethevariance?
| 1.  | Theerrorvariance(σ2) |      |     |     |
| --- | -------------------- | ---- | --- | --- |
| 2.  | Thevarianceofx       | (s2) |     |     |
x
| 3.  | Thesamplesize(n) |     |     |     |
| --- | ---------------- | --- | --- | --- |
25/112

1.-3. Sameasforvar(βˆ )
1
4. Theaveragevalueofx squared
| Sampling | distribution | of ˆ |     |     |     |
| -------- | ------------ | ---- | --- | --- | --- |
β
0
|                                        |     |     |      | (cid:16)      | (cid:17) |
| -------------------------------------- | --- | --- | ---- | ------------- | -------- |
| - Theinterceptisalsonormalandunbiased: |     |     | βˆ ∼ | N β ,var(βˆ ) |          |
|                                        |     |     | 0    | 0 0           |          |
- Itsvarianceis
|     |     |        | (cid:18) 1 | x¯2 (cid:19) |     |
| --- | --- | ------ | ---------- | ------------ | --- |
|     |     | var(βˆ | σ2         |              |     |
|     |     |        | ) = +      |              |     |
|     |     |        | 0 n        | (n−1)s2      |     |
x
- Theintuition:
var(cid:0) (cid:1)
|     |     | y¯ −βˆ x¯ | = var(y¯)+x¯2var(βˆ | )−2x¯cov(y¯,βˆ | )   |
| --- | --- | --------- | ------------------- | -------------- | --- |
|     |     | 1         |                     | 1              | 1   |
covarianceiszero,sincetheslope( βˆ )doesn’tchangeifthedataisshifted(y¯)
1
- Whichfourfactorsdeterminethisvariance?
26/112

| Sampling | distribution | of ˆ |     |     |     |
| -------- | ------------ | ---- | --- | --- | --- |
β
0
|                                        |     |     |      | (cid:16)      | (cid:17) |
| -------------------------------------- | --- | --- | ---- | ------------- | -------- |
| - Theinterceptisalsonormalandunbiased: |     |     | βˆ ∼ | N β ,var(βˆ ) |          |
|                                        |     |     | 0    | 0 0           |          |
- Itsvarianceis
|     |     |        | (cid:18) 1 | x¯2 (cid:19) |     |
| --- | --- | ------ | ---------- | ------------ | --- |
|     |     | var(βˆ | σ2         |              |     |
|     |     |        | ) = +      |              |     |
|     |     |        | 0 n        | (n−1)s2      |     |
x
- Theintuition:
var(cid:0) (cid:1)
|     |     | y¯ −βˆ x¯ | = var(y¯)+x¯2var(βˆ | )−2x¯cov(y¯,βˆ | )   |
| --- | --- | --------- | ------------------- | -------------- | --- |
|     |     | 1         |                     | 1              | 1   |
covarianceiszero,sincetheslope( βˆ )doesn’tchangeifthedataisshifted(y¯)
1
- Whichfourfactorsdeterminethisvariance?
| 1.-3. | Sameasforvar(βˆ | )   |     |     |     |
| ----- | --------------- | --- | --- | --- | --- |
1
| 4.  | Theaveragevalueofx | squared |     |     |     |
| --- | ------------------ | ------- | --- | --- | --- |
26/112

- Thisisanissuethatweoftenfaceinstatistics,soit’sworthtryingtoreallyunderstand
whywecannotuse σ2 inpractice
| Estimating | the error | variance |
| ---------- | --------- | -------- |
- Thevarianceformulaisnotfeasibletocomputeinpracticebecauseitdependsonthe
| populationerrorvariance, |     | σ2,whichisunobservable |
| ------------------------ | --- | ---------------------- |
- Instead,wehavetoestimatetheerrorvariance
27/112

| Estimating | the error | variance |
| ---------- | --------- | -------- |
- Thevarianceformulaisnotfeasibletocomputeinpracticebecauseitdependsonthe
| populationerrorvariance, |     | σ2,whichisunobservable |
| ------------------------ | --- | ---------------------- |
- Instead,wehavetoestimatetheerrorvariance
- Thisisanissuethatweoftenfaceinstatistics,soit’sworthtryingtoreallyunderstand
| whywecannotuse |     | σ2 inpractice |
| -------------- | --- | ------------- |
27/112

| Estimating                                  | the error | variance |     |     |
| ------------------------------------------- | --------- | -------- | --- | --- |
| - Fortunately,it’sstraightforwardtoestimate |           |          | σ2  |     |
- Toseehow,notethattheerrorvariancedeterminesthedispersioninu:
|     |     | σ2 = var(u) | = E[(u−E[u])2] | = E[u2] |
| --- | --- | ----------- | -------------- | ------- |
- Thetrueu isunobservablebutwecanusetheregressionresiduals,uˆ,asaproxy
- AseeminglyreasonablestrategyistoestimateE[u2]with
1 n
|     |     |     | σ˜ˆ2 = ∑ uˆ2 |     |
| --- | --- | --- | ------------ | --- |
|     |     |     | n i          |     |
i=1
28/112

Estimating the error variance
- Itturnsoutthat σ˜ˆ2 isbiased,soinsteadweusetheunbiasedestimator:
σˆ2 = 1 ∑ n uˆ2, (2)
n−k −1 i
i=1
wherek isthenumberofexplanatoryvariables,i.e.,k = 1fortheSLRmodel
√
- Wesometimesrefertotheerrorstandarddeviation, σˆ = σˆ2,whichisinthesame
unitsasy
- Wedividebyn−k −1ratherthann,becausethere’sonlyn−k −1effectivedegrees
offreedomintheOLSresiduals(I’llexplainthissoon)
29/112

| Estimating |     | the error | variance | in  |     |     |     |
| ---------- | --- | --------- | -------- | --- | --- | --- | --- |
R
EstimatingtheerrorvarianceorstandarddeviationisstraightforwardinR:
| > summary(house |     | reg) |     |     |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- | --- |
Call:
lm(formula = saleamount ∼ assessedvalue_true, data = house_data)
.
.
.
| Residual        | standard   |            | error: 66.3 | on 454   | degrees    | of freedom |        |
| --------------- | ---------- | ---------- | ----------- | -------- | ---------- | ---------- | ------ |
| Multiple        | R-squared: |            | 0.7093,     | Adjusted | R-squared: |            | 0.7086 |
| F-statistic:    |            | 1108       | on 1 and    | 454 DF,  | p-value:   | < 2.2e-16  |        |
| > summary(house |            | reg)$sigma |             |          |            |            |        |
[1] 66.30415
| > n <-                   | length(house | reg$residuals) |                   |     |     |     |     |
| ------------------------ | ------------ | -------------- | ----------------- | --- | --- | --- | --- |
| > sqrt(1/(n-2)*sum(house |              |                | reg$residuals^2)) |     |     |     |     |
[1] 66.30415
30/112

Again,weusuallytakethesquareofthesevariancestoworkwithstandarddeviations,and
thesestandarddeviationsaretypicallycalledthestandarderrors:
|              |              |            |     |     |           | (cid:113) |         | (cid:113)   |     |
| ------------ | ------------ | ---------- | --- | --- | --------- | --------- | ------- | ----------- | --- |
|              |              |            |     |     | se(βˆ ) = | vaˆr(βˆ ) | & se(βˆ | ) = vaˆr(βˆ | )   |
|              |              |            |     |     | 0         | 0         |         | 1           | 1   |
| The feasible | OLS variance | estimators |     |     |           |           |         |             |     |
Replacingthepopulationerrorvariance, σ2,withtheestimatederrorvariance, σˆ2,givesthe
feasibleOLSvarianceestimatorsweuseinpractice
Thevarianceoftheinterceptis
(cid:18) x¯2 (cid:19)
1
|     |     | vaˆr(βˆ | ) = σˆ2 + | (3) |     |     |     |     |     |
| --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
0
n (n−1)s2
x
Thevarianceoftheslopeis
σˆ2
|     |     | vaˆr(βˆ | ) = | (4) |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
1
(n−1)s2
x
31/112

| The feasible | OLS | variance |     | estimators |     |     |     |     |
| ------------ | --- | -------- | --- | ---------- | --- | --- | --- | --- |
Replacingthepopulationerrorvariance, σ2,withtheestimatederrorvariance, σˆ2,givesthe
feasibleOLSvarianceestimatorsweuseinpractice
Thevarianceoftheinterceptis
|     |     |     |     |     | (cid:18) | x¯2 (cid:19) |     |     |
| --- | --- | --- | --- | --- | -------- | ------------ | --- | --- |
1
|     |     |     | vaˆr(βˆ | ) = | σˆ2 + |     |     | (3) |
| --- | --- | --- | ------- | --- | ----- | --- | --- | --- |
0
|     |     |     |     |     | n (n−1)s2 |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- |
x
Thevarianceoftheslopeis
σˆ2
|     |     |     |     | vaˆr(βˆ | ) = |     |     | (4) |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
1
(n−1)s2
x
Again,weusuallytakethesquareofthesevariancestoworkwithstandarddeviations,and
thesestandarddeviationsaretypicallycalledthestandarderrors:
|     |       |     | (cid:113) |     |         | (cid:113)   |     |     |
| --- | ----- | --- | --------- | --- | ------- | ----------- | --- | --- |
|     | se(βˆ | ) = | vaˆr(βˆ   | )   | & se(βˆ | ) = vaˆr(βˆ | )   |     |
|     |       | 0   |           | 0   |         | 1           | 1   |     |
31/112

| Estimating | the standard | errors | of ˆ and | ˆ in |
| ---------- | ------------ | ------ | -------- | ---- |
|            |              |        | β        | β R  |
|            |              |        | 0        | 1    |
# Inputs
x <- house_data$assessedvalue_true
| varx <- | var(x) |     |     |     |
| ------- | ------ | --- | --- | --- |
n <- length(x)
| res <- house_reg$residuals              |                    |           |           |          |
| --------------------------------------- | ------------------ | --------- | --------- | -------- |
| # Error                                 | variance           |           |           |          |
| evar <-                                 | 1/(n-2)*sum(res^2) |           |           |          |
| # Standard                              | error              | of bhat_0 |           |          |
| sqrt(evar*(1/n+mean(x)^2/((n-1)*varx))) |                    |           | # Result: | 8.369056 |
| # Standard                              | error              | of bhat_1 |           |          |
| sqrt(evar/((n-1)*varx))                 |                    |           | # Result: | 0.041213 |
32/112

| The | standard |     | errors | are | also | available | from |     |
| --- | -------- | --- | ------ | --- | ---- | --------- | ---- | --- |
summary()
| >   | summary(house |     | reg) |     |     |     |     |     |
| --- | ------------- | --- | ---- | --- | --- | --- | --- | --- |
Call:
lm(formula = saleamount ∼ assessedvalue_true, data = house_data)
Residuals:
|          | Min |         | 1Q  | Median |     | 3Q     | Max     |     |
| -------- | --- | ------- | --- | ------ | --- | ------ | ------- | --- |
| -251.263 |     | -37.898 |     | 3.782  |     | 39.297 | 271.605 |     |
Coefficients:
|                    |     |     |     | Estimate |     | Std. Error | t value | Pr(>|t|)   |
| ------------------ | --- | --- | --- | -------- | --- | ---------- | ------- | ---------- |
| (Intercept)        |     |     |     | -4.69322 |     | 8.36906    | -0.561  | 0.575      |
| assessedvalue_true |     |     |     | 1.37165  |     | 0.04121    | 33.282  | <2e-16 *** |
.
.
.
33/112

Degrees of freedom
34/112

- Ifweestimatethevariance,wehaven−1degreesoffreedom:
var(x) = 1 ∑ n (x −x¯)2
n−1 i
i=1
becauseweusedup1degreeoffreedomtoestimatex¯
Degrees of freedom
- Thedegreesoffreedomisthenumberofindependentobservationsusedtoestimatea
statistic. Let’sseesomeexamples:
- Ifweestimatethemean,wehavendegreesoffreedom:
1 ∑ n
x¯ = x,
i
n
i=1
35/112

Degrees of freedom
- Thedegreesoffreedomisthenumberofindependentobservationsusedtoestimatea
statistic. Let’sseesomeexamples:
- Ifweestimatethemean,wehavendegreesoffreedom:
1 ∑ n
x¯ = x,
i
n
i=1
- Ifweestimatethevariance,wehaven−1degreesoffreedom:
var(x) = 1 ∑ n (x −x¯)2
n−1 i
i=1
becauseweusedup1degreeoffreedomtoestimatex¯
35/112

Degrees of Freedom
- IfweestimatetheerrorvariancefromtheSLRmodel,wehaven−2degreesof
freedom:
|                                              | n     | n       |            |
| -------------------------------------------- | ----- | ------- | ---------- |
| 1                                            | ∑ 1   | ∑       |            |
| σˆ2 =                                        | uˆ2 = | (y −(βˆ | +βˆ x ))2, |
|                                              | i     | i 0     | 1 i        |
| n−2                                          | n−2   |         |            |
|                                              | i=1   | i=1     |            |
| becausewe’reusedup2degreeoffreedomtoestimate |       | βˆ      | and βˆ     |
0 1
- Thedegreeoffreedomtellsushowmanyobservationsareusefultoestimatethe
statistic:
- Ifn =1,wecanestimateausefulmean,buttheestimatedvariancewouldalwaysbe0
(andthereforeuseless),andwecouldn’tevenestimatetheSLRerrorvariance
- Ifn =2,wecanestimateausefulmeanandvariance,buttheestimatedSLRerror
variancewouldalwaysbe0
- Ifn ≥3,wecanestimateausefulmean,variance,andSLRerrorvariance
36/112

| Some | practical | considerations |
| ---- | --------- | -------------- |
37/112

The normality assumption is not crucial
- Thenormalityassumptionisstronganddoesn’tholdformanyfinancialdatasets.
- Forexample,fortheUSstockmarket,dailyreturnsmorethan3 sfromthemeanare
σ
6.5timesmorelikelythananormaldistributionwouldpredict
60
40
Monday 19th, 1987:
20 Return of −17%, a −16sd move!
0
−0.1 0.0 0.1
Daily US stock market return
ytisned
- Nevertheless,for“large”samplesizes,thesamplingdistributionof and is
β β
0 1
approximatelynormal,evenifu isnot,duetotheCentralLimitTheorem(CLT)
38/112

The normality assumption is not crucial
- Thenormalityassumptionisstronganddoesn’tholdformanyfinancialdatasets.
- Forexample,fortheUSstockmarket,dailyreturnsmorethan3 sfromthemeanare
σ
6.5timesmorelikelythananormaldistributionwouldpredict
60
40
Monday 19th, 1987:
20 Return of −17%, a −16sd move!
0
−0.1 0.0 0.1
Daily US stock market return
ytisned
- Nevertheless,for“large”samplesizes,thesamplingdistributionof and is
β β
0 1
approximatelynormal,evenifu isnot,duetotheCentralLimitTheorem(CLT)
38/112

Waitwhat? Surelythere’resomeweirddistributionswhereCLTdoesn’thold?
The Central Limit Theorem
The Central Limit Theorem (CLT) The average from a random sample for any population
(withfinitevariance),whenstandardized,hasanasymptoticstandardnormaldistribution
- Forexample,let{y ,y ,...,y }bearandomsamplewithmean µ andvariance σ2,
1 2 n
then
Y¯ −µ
z = √
σ/ n
hasanasymptoticstandardnormaldistribution
- Inotherwords,thesamplingdistributionofz getscloserandclosertoN(0,1)asn
increasesregardlessofthedistributionofY!
39/112

The Central Limit Theorem
The Central Limit Theorem (CLT) The average from a random sample for any population
(withfinitevariance),whenstandardized,hasanasymptoticstandardnormaldistribution
- Forexample,let{y ,y ,...,y }bearandomsamplewithmean µ andvariance σ2,
1 2 n
then
Y¯ −µ
z = √
σ/ n
hasanasymptoticstandardnormaldistribution
- Inotherwords,thesamplingdistributionofz getscloserandclosertoN(0,1)asn
increasesregardlessofthedistributionofY!
Waitwhat? Surelythere’resomeweirddistributionswhereCLTdoesn’thold?
39/112

|     |     |     |     | Normal distribution | Y distribution |     |
| --- | --- | --- | --- | ------------------- | -------------- | --- |
1.5
ytisneD
1.0
0.5
0.0
|     |     |     |     | −2  | 0   | 2   |
| --- | --- | --- | --- | --- | --- | --- |
Y
- Andifwecompareitsdensitytothatofthestandardnormaldistribution(right)wesee
thatit’sveryfaranormaldistribution
| Demonstrating | CLT | with a weird | distribution |     |     |     |
| ------------- | --- | ------------ | ------------ | --- | --- | --- |
Aweirddistribution
- iseither1or-1withequalprobability
Y
- Ifwesampled10,000randomY’s,thehistogramwouldlooksomethinglike:
5000
4000
| tnuoC 3000 |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
2000
1000
0
|     | −1.0 −0.5 | 0.0 0.5 | 1.0 |     |     |     |
| --- | --------- | ------- | --- | --- | --- | --- |
Y
40/112

| Demonstrating |     | CLT with | a weird | distribution |     |     |     |
| ------------- | --- | -------- | ------- | ------------ | --- | --- | --- |
Aweirddistribution
- iseither1or-1withequalprobability
Y
- Ifwesampled10,000randomY’s,thehistogramwouldlooksomethinglike(left):
|     | 5000       |     |     |         | Normal distribution | Y distribution |     |
| --- | ---------- | --- | --- | ------- | ------------------- | -------------- | --- |
|     | 4000       |     |     | 1.5     |                     |                |     |
|     | tnuoC 3000 |     |     | ytisneD |                     |                |     |
1.0
2000
0.5
1000
|     | 0    |      |         | 0.0 |     |     |     |
| --- | ---- | ---- | ------- | --- | --- | --- | --- |
|     | −1.0 | −0.5 | 0.0 0.5 | 1.0 | −2  | 0   | 2   |
|     |      |      | Y       |     |     | Y   |     |
- Andifwecompareitsdensitytothatofthestandardnormaldistribution(right)wesee
thatit’sveryfaranormaldistribution
40/112

|     |     |     |     |     |     | Normal distribution |      | Sampling distribution |      |     |
| --- | --- | --- | --- | --- | --- | ------------------- | ---- | --------------------- | ---- | --- |
|     |     |     |     |     | n=1 |                     | n=10 |                       | n=30 |     |
0.5
|     |     |     |     | 1.5 |     | 0.75 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
0.4
|     |     |     |     | 1.0 |     | 0.50 |     | 0.3 |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
0.2
|     |     |     |     | 0.5 |     | 0.25 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
0.1
|     |     |     |     | ytisneD 0.0 |      | 0.00 |       | 0.0 |         |     |
| --- | --- | --- | --- | ----------- | ---- | ---- | ----- | --- | ------- | --- |
|     |     |     |     |             | n=50 |      | n=100 |     | n=10000 |     |
|     |     |     |     |             |      | 0.4  |       | 0.4 |         |     |
|     |     |     |     | 0.4         |      | 0.3  |       | 0.3 |         |     |
0.3
|     |     |     |     | 0.2 |      | 0.2 |      | 0.2 |      |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- |
|     |     |     |     | 0.1 |      | 0.1 |      | 0.1 |      |     |
|     |     |     |     | 0.0 |      | 0.0 |      | 0.0 |      |     |
|     |     |     |     |     | −2 0 | 2   | −2 0 | 2   | −2 0 | 2   |
Standardized sample mean
| Demonstrating | the CLT | with a weird | distribution |     |     |     |     |     |     |     |
| ------------- | ------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
CLTpredictsthattheaverageofnrandomY’sapproachesanormaldistributionaswe
| increasen,despiteY | beingweird. | Let’sseeifthat’strue |     |     |     |     |     |     |     |     |
| ------------------ | ----------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
41/112

| Demonstrating |     | the CLT | with | a   | weird | distribution |     |     |     |
| ------------- | --- | ------- | ---- | --- | ----- | ------------ | --- | --- | --- |
CLTpredictsthattheaverageofnrandomY’sapproachesanormaldistributionaswe
| increasen,despiteY |     | beingweird. |     | Let’sseeifthat’strue |     |                       |     |      |     |
| ------------------ | --- | ----------- | --- | -------------------- | --- | --------------------- | --- | ---- | --- |
|                    |     |             |     | Normal distribution  |     | Sampling distribution |     |      |     |
|                    |     | n=1         |     |                      |     | n=10                  |     | n=30 |     |
0.5
|     | 1.5 |     |     | 0.75 |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.4
|     | 1.0 |     |     | 0.50 |     |     | 0.3 |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.2
|     | 0.5 |     |     | 0.25 |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.1
|     | ytisneD 0.0 |      |     | 0.00 |     |       | 0.0 |         |     |
| --- | ----------- | ---- | --- | ---- | --- | ----- | --- | ------- | --- |
|     |             | n=50 |     |      |     | n=100 |     | n=10000 |     |
|     |             |      |     | 0.4  |     |       | 0.4 |         |     |
|     | 0.4         |      |     | 0.3  |     |       | 0.3 |         |     |
0.3
|     | 0.2 |      |     | 0.2 |     |     | 0.2 |      |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- |
|     | 0.1 |      |     | 0.1 |     |     | 0.1 |      |     |
|     | 0.0 |      |     | 0.0 |     |     | 0.0 |      |     |
|     |     | −2 0 | 2   |     | −2  | 0 2 |     | −2 0 | 2   |
Standardized sample mean
41/112

- Thisistrulyamazingandsomethingthatalotofpeopledon’tappreciate
- You’llsometimeshearpeoplesayingthat“linearregressionisnotappropriatefor
predictingreturnsbecausereturnsaren’tnormallydistributed.”
- Butthatsimplynottrue
- ForSLRpredictions,youdon’tneednormalityassumption
- ForSLRinference,we’re“saved”byCLT
Bottom line: CLT makes our lives much easier!
- BecauseofCLT,nonnormalityofu isnotaseriousproblemwithlargesamplesizes
- Inotherwords,forlargesamplesizesthesamplingdistributionoftheOLSestimators
isapproximatelynormal,evenifu isnot
- Inmanysituations,approximatenormalitystartskickinginataroundn = 30,which
willbesatisfiedinthevastmajorityofexamplesweconsider
42/112

| Bottom | line: CLT | makes our | lives much | easier! |
| ------ | --------- | --------- | ---------- | ------- |
- BecauseofCLT,nonnormalityofu isnotaseriousproblemwithlargesamplesizes
- Inotherwords,forlargesamplesizesthesamplingdistributionoftheOLSestimators
| isapproximatelynormal,evenifu |     |     | isnot |     |
| ----------------------------- | --- | --- | ----- | --- |
- Inmanysituations,approximatenormalitystartskickinginataroundn 30,which
=
willbesatisfiedinthevastmajorityofexamplesweconsider
- Thisistrulyamazingandsomethingthatalotofpeopledon’tappreciate
- You’llsometimeshearpeoplesayingthat“linearregressionisnotappropriatefor
predictingreturnsbecausereturnsaren’tnormallydistributed.”
|     | - Butthatsimplynottrue |     |     |     |
| --- | ---------------------- | --- | --- | --- |
- ForSLRpredictions,youdon’tneednormalityassumption
- ForSLRinference,we’re“saved”byCLT
42/112

| The sampling | distribution | is actually | , not normal |     |
| ------------ | ------------ | ----------- | ------------ | --- |
t
- Asmalltwist: Itturnsoutthatifavariableisnormallydistributed, N(µ,σ2),but
θ ∼
weestimateitsvariance
σ2 ≈ σˆ2
| basedonn−k | −1degreesoffreedom,thenitbecomest |     |     | distributed |
| ---------- | --------------------------------- | --- | --- | ----------- |
- Similarly,ifwestandardizethevariableusinganestimatedstandarddeviation,
θ−µ
|     |     | t = | ,   |     |
| --- | --- | --- | --- | --- |
θ
σˆ
thenthisstandardizedvariablehasastandardt distribution,denoted
|     |     | t ∼ t(n−k | −1) |     |
| --- | --- | --------- | --- | --- |
θ
43/112

| The sampling | distribution | is actually | , not normal |
| ------------ | ------------ | ----------- | ------------ |
t
Inpractice,therefore,we’llusethesamplingdistributions:
βˆ −β
j j (5)
|     |     | ∼   | t(n−k −1) |
| --- | --- | --- | --------- |
se(βˆ )
j
| wheren−k | −1isthedegreesoffreedom |     |     |
| -------- | ----------------------- | --- | --- |
⇒Don’tworrytoomuchaboutthedetails. Thepracticalimplicationisthatthesampling
| distributionist | ratherthannormal |     |     |
| --------------- | ---------------- | --- | --- |
44/112

⇒Differencebetweent andnormalistypicallysmall(e.g.,inhousingexamplev = 454)
| The sampling | distribution | is actually | , not normal |     |
| ------------ | ------------ | ----------- | ------------ | --- |
t
- Thestandardt distributionisjustafat-tailedversionofthestandardnormal
distribution. Asn−k −1increasesthetailsbecome“skinnier”andthet distribution
convergestothenormal
- InR,canusedt(n−k −1)togetthedensityofastandardt distributionwith
| n−k −1dfs: |     |                 |            |     |
| ---------- | --- | --------------- | ---------- | --- |
|            |     | Standard Normal | Standard t |     |
v: 1 v: 3
|     | 0.4         |     | 0.4 |     |
| --- | ----------- | --- | --- | --- |
|     | 0.3         |     | 0.3 |     |
|     | 0.2         |     | 0.2 |     |
|     | 0.1         |     | 0.1 |     |
|     | ytisneD 0.0 |     | 0.0 |     |
v: 50 v: 500
|     | 0.4  |              | 0.4                   |     |
| --- | ---- | ------------ | --------------------- | --- |
|     | 0.3  |              | 0.3                   |     |
|     | 0.2  |              | 0.2                   |     |
|     | 0.1  |              | 0.1                   |     |
|     | 0.0  |              | 0.0                   |     |
|     | −5.0 | −2.5 0.0 2.5 | 5.0 −5.0 −2.5 0.0 2.5 | 5.0 |
x
45/112

| The sampling | distribution | is actually | , not normal |     |
| ------------ | ------------ | ----------- | ------------ | --- |
t
- Thestandardt distributionisjustafat-tailedversionofthestandardnormal
distribution. Asn−k −1increasesthetailsbecome“skinnier”andthet distribution
convergestothenormal
- InR,canusedt(n−k −1)togetthedensityofastandardt distributionwith
| n−k −1dfs: |     |                 |            |     |
| ---------- | --- | --------------- | ---------- | --- |
|            |     | Standard Normal | Standard t |     |
v: 1 v: 3
|     | 0.4         |     | 0.4 |     |
| --- | ----------- | --- | --- | --- |
|     | 0.3         |     | 0.3 |     |
|     | 0.2         |     | 0.2 |     |
|     | 0.1         |     | 0.1 |     |
|     | ytisneD 0.0 |     | 0.0 |     |
v: 50 v: 500
|     | 0.4  |              | 0.4                   |     |
| --- | ---- | ------------ | --------------------- | --- |
|     | 0.3  |              | 0.3                   |     |
|     | 0.2  |              | 0.2                   |     |
|     | 0.1  |              | 0.1                   |     |
|     | 0.0  |              | 0.0                   |     |
|     | −5.0 | −2.5 0.0 2.5 | 5.0 −5.0 −2.5 0.0 2.5 | 5.0 |
x
⇒Differencebetweent andnormalistypicallysmall(e.g.,inhousingexamplev = 454)
45/112

| Statistical | inference | in action: | Four tools |
| ----------- | --------- | ---------- | ---------- |
46/112

⇒Nowwe’rereadytodosomeseriousstatisticalinference!
- Whatwedon’tknowisthevalueofthepopulationparameters β and β
0 1
- I’llshowfourstatisticaltoolstoinfertheirlikelyvalues
...butfirst,amotivatingexample
| Statistical | inference | in action |
| ----------- | --------- | --------- |
- WhatweknowaboutthesamplingdistributionoftheOLSestimators:
| -   | Centeredaroundthepopulationparameters  |                            |
| --- | -------------------------------------- | -------------------------- |
| -   | Formulasforestimatingsamplingvariances |                            |
| -   | Approximatet                           | distributioninlargesamples |
47/112

- Whatwedon’tknowisthevalueofthepopulationparameters β and β
0 1
- I’llshowfourstatisticaltoolstoinfertheirlikelyvalues
...butfirst,amotivatingexample
| Statistical | inference | in action |
| ----------- | --------- | --------- |
- WhatweknowaboutthesamplingdistributionoftheOLSestimators:
| -   | Centeredaroundthepopulationparameters  |                            |
| --- | -------------------------------------- | -------------------------- |
| -   | Formulasforestimatingsamplingvariances |                            |
| -   | Approximatet                           | distributioninlargesamples |
⇒Nowwe’rereadytodosomeseriousstatisticalinference!
47/112

...butfirst,amotivatingexample
| Statistical | inference | in action |
| ----------- | --------- | --------- |
- WhatweknowaboutthesamplingdistributionoftheOLSestimators:
| -   | Centeredaroundthepopulationparameters  |                            |
| --- | -------------------------------------- | -------------------------- |
| -   | Formulasforestimatingsamplingvariances |                            |
| -   | Approximatet                           | distributioninlargesamples |
⇒Nowwe’rereadytodosomeseriousstatisticalinference!
- Whatwedon’tknowisthevalueofthepopulationparameters β and β
0 1
- I’llshowfourstatisticaltoolstoinfertheirlikelyvalues
47/112

| Statistical | inference | in action |
| ----------- | --------- | --------- |
- WhatweknowaboutthesamplingdistributionoftheOLSestimators:
| -   | Centeredaroundthepopulationparameters  |                            |
| --- | -------------------------------------- | -------------------------- |
| -   | Formulasforestimatingsamplingvariances |                            |
| -   | Approximatet                           | distributioninlargesamples |
⇒Nowwe’rereadytodosomeseriousstatisticalinference!
- Whatwedon’tknowisthevalueofthepopulationparameters β and β
0 1
- I’llshowfourstatisticaltoolstoinfertheirlikelyvalues
...butfirst,amotivatingexample
47/112

| Example: | Does | Warren | Buffett | have alpha? |
| -------- | ---- | ------ | ------- | ----------- |
48/112

- Nevertheless,somepeoplehavearguedthatBuffetthasmerelybeenlucky
- Wecanusestatisticalinferencetoevaluatethisargument1
Does Warren Buffett have alpha?
WarrenBuffettisoneofthemostsuccessfulinvestorsinhistory
- Sincehiscompany,BerkshireHathaway,waslistedin1976to2023,ithashada
monthlyexcessreturnof1.48%vs.0.69%forthestockmarket
- Toputthisinperspective,a$100,000investmentinthestockmarketwouldbeworth
$18.4mil,whileoneinBuffettwouldbeworth$802mil!
1ThisanalysisisinspiredbythepaperBuffett’sAlpha
49/112

- Wecanusestatisticalinferencetoevaluatethisargument1
Does Warren Buffett have alpha?
WarrenBuffettisoneofthemostsuccessfulinvestorsinhistory
- Sincehiscompany,BerkshireHathaway,waslistedin1976to2023,ithashada
monthlyexcessreturnof1.48%vs.0.69%forthestockmarket
- Toputthisinperspective,a$100,000investmentinthestockmarketwouldbeworth
$18.4mil,whileoneinBuffettwouldbeworth$802mil!
- Nevertheless,somepeoplehavearguedthatBuffetthasmerelybeenlucky
1ThisanalysisisinspiredbythepaperBuffett’sAlpha
49/112

Does Warren Buffett have alpha?
WarrenBuffettisoneofthemostsuccessfulinvestorsinhistory
- Sincehiscompany,BerkshireHathaway,waslistedin1976to2023,ithashada
monthlyexcessreturnof1.48%vs.0.69%forthestockmarket
- Toputthisinperspective,a$100,000investmentinthestockmarketwouldbeworth
$18.4mil,whileoneinBuffettwouldbeworth$802mil!
- Nevertheless,somepeoplehavearguedthatBuffetthasmerelybeenlucky
- Wecanusestatisticalinferencetoevaluatethisargument1
1ThisanalysisisinspiredbythepaperBuffett’sAlpha
49/112

- UsingOLStoestimatethismodelondatafrom1976to2023,weget
αˆb = 0.010 & βˆb = 0.709,
- Statisticallyspeaking,the“luckargument”saysthatBuffett’ssamplealpha, αˆ,is
positive,butthathistruealpha, ,iszero
α
⇒Tool1-3canhelpevaluatetheluckargument,tool4canhelppredictthedistributionof
Buffett’sfuturealpha
Does Warren Buffett have alpha?
- SupposeweassumethatthetruemodelforBuffett’sreturnis
rb = αb+βbrmkt +ub,
t t t
whererb andrmkt isthemonthlyexcessreturnofBuffettandthemarket,respectively,
t t
βb isBuffett’smarketbeta,and αb isBuffett’struealpha
50/112

- Statisticallyspeaking,the“luckargument”saysthatBuffett’ssamplealpha, αˆ,is
positive,butthathistruealpha, ,iszero
α
⇒Tool1-3canhelpevaluatetheluckargument,tool4canhelppredictthedistributionof
Buffett’sfuturealpha
Does Warren Buffett have alpha?
- SupposeweassumethatthetruemodelforBuffett’sreturnis
rb = αb+βbrmkt +ub,
t t t
whererb andrmkt isthemonthlyexcessreturnofBuffettandthemarket,respectively,
t t
βb isBuffett’smarketbeta,and αb isBuffett’struealpha
- UsingOLStoestimatethismodelondatafrom1976to2023,weget
αˆb = 0.010 & βˆb = 0.709,
50/112

⇒Tool1-3canhelpevaluatetheluckargument,tool4canhelppredictthedistributionof
Buffett’sfuturealpha
Does Warren Buffett have alpha?
- SupposeweassumethatthetruemodelforBuffett’sreturnis
rb = αb+βbrmkt +ub,
t t t
whererb andrmkt isthemonthlyexcessreturnofBuffettandthemarket,respectively,
t t
βb isBuffett’smarketbeta,and αb isBuffett’struealpha
- UsingOLStoestimatethismodelondatafrom1976to2023,weget
αˆb = 0.010 & βˆb = 0.709,
- Statisticallyspeaking,the“luckargument”saysthatBuffett’ssamplealpha, αˆ,is
positive,butthathistruealpha, ,iszero
α
50/112

Does Warren Buffett have alpha?
- SupposeweassumethatthetruemodelforBuffett’sreturnis
rb = αb+βbrmkt +ub,
t t t
whererb andrmkt isthemonthlyexcessreturnofBuffettandthemarket,respectively,
t t
βb isBuffett’smarketbeta,and αb isBuffett’struealpha
- UsingOLStoestimatethismodelondatafrom1976to2023,weget
αˆb = 0.010 & βˆb = 0.709,
- Statisticallyspeaking,the“luckargument”saysthatBuffett’ssamplealpha, αˆ,is
positive,butthathistruealpha, ,iszero
α
⇒Tool1-3canhelpevaluatetheluckargument,tool4canhelppredictthedistributionof
Buffett’sfuturealpha
50/112

| Tool 1: | Hypothesis | testing |
| ------- | ---------- | ------- |
51/112

| Tool 1: Hypothesis | testing |     |
| ------------------ | ------- | --- |
- IntheBuffettexample,weobservedahighsamplealpha,butwishtotestwhetherthe
| truealphacouldbezero. | Thisisexactlywhatahypothesistestdoes |     |
| --------------------- | ------------------------------------ | --- |
- Wehavesomenullhypothesisaboutthetruevalueof αb,inthiscase
0
H : αb = 0,
0 0
andwishtotestitagainstanalternativehypothesis,inthiscase
H : αb > 0
A 0
- Forthegeneralexplanation,I’lldropthefinancelingoandrefertotheinterceptas ,
β 0
| theslopeas | β ,andeitheras | β   |
| ---------- | -------------- | --- |
|            | 1              | j   |
52/112

| Hypothesis | testing: | The null | hypothesis |
| ---------- | -------- | -------- | ---------- |
- Thenullhypothesiscanbeanyvalueofinterest,
H : β = β0
0 j j
- Nevertheless,themostcommonnullhypothesis,asintheBuffettexample,iswhere
| thetrueparameteriszero(β0 |     |     | = 0) |
| ------------------------- | --- | --- | ---- |
j
53/112

- Asimpleheuristicistolookatthedifference βˆ −βˆ0
0 0
- Butthismeasuredoesn’taccountforthesamplingvariabilityinβˆ
0
- Abettermeasureistolookatthet-statistic
| A heuristic | hypothesis | test |
| ----------- | ---------- | ---- |
- ReturningtotheBuffettexample,itseemsobvioustouse βˆ forourhypothesistest:
0
| - RejectH      | whenβˆ | isfarfrom0 |
| -------------- | ------ | ---------- |
|                | 0      | 0          |
| - Don’trejectH | whenβˆ | iscloseto0 |
|                | 0      | 0          |
54/112

| A heuristic | hypothesis | test |
| ----------- | ---------- | ---- |
- ReturningtotheBuffettexample,itseemsobvioustouse βˆ forourhypothesistest:
0
| - RejectH      | whenβˆ | isfarfrom0 |
| -------------- | ------ | ---------- |
|                | 0      | 0          |
| - Don’trejectH | whenβˆ | iscloseto0 |
|                | 0      | 0          |
- Asimpleheuristicistolookatthedifference βˆ −βˆ0
0 0
| - Butthismeasuredoesn’taccountforthesamplingvariabilityinβˆ |     |     |
| ----------------------------------------------------------- | --- | --- |
0
- Abettermeasureistolookatthet-statistic
54/112

The statistic
t
The t-statistic measures how far the estimated coefficient is from the null hypothesis
scaledbythestandarderror:
βˆ −β0
t = j j , (6)
βˆ j se(βˆ )
j
whichisequalto
βˆ
t = j , (7)
βˆ j se(βˆ )
j
when β0 = 0.
j
- Thelarger|t |thestrongerthestatisticalsupportforthealternativehypothesis
βˆ
j
55/112

- Useful,butisthisenoughtorejectthenullhypothesis? Inotherwords,isadistanceof
4standarderrors“large”inastatisticalsense?
| Buffett’s | alpha’s | -statistic |     |     |
| --------- | ------- | ---------- | --- | --- |
t
| - Buffett’ssamplealphais                  |     | αˆb = 0.99% |     |     |
| ----------------------------------------- | --- | ----------- | --- | --- |
| - Thestandarderrorofthisestimateisse(αˆb) |     |             | =   |     |
0.25%
- Hence,thet-statisticwiththenullhypothesisofzerois
αˆb
0.99%
|     |     | t = | =   | = 3.99 |
| --- | --- | --- | --- | ------ |
αˆb se(αˆb) 0.25%
⇒ Therealizedalphaisapproximately4standarderrorsawayfromzero
56/112

| Buffett’s | alpha’s | -statistic |     |     |
| --------- | ------- | ---------- | --- | --- |
t
| - Buffett’ssamplealphais                  |     | αˆb = 0.99% |     |     |
| ----------------------------------------- | --- | ----------- | --- | --- |
| - Thestandarderrorofthisestimateisse(αˆb) |     |             | =   |     |
0.25%
- Hence,thet-statisticwiththenullhypothesisofzerois
αˆb
0.99%
|     |     | t = | =   | = 3.99 |
| --- | --- | --- | --- | ------ |
αˆb se(αˆb) 0.25%
⇒ Therealizedalphaisapproximately4standarderrorsawayfromzero
- Useful,butisthisenoughtorejectthenullhypothesis? Inotherwords,isadistanceof
4standarderrors“large”inastatisticalsense?
56/112

| Determining | the rejection | rule |
| ----------- | ------------- | ---- |
Todeterminearejectionrule,wemust:
1. Decideonthealternativehypothesis
| - What’sthealternativethatwewishtotestthenullagainst? |     |     |
| ----------------------------------------------------- | --- | --- |
2. Decideonthesignificancelevel
| - Atwhichlevelofcertaintywillwerejectthenull? |     |     |
| --------------------------------------------- | --- | --- |
Thesedecisionsresultinacriticalvalue,whichdetermineswhenthet-statistcis
sufficientlylargetorejectthenullhypothesis
57/112

The alternative hypothesis
Therearethreepossiblealternativehypotheses:
- Aone-sidedalternativehypothesisiseitherthatthetrueparameterislargerthanthe
null:
H : β > β0,
A j j
orthatthetrueparameterissmallerthanthenull:
H : β < β0
A j j
- Atwo-sidedalternativehypothesisisthatthetrueparametersdiffersfromthenull:
H : β ̸= β0
A j j
58/112

⇒Thefinalstepisthentofindacriticalvaluethatsatisfythesignificancelevel
The significance level
- ThesignificanceleveldeterminestheprobabilityofrejectingH whenit’sinfacttrue
0
- Themostcommonsignificancelevelis5%
- Thetiedsecondandthirdmostcommonare1%and10%
- But,youcanchooseanysignificancelevelyouwant
- Wedenotethesignificancelevelwith α ,e.g., α = 0.05fora5%significancelevel
59/112

The significance level
- ThesignificanceleveldeterminestheprobabilityofrejectingH whenit’sinfacttrue
0
- Themostcommonsignificancelevelis5%
- Thetiedsecondandthirdmostcommonare1%and10%
- But,youcanchooseanysignificancelevelyouwant
- Wedenotethesignificancelevelwith α ,e.g., α = 0.05fora5%significancelevel
⇒Thefinalstepisthentofindacriticalvaluethatsatisfythesignificancelevel
59/112

- Thecriticalvalueisanumberc suchthat,underthenulldistributionin(8)estimates
moreextremethanc onlyhappenin,say,
α
ofthesamples
The critical value
- Rememberfrom(5)thatthesamplingdistributionofthestandardizedOLSestimatoris
βˆ −β
j j
∼ t(n−k −1),
se(βˆ )
j
- Ifthenullhypothesisistrue,thenwecanreplace
β
with β0,andthentheleft-hand
j j
sideisequaltothet-statisticfrom(6),sounderH thet-statisticist distributed:
0
t ∼ t(n−k −1) (8)
βˆ
j
60/112

The critical value
- Rememberfrom(5)thatthesamplingdistributionofthestandardizedOLSestimatoris
βˆ −β
j j
∼ t(n−k −1),
se(βˆ )
j
- Ifthenullhypothesisistrue,thenwecanreplace
β
with β0,andthentheleft-hand
j j
sideisequaltothet-statisticfrom(6),sounderH thet-statisticist distributed:
0
t ∼ t(n−k −1) (8)
βˆ
j
- Thecriticalvalueisanumberc suchthat,underthenulldistributionin(8)estimates
moreextremethanc onlyhappenin,say,
α
ofthesamples
60/112

The percentile function
t
- Tofindthecriticalvalue,we’llusethepercentilefunctionofthet-distribution
- I’llusethenotationc toindicatethepthpercentileofat-distributionwithn−k −1
p
degreesoffreedom
- InR,youcangetthet percentilesusingthefunctionqt()bysupplyingthedesired
percentile(calledp)andthedegreesoffreedom(calleddf),e.g.,
| Notation |        | Rcall            | Result |
| -------- | ------ | ---------------- | ------ |
| c        | qt(p = | 0.025, df = 100) | -1.98  |
0.025
| c   | qt(p = | 0.050, df = 100) | -1.66 |
| --- | ------ | ---------------- | ----- |
0.050
0.00
| c   | qt(p = | 0.500, df = 100) |     |
| --- | ------ | ---------------- | --- |
0.500
| c   | qt(p = | 0.050, df = 100) | 1.66 |
| --- | ------ | ---------------- | ---- |
0.950
| c   | qt(p = | 0.975, df = 100) | 1.98 |
| --- | ------ | ---------------- | ---- |
0.975
- Sincethet distributionissymmetric,p and1−p arethesame,exceptforthesign
61/112

| Finding | the critical | value | in  |     |
| ------- | ------------ | ----- | --- | --- |
R
Herearethreeexamplesforfindingthecriticalvalue One−sided alternative (positive)
| inRwithasignificancevalueof5%and100DFs |     |     |     | 0.4 |
| -------------------------------------- | --- | --- | --- | --- |
ytisneD 0.3 1.66
1. Thepercentilewhere5%ofobservationsare
0.2 Area: 5%
0.1
| largerisc |        | = qt(p=1-0.05, | df=100) |     |
| --------- | ------ | -------------- | ------- | --- |
|           | 1−0.05 |                |         | 0.0 |
−2 0 2
2. Thepercentilewhere5%ofobservationsare
One−sided alternative (negative)
| smallerisc |     | = qt(p=0.05, | df=100) |     |
| ---------- | --- | ------------ | ------- | --- |
|            |     | 0.05         |         | 0.4 |
0.3
ytisneD −1.66
0.2 Area: 5%
3. Thepercentilewhere2.5%ofobservationsare
0.1
| smallerisc |     | = qt(p=0.05/2, | df=100) | 0.0 |
| ---------- | --- | -------------- | ------- | --- |
0.05/2
−2 0 2
andtheonewhere2.5%islargeris
Two−sided alternative
| c        | =   | qt(p=1-0.05/2, | df=100) |     |
| -------- | --- | -------------- | ------- | --- |
| 1−0.05/2 |     |                |         | 0.4 |
ytisneD 0.3 −1.98 1.98
0.2 Area: 2.5% Area: 2.5%
0.1
0.0
−2 0 2
62/112

The rejection rule
Therejectionrule
| - Withaone-sidedalternativeofH | : β0,rejectH | if  |
| ------------------------------ | ------------ | --- |
β >
|     | A j j | 0   |
| --- | ----- | --- |
>
t c 1−α
βj
| - Withaone-sidedalternativeofH | : β < β0,rejectH | if  |
| ------------------------------ | ---------------- | --- |
|                                | A j j            | 0   |
t < c
βj α
| - Withatwo-sidedalternativeofH | : β0,rejectH | if  |
| ------------------------------ | ------------ | --- |
β ̸=
|     | A j j | 0   |
| --- | ----- | --- |
|t | > c
βj 1−α/2
63/112

| Was Buffett’s | alpha just | luck? |     |     |
| ------------- | ---------- | ----- | --- | --- |
- ForBuffett’salphawehadthefollowingnullandalternativehypotheses:
|              |     | :       | αb :                  | αb   |
| ------------ | --- | ------- | --------------------- | ---- |
|              |     | H 0     | = 0 & H A             | > 0, |
|              |     |         | 0                     | 0    |
| andwehaven−k | −1  | = 551−2 | = 549degreesoffreedom |      |
- Choosingasignificancelevelof5%,givesthecriticalvalue
c 1−0.05 = 1.66
- Sincethealphat-statisticishigherthanthislevel,
|     |     | t   | = 3.99 > 1.66 = c | ,   |
| --- | --- | --- | ----------------- | --- |
|     |     | αˆb | 1−0.05            |     |
werejectthenullhypothesisata5%significancelevel
64/112

- Further,yousometimeshearpeoplesay{someestimate}isstatisticallysignificantat
conventionalsignificancelevels. “conventionalsignificancelevels”are0.01,0.05,and
0.10
- Soifyourejectthenullhypothesisatthe1%significancelevel,youcansaythatyour
estimateissignificantatconventionalsignificancelevels
Terminology: Statistical significance
- Ifwerejectanullhypothesisatasignificancelevelof,say,5%,thenit’scommontosay
thattheparameterestimateissignificantatthestatedsignificancelevel
- Forexample,werejectedthenullhypothesisthat αˆb waszeroata5%significance
level,sowecansaythatBuffett’salphaisstatisticallysignificantlydifferentfromzero
atthe5%significancelevel
- Inpractice,mostpeoplewouldusetheshorthandexpressionBuffett’salphaisstatistically
significantatthe5%level
65/112

Terminology: Statistical significance
- Ifwerejectanullhypothesisatasignificancelevelof,say,5%,thenit’scommontosay
thattheparameterestimateissignificantatthestatedsignificancelevel
- Forexample,werejectedthenullhypothesisthat αˆb waszeroata5%significance
level,sowecansaythatBuffett’salphaisstatisticallysignificantlydifferentfromzero
atthe5%significancelevel
- Inpractice,mostpeoplewouldusetheshorthandexpressionBuffett’salphaisstatistically
significantatthe5%level
- Further,yousometimeshearpeoplesay{someestimate}isstatisticallysignificantat
conventionalsignificancelevels. “conventionalsignificancelevels”are0.01,0.05,and
0.10
- Soifyourejectthenullhypothesisatthe1%significancelevel,youcansaythatyour
estimateissignificantatconventionalsignificancelevels
65/112

Tool 2: -values
p
66/112

RenTech uses -values
p
“The team uncovered predictive effects related to volatility, as well as a series of
combination effects, such as the propensity of pairs of investments—such as gold and
silver,orheatingoilandcrudeoil—tomoveinthesamedirectionatcertaintimesinthe
tradingdaycomparedwithothers.Itwasn’timmediatelyobviouswhysomeofthenew
trading signals worked, but as long as they had p-values, or probability values, under
0.01—meaning they appeared statisticallysignificant, with a low probability of being
statisticalmirages—theywereaddedtothesystem.”
-NickPatterson,formerseniorstatisticianatRenaissanceTechnologies
67/112

Tool 2: -values
p
Strictrejectionrulesrelyonarbitrarycutoffs
- Forexample,ifBuffett’salphat-statisticwas1.65wewouldhavefailedtorejectthe
null,butifitwas1.67wewouldhaverejectedthenull
- Inpractice,statisticalevidenceiscontinuousanditdoesn’tmakesensetorelyona
binaryrule
Abettermeasureisthep-value
- Ap-valuemeasurestheprobabilityofobservingsomethingatleastasextremeasthe
sampleestimateifthenullhypothesisistrue
- Alternatively,youcanthinkofthep-valueasthesmallestsignificancelevelwherethe
nullwouldberejected
68/112

| Computing | the -value | in  |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- |
|           | p          | R   |     |     |     |     |
- p-valuesareasimpletransformationoft-statistics
- Forone-sidedalternatives,it’ssimplytheprobabilitymassinthenulldistribution
aboveorbelowthet-statistics
- Fortwo-sidedalternatives,it’sthetotalprobabilitymassaboveabs(t)andbelow-abs(t)
| - Togetp-valuesinRfor,say,t |                       | = 1.3withdf | = 100: |     |       |        |
| --------------------------- | --------------------- | ----------- | ------ | --- | ----- | ------ |
|                             | Alternativehypothesis |             |        |     | Rcall | Result |
β0
|     | β j > |     | 1-pt(q | = 1.3, df | = 100) | 9.83% |
| --- | ----- | --- | ------ | --------- | ------ | ----- |
j
< β0
|     | β j |     | pt(q | = 1.3, df | = 100) | 90.17% |
| --- | --- | --- | ---- | --------- | ------ | ------ |
j
̸= β0
|     | β j | 2*pt(q | = -abs(1.3), | df  | = 100) | 19.66% |
| --- | --- | ------ | ------------ | --- | ------ | ------ |
j
69/112

| What’s the | -value | of Buffett’s | alpha? |     |
| ---------- | ------ | ------------ | ------ | --- |
p
| - Thet-statisticofBuffettwast |     |     | = 3.99 |     |
| ----------------------------- | --- | --- | ------ | --- |
αˆb
| - ThealternativehypothesiswasH |     |     | : αb |     |
| ------------------------------ | --- | --- | ---- | --- |
> 0
A 0
- InR,wecancalculatethep-valueas
|     |     | 1-pt(q = buffett | t, df = df) | = 0.0038% |
| --- | --- | ---------------- | ----------- | --------- |
- ⇒ifBuffett’struealphawas0theprobabilityofobservingasamplealphaof0.99%or
| moreis0.0038% | underthenull |     |     |     |
| ------------- | ------------ | --- | --- | --- |
70/112

Thismightseemlikeunimportantsemanticsbutit’sabigdealinstatisticsandscience2
Be careful when interpreting -values
p
p-valuesareanexcellenttool,butwemustbecautiouswiththeirinterpretation
1. p-valuesmeasuretheprobabilityofobservingsomethingatleastasextremeasthe
sampleestimateifthenullhypothesisistrue
2. p-valuesdonotmeasuretheprobabilitythatthenullhypothesisistrue
3. p-valuesdonotmeasuretheprobabilitythatthealternativehypothesisistrue
4. p-valuesshouldbeinterpretedcontinuously,so,e.g.,thedifferencebetween
p = 0.049andp = 0.051istinyevenifitcrossedacommonsignificancelevel
5. p-valuesshouldbesupplementedwitht-statistics. Thisisespeciallytrueforsituations
suchasBuffett’swheretheevidenceagainstthenullisoverwhelming
2
71/112

Be careful when interpreting -values
p
p-valuesareanexcellenttool,butwemustbecautiouswiththeirinterpretation
1. p-valuesmeasuretheprobabilityofobservingsomethingatleastasextremeasthe
sampleestimateifthenullhypothesisistrue
2. p-valuesdonotmeasuretheprobabilitythatthenullhypothesisistrue
3. p-valuesdonotmeasuretheprobabilitythatthealternativehypothesisistrue
4. p-valuesshouldbeinterpretedcontinuously,so,e.g.,thedifferencebetween
p = 0.049andp = 0.051istinyevenifitcrossedacommonsignificancelevel
5. p-valuesshouldbesupplementedwitht-statistics. Thisisespeciallytrueforsituations
suchasBuffett’swheretheevidenceagainstthenullisoverwhelming
Thismightseemlikeunimportantsemanticsbutit’sabigdealinstatisticsandscience2
2Sobigthat20oftheworld’sleadingstatisticiansreleasedastatementonhowtousep-values
71/112

Hypothesis testing, -statistics, and -values in
t p R
> summary(buffett reg)
Call:
lm(formula = buffett_exc ∼ mkt_exc, data = buffett)
Residuals:
Min 1Q Median 3Q Max
-0.17219 -0.03369 -0.00564 0.02691 0.33071
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) 0.009911 0.002485 3.989 7.51e-05 ***
mkt_exc 0.708694 0.054334 13.043 < 2e-16 ***
---
Signif. codes: 0 ’***’ 0.001 ’**’ 0.01 ’*’ 0.05 ’.’ 0.1 ’ ’ 1
Residual standard error: 0.05828 on 561 degrees of freedom
Multiple R-squared: 0.2327, Adjusted R-squared: 0.2313
F-statistic: 170.1 on 1 and 561 DF, p-value: < 2.2e-16
- t valueisthet-statistic,Pr(> |t|)isthetwo-sidedp-value,andthestars (*)
indicatesignificanceatcommonlevels
72/112

| Tool 3: | Confidence | intervals |
| ------- | ---------- | --------- |
73/112

⇒OurgoalistoquantifytheCIforanyspecifiedcoverageprobability
| Tool 3: Confidence intervals |     |     |
| ---------------------------- | --- | --- |
Whatisaconfidenceinterval(CI)?3
- ACIisarangearound βˆ thatcoversthetrue withacertaindegreeofconfidence
|                        | 1            | β 1            |
| ---------------------- | ------------ | -------------- |
| - Forexample,a95%CIfor | βˆ willcover | in95%ofsamples |
β
|     | 1   | 1   |
| --- | --- | --- |
- A95%CIindartswouldbeanareaaroundeachshot,thatcoversthecenterfor95%
oftheshots
3I’llfocusonβˆ buteverythingisthesameforβˆ
1 0
74/112

| Tool 3: Confidence intervals |     |     |
| ---------------------------- | --- | --- |
Whatisaconfidenceinterval(CI)?3
- ACIisarangearound βˆ thatcoversthetrue withacertaindegreeofconfidence
|                        | 1            | β 1            |
| ---------------------- | ------------ | -------------- |
| - Forexample,a95%CIfor | βˆ willcover | in95%ofsamples |
β
|     | 1   | 1   |
| --- | --- | --- |
- A95%CIindartswouldbeanareaaroundeachshot,thatcoversthecenterfor95%
oftheshots
⇒OurgoalistoquantifytheCIforanyspecifiedcoverageprobability
3I’llfocusonβˆ buteverythingisthesameforβˆ
1 0
74/112

| A note: Confidence | intervals | are confusing |     |
| ------------------ | --------- | ------------- | --- |
- Beforeweproceed,letmejustpointoutthatconfidenceintervalshaveasomewhat
strangeinterpretation
| - Tore-iterate: | a95%CIfor | βˆ willcover | in95%ofsamples |
| --------------- | --------- | ------------ | -------------- |
|                 |           | 1            | β 1            |
- ThisdoesNOTmeanthata95%CIhasa95%probabilityofcontainingthetrue
β 1
- Theparameterisfixed,theintervalsisthethingthatvariesfromsampletosample
- Tounderstandwhatisdoesmean,let’srunasimulation
75/112

| Confidence   | interval   | example |     |     |
| ------------ | ---------- | ------- | --- | --- |
| # Population | parameters |         |     |     |
b0 <- 1
b1 <- 3
| # Simulation | details |     |     |     |
| ------------ | ------- | --- | --- | --- |
set.seed(1)
n <- 100
| x <- runif(n | = n, | min = -2, | max = 2) |     |
| ------------ | ---- | --------- | -------- | --- |
# Simulation
| sim_ci | <- 1:1000 | |> lapply(function(s) |         | {   |
| ------ | --------- | --------------------- | ------- | --- |
| u <-   | rnorm(n = | n, mean = 0,          | sd = 5) |     |
y <- b0+b1*x+u
| # Parameter | estimates                |           |     |     |
| ----------- | ------------------------ | --------- | --- | --- |
| bhat1       | <- cov(y,                | x)/var(x) |     |     |
| bhat0       | <- mean(y)-bhat1*mean(x) |           |     |     |
# Residuals
| res <-     | y-(bhat0+bhat1*x)                         |           |     |     |
| ---------- | ----------------------------------------- | --------- | --- | --- |
| # Error    | variance                                  | estimate  |     |     |
| evar       | <- 1/(n-2)*sum(res^2)                     |           |     |     |
| # Standard | error                                     | estimates |     |     |
| se0 <-     | sqrt(evar*(1/n+mean(x)^2/((n-1)*var(x)))) |           |     |     |
| se1 <-     | sqrt(evar/((n-1)*var(x)))                 |           |     |     |
# Output
| tibble(sim | = s, | bhat0=bhat0, | bhat1=bhat1, | se0=se0, se1=se1) |
| ---------- | ---- | ------------ | ------------ | ----------------- |
}) |> bind_rows() 76/112

| Confidence | interval | example |     |     |     |
| ---------- | -------- | ------- | --- | --- | --- |
- Thefigureshowsthe90%CI
|     | 90% CI covers b1: | Yes | No  |     |     |
| --- | ----------------- | --- | --- | --- | --- |
for βˆ forthefirst10
1
simulations
10
- We’llexplainexactlyhow
| 9   |     |     |     | they’recalculatedlater |     |
| --- | --- | --- | --- | ---------------------- | --- |
8
- Thetrue isindicatedbythe
7 β 1
on noitalumiS
dashedline
6
| 5   |     |     |     | - Aspredicted(andwithalittle |     |
| --- | --- | --- | --- | ---------------------------- | --- |
| 4   |     |     |     | luck)9outof10CIscover        | β   |
1
3
- Acrossall1000simulations,
2
|     |     |     |     | 89.9%oftheCIscover | β   |
| --- | --- | --- | --- | ------------------ | --- |
1
| 1   |     |     |     | (increasingno.ofsimulations |     |
| --- | --- | --- | --- | --------------------------- | --- |
|     | 2   | 3   | 4   | getsthisto90.0%)            |     |
bhat1
77/112

| Computing | the confidence | interval |
| --------- | -------------- | -------- |
- Tocomputetheconfidenceinterval,weagainrelyonthesamplingdistribution
- Ourgoal: Findanintervalaroundtheestimatethatisbroadenoughtocontainthe
trueestimatewithacertaincoverageprobability
78/112

Centered intervals
t
- Supposez ∼ t(n−k −1),thenacenteredintervalis
| Pr(t      | < z < t     | ) = 1−α |
| --------- | ----------- | ------- |
| n−k−1,α/2 | n−k−1,1−α/2 |         |
wheret isthepthpercentileofthet distributionwithn−k −1degreesof
n−k−1,p
freedom
79/112

| Finding | the percentiles |     | in (again) |     |     |
| ------- | --------------- | --- | ---------- | --- | --- |
|         | t               |     | R          |     |     |
- Aswesawononeofthepreviousslides,youcangetthet percentilesusingthe
functionqt()bysupplyingthedesiredpercentileandthedegreesoffreedom,e.g.,
|     |     | Notation |     | Rcall | Result |
| --- | --- | -------- | --- | ----- | ------ |
-1.96
|     |     | t   | qt(p = | 0.025, df = | 500) |
| --- | --- | --- | ------ | ----------- | ---- |
500,0.025
|     |     | t   | qt(p = | 0.500, df = | 500) 0.00 |
| --- | --- | --- | ------ | ----------- | --------- |
500,0.500
1.96
|     |     | t   | qt(p = | 0.975, df = | 500) |
| --- | --- | --- | ------ | ----------- | ---- |
500,0.975
- Sincethet distributionissymmetric,theupperandlowerboundsonacentered
| intervalarethesame,exceptforthesign,e.g. |     |     |     | abs(t | ) = |
| ---------------------------------------- | --- | --- | --- | ----- | --- |
t
500,0.025 500,0.975
- Therefore,let’sdefineaconstant,c ,whichisthe1−α/2percentileinat distribution
α
| withn−k | −1degreesoffreedom: |     |     |             |     |
| ------- | ------------------- | --- | --- | ----------- | --- |
|         |                     |     | c = | t           |     |
|         |                     |     | α   | n−k−1,1−α/2 |     |
80/112

| Computing                      | the confidence |     | intervals |     |     |     |     |     |
| ------------------------------ | -------------- | --- | --------- | --- | --- | --- | --- | --- |
| Sincethesamplingdistributionof |                |     | βˆ        | is  |     |     |     |     |
1
βˆ
1 −β 1
|     |     |     |     | ∼ t(n−k |     | −1) |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
se(βˆ
)
1
wehavethat
|     |     |     | (cid:32) |         |     | (cid:33) |     |     |
| --- | --- | --- | -------- | ------- | --- | -------- | --- | --- |
|     |     |     |          | βˆ −β   |     |          |     |     |
|     |     | Pr  |          | 1       | 1   |          |     |     |
|     | 1−α | =   | −c       | <       | < c |          |     |     |
|     |     |     |          | α se(βˆ | )   | α        |     |     |
1
|     |     | Pr(cid:0) |       |       |       |               | (cid:1) |     |
| --- | --- | --------- | ----- | ----- | ----- | ------------- | ------- | --- |
|     |     | =         | βˆ −c | se(βˆ | ) < β | < βˆ +c se(βˆ | )       |     |
|     |     |           | 1     | α 1   | 1     | 1 α           | 1       |     |
Theconfidenceinterval
|               |                                       |     |     | βˆ ±c | se(βˆ ), |     |     | (9) |
| ------------- | ------------------------------------- | --- | --- | ----- | -------- | --- | --- | --- |
|               |                                       |     |     | j α   | 1        |     |     |     |
| coversthetrue | β in100(1−α)%ofthehypotheticalsamples |     |     |       |          |     |     |     |
j
81/112

| Confidence   | interval   | example |     |     |
| ------------ | ---------- | ------- | --- | --- |
| # Population | parameters |         |     |     |
b0 <- 1
b1 <- 3
| # Simulation | details |     |     |     |
| ------------ | ------- | --- | --- | --- |
set.seed(1)
n <- 100
| x <- runif(n | = n, | min = -2, | max = 2) |     |
| ------------ | ---- | --------- | -------- | --- |
# Simulation
| sim_ci | <- 1:1000 | |> lapply(function(s) |         | {   |
| ------ | --------- | --------------------- | ------- | --- |
| u <-   | rnorm(n = | n, mean = 0,          | sd = 5) |     |
y <- b0+b1*x+u
| # Parameter | estimates                |           |     |     |
| ----------- | ------------------------ | --------- | --- | --- |
| bhat1       | <- cov(y,                | x)/var(x) |     |     |
| bhat0       | <- mean(y)-bhat1*mean(x) |           |     |     |
# Residuals
| res <-     | y-(bhat0+bhat1*x)                         |           |     |     |
| ---------- | ----------------------------------------- | --------- | --- | --- |
| # Error    | variance                                  | estimate  |     |     |
| evar       | <- 1/(n-2)*sum(res^2)                     |           |     |     |
| # Standard | error                                     | estimates |     |     |
| se0 <-     | sqrt(evar*(1/n+mean(x)^2/((n-1)*var(x)))) |           |     |     |
| se1 <-     | sqrt(evar/((n-1)*var(x)))                 |           |     |     |
# Output
| tibble(sim | = s, | bhat0=bhat0, | bhat1=bhat1, | se0=se0, se1=se1) |
| ---------- | ---- | ------------ | ------------ | ----------------- |
}) |> bind_rows() 82/112

| Confidence | interval | example |     |
| ---------- | -------- | ------- | --- |
- Runningtheabovecodegivesus:
- Focusingonthefirstsimulation,wecancalculate,say,the90%CIof as
βˆ
1
| c <- qt(p      | = 1-0.1/2, | df = n-2) |     |
| -------------- | ---------- | --------- | --- |
| sim_ci         | |>         |           |     |
| filter(sim==1) |            | |>        |     |
mutate(
| ci_low  | = bhat1 | - c*se1, |     |
| ------- | ------- | -------- | --- |
| ci_high | = bhat1 | + c*se1, |     |
)
| - Givingci | low=2.66andci | high=4.12,whichcoversthetrue | β = 3 |
| ---------- | ------------- | ---------------------------- | ----- |
1
83/112

| Confidence | interval | example |     |     |     |
| ---------- | -------- | ------- | --- | --- | --- |
- Thefigureshowsthe90%CI
|     | 90% CI covers b1: | Yes | No  |                   |     |
| --- | ----------------- | --- | --- | ----------------- | --- |
|     |                   |     |     | for forthefirst10 |     |
βˆ
1
simulations
10
| 9   |     |     |     | - Thetrue | isindicatedbythe |
| --- | --- | --- | --- | --------- | ---------------- |
β
1
| 8   |     |     |     | dashedline |     |
| --- | --- | --- | --- | ---------- | --- |
7
on noitalumiS
- Aspredicted(andwithalittle
6
luck)9outof10CIscover
β 1
5
| 4   |     |     |     | - Acrossall1000simulations, |     |
| --- | --- | --- | --- | --------------------------- | --- |
89.9%oftheCIscover
3 β
1
(increasingno.ofsimulations
2
getsthisto90.0%)
1
|     | 2   | 3   | 4   |     |     |
| --- | --- | --- | --- | --- | --- |
bhat1
84/112

| Why should | we care | about confidence | intervals? |
| ---------- | ------- | ---------------- | ---------- |
- Theconfidenceintervalcapturestheinformationinthedataabouttheparameter
- Thecenteroftheintervalisyourbestguessaboutthetrueparameter(yourestimate)
- Thelengthoftheintervalshowstheaccuracyofthisestimate
85/112

| Tool 4: | Prediction | intervals |
| ------- | ---------- | --------- |
86/112

Tool 4: Prediction intervals
- Predictionproblem
- Givenanexplanatoryvariablex predictthefutureobservationy
| new |     | new |
| --- | --- | --- |
- Predictionrecipesofar
1. Collectasampleofhistoricaldata{(x ,y ),(x ,y ),...,(x ,y )}
| n n                                       | n n   | n n |
| ----------------------------------------- | ----- | --- |
| 2. UseOLStobuildapredictionrule,f(x) = βˆ | +βˆ x |     |
| 0                                         | 1     |     |
3. Pluggingx intopredictionrulegivesthepredictionyˆ
new new
- Predictionaccuracy
- isourbestguessofy,butit’sjustoneofmanypossibilities
yˆ new
- Toassestherangeofplausiblevaluesofy weusepredictioninvervals
87/112

| The prediction | error | has two components |     |     |     |
| -------------- | ----- | ------------------ | --- | --- | --- |
Thepredictionerror,uˆ ,reflectstherandompopulationerrorandtheestimationerror
new
|     | y −yˆ | = uˆ = u | +(β −βˆ | +(β −βˆ | )x )  |
| --- | ----- | -------- | ------- | ------- | ----- |
|     | new   | new new  | new 0   | 0 1     | 1 new |
y
y = β +β x
0 1
y
new
unew
uˆ
new
|     |     |     | estimationerror |     | βˆ +βˆ |
| --- | --- | --- | --------------- | --- | ------ |
yˆ = x
0 1
yˆ new
|     |     | x   |     | x   |     |
| --- | --- | --- | --- | --- | --- |
new
88/112

| Decomposing | the prediction |     | error |     |     |     |     |
| ----------- | -------------- | --- | ----- | --- | --- | --- | --- |
- Thepredictionerrorcanbedecomposedas:
|     | uˆ  | =   | y −yˆ                                |           |                 |                    |           |
| --- | --- | --- | ------------------------------------ | --------- | --------------- | ------------------ | --------- |
|     |     | new | new                                  | new       |                 |                    |           |
|     |     | =   | (β +β                                | )+u       |                 | −(βˆ               | +βˆ )     |
|     |     |     | 0                                    | 1 x new   | new             | 0                  | 1 x new   |
|     |     | =   | u                                    | +(β       | −βˆ             | +(β −βˆ            | )x )      |
|     |     |     | new                                  |           | 0 0             | 1                  | 1 new     |
|     |     |     | (cid:124)(cid:123)(cid:122)(cid:125) | (cid:124) |                 | (cid:123)(cid:122) | (cid:125) |
|     |     |     | randomerror                          |           | estimationerror |                    |           |
where
- Therandomerrorreflectsinherentidiosyncrasiesduetou
- Estimationerrorreflectsthedifferencebetweenourestimatedregressionlineandthe
truepopulationline
89/112

Prediction error variance
- Wecannotobservethepredictionerrorforaspecificobservation. Instead,a
predictionintervalgivesarangeofplausiblevaluessimilartowhataconfidence
intervaldoesforaparameter
- Todoso,wefirstcomputethevarianceofourpredictionerroras
| var(uˆ | ) = var((β +β | x )+u    | −(βˆ    | +βˆ x )) |
| ------ | ------------- | -------- | ------- | -------- |
| new    | 0             | 1 new    | new 0   | 1 new    |
|        | var(u         | )+var(βˆ | +βˆ     |          |
|        | = new         |          | x new ) |          |
|        |               | 0        | 1       |          |
|        | = σ2+var(yˆ   | ),       |         |          |
new
whichreflectsthevarianceoftherandomandestimationerror
- Theerrorvariance σ2 isfamiliarbuttheestimationerrorvariance,var(yˆ ),isnew
new
90/112

| Estimation error variance |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- |
- Thepopulationestimationerrorvarianceis
| var(yˆ | var(βˆ   | +βˆ      |               |             |       |
| ------ | -------- | -------- | ------------- | ----------- | ----- |
|        | ) =      |          | x )           |             |       |
|        | new      | 0        | 1 new         |             |       |
|        | = var(βˆ | )+x2     | var(βˆ        | )+2x cov(βˆ | ,βˆ ) |
|        |          | 0        | new           | 1 new       | 0 1   |
|        |          | (cid:18) | −x¯)2(cid:19) |             |       |
1 (x
|     | = σ2 | +   | new | ,   |     |
| --- | ---- | --- | --- | --- | --- |
n (n−1)s2
x
whichcanbeinferredfromthesamplingdistributionsof βˆ and βˆ coveredearlier,
|                      |         |          |          | 0   | 1   |
| -------------------- | ------- | -------- | -------- | --- | --- |
|                      |         | (cid:16) | (cid:17) |     |     |
| andthefactthatcov(βˆ | ,βˆ ) = | −σ2      | x¯       |     |     |
0 1
|     |     | (n−1)s2 | x   |     |     |
| --- | --- | ------- | --- | --- | --- |
- Toestimatetheestimationerrorvariance,wesimplyreplace σ2 with σˆ2
91/112

Prediction error variance
- Togetthevarianceofthepredictionerror,wesimplyaddtherandomerrorvariance
totheestimationerrorvariance:
|     | (cid:18) | (x −x¯)2(cid:19) |
| --- | -------- | ---------------- |
1 new
| var(uˆ | ) = σˆ2 1+ | +       |
| ------ | ---------- | ------- |
| new    |            | (n−1)s2 |
n
x
- Takingthesquareroot,wegetthestandarderroroftheprediction:
(cid:113)
| se(uˆ | ) = | var(uˆ ) |
| ----- | --- | -------- |
|       | new | new      |
92/112

| The prediction                      | distribution |     |         |         |     |
| ----------------------------------- | ------------ | --- | ------- | ------- | --- |
| - SinceOLSisunbiased,weknowthatE[uˆ |              |     | ] = E[y | −yˆ     | ] = |
|                                     |              |     | new     | new new | 0   |
- Further,becauseweestimateitsvariance,thescaledscaledpredictionerrorist
| distributedwithn−k | −1degreesoffreedom: |     |     |     |     |
| ------------------ | ------------------- | --- | --- | --- | --- |
uˆ
|     |     | new | ∼ t(n−k −1) |     |     |
| --- | --- | --- | ----------- | --- | --- |
se(uˆ
)
new
| - Expandinguˆ          | = y −yˆ | andre-arranging,weseethata(1−α)100% |     |     |     |
| ---------------------- | ------- | ----------------------------------- | --- | --- | --- |
|                        | new new | new                                 |     |     |     |
| predictionintervalforY |         | is                                  |     |     |     |
new
|                                                       |     | yˆ ±c | ×se(uˆ | )   |     |
| ----------------------------------------------------- | --- | ----- | ------ | --- | --- |
|                                                       |     | new   | α new  |     |     |
| wherec istheconstantwealsousedwithconfidenceintervals |     |       |        |     |     |
α
93/112

- Roughlyspeaking,wehavemoreobservationsclosetothemeanofx,andmoredata
equalshigheraccuracy
| A closer | look at the | prediction | error variance |     |
| -------- | ----------- | ---------- | -------------- | --- |
Recallthatthepredictionerrorvarianceis
|     |     | (cid:18) | −x¯)2(cid:19) |     |
| --- | --- | -------- | ------------- | --- |
1 (x
|     | var(uˆ | ) = σˆ2 | 1+ + new | = σˆ2+σˆ2 |
| --- | ------ | ------- | -------- | --------- |
new
n (n−1)s2 fit
x
Alargepredictionstandarderror(lowaccuracy)reflects
| - Large | σˆ (i.e.,largeu’s) |     |     |     |
| ------- | ------------------ | --- | --- | --- |
- Smalln(notenoughdata)
| - Smalls | (notenoughdispersioninexplanatoryvariables) |     |     |     |
| -------- | ------------------------------------------- | --- | --- | --- |
x
| - Large(x | −x¯)(Newexplanatoryvariableisfarfromaverage) |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- |
new
Thefirstthreearefamiliar;whataboutthelastone?
94/112

| A closer | look at the | prediction | error variance |     |
| -------- | ----------- | ---------- | -------------- | --- |
Recallthatthepredictionerrorvarianceis
|     |     | (cid:18) | −x¯)2(cid:19) |     |
| --- | --- | -------- | ------------- | --- |
1 (x
|     | var(uˆ | ) = σˆ2 | 1+ + new | = σˆ2+σˆ2 |
| --- | ------ | ------- | -------- | --------- |
new
n (n−1)s2 fit
x
Alargepredictionstandarderror(lowaccuracy)reflects
| - Large | σˆ (i.e.,largeu’s) |     |     |     |
| ------- | ------------------ | --- | --- | --- |
- Smalln(notenoughdata)
| - Smalls | (notenoughdispersioninexplanatoryvariables) |     |     |     |
| -------- | ------------------------------------------- | --- | --- | --- |
x
| - Large(x | −x¯)(Newexplanatoryvariableisfarfromaverage) |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- |
new
Thefirstthreearefamiliar;whataboutthelastone?
- Roughlyspeaking,wehavemoreobservationsclosetothemeanofx,andmoredata
equalshigheraccuracy
94/112

| Estimation | error vs. | random | error |
| ---------- | --------- | ------ | ----- |
- Finance101: Systematicriskismoredangerousthanidiosyncraticriskbecausethe
lattercanbediversifiedawayinlargeportfolios
- Intermsofpredictionerror
| - Estimationerrorissystematicrisk |     |     |     |
| --------------------------------- | --- | --- | --- |
| - Randomerrorisidiosyncraticrisk  |     |     |     |
- Implication
- Ifyou’reanindividualbuyingonehouse,estimationerrorandrandomerrorareequally
important
- Ifyou’reaquantitativerealestateinvestorbuying100houses,estimationerroris
potentiallythegreaterconcern
95/112

| Prediction | in is straightforward | with      |
| ---------- | --------------------- | --------- |
|            | R                     | predict() |
- $fitgivesprediction+predictioninterval
- $se.fitgivessquarerootoftheestimationerrorvariance
- $dfgivesthedegreesoffreedomusedtofindc
α
- $residual.scalegivestheestimatederrorstandarddeviation,
σˆ
96/112

| Bayesian | inference: | A fifth | tool |
| -------- | ---------- | ------- | ---- |
97/112

| Frequentist | versus Bayesian | statistics |
| ----------- | --------------- | ---------- |
- Frequentiststatistics
| - Everythingwe’vecoveredsofarinthiscourse |     |     |
| ----------------------------------------- | --- | --- |
| - Mostof“classicalstatistics”             |     |     |
| - Keyidea:“Trustthedatablindly”           |     |     |
- Bayesianstatistics
| - A“newer”morecomputationallyintensivebranchofstatistics4 |     |     |
| --------------------------------------------------------- | --- | --- |
| - ThestandardtextbookisBayesianDataAnalysis               |     |     |
| - Keyidea:“Trustindatadependsonyourpriorbeliefs”          |     |     |
4Well,newerinthesensethatitswidespreaduseinstatisticsismorerecentthanfrequentism.Butthe
originalideasgoesbacktoBayes,T.(1763).”AnEssaytowardssolvingaProblemintheDoctrineofChances.”
98/112

Frequentist statistics: trust the data blindly
- ThefrequentistestimateofBuffett’struealpha:
Frequentistestimateof αb = 0.010,
whichisequaltoBuffett’srealizedalpha⇒blindtrustindata
- Frequentistinferenceisbasedontoolssuchasconfidenceintervalsthatarealways
centeredaroundthedataestimate
- Roughlyspeaking,Ithinkthere’sa50%chancethattherealizedalphaistoohighanda
50%chancethattherealizedalphaistoolow
- Isayroughlybecausefrequentistinferencedoesnotallowyoutospeakinprobabilities,
onlyabstractstufflike“coverageprobability”—incontrasttoBayesianinference
99/112

Bayesian statistics: Trust in data depends on your prior beliefs
- BayesianestimateofBuffett’struealpha:
| Bayesianestimateof | αb            | +αb             |     |
| ------------------ | ------------- | --------------- | --- |
|                    | = 0.010×wdata | prior ×(1−wdata | )   |
where
αb :Yourpriorbeliefaboutwhatisanexpectedalphaofamutualfund
prior
wdata :theweightyouputonthedata,i.e.,yourtrustinthedata
- Togettheseinputs,youneedtoneedtodetermineyoursubjectivepriordistribution
100/112

- Thingstoconsider:
- Mostmutualfundmanagersdon’tbeatthemarket⇒distributioncenteredaroundzero
- Somemanagersmighthaveskill,butalphaabove,say,1%permonthisextremelyunlikely
- Areasonablepriordistributionmightbenormalwithmeanofzeroandvarianceof
0.25%:
αb ∼= N(αb = 0,σ2 = 0.25%2)
prior prior
A subjective prior distribution of Buffett’s alpha
- Askyourself: SupposeIknewnothingaboutafundlikeBuffett’struealpha. What
wouldbeareasonableguessaboutitsdistribution?
101/112

- Areasonablepriordistributionmightbenormalwithmeanofzeroandvarianceof
0.25%:
αb ∼= N(αb = 0,σ2 = 0.25%2)
prior prior
A subjective prior distribution of Buffett’s alpha
- Askyourself: SupposeIknewnothingaboutafundlikeBuffett’struealpha. What
wouldbeareasonableguessaboutitsdistribution?
- Thingstoconsider:
- Mostmutualfundmanagersdon’tbeatthemarket⇒distributioncenteredaroundzero
- Somemanagersmighthaveskill,butalphaabove,say,1%permonthisextremelyunlikely
101/112

| A subjective | prior distribution |     | of Buffett’s | alpha |
| ------------ | ------------------ | --- | ------------ | ----- |
- Askyourself: SupposeIknewnothingaboutafundlikeBuffett’struealpha. What
wouldbeareasonableguessaboutitsdistribution?
- Thingstoconsider:
- Mostmutualfundmanagersdon’tbeatthemarket⇒distributioncenteredaroundzero
- Somemanagersmighthaveskill,butalphaabove,say,1%permonthisextremelyunlikely
- Areasonablepriordistributionmightbenormalwithmeanofzeroandvarianceof
0.25%:
|     |     | αb ∼= | N(αb = 0,σ2 | = 0.25%2) |
| --- | --- | ----- | ----------- | --------- |
|     |     |       | prior       | prior     |
101/112

- Plugginginthenumbersweget:
0.25%2
wdata = =0.5,
0.25%2+0.25%2
- OurBayesian(posterior)estimateofBuffett’salpha:
|     |     |     |     | Bayesianestimateofαb | =0.99%×0.5+0×(1−0.5) | =0.5% |
| --- | --- | --- | --- | -------------------- | -------------------- | ----- |
⇒ Ifindthisshocking.BayesianperspectivecutsBuffett’salphaintohalf!
| The Bayesian | estimate | of Buffett’s | alpha |     |     |     |
| ------------ | -------- | ------------ | ----- | --- | --- | --- |
- IfweassumethatBuffett’sestimatedalphaisnormallydistributed(e.g.,becauseoftheCLT),
| thentheformulatogetw |     | is  |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
data
σ2
prior
|     |     | wdata | =   |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
σ2 +se(αˆ)2
prior
⇒trustindatadependsonyourprioruncertainty(σ2 )relativetothedatauncertainty(se[αˆ])
prior
102/112

- OurBayesian(posterior)estimateofBuffett’salpha:
|     |     |     |     | Bayesianestimateofαb | =0.99%×0.5+0×(1−0.5) | =0.5% |
| --- | --- | --- | --- | -------------------- | -------------------- | ----- |
⇒ Ifindthisshocking.BayesianperspectivecutsBuffett’salphaintohalf!
| The Bayesian | estimate | of Buffett’s | alpha |     |     |     |
| ------------ | -------- | ------------ | ----- | --- | --- | --- |
- IfweassumethatBuffett’sestimatedalphaisnormallydistributed(e.g.,becauseoftheCLT),
| thentheformulatogetw |     | is  |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
data
σ2
prior
|     |     | wdata | =   |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
σ2 +se(αˆ)2
prior
⇒trustindatadependsonyourprioruncertainty(σ2 )relativetothedatauncertainty(se[αˆ])
prior
- Plugginginthenumbersweget:
0.25%2
wdata = =0.5,
0.25%2+0.25%2
102/112

⇒ Ifindthisshocking.BayesianperspectivecutsBuffett’salphaintohalf!
| The Bayesian | estimate | of Buffett’s | alpha |     |
| ------------ | -------- | ------------ | ----- | --- |
- IfweassumethatBuffett’sestimatedalphaisnormallydistributed(e.g.,becauseoftheCLT),
| thentheformulatogetw |     | is  |     |     |
| -------------------- | --- | --- | --- | --- |
data
σ2
prior
|     |     |     | wdata = |     |
| --- | --- | --- | ------- | --- |
σ2 +se(αˆ)2
prior
⇒trustindatadependsonyourprioruncertainty(σ2 )relativetothedatauncertainty(se[αˆ])
prior
- Plugginginthenumbersweget:
0.25%2
wdata = =0.5,
0.25%2+0.25%2
- OurBayesian(posterior)estimateofBuffett’salpha:
|     | Bayesianestimateofαb |     | =0.99%×0.5+0×(1−0.5) | =0.5% |
| --- | -------------------- | --- | -------------------- | ----- |
102/112

| The Bayesian | estimate | of Buffett’s | alpha |     |
| ------------ | -------- | ------------ | ----- | --- |
- IfweassumethatBuffett’sestimatedalphaisnormallydistributed(e.g.,becauseoftheCLT),
| thentheformulatogetw |     | is  |     |     |
| -------------------- | --- | --- | --- | --- |
data
σ2
prior
|     |     |     | wdata = |     |
| --- | --- | --- | ------- | --- |
σ2 +se(αˆ)2
prior
⇒trustindatadependsonyourprioruncertainty(σ2 )relativetothedatauncertainty(se[αˆ])
prior
- Plugginginthenumbersweget:
0.25%2
wdata = =0.5,
0.25%2+0.25%2
- OurBayesian(posterior)estimateofBuffett’salpha:
|     | Bayesianestimateofαb |     | =0.99%×0.5+0×(1−0.5) | =0.5% |
| --- | -------------------- | --- | -------------------- | ----- |
⇒ Ifindthisshocking.BayesianperspectivecutsBuffett’salphaintohalf!
102/112

Bayesian inference
- Sofar,we’veonlydoneBayesianestimation
- TodoBayesianinference,weneedtoestimatetheposteriorstandarddeviation:
(cid:118)
|     | (cid:117) se(αˆ)2×σ 2 |     |
| --- | --------------------- | --- |
(cid:117)
|            | = p rior  | =     |
| ---------- | --------- | ----- |
| σposterior | (cid:116) | 0.18% |
se(αˆ)2+σ2
prior
- NowwehavethefullposteriordistributionofBuffett’salpha:
| Bufffett’salphaposterior | ∼ N(0.5%,0.18%2), |     |
| ------------------------ | ----------------- | --- |
fromwhichallinferencecanbedonewithout“hacks”suchasp-valuesandconfidence
intervals
103/112

| Buffett’s | alpha | posterior | distribution |     |     |     |
| --------- | ----- | --------- | ------------ | --- | --- | --- |
Bayesianinference
- Probability
| 200 |     |     |     |               | αb < 0.0% | = 0.23%  |
| --- | --- | --- | --- | ------------- | --------- | -------- |
|     |     |     |     | - Probability | αb < 0.3% | = 12.89% |
150
| ytisneD |     |     |     | - Probability | αb < 0.5% | = 50.00% |
| ------- | --- | --- | --- | ------------- | --------- | -------- |
100
- Probability αb
|     |     |     |     |     | > 0.7% | = 12.89% |
| --- | --- | --- | --- | --- | ------ | -------- |
50
|     |     |     |     | - Probability | αb > 1.0% | = 0.23% |
| --- | --- | --- | --- | ------------- | --------- | ------- |
0
|     | 0.0% | 0.4% | 0.8% | 1.2% |     |     |
| --- | ---- | ---- | ---- | ---- | --- | --- |
Buffett's alpha
104/112

- Butithasonebigflaw: itreliesonyour(potentiallybiased)subjectivebeliefs
- EmpiricalBayesisanattempttomakeBayesianinferenceobjective
- Idea:Estimateparametersofpriordistributionfromdata(likeafrequentist)
- Fantastictool.Formoreinformationseechapter6inComputerAgeStatisticalInference
| Empirical | Bayes: Frequentism | meets Bayesianism |
| --------- | ------------------ | ----------------- |
- Bayesianinferencehasmanybenefits:
| -   | Followstheaxiomsofprobabilitytheory   |     |
| --- | ------------------------------------- | --- |
| -   | Incorporatespriorknowledge            |     |
| -   | Inferenceisstraightforwardandflexible |     |
105/112

| Empirical | Bayes: Frequentism | meets Bayesianism |
| --------- | ------------------ | ----------------- |
- Bayesianinferencehasmanybenefits:
| -   | Followstheaxiomsofprobabilitytheory   |     |
| --- | ------------------------------------- | --- |
| -   | Incorporatespriorknowledge            |     |
| -   | Inferenceisstraightforwardandflexible |     |
- Butithasonebigflaw: itreliesonyour(potentiallybiased)subjectivebeliefs
- EmpiricalBayesisanattempttomakeBayesianinferenceobjective
- Idea:Estimateparametersofpriordistributionfromdata(likeafrequentist)
- Fantastictool.Formoreinformationseechapter6inComputerAgeStatisticalInference
105/112

| Example: | Using | statistical      | inference | to test    |
| -------- | ----- | ---------------- | --------- | ---------- |
| whether  | there | is a replication | crisis    | in finance |
106/112

| Is there | a replication | crisis | in finance? |
| -------- | ------------- | ------ | ----------- |
- ThepaperIsthereareplicationcrisisinfinance? bymyself,BryanKelly,andLasse
HejePedersenisanexampleofstatisticalinferenceinaction:
107/112

1. Nointernalvalidity
Resultscannotbereproducedsmallchangestomethodologyordata
“Mostanomaliesfailtoholduptocurrentlyacceptablestandards”
–Houetal.(2020)→replicationrate:35%
2. Noexternalvalidity
Resultsreplicatein-sample,butarespuriousdueto“p-hacking”
“Mostclaimedresearchfindingsinfinancialeconomicsarelikelyfalse”
–Harveyetal.(2016)→replicationrate:<50%
Is there a replication crisis in finance?
- Severalfieldsfacereplicationcrises(orcredibilitycrises):
- Medicine(Ioannidis2005),psychology(Noseketal.2012),management(Bettis2012),...
- Nowfinance–twomainchallengestofactorresearch:
108/112

2. Noexternalvalidity
Resultsreplicatein-sample,butarespuriousdueto“p-hacking”
“Mostclaimedresearchfindingsinfinancialeconomicsarelikelyfalse”
–Harveyetal.(2016)→replicationrate:<50%
Is there a replication crisis in finance?
- Severalfieldsfacereplicationcrises(orcredibilitycrises):
- Medicine(Ioannidis2005),psychology(Noseketal.2012),management(Bettis2012),...
- Nowfinance–twomainchallengestofactorresearch:
1. Nointernalvalidity
Resultscannotbereproducedsmallchangestomethodologyordata
“Mostanomaliesfailtoholduptocurrentlyacceptablestandards”
–Houetal.(2020)→replicationrate:35%
108/112

Is there a replication crisis in finance?
- Severalfieldsfacereplicationcrises(orcredibilitycrises):
- Medicine(Ioannidis2005),psychology(Noseketal.2012),management(Bettis2012),...
- Nowfinance–twomainchallengestofactorresearch:
1. Nointernalvalidity
Resultscannotbereproducedsmallchangestomethodologyordata
“Mostanomaliesfailtoholduptocurrentlyacceptablestandards”
–Houetal.(2020)→replicationrate:35%
2. Noexternalvalidity
Resultsreplicatein-sample,butarespuriousdueto“p-hacking”
“Mostclaimedresearchfindingsinfinancialeconomicsarelikelyfalse”
–Harveyetal.(2016)→replicationrate:<50%
108/112

| Is there | a replication | crisis | in finance? |     |
| -------- | ------------- | ------ | ----------- | --- |
- Weimplement153equityfactorsproposedintheacademicliterature,e.g.,Value,
Momentum,Quality,Size,etc.
- Foreachfactor,weuseOLStoestimatetheCAPMmodel:
|     |     |     | ri = αi +βirmkt | +ui |
| --- | --- | --- | --------------- | --- |
|     |     |     | t t             | t   |
- Foreachfactor,wetest
|     |     | H   | : αi = 0 against | H : αi > 0 |
| --- | --- | --- | ---------------- | ---------- |
|     |     | 0   |                  | A          |
ata2.5%significancelevel. Saiddifferently,wecountafactorasreplicatedifit’s
p-valueisbelow2.5%.
- WealsouseempiricalBayesbuttheresultsaresimilar
109/112

Is there a replication crisis in finance?
- Column1isthe35%replicationratefromHouetal,column2and3aredataconsiderations
- Column4showsthatwerejectH atthe2.5%levelfor82.4%ofthefactorsinoursample
0
- Column5-6areextensionswithmultipletestingandempiricalBayesianinference
110/112

Is there a replication crisis in finance? Useful code and data
- Weuploadallthecodefromourpaperat
https://github.com/bkelly-lab/ReplicationCrisis
⇒ LearnhowtouseBayesianstatisticsandhowtobuildadatasetofstockslistedin93
differentcountries
- Weuploadequityfactorsaroundtheworldathttps://jkpfactors.com/
⇒ ResearchofequityfactorsoutsideoftheU.S.islacking,soconsiderusingthisdatafor
findingoverlookedalpha,orforwriting,say,anindependentresearchproject
111/112

Thank you!
112/112
