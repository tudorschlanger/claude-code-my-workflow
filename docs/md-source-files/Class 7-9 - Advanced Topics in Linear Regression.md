MGMT924StatisticalFoundations
Class 7-9: Advanced Topics in Linear Regression
Topics: Multiplelinearregression,datatransformations,economicsignificance,
backtesting,linearalgebraforOLSestimation,theGauss-Markovtheorem,ridge
regression,lassoregression,elasticnet,bias-variancetradeoff,modelselection,
cross-validation,clusteredstandarderrors,Occam’srazor
TheisIngerslevJensen
YaleSOM
1/107

| Multiple | Linear | Regression |
| -------- | ------ | ---------- |
2/107

Tobuildbetterpredictionrules!
| Multiple                  | vs. simple                                                 | linear regression      |
| ------------------------- | ---------------------------------------------------------- | ---------------------- |
| - Simplelinearregression: |                                                            | Oneexplanatoryvariable |
|                           | - Pros:Greatforunderstanding                               |                        |
|                           | - Cons:Mostoutcomesintherealworlddependonmorethanonefactor |                        |
- Multiplelinearregression(MLR):Manyexplanatoryvariables
- MLRiswhatyou’llusemostofthetimewhenbuildinganOLSpredictionrule
- It’salsothefoundationofprominentmachinelearningmethods,suchasridgeandlasso
regressions(whichwe’llcoverlater)
- Q:Whydowewantmoreexplanatoryvariables?
3/107

| Multiple                  | vs. simple                                                 | linear regression      |
| ------------------------- | ---------------------------------------------------------- | ---------------------- |
| - Simplelinearregression: |                                                            | Oneexplanatoryvariable |
|                           | - Pros:Greatforunderstanding                               |                        |
|                           | - Cons:Mostoutcomesintherealworlddependonmorethanonefactor |                        |
- Multiplelinearregression(MLR):Manyexplanatoryvariables
- MLRiswhatyou’llusemostofthetimewhenbuildinganOLSpredictionrule
- It’salsothefoundationofprominentmachinelearningmethods,suchasridgeandlasso
regressions(whichwe’llcoverlater)
- Q:Whydowewantmoreexplanatoryvariables? Tobuildbetterpredictionrules!
3/107

Example: More variables = better predictions of stock returns
Problem
- Yourinvestmentuniverseisthe500largestUSstocks
- Yourgoalistobuildadollar-neutralportfoliowhereyoubuystockswithahigh
expectedreturnandshortstockswithalowexpectedreturn
- Issue: Youdon’thavetimetomanuallyanalyze500stocks
Solution: Buildaquantitativepredictionrule!
- Collecthistoricaldataonstockreturns
- Buildpredictionruletopredictfuturestockreturns
4/107

Stock data
- Datasource
- IgetthedataonhistoricalstockreturnsfromCRSPviaWRDS
- WRDSisagoldmineforresearchqualitydata,andYalestudentshavefreeaccess(link)
- AlternativessuchasYahooorGooglefinance,sufferfromissuessuchassurvivorshipbias
thatmakethemunsuitableforseriousquantitativework
- Datascreens
- Commonstocks(shrcd:10,11,or12)
- ListedonNYSE,Nasdaq,orAMEX(exchcd:1,2,or3)
- Largest500stocks
- Periodfrom1980to2022
- Dependentandexplanatoryvariables
- Dependentvariable:Excessreturns,i.e.,thestock’stotalreturnminustherisk-freerate,
denotedri
t
- Exploratoryvariables:Excessreturnsfromthepast12months,denotedri ,...,ri
t−1 t−12
5/107

Stock data
Here’swhatthedatalookslikeinR:
6/107

- EstimatingthemodelinRwithlm()andsummarizingwithsummary():
reg1 <- lm(r∼r_lg1, data=stock_returns)
summary(reg1)
gives
Estimating the simple linear regression model
- It’salwaysagoodideatostartwithasimplepredictionmodel,sowe’lltry
ri = β +β ri
t 0 1 t−1
7/107

| Estimating | the simple | linear regression | model |
| ---------- | ---------- | ----------------- | ----- |
- It’salwaysagoodideatostartwithasimplepredictionmodel,sowe’lltry
ri ri
= β +β
t 0 1 t−1
- EstimatingthemodelinRwithlm()andsummarizingwithsummary():
| reg1 | <- lm(r∼r_lg1, | data=stock_returns) |     |
| ---- | -------------- | ------------------- | --- |
summary(reg1)
gives
7/107

- Intermsof“statisticalsignificance”:
- TheR2 isabysmallylowat0.00000103
- Ther lg1termisalsonotreallystatisticallysignificantwithap-valueof0.26
- Buthowdoesthistranslateintoeconomicsignificance?
- Inotherwords,howusefulisthepredictionrulefortradingstocks?
- Afantasticwaytoevaluateeconomicsignificanceistouseaportfoliosort
- Sidepoint:Whenpeoplesaytheyrunabacktest,theyoftenmeanthattheydoa
portfoliosort
Economic significance
- Howusefulisourpredictionrule?
8/107

- Buthowdoesthistranslateintoeconomicsignificance?
- Inotherwords,howusefulisthepredictionrulefortradingstocks?
- Afantasticwaytoevaluateeconomicsignificanceistouseaportfoliosort
- Sidepoint:Whenpeoplesaytheyrunabacktest,theyoftenmeanthattheydoa
portfoliosort
Economic significance
- Howusefulisourpredictionrule?
- Intermsof“statisticalsignificance”:
- TheR2 isabysmallylowat0.00000103
- Ther lg1termisalsonotreallystatisticallysignificantwithap-valueof0.26
8/107

- Afantasticwaytoevaluateeconomicsignificanceistouseaportfoliosort
- Sidepoint:Whenpeoplesaytheyrunabacktest,theyoftenmeanthattheydoa
portfoliosort
Economic significance
- Howusefulisourpredictionrule?
- Intermsof“statisticalsignificance”:
- TheR2 isabysmallylowat0.00000103
- Ther lg1termisalsonotreallystatisticallysignificantwithap-valueof0.26
- Buthowdoesthistranslateintoeconomicsignificance?
- Inotherwords,howusefulisthepredictionrulefortradingstocks?
8/107

Economic significance
- Howusefulisourpredictionrule?
- Intermsof“statisticalsignificance”:
- TheR2 isabysmallylowat0.00000103
- Ther lg1termisalsonotreallystatisticallysignificantwithap-valueof0.26
- Buthowdoesthistranslateintoeconomicsignificance?
- Inotherwords,howusefulisthepredictionrulefortradingstocks?
- Afantasticwaytoevaluateeconomicsignificanceistouseaportfoliosort
- Sidepoint:Whenpeoplesaytheyrunabacktest,theyoftenmeanthattheydoa
portfoliosort
8/107

| What | is a portfolio | sort? |
| ---- | -------------- | ----- |
- Portfoliosortsareaclassicaltoolinfinancetoseeifsomestocks,suchashigh
book-to-market(value)stocksoutperformlowbook-to-market(growth)stocks.
- Theclassicalportfoliosortimplementationisstraightforward:
1. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirbook-to-marketratio
|     | 2. Computethereturnofeachportfolioinmontht+1 |     |
| --- | -------------------------------------------- | --- |
|     | 3. Computetheaveragereturnofeachportfolio    |     |
|     | 4. Visualizetheresults,oftenbyusingabarplot  |     |
9/107

| Here’s | an example | of a portfolio | sort: |
| ------ | ---------- | -------------- | ----- |
FromBordalo,Gennaioli,LaPorta,andShleifer(2019)
10/107

1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
3. Computethereturnofeachportfolioinmontht+1
4. Computetheaveragereturnofeachportfolio
5. Visualizetheresults,oftenbyusingabarplot
Evaluating a prediction rule with portfolio sorts
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
11/107

2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
3. Computethereturnofeachportfolioinmontht+1
4. Computetheaveragereturnofeachportfolio
5. Visualizetheresults,oftenbyusingabarplot
Evaluating a prediction rule with portfolio sorts
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
11/107

3. Computethereturnofeachportfolioinmontht+1
4. Computetheaveragereturnofeachportfolio
5. Visualizetheresults,oftenbyusingabarplot
Evaluating a prediction rule with portfolio sorts
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
11/107

4. Computetheaveragereturnofeachportfolio
5. Visualizetheresults,oftenbyusingabarplot
| Evaluating | a prediction | rule with | portfolio | sorts |
| ---------- | ------------ | --------- | --------- | ----- |
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
| 3. Computethereturnofeachportfolioinmontht+1 |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- |
11/107

5. Visualizetheresults,oftenbyusingabarplot
| Evaluating | a prediction | rule with | portfolio | sorts |
| ---------- | ------------ | --------- | --------- | ----- |
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
| 3. Computethereturnofeachportfolioinmontht+1 |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- |
| 4. Computetheaveragereturnofeachportfolio    |     |     |     |     |
11/107

| Evaluating | a prediction | rule with | portfolio | sorts |
| ---------- | ------------ | --------- | --------- | ----- |
- Whenyou’retryingtopredictassetreturnsportfoliosortsareafantastictoolfor
evaluatingtheeconomicsignificanceofyourpredictionrule
- Implementation:
1. Generateapredictionforeachstockinyourtradinguniverseusingthepredictionrule
2. Eachmontht,sortstocksinto,say,tenportfoliosbasedontheirpredictedreturn
| 3. Computethereturnofeachportfolioinmontht+1 |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- |
| 4. Computetheaveragereturnofeachportfolio    |     |     |     |     |
| 5. Visualizetheresults,oftenbyusingabarplot  |     |     |     |     |
11/107

| Evaluating | our prediction | rule with | a portfolio | sort in R |
| ---------- | -------------- | --------- | ----------- | --------- |
1. Generatepredictionsforeachstock:
| ps_data | <- stock_returns | |>  |     |     |
| ------- | ---------------- | --- | --- | --- |
mutate(
|     | pred = predict(reg1, | newdata=stock_returns) |     |     |
| --- | -------------------- | ---------------------- | --- | --- |
) |>
| select(permno, | eom, | r, pred) |     |     |
| -------------- | ---- | -------- | --- | --- |
2. Sortstocksintotenportfolios:
| ps_data       | <- ps_data |> |     |     |     |
| ------------- | ------------- | --- | --- | --- |
| group_by(eom) | |>            |     |     |     |
mutate(
|     | pred_percentile | = ecdf(pred)(pred), |     |     |
| --- | --------------- | ------------------- | --- | --- |
pf = ceiling(pred_percentile*10)
)
Note: ecdf(x)(x)createsthepercentilesofxso,e.g.,ecdf(1:10)(1:10)gives
0.1,0.2,...,1.0
12/107

| Evaluating | our prediction | rule with | a portfolio | sort in R |
| ---------- | -------------- | --------- | ----------- | --------- |
3. Computeportfolioreturninmontht:
| pfs <-       | ps_data |> |     |     |     |
| ------------ | ---------- | --- | --- | --- |
| group_by(pf, | eom)       | |>  |     |     |
summarise(
n = n(),
pf_ret = mean(r)
)
4. Computetheaveragereturnofeachportfolio:
| stock_summary | <- pfs | |>  |     |     |
| ------------- | ------ | --- | --- | --- |
group_by(pf) |>
summarise(
mean = mean(pf_ret)*12
)
13/107

| Evaluating | our | prediction | rule with | a portfolio | sort | in R |
| ---------- | --- | ---------- | --------- | ----------- | ---- | ---- |
5. Visualizetheresult:
| stock_summary |                                   | |>            |          |              |                    |           |
| ------------- | --------------------------------- | ------------- | -------- | ------------ | ------------------ | --------- |
|               | ggplot(aes(factor(pf),            |               | mean))   | +            |                    |           |
|               | geom_col(fill=colours_theme[1])   |               |          | +            |                    |           |
|               | geom_text(aes(label=formatC(mean, |               |          | digits       | = 2, format="f")), |           |
|               |                                   | vjust=0,      | nudge_y  | = 0.001)     | +                  |           |
|               | labs(x                            | = "Portfolios | sorted   | by predicted | return             | (1=low)", |
|               | y                                 | = "Average    | return") |              |                    |           |
0.11 0.11
|     |     |                     |     | 0.09 0.09 | 0.09 |      |
| --- | --- | ------------------- | --- | --------- | ---- | ---- |
|     |     | nruter egarevA 0.09 |     |           |      | 0.09 |
0.08
0.07
0.06 0.06
0.06
0.03
0.00
|     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
14/107

| Pro tip:  | Wrap code         | you want    | to repeat | in a function |
| --------- | ----------------- | ----------- | --------- | ------------- |
| pf_sort   | <- function(data, | reg, n_pfs) | {         |               |
| # Predict | based on          | regression  |           |               |
| ps_data   | <- data |>        |             |           |               |
mutate(
|     | pred = predict(reg, | newdata=data) |     |     |
| --- | ------------------- | ------------- | --- | --- |
) |>
|         | select(permno,   | eom, r, pred) |                     |     |
| ------- | ---------------- | ------------- | ------------------- | --- |
| # Sort  | stocks into      | 10 portfolios | based on prediction |     |
| ps_data | <- ps_data       | |>            |                     |     |
|         | group_by(eom) |> |               |                     |     |
mutate(
|     | pred_percentile | = ecdf(pred)(pred), |     |     |
| --- | --------------- | ------------------- | --- | --- |
.
.
.
| # Visualize   | the result                      |        |     |     |
| ------------- | ------------------------------- | ------ | --- | --- |
| stock_summary | |>                              |        |     |     |
|               | ggplot(aes(factor(pf),          | mean)) | +   |     |
|               | geom_col(fill=colours_theme[1]) |        | +   |     |
geom_text(aes(label=formatC(mean, digits = 2, format="f")), vjust=0,
|     | nudge_y = 0.001) | +   |     |     |
| --- | ---------------- | --- | --- | --- |
labs(x = "Portfolios sorted by predicted return (1=low)", y = "Average
return")
} 15/107

| Data transformation | 1: Remove | the market | return |
| ------------------- | --------- | ---------- | ------ |
- Beforeaddingmoreexplanatoryvariables,let’strytodosomedatatransformations
- Inthemodelwejustestimated,thedependentvariablewastheexcessreturnofa
stock,whichwecandecomposeas
|     | ri = | r¯ +                                 | (ri −r¯)                               |
| --- | ---- | ------------------------------------ | -------------------------------------- |
|     | t    | t                                    | t t                                    |
|     |      | (cid:124)(cid:123)(cid:122)(cid:125) | (cid:124) (cid:123)(cid:122) (cid:125) |
|     |      | averagereturn relativereturn         |                                        |
- However,weusepredictiontobuildadollar-neutrallong-shortportfolio,sowedon’t
careaboutpredictingtheaveragereturn
- Therefore,wecouldtrytosubtracttheaveragereturnfromthedependentvariable:
r˜i = ri −r¯,
|     |     | t t t |     |
| --- | --- | ----- | --- |
anddothesamefortheexplanatoryvariables.
16/107

| Data transformation | 1: Remove | the market | return |
| ------------------- | --------- | ---------- | ------ |
- Codefordatatransformation:
| # Demean dependent | variable         |     |     |
| ------------------ | ---------------- | --- | --- |
| stock_returns      | <- stock_returns | |>  |     |
| group_by(eom)      | |>               |     |     |
mutate(
rt = r - mean(r)
)
| # Demean explanatory | variables        |     |     |
| -------------------- | ---------------- | --- | --- |
| stock_returns        | <- stock_returns | |>  |     |
| group_by(eom)        | |>               |     |     |
mutate(
across(r_lg1:r_lg12, ∼ .x - mean(.x))
) |>
rename_with(.fn = ∼str_replace(.x, pattern = "r_lg", replacement = "rt_lg"),
|     | .cols = starts_with("r_lg")) | |>  |     |
| --- | ---------------------------- | --- | --- |
ungroup()
- Andnowwecanestimatethemodel:
|     |     | r˜i r˜i | +ui |
| --- | --- | ------- | --- |
= β +β
|     |     | t 0 1 t−1 | t   |
| --- | --- | --------- | --- |
17/107

0.11
0.11
|     |     |     |      |     | 0.09 | 0.09 |      |
| --- | --- | --- | ---- | --- | ---- | ---- | ---- |
|     |     |     | 0.09 |     | 0.09 |      |      |
|     |     |     |      |     | 0.08 |      | 0.09 |
nruter egarevA
0.07
0.06 0.06
0.06
0.03
0.00
|     |     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
Same,why?
| Data transformation     | 1: Remove | the market           | return |     |     |     |     |
| ----------------------- | --------- | -------------------- | ------ | --- | --- | --- | --- |
| Statisticalsignificance |           | Economicsignificance |        |     |     |     |     |
Lowerestimatebutmuchlowerstandard
error=hugeincreaseint-stat!
R2 gaindifficulttointerpretbecausethe
dependentvariablechanged 18/107

| Data transformation     | 1: Remove | the market           | return |     |     |     |
| ----------------------- | --------- | -------------------- | ------ | --- | --- | --- |
| Statisticalsignificance |           | Economicsignificance |        |     |     |     |
0.11
0.11
|     |     |      |     | 0.09 | 0.09 |      |
| --- | --- | ---- | --- | ---- | ---- | ---- |
|     |     | 0.09 |     | 0.09 |      |      |
|     |     |      |     | 0.08 |      | 0.09 |
nruter egarevA
0.07
0.06 0.06
0.06
0.03
0.00
|     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
Lowerestimatebutmuchlowerstandard
Same,why?
error=hugeincreaseint-stat!
R2 gaindifficulttointerpretbecausethe
| dependentvariablechanged |     |     |     |     |     | 18/107 |
| ------------------------ | --- | --- | --- | --- | --- | ------ |

| Data transformation     | 1: Remove | the market           | return |     |     |     |
| ----------------------- | --------- | -------------------- | ------ | --- | --- | --- |
| Statisticalsignificance |           | Economicsignificance |        |     |     |     |
0.11
0.11
|     |     |      |     | 0.09 | 0.09 |      |
| --- | --- | ---- | --- | ---- | ---- | ---- |
|     |     | 0.09 |     | 0.09 |      |      |
|     |     |      |     | 0.08 |      | 0.09 |
nruter egarevA
0.07
0.06 0.06
0.06
0.03
0.00
|     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
Lowerestimatebutmuchlowerstandard
|     |     | Same,why? | Becausethetwoprediction |     |     |     |
| --- | --- | --------- | ----------------------- | --- | --- | --- |
error=hugeincreaseint-stat! rulesgivesthesamecross-sectionalranking
R2 gaindifficulttointerpretbecausethe (rankingonlydependonrelativepast
| dependentvariablechanged |     | return) |     |     |     | 18/107 |
| ------------------------ | --- | ------- | --- | --- | --- | ------ |

| Data transformation | 2: Include | non-linear | variable |
| ------------------- | ---------- | ---------- | -------- |
- Now,let’sstarttoaddmorevariables!
- Theportfoliosortplotindicatesomenon-linearitiesinportfolio10withverylowpast
returnshavelowerreturnthanstocksinportfolio5-9
- Wecouldhandlethisnon-linearitybyincludingadummyvariablewithis1forvery
lowpastreturnsand0otherwise
- Alternatively,wecouldaddaquadratictermtothemodel:
|     | r˜i = | +β r˜i +β | (r˜i )2+ui, |
| --- | ----- | --------- | ----------- |
|     | β     | 0 1 t−1   | 2 t−1       |
|     | t     |           | t           |
we’regoingtotakethelatterapproach
19/107

0.11
0.10
0.10
|     |     |     |                |     | 0.09 |     | 0.09 |
| --- | --- | --- | -------------- | --- | ---- | --- | ---- |
|     |     |     | 0.09           |     | 0.09 |     |      |
|     |     |     | nruter egarevA |     | 0.08 |     |      |
0.07
0.06 0.06 0.06
0.03
0.00
|     |     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
Certainlynoearth-shatteringeconomic
gains,althoughtheincreasefrompf1to
pf10isslightlymoremonotone
| Data transformation     | 2: Include | non-linear           | variable |     |     |     |     |
| ----------------------- | ---------- | -------------------- | -------- | --- | --- | --- | --- |
| Statisticalsignificance |            | Economicsignificance |          |     |     |     |     |
HugestatisticalgainwithadjustedR2
almosttripling. Butwhataboutthe
economicgain?
20/107

| Data transformation     | 2: Include | non-linear           | variable |     |     |     |
| ----------------------- | ---------- | -------------------- | -------- | --- | --- | --- |
| Statisticalsignificance |            | Economicsignificance |          |     |     |     |
0.11
0.10
0.10
|     |     |                |     | 0.09 |     | 0.09 |
| --- | --- | -------------- | --- | ---- | --- | ---- |
|     |     | 0.09           |     | 0.09 |     |      |
|     |     | nruter egarevA |     | 0.08 |     |      |
0.07
0.06 0.06 0.06
0.03
0.00
|     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
HugestatisticalgainwithadjustedR2 Certainlynoearth-shatteringeconomic
almosttripling. Butwhataboutthe gains,althoughtheincreasefrompf1to
| economicgain? |     | pf10isslightlymoremonotone |     |     |     |     |
| ------------- | --- | -------------------------- | --- | --- | --- | --- |
20/107

- Ratherthanseethefullsummary()output,let’svisualizeit:
reg4 |>
|     |     |     |     |     |     | broom::tidy()          |                               | |>             |            |                    |            |            |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | ----------------------------- | -------------- | ---------- | ------------------ | ---------- | ---------- | --- |
|     |     |     |     |     |     | filter(term            | !=                            | "(Intercept)") |            | |>                 |            |            |     |
|     |     |     |     |     |     | mutate(lg              | = as.integer(str_remove(term, |                |            |                    | "rt_lg"))) |            | |>  |
|     |     |     |     |     |     | ggplot(aes(factor(lg), |                               |                | statistic, | group=1))          |            | +          |     |
|     |     |     |     |     |     | geom_point()           | +                             |                |            |                    |            |            |     |
|     |     |     |     |     |     | geom_hline(yintercept  |                               |                | = 0)       | +                  |            |            |     |
|     |     |     |     |     |     | geom_hline(yintercept  |                               |                | = -1.96,   | linetype="dotted") |            |            | +   |
|     |     |     |     |     |     | geom_hline(yintercept  |                               |                | = +1.96,   | linetype="dotted") |            |            | +   |
|     |     |     |     |     |     | geom_line()            | +                             |                |            |                    |            |            |     |
|     |     |     |     |     |     | labs(x                 | = "Return                     | lag",          | y =        | "t-stat            | of OLS     | estimate", |     |
title = paste0("Adj. R2: ", round(summary(reg4)$adj.r.squared, 5)))
| Data transformation | 3: Include |     | more explanatory |     | variables |     |     |     |     |     |     |     |     |
| ------------------- | ---------- | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
- Now,let’strytoaddtheadditionalpastreturnstothemodel:
|     | r˜i = +β | r˜i   | +β r˜i +···+β |     | r˜i +ui, |     |     |     |     |     |     |     |     |
| --- | -------- | ----- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | β 0      | 1 t−1 | 2 t−2         | 12  | t−12     |     |     |     |     |     |     |     |     |
|     | t        |       |               |     | t        |     |     |     |     |     |     |     |     |
(I’mdroppingthequadratictermforsimplicity)
21/107

Data transformation 3: Include more explanatory variables
- Now,let’strytoaddtheadditionalpastreturnstothemodel:
r˜i = β +β r˜i +β r˜i +···+β r˜i +ui,
t 0 1 t−1 2 t−2 12 t−12 t
(I’mdroppingthequadratictermforsimplicity)
- Ratherthanseethefullsummary()output,let’svisualizeit:
reg4 |>
broom::tidy() |>
filter(term != "(Intercept)") |>
mutate(lg = as.integer(str_remove(term, "rt_lg"))) |>
ggplot(aes(factor(lg), statistic, group=1)) +
geom_point() +
geom_hline(yintercept = 0) +
geom_hline(yintercept = -1.96, linetype="dotted") +
geom_hline(yintercept = +1.96, linetype="dotted") +
geom_line() +
labs(x = "Return lag", y = "t-stat of OLS estimate",
title = paste0("Adj. R2: ", round(summary(reg4)$adj.r.squared, 5)))
21/107

|     |     |     | 0.15 |     |     |     | 0.15 |
| --- | --- | --- | ---- | --- | --- | --- | ---- |
0.12
0.11
|     |     |     | nruter egarevA |     |     | 0.11 |     |
| --- | --- | --- | -------------- | --- | --- | ---- | --- |
0.10
0.09
0.09 0.08
0.05
0.05 0.05
0.01
0.00
|     |     |     |     | 1 2 | 3 4 5 | 6 7 8 | 9 10 |
| --- | --- | --- | --- | --- | ----- | ----- | ---- |
Portfolios sorted by predicted return (1=low)
|     |     |     | Economicgainishighly“significant.” |     |     |     | Long |
| --- | --- | --- | ---------------------------------- | --- | --- | --- | ---- |
pf10/shortpf1leadsto14%annualexcess
return—roughlytwicethatofS&P500!
| Data transformation | 3:  | Include more explanatory | variables |     |     |     |     |
| ------------------- | --- | ------------------------ | --------- | --- | --- | --- | --- |
Statisticalsignificance Economicsignificance
Adj. R2: 0.00154
etamitse SLO fo tats−t
5
0
−5
−10
| 1 2 3 | 4 5 6 7 | 8 9 10 11 12 |     |     |     |     |     |
| ----- | ------- | ------------ | --- | --- | --- | --- | --- |
Return lag
| Returnsatt −1andt | −2predictreversals, |     |     |     |     |     |     |
| ----------------- | ------------------- | --- | --- | --- | --- | --- | --- |
whilet −3andabovepredictmomentum
GaininR2,butnothingdramatic
22/107

| Data transformation     | 3:  | Include more explanatory |     | variables |     |     |
| ----------------------- | --- | ------------------------ | --- | --------- | --- | --- |
| Statisticalsignificance |     | Economicsignificance     |     |           |     |     |
Adj. R2: 0.00154
|     |     | 0.15 |     |     |     | 0.15 |
| --- | --- | ---- | --- | --- | --- | ---- |
0.12
| etamitse SLO fo tats−t |     |                |     |     | 0.11 |     |
| ---------------------- | --- | -------------- | --- | --- | ---- | --- |
|                        |     | nruter egarevA |     |     | 0.11 |     |
| 5                      |     | 0.10           |     |     |      |     |
0.09
0.09 0.08
0
0.05
0.05 0.05
−5
0.01
| −10   |            | 0.00         |                                               |       |       |      |
| ----- | ---------- | ------------ | --------------------------------------------- | ----- | ----- | ---- |
| 1 2 3 | 4 5 6 7    | 8 9 10 11 12 | 1 2                                           | 3 4 5 | 6 7 8 | 9 10 |
|       | Return lag |              | Portfolios sorted by predicted return (1=low) |       |       |      |
Returnsatt −1andt −2predictreversals, Economicgainishighly“significant.” Long
whilet −3andabovepredictmomentum pf10/shortpf1leadsto14%annualexcess
| GaininR2,butnothingdramatic |     | return—roughlytwicethatofS&P500! |     |     |     |     |
| --------------------------- | --- | -------------------------------- | --- | --- | --- | --- |
22/107

- Take-aways:
- Moreexplanatoryvariables=betterpredictions
- Datatransformationsarecrucialtobuildingagoodpredictionrule,butit’snotalways
obvioushowstatisticalgainstranslateintoeconomicgains
- Alwaysevaluatetheeconomicsignificanceofyourpredictionrule
- Methodstoevaluateeconomicsignificanceextendwaybeyondportfoliosorts. It’s
crucialtoalwaysthinkaboutthepracticalimplicationofyourstatisticalestimates
- Whatwehaven’tcovered(butwillcoverlater)isthedifferencebetweenin-sample
andout-of-samplepredictability
- Preview:The14%returnisnotrealisticout-of-sample
What can we learn from this example?
23/107

- Whatwehaven’tcovered(butwillcoverlater)isthedifferencebetweenin-sample
andout-of-samplepredictability
- Preview:The14%returnisnotrealisticout-of-sample
| What can | we learn | from this | example? |
| -------- | -------- | --------- | -------- |
- Take-aways:
| -   | Moreexplanatoryvariables=betterpredictions |     |     |
| --- | ------------------------------------------ | --- | --- |
- Datatransformationsarecrucialtobuildingagoodpredictionrule,butit’snotalways
obvioushowstatisticalgainstranslateintoeconomicgains
| -   | Alwaysevaluatetheeconomicsignificanceofyourpredictionrule |     |     |
| --- | --------------------------------------------------------- | --- | --- |
- Methodstoevaluateeconomicsignificanceextendwaybeyondportfoliosorts. It’s
crucialtoalwaysthinkaboutthepracticalimplicationofyourstatisticalestimates
23/107

| What can | we learn | from this | example? |
| -------- | -------- | --------- | -------- |
- Take-aways:
| -   | Moreexplanatoryvariables=betterpredictions |     |     |
| --- | ------------------------------------------ | --- | --- |
- Datatransformationsarecrucialtobuildingagoodpredictionrule,butit’snotalways
obvioushowstatisticalgainstranslateintoeconomicgains
| -   | Alwaysevaluatetheeconomicsignificanceofyourpredictionrule |     |     |
| --- | --------------------------------------------------------- | --- | --- |
- Methodstoevaluateeconomicsignificanceextendwaybeyondportfoliosorts. It’s
crucialtoalwaysthinkaboutthepracticalimplicationofyourstatisticalestimates
- Whatwehaven’tcovered(butwillcoverlater)isthedifferencebetweenin-sample
andout-of-samplepredictability
| -   | Preview:The14%returnisnotrealisticout-of-sample |     |     |
| --- | ----------------------------------------------- | --- | --- |
23/107

| OLS estimation | of the | MLR model |
| -------------- | ------ | --------- |
24/107

The MLR model
| - TheMLRmodelwithk | explanatoryvariables: |     |     |     |     |     |
| ------------------ | --------------------- | --- | --- | --- | --- | --- |
Themultiplelinearregressionmodel
|     | y   | = β +β x | +β x +···+β | x +u |     | (1) |
| --- | --- | -------- | ----------- | ---- | --- | --- |
|     |     | 0 1 1    | 2 2         | k k  |     |     |
where
- β isthepopulationintercept
0
| - β ,...,β                                           | isthepopulationparametersrelatingx |     |     | ,...,x toy |     |     |
| ---------------------------------------------------- | ---------------------------------- | --- | --- | ---------- | --- | --- |
| 1                                                    | k                                  |     | 1   | k          |     |     |
| - uisarandomerrorthatismeanzeroandmeanindependentofx |                                    |     |     |            | ,   |     |
1 ,...,x k
| E[u] =E[u|x | ,...,x | ] =0 |     |     |     |     |
| ----------- | ------ | ---- | --- | --- | --- | --- |
|             | 1 k    |      |     |     |     |     |
- IntheMLRmodel, measuresthechangeiny fromachangeinx holdingx ,...,x
|     | β 1 |     |     |     | 1   | 2 k |
| --- | --- | --- | --- | --- | --- | --- |
fixed
25/107

- TheOLSobjectiveisnow
n
∑
|     |     |     | argmin | (yi −[βˆ +βˆ | xi +βˆ xi])2, | (2) |
| --- | --- | --- | ------ | ------------ | ------------- | --- |
|     |     |     |        | 0            | 1 1 2 2       |     |
βˆ ,βˆ ,βˆ
0 1 2 i=1
andwecanderivetheanalyticalsolutionoruseRtofindthenumericalsolution
| OLS estimation | of the MLR | model |     |     |     |     |
| -------------- | ---------- | ----- | --- | --- | --- | --- |
- OLSestimationoftheMLRmodelisverysimilartotheSLRmodel
- Considerestimatingtheparametersofamodelwithtwoexplanatoryvariables:
= +β +β +u
y β 0 1 x 1 2 x 2
26/107

| OLS estimation | of the MLR | model |     |     |
| -------------- | ---------- | ----- | --- | --- |
- OLSestimationoftheMLRmodelisverysimilartotheSLRmodel
- Considerestimatingtheparametersofamodelwithtwoexplanatoryvariables:
|     |     | = +β        | +β +u |     |
| --- | --- | ----------- | ----- | --- |
|     |     | y β 0 1 x 1 | 2 x 2 |     |
- TheOLSobjectiveisnow
n
∑
|     | argmin | (yi −[βˆ +βˆ | xi +βˆ xi])2, | (2) |
| --- | ------ | ------------ | ------------- | --- |
0 1 1 2 2
βˆ ,βˆ ,βˆ
0 1 2 i=1
andwecanderivetheanalyticalsolutionoruseRtofindthenumericalsolution
26/107

| Numerical | Solution | in R |     |     |
| --------- | -------- | ---- | --- | --- |
- It’seasytoadapttheRcodeweusedinclasses2and3tothecasewithmore
explanatoryvariables:
| # Construct | input                | variables |     |     |
| ----------- | -------------------- | --------- | --- | --- |
| y <-        | stock_returns$rt     |           |     |     |
| x1 <-       | stock_returns$rt_lg1 |           |     |     |
stock_returns$rt2_lg1
| x2 <-         |          |                |     |     |
| ------------- | -------- | -------------- | --- | --- |
| # Objective   | function |                |     |     |
| objective_fun |          | <- function(b) | {   |     |
sum((y-(b[1]+b[2]*x1+b[3]*x2))^2)
}
| # Estimate | parameters |     |     |     |
| ---------- | ---------- | --- | --- | --- |
optim(par = c(0, 0, 0), fn = objective_fun, method = "BFGS")$par
Notethatthefunctionargumentbisnowavectorwiththreearguments,wherethe
firstentryb[1]is βˆ ,thesecondb[2]is βˆ ,andthethirdisb[3]is βˆ
|     |     | 0   | 1   | 2   |
| --- | --- | --- | --- | --- |
- Givessameresultaslm()totheeightdecimal
27/107

| Deriving | the | OLS | solution | for MLR |     |     |     |     |     |
| -------- | --- | --- | -------- | ------- | --- | --- | --- | --- | --- |
1. Thefunctionwewanttominimizeis
n
∑
|     |     |     | f(βˆ | ,βˆ ,βˆ ) = | (yi −[βˆ | +βˆ | xi  | +βˆ xi])2 |     |
| --- | --- | --- | ---- | ----------- | -------- | --- | --- | --------- | --- |
|     |     |     |      | 0 1 2       |          | 0   | 1 1 | 2 2       |     |
i=1
2. Thepartialderivativesare
n
∑
|     |     | ∂f(βˆ | ,βˆ | ,βˆ )/∂βˆ = | −2  | (yi −[βˆ | +βˆ | xi +βˆ | xi]) |
| --- | --- | ----- | --- | ----------- | --- | -------- | --- | ------ | ---- |
|     |     |       | 0 1 | 2 0         |     |          | 0   | 1 1    | 1 2  |
i=1
n
|     |     | ∂f(βˆ | ,βˆ | ,βˆ )/∂βˆ | ∑   | xi(yi −[βˆ | +βˆ | xi  | +βˆ xi]) |
| --- | --- | ----- | --- | --------- | --- | ---------- | --- | --- | -------- |
|     |     |       |     | =         | −2  |            |     |     |          |
|     |     |       | 0 1 | 2 1       |     | 1          | 0   | 1 1 | 1 2      |
i=1
n
|     |     | ∂f(βˆ | ,βˆ | ,βˆ )/∂βˆ = | −2 ∑ | xi(yi −[βˆ | +βˆ | xi  | +βˆ xi]) |
| --- | --- | ----- | --- | ----------- | ---- | ---------- | --- | --- | -------- |
|     |     |       | 0 1 | 2 2         |      |            | 0   | 1   | 1        |
|     |     |       |     |             |      | 2          |     | 1   | 2        |
i=1
28/107

- Exceptfortheintercept,theexpressionsareprettycomplicated,andthisgetsworse
asweaddmorevariables
- Fortunately,theexpressionsaremuchsimplertoexpressinmatrixnotation
| Deriving | the OLS | solution |     | for MLR |     |     |     |
| -------- | ------- | -------- | --- | ------- | --- | --- | --- |
- Wewon’tgothroughthederivation,buttheOLSsolutionis:
|     |     | βˆ  | = −β    | −β     |           |        |      |
| --- | --- | --- | ------- | ------ | --------- | ------ | ---- |
|     |     | 0   | y¯      | 1 x¯ 1 | 2 x¯ 2    |        |      |
|     |     |     | cov(y,x | )var(x | )−cov(y,x | )cov(x | ,x ) |
|     |     | βˆ  | =       | 1      | 2         | 2      | 1 2  |
1
|     |     |     |         | var(x  | )var(x )−cov(x | ,x )2  |      |
| --- | --- | --- | ------- | ------ | -------------- | ------ | ---- |
|     |     |     |         | 1      | 2              | 1 2    |      |
|     |     |     | cov(y,x | )var(x | )−cov(y,x      | )cov(x | ,x ) |
|     |     | βˆ  | =       | 2      | 1              | 1      | 1 2  |
2
|     |     |     |     | var(x | )var(x )−cov(x | ,x )2 |     |
| --- | --- | --- | --- | ----- | -------------- | ----- | --- |
|     |     |     |     | 1     | 2              | 1 2   |     |
29/107

| Deriving | the OLS | solution |     | for MLR |     |     |     |
| -------- | ------- | -------- | --- | ------- | --- | --- | --- |
- Wewon’tgothroughthederivation,buttheOLSsolutionis:
|     |     | βˆ  | = −β    | −β     |           |        |      |
| --- | --- | --- | ------- | ------ | --------- | ------ | ---- |
|     |     | 0   | y¯      | 1 x¯ 1 | 2 x¯ 2    |        |      |
|     |     |     | cov(y,x | )var(x | )−cov(y,x | )cov(x | ,x ) |
|     |     | βˆ  | =       | 1      | 2         | 2      | 1 2  |
1
|     |     |     |         | var(x  | )var(x )−cov(x | ,x )2  |      |
| --- | --- | --- | ------- | ------ | -------------- | ------ | ---- |
|     |     |     |         | 1      | 2              | 1 2    |      |
|     |     |     | cov(y,x | )var(x | )−cov(y,x      | )cov(x | ,x ) |
|     |     | βˆ  | =       | 2      | 1              | 1      | 1 2  |
2
|     |     |     |     | var(x | )var(x )−cov(x | ,x )2 |     |
| --- | --- | --- | --- | ----- | -------------- | ----- | --- |
|     |     |     |     | 1     | 2              | 1 2   |     |
- Exceptfortheintercept,theexpressionsareprettycomplicated,andthisgetsworse
asweaddmorevariables
- Fortunately,theexpressionsaremuchsimplertoexpressinmatrixnotation
29/107

| Solving | the OLS | objective | with matrix | notation |
| ------- | ------- | --------- | ----------- | -------- |
30/107

| A quick | refresher | on matrix | notation |
| ------- | --------- | --------- | -------- |
- Conventionusedinthiscourse:
- Scalars(numberssuchas“2”)areexpressedin“non-bold”lowercaseletters,e.g,z
|     | - Vectorsareexpressedinboldlowercaseletters,e.g.,z  |     |     |
| --- | --------------------------------------------------- | --- | --- |
|     | - Matricesareexpressedinbolduppercaseletters,e.g.,Z |     |     |
31/107

A quick refresher on matrix notation
- Amatrixisacollectionofnumbersstoredinrowsandcolumns,suchas
 
0 1 1 2
Z =  3 5 8 13
21 34 55 89
- Wealwaysexpressthedimensionofamatrixintermsof{#rows}×{#columns}. For
example,theZ matrixhasdimensions3×4
- Amatrixwith1columniscalledacolumnvector,e.g.,
 
0
z = 1
1
- We’llusetheconventionthatvectorsarecolumnvectors. However,tocreatearow
vector,wecantranspose(indicatedby′)acolumnvectortogetarowvector:
z′ = (cid:2) 0 1 1 (cid:3)
32/107

A quick refresher on matrix notation
- LetX beamatrixwithdimensionsn×k andb beavectorwithdimensionsk ×1and
- Wehavethat:
b′b = dimension1×1(ascalar)
bb′ = dimensionk ×k (amatrix)
Xb = dimensionn×1(avector)
X′X = dimensionk ×k (amatrix)
- Forbasicpropertiesofmatrices,TheMatrixCookbookisanexcellentreference.
Sections1and2aresufficientforthiscourse
33/107

| Working | with matrices | in R |
| ------- | ------------- | ---- |
Creatematrices/vectorswithmatrix() Matrixmultiplicationwith%*%,transpose
witht(),inversewithsolve()
34/107

- Inmatrixnotation,thiscanbeexpressedas
Xβˆ+uˆ,
|     |     |     |     |     |     |     |     |     | y   | =   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where
|     |     |     |     |     |     |     |  y1   |     |             |       |        |     |  uˆ1 |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ----- | -------- | --- | ------ |
|     |     |     |     |     |     |     |         |    |             | x1   | βˆ       |     |        |
|     |     |     |     |     |     |     |         | 1   | x1          |       | 0        |     |        |
|     |     |     |     |     |     |     | 2      |     | ...         |       | βˆ       |     | 2     |
|     |     |     |     |     |     |     |  y     |     | 1           | k     |        |     |  uˆ   |
|     |     |     |     |     |     |     |       |    | . . . . ... | . .  | βˆ  1  |     |      |
|     |     |     |     |     |     | y   | = . , X | =   | . .         | . ,   | = . ,    | uˆ  | = .    |
|     |     |     |     |     |     |     |  .    |    |             |      |  .     |     |  .   |
|     |     |     |     |     |     |     |  .    |     |             |       |  .     |     |  .   |
|     |     |     |     |     |     |     |         | 1   | xn ...      | xn    |          |     |        |
|     |     |     |     |     |     |     | yn      |     | 1           | k     | βˆ       |     | uˆn    |
k
|               |     |       |           |          | NoticethatIaddacolumnof1toX     |     |     |     | toaccountfortheintercept |     |     |     |     |
| ------------- | --- | ----- | --------- | -------- | ------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
|               |     |       |           |          | - Q:What’sthedimensionsofy,X,βˆ |     |     |     | and,uˆ?                  |     |     |     |     |
| The estimated | MLR | model | in matrix | notation |                                 |     |     |     |                          |     |     |     |     |
- Withnobservationsandk explanatoryvariables,thestandardexpressionofthe
estimatedmodelwas
|     |     | yi   | xi          | xi  |                  |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | = βˆ | +βˆ +···+βˆ |     | fori = 1,2,...,n |     |     |     |     |     |     |     |     |
|     |     | 0    | 1 1         | k   | k                |     |     |     |     |     |     |     |     |
35/107

- Q:What’sthedimensionsofy,X,βˆ and,uˆ?
| The estimated |     | MLR | model |     | in matrix | notation |     |     |     |     |
| ------------- | --- | --- | ----- | --- | --------- | -------- | --- | --- | --- | --- |
- Withnobservationsandk explanatoryvariables,thestandardexpressionofthe
estimatedmodelwas
|     |     |     | yi  |        | xi      | xi  |      |             |     |     |
| --- | --- | --- | --- | ------ | ------- | --- | ---- | ----------- | --- | --- |
|     |     |     | =   | βˆ +βˆ | +···+βˆ |     | fori | = 1,2,...,n |     |     |
|     |     |     |     | 0      | 1 1     | k   | k    |             |     |     |
- Inmatrixnotation,thiscanbeexpressedas
Xβˆ+uˆ,
|     |     |     |     |     | y   | =   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where
|     |     |  y1 |     |     |             |       |     |     |     |  uˆ1 |
| --- | --- | ----- | --- | --- | ----------- | ----- | --- | ----- | --- | ------ |
|     |     |       |     |    |             | x1   |     | βˆ    |     |        |
|     |     |       |     | 1   | x1          |       |     | 0     |     |        |
|     |     | 2    |     |     | ...         |       |     | βˆ    |     | 2     |
|     |     |  y   |     |     | 1           | k     |     |     |     |  uˆ   |
|     |     |      |    |    | . . . . ... | . .  | βˆ  |  1  |     |      |
|     | y   | = .   | , X | =   | . .         | .     | ,   | = . , | uˆ  | = .    |
|     |     |  .   |    |    |             |      |     |  .  |     |  .   |
|     |     |  .   |    |     |             |       |     |  .  |     |  .   |
|     |     |       |     | 1   | xn ...      | xn    |     |       |     |        |
|     |     | yn    |     |     | 1           | k     |     | βˆ    |     | uˆn    |
k
| NoticethatIaddacolumnof1toX |     |     |     |     | toaccountfortheintercept |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
35/107

| The estimated |     | MLR | model |     | in matrix | notation |     |     |     |     |
| ------------- | --- | --- | ----- | --- | --------- | -------- | --- | --- | --- | --- |
- Withnobservationsandk explanatoryvariables,thestandardexpressionofthe
estimatedmodelwas
|     |     |     | yi  |        | xi      | xi  |      |             |     |     |
| --- | --- | --- | --- | ------ | ------- | --- | ---- | ----------- | --- | --- |
|     |     |     | =   | βˆ +βˆ | +···+βˆ |     | fori | = 1,2,...,n |     |     |
|     |     |     |     | 0      | 1 1     | k   | k    |             |     |     |
- Inmatrixnotation,thiscanbeexpressedas
Xβˆ+uˆ,
|     |     |     |     |     | y   | =   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where
|     |     |  y1 |     |     |             |       |     |     |     |  uˆ1 |
| --- | --- | ----- | --- | --- | ----------- | ----- | --- | ----- | --- | ------ |
|     |     |       |     |    |             | x1   |     | βˆ    |     |        |
|     |     |       |     | 1   | x1          |       |     | 0     |     |        |
|     |     | 2    |     |     | ...         |       |     | βˆ    |     | 2     |
|     |     |  y   |     |     | 1           | k     |     |     |     |  uˆ   |
|     |     |      |    |    | . . . . ... | . .  | βˆ  |  1  |     |      |
|     | y   | = .   | , X | =   | . .         | .     | ,   | = . , | uˆ  | = .    |
|     |     |  .   |    |    |             |      |     |  .  |     |  .   |
|     |     |  .   |    |     |             |       |     |  .  |     |  .   |
|     |     |       |     | 1   | xn ...      | xn    |     |       |     |        |
|     |     | yn    |     |     | 1           | k     |     | βˆ    |     | uˆn    |
k
| NoticethatIaddacolumnof1toX     |     |     |     |     | toaccountfortheintercept |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
| - Q:What’sthedimensionsofy,X,βˆ |     |     |     |     | and,uˆ?                  |     |     |     |     |     |
35/107

- Inmatrixnotation,thisobjectiveis:
−Xβˆ)′(y −Xβˆ),
argmin(y
βˆ
- Somebenefitsofthematrixnotationarethatwecanexpresstheobjectivemore
compactlyandthattheobjectiveisthesameregardlessofthenumberofexplanatory
variables
| The OLS | solution | in matrix | notation |     |     |     |
| ------- | -------- | --------- | -------- | --- | --- | --- |
- Similarly,theOLSobjectivewe’veseensofaris:
n
∑
|     |     | argmin         | (yi −[βˆ +βˆ | xi +···+βˆ | xi])2, | (3) |
| --- | --- | -------------- | ------------ | ---------- | ------ | --- |
|     |     |                | 0            | 1 1        | k k    |     |
|     |     | βˆ ,βˆ ,...,βˆ | ki=1         |            |        |     |
0 1
36/107

| The OLS | solution | in matrix | notation |     |     |     |
| ------- | -------- | --------- | -------- | --- | --- | --- |
- Similarly,theOLSobjectivewe’veseensofaris:
n
∑
|     |     | argmin         | (yi −[βˆ +βˆ | xi +···+βˆ | xi])2, | (3) |
| --- | --- | -------------- | ------------ | ---------- | ------ | --- |
|     |     |                | 0            | 1 1        | k k    |     |
|     |     | βˆ ,βˆ ,...,βˆ | ki=1         |            |        |     |
0 1
- Inmatrixnotation,thisobjectiveis:
−Xβˆ)′(y −Xβˆ),
argmin(y
βˆ
- Somebenefitsofthematrixnotationarethatwecanexpresstheobjectivemore
compactlyandthattheobjectiveisthesameregardlessofthenumberofexplanatory
variables
36/107

| Deriving | the OLS | solution | with matrix | notation |
| -------- | ------- | -------- | ----------- | -------- |
- Let’sstartbyexpandingtheOLSobjective:
|     |     |     | (y −Xβˆ)′(y | −Xβˆ) = |
| --- | --- | --- | ----------- | ------- |
′ ′
|     |     |     | y′y +βˆ X′Xβˆ−2βˆ | X′y |
| --- | --- | --- | ----------------- | --- |
- Differentiatingtheobjectivewithrespectto βˆ andsettingittozeroweget:
|     |     |     | 2X′Xβˆ−2X′y | = 0 → |
| --- | --- | --- | ----------- | ----- |
X′Xβˆ X′y
=
| - Solvingfor | βˆ wegettheresult: |     |                 |     |
| ------------ | ------------------ | --- | --------------- | --- |
|              |                    |     | βˆ = (X′X)−1X′y |     |
37/107

| Implementing |     | matrix | solution | in R |     |
| ------------ | --- | ------ | -------- | ---- | --- |
- Runningthecode:
# Prepare
stock_returns$rt
y <-
x1 <- stock_returns$rt_lg1
x2 <- stock_returns$rt2_lg1
n <- length(y)
k <- 2
|     | X <- | matrix(data | = c(rep(1, | n), x1, x2), | ncol = k+1) |
| --- | ---- | ----------- | ---------- | ------------ | ----------- |
# Result
|     | solve(t(X) | %*% | X) %*% | t(X) %*% y |     |
| --- | ---------- | --- | ------ | ---------- | --- |
- Gives:
38/107

| Inference | for the | MLR Model |
| --------- | ------- | --------- |
39/107

| The sampling | distribution | for the OLS | estimators |
| ------------ | ------------ | ----------- | ---------- |
N(0,σ2)totheMLRmodel,theOLS
| - Ifweaddthenormalityassumption,u |     | ∼   |     |
| --------------------------------- | --- | --- | --- |
estimatorsarenormallydistributedandunbiased:
|     |     | βˆ ∼ N(β | ,var(βˆ )), |
| --- | --- | -------- | ----------- |
|     |     | j        | j j         |
exactlythesameasfortheSLRmodel
- Thefullparametervectorismultivariatelynormallydistributed:
|                                        |     | βˆ = N(β,Σ), |     |
| -------------------------------------- | --- | ------------ | --- |
| whereΣisthevariance-covariancematrixof |     |              | βˆ  |
40/107

| The sampling | distribution | for the OLS | estimators |
| ------------ | ------------ | ----------- | ---------- |
- Thevariance-covarianceestimateis
|                               |     | Σ = σ2(cid:0)    | X′X (cid:1)−1 |
| ----------------------------- | --- | ---------------- | ------------- |
| - Wherewecan,again,estimateσ2 |     | fromtheresiduals |               |
n
1 ∑
|     |     | σˆ2 = | uˆ2 |
| --- | --- | ----- | --- |
n−k −1 i
i=1
- So,thefeasiblevariance-covarianceestimatoris
|     |     | Σˆ σˆ2(cid:0) | X′X (cid:1)−1 |
| --- | --- | ------------- | ------------- |
=
41/107

| The sampling | distribution | for the OLS | estimators |
| ------------ | ------------ | ----------- | ---------- |
- ThevariancesoftheestimatesareinthediagonalofΣˆ
Inparticular,letΣˆ
| -   | denotetheentryintheithrowandjthcolumn,sowehave: |     |     |
| --- | ----------------------------------------------- | --- | --- |
i,j
Σˆ
|     |     | vaˆr(βˆ ) | =   |
| --- | --- | --------- | --- |
0 1,1
|     |     | vaˆr(βˆ ) | = Σˆ |
| --- | --- | --------- | ---- |
1 2,2
. .
.
|     |     | vaˆr(βˆ | Σˆ  |
| --- | --- | ------- | --- |
) =
k k+1,k+1
- Togetthestandarderror,justtakethesquareroot:
(cid:113)
|     |     | se(βˆ | vaˆr(βˆ |
| --- | --- | ----- | ------- |
) = )
j j
42/107

| The sampling | distribution | for the OLS | estimators |
| ------------ | ------------ | ----------- | ---------- |
- Exceptforthestandarderrorcalculation,wecanusethefourtoolsofstatistical
inferenceinexactlythesamewayasfortheSLRmodel
- Also,rememberthat:
- Weestimatetheerrorvariance,sotheestimatorsaret distributed(i.e.notnormal)
- Therelevantdegreesoffreedomforthet distributionisthenumberofobservations
minusthenumberofexplanatoryvariableminusonetoaccountfortheintercept:
βˆ −β
|     |     | j j     | ∼t(n−k −1) |
| --- | --- | ------- | ---------- |
|     |     | se(βˆ ) |            |
j
43/107

Adjusted R2
- ThestandardR2 neverdescreaseswhenaddingavariable(atleastin-samplewith
OLS)
- Hence,toevaluatetwomodelswithdifferentnumberofexplanatoryvariablesit’s
commontousetheadjustedR2
SSR/(n−k −1)
R2 = 1− ,
adj SST/(n−1)
wherek isthenumberofexplanatoryvariablesandnisthenumberofobservations
- Ifnisverylarge,R2 ≈ R
adj 2
- Aninterestingalgebraricfactisthat,whenaddinganewexplanatoryvariable,R2
adj
onlyincreasesifthet statisticonthenewvariableisgreaterthanoneinabsolutevalue
44/107

Because it’s BLUE
TheGauss-MarkowTheorem
| Why do | we use | OLS? |
| ------ | ------ | ---- |
45/107

| Why do | we use | OLS? | Because | it’s BLUE |
| ------ | ------ | ---- | ------- | --------- |
TheGauss-MarkowTheorem
45/107

- Tounderstandwhatthatmeans,let’sreturntotheDartsexample
OLS is the Best Linear Unbiased Estimator
It’snaturaltoaskwhywehavefocusedsomuchonOLS
- Thepracticalansweristhatit’swidelyusedandveryuseful
- ThetheoreticalansweristhatOLShassomenicestatisticalproperties:
- OLSestimatorsareunbiased
- OLSestimatorsarethe“best”amonglinearunbiasedestimators
⇒ TheGauss-Markovtheorem
undercertainassumptions(coveredlater)
46/107

OLS is the Best Linear Unbiased Estimator
It’snaturaltoaskwhywehavefocusedsomuchonOLS
- Thepracticalansweristhatit’swidelyusedandveryuseful
- ThetheoreticalansweristhatOLShassomenicestatisticalproperties:
- OLSestimatorsareunbiased
- OLSestimatorsarethe“best”amonglinearunbiasedestimators
⇒ TheGauss-Markovtheorem
undercertainassumptions(coveredlater)
- Tounderstandwhatthatmeans,let’sreturntotheDartsexample
46/107

The Gauss-Markow Theorem
- RecallthatweusedtheDartshotstorepresent
thesamplingdistributionof βˆ ,andthecenter
j
torepresent β
j
- WealreadydiscussedthatOLSisanunbiased
estimatorofthetruepopulationparameters
- Inotherwords,OLSiseitherstrategy1or2
- Butmanyestimatorsareunbiased. Whatdoesit
meanthatOLSis“best”?
47/107

The Gauss-Markov theorem: OLS is strategy 1
- OLSisthebestbecause,amongunbiasedand
linearestimators,ithasthelowestvariance
- Inotherwords,OLSisthemostaccurate
estimatorof β amongallestimatorsthatare
j
unbiasedandlinear
- TheGauss-Markovtheoremisoneofthemost
importantresultsinstatistics,andit’sakey
reasonforthepopularityofOLS
48/107

| The Gauss-Markov assumptions |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- |
ToprovethatOLSisunbiasedweneedthefollowingassumptions:
MLR.1 Linearity: Thetrue(population)modelis
|                       | y = β +β                               | x +β x +···+β | x +u | (4) |
| --------------------- | -------------------------------------- | ------------- | ---- | --- |
|                       | 0                                      | 1 1 2 2       | k k  |     |
| MLR.2 Randomsampling: | Thedataweobserveisarandomsamplefrom(4) |               |      |     |
MLR.3 Noperfectcollinearity: Noneoftheexplanatoryvariablesareperfectly
correlated
MLR.4 Zeroconditionalmeanoferror: Theerrorhasanexpectedvalueofzerogiven
| anyoftheexplanatoryvariables: |     | E(u|x ,x ,...,x | ) = 0 |     |
| ----------------------------- | --- | --------------- | ----- | --- |
|                               |     | 1 2             | k     |     |
ToprovethatOLSisBLUE(Gauss-Markov),weneedanadditionalassumption:
MLR.5 Homoskedasticity: Theerrorhasthesamevariancegivenanyvalueofthe
σ2
| explanatoryvariables: | var(u|x | ,x ,...,x ) = |     |     |
| --------------------- | ------- | ------------- | --- | --- |
1 2 k
49/107

| Example: | non-linearity | (violation | of  | MLR.4) |     |     |
| -------- | ------------- | ---------- | --- | ------ | --- | --- |
+0.03x2+u,butwetryto
| - Supposethetruepopulationmodelisy |     |     | =   | 100−0.2x |     |     |
| ---------------------------------- | --- | --- | --- | -------- | --- | --- |
1
estimatetheparameterswithoutincludingthequadraticterm.
- Theexpectedvalueofu ispositive(negative)inthetails(middle),soE[u|x 1 ] ̸= 0
- ThemisspecificationmeansthatOLSisbiased
|     |     |     | Population model | SLR model: y=b0+b1*x |     |     |
| --- | --- | --- | ---------------- | -------------------- | --- | --- |
800
600
y 400
200
0
|     |     | −50 | 0   | 50  | 100 | 150 |
| --- | --- | --- | --- | --- | --- | --- |
x
50/107

| Example: | non-constant | variance | (violation | of  | MLR.5) |     |
| -------- | ------------ | -------- | ---------- | --- | ------ | --- |
- Here,thepopulationmodelisy = 0−20x +u andweuseOLStoestimatethissame
model
- Thevarianceofu isincreasinginx,sotheconstanterrorvarianceassumptionis
| wrong,var(u|x | ) ̸= | σ2,meaningthat |     |     |     |     |
| ------------- | ---- | -------------- | --- | --- | --- | --- |
1
- TheheteroskedasticitymeansthatOLSisnolongerBLUE,butit’sstillunbiased
|     |     |     | Population model | SLR model: y=b0+b1 |     |     |
| --- | --- | --- | ---------------- | ------------------ | --- | --- |
5000
4000
3000
y
2000
1000
0
|     |     | 0   | 50  | 100 | 150 | 200 |
| --- | --- | --- | --- | --- | --- | --- |
x
51/107

- Otherusefultransformations:
- Scalebysomeotherfactor,y/z,e.g.,ify =salesyoucouldchoosez =assets.The
benefitofscalingisthatitalsoworkify cantakenegativevalues
√
- y isanotherlessusedalternative
⇒Ingeneral,thinkaboutinwhatscaleyouexpectlinearity
Variance stabilizing transformations
- Thisisoneofthemostcommonmodelviolations—luckily,itisusuallyfixableby
transformingthedependentvariable(y)
- log(y)isthemostcommonvariancestabilizingdatatransformations
- Ify onlytakespositivevalues(e.g.,sales)orisacount(#ofcustomers),takethenatural
logarithm,log(y)
52/107

Variance stabilizing transformations
- Thisisoneofthemostcommonmodelviolations—luckily,itisusuallyfixableby
transformingthedependentvariable(y)
- log(y)isthemostcommonvariancestabilizingdatatransformations
- Ify onlytakespositivevalues(e.g.,sales)orisacount(#ofcustomers),takethenatural
logarithm,log(y)
- Otherusefultransformations:
- Scalebysomeotherfactor,y/z,e.g.,ify =salesyoucouldchoosez =assets.The
benefitofscalingisthatitalsoworkify cantakenegativevalues
√
- y isanotherlessusedalternative
⇒Ingeneral,thinkaboutinwhatscaleyouexpectlinearity
52/107

| Linear | Regression | in Machine | Learning |
| ------ | ---------- | ---------- | -------- |
RidgeandLassoRegression
53/107

Ridge and lasso regression
Ridgeandlassoare
- Examplesofpenalizedregressionmethods,inthat,theyhaveasimilarobjective
functiontoOLS,butridgeaddsanL2penaltyandlassoaddsanL1penaltytothe
objective
- Especiallyusefulwithmanyexplanatoryvariables,i.e.,theyarepreferabletoOLSina
bigdatasetting
- Extremelyusefulinassetpricing. Forexample,wheneverI’mfacingaprediction
problem,e.g.,predictingreturns,earnings,portfolioetc.,Ialwaysstart(andoftenend)
withridgeregression
- Usedasbuildingblocksinothermethodssuchasrandomfeaturesregressionand
neutralnetworks
54/107

Ridge Regression
- ThedifferencebetweenOLSandridge/lassocomesfromtheirobjectivefunction
- TheOLSobjectiveistominimizethesumofsquaredresiduals:
n
∑
| argmin | (yi −[βˆ | +βˆ xi | +···+βˆ xi])2 |     |
| ------ | -------- | ------ | ------------- | --- |
|        |          | 0 1 1  | k k           |     |
βˆ ,βˆ ,...,βˆ ki=1
0 1
- TheridgeobjectiveistominimizethesumofsquaredresidualsandanL penaltythat
2
dependsonthesumofsquaredparameterestimates:
| n                   |          |            |         | k      |
| ------------------- | -------- | ---------- | ------- | ------ |
| ∑ (yi               | −[βˆ +βˆ | xi +···+βˆ | xi])2+λ | ∑ βˆ2, |
| argmin              | 0        | 1          |         |        |
|                     |          | 1          | k k     | j      |
| βˆ ,βˆ ,...,βˆ ki=1 |          |            |         | j=0    |
0 1
whereλisaridgepenaltythatwe’llcomebackto.
- TheL penaltyshrinkstheparameterestimatestowardszero
2
55/107

| Solving the | ridge | regression |     | objective |     |     |     |     |     |
| ----------- | ----- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
- Wecouldsolvetheobjectivenumerically,buttheproblemissolvableinclosed-form
- Tofindthissolution,it’seasiesttoreturntothematrixnotationweusedearlier:
|     |     |     |   |     |  y1 |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
βˆ
|     |     |     | 0       |     |         |     |    | x1      | x1   |
| --- | --- | --- | ------- | --- | ------- | --- | --- | ------- | ----- |
|     |     |     |         |     |         |     | 1   | ...     |       |
|     |     |     |  βˆ   |     |  y 2  |     |     | 1       | k     |
|     |     | βˆ  | 1       |     |         |     |     | . . ... | .     |
|     |     | =   |  .  , | y   | =  .  | , X | =  | . . . . | . .  |
|     |     |     |  .    |     |  .    |     |    |         |      |
|     |     |     |  .    |     |  .    |     |     |         |       |
|     |     |     |         |     |         |     | 1   | xn ...  | xn    |
|     |     |     | βˆ      |     | yn      |     |     | 1       | k     |
k
- Theridgeobjectiveinmatrixnotationis:
|     |     |     |          |     | −Xβˆ)′(y |           |     | ′   |     |
| --- | --- | --- | -------- | --- | -------- | --------- | --- | --- | --- |
|     |     |     | argmin(y |     |          | −Xβˆ)+λβˆ |     | βˆ  |     |
βˆ
56/107

| Solving the | ridge regression | objective |
| ----------- | ---------------- | --------- |
- Thesolutionis:
βˆ = (X′X +λI)−1X′y, (5)
| whereI | isthe(k +1)×(k +1)identitymatrix |     |
| ------ | -------------------------------- | --- |
- ThissolutionisexactlythesameastheOLSsolution,exceptfortheλI part
- Ifλisbig,we’redividingbyalargenumber,whichmakestheparameterestimates
smaller
57/107

Lasso regression
- Lassoregressionisapenalizedregressionmethodlikeridge,butitsobjectivefunction
isslightlydifferent
- InsteadofaddingtheL penaltythatpenalizessquaredparameterestimates,thelasso
2
addstheL penaltythatpenalizesabsoluteparameterestimates:
1
|        | n            |            |         | k      |
| ------ | ------------ | ---------- | ------- | ------ |
|        | ∑            |            |         | ∑      |
| argmin | (yi −[βˆ +βˆ | xi +···+βˆ | xi])2+λ | |βˆ |, |
|        | 0            | 1 1        | k k     | j      |
βˆ ,βˆ ,...,βˆ
| 0 1                                   | ki=1 |     |     | j=0 |
| ------------------------------------- | ---- | --- | --- | --- |
| where|βˆ |justmeanstheabsolutevalueof |      | βˆ  |     |     |
| j                                     |      | j   |     |     |
58/107

Lasso regression
- Similartoridge,thishastheeffectofshrinkingtheestimatestowardszero,but,in
contrasttoridge,lassosetssomeoftheparameterstozero
- That’swhythelassoissometimesinterpretedasavariableselectionmethod
- Thelassoobjectiveisnotdifferentiable,becausethere’sadiscontinuitywhena
parameterestimateswitchessigns,sothere’snoclosed-formsolution
- Nevertheless,there’remanyefficientalgorithmstofindthelassosolution,so,in
practice,findingtheridgeandlassoestimatestakesroughlythesametime
59/107

Elastic net
- Elasticnetisanothermethod,whichcanbeseenasacompromisebetweenridgeand
lasso
- Specifically,theelasticnetobjectiveaddsboththeL (lasso)andL (ridge)penaltyto
1 2
theOLSobjective:
n k
argmin ∑ (yi −[βˆ +βˆ xi +···+βˆ xi])2+λ ∑ ([1−α]βˆ2+α|βˆ |), (6)
0 1 1 k k j j
βˆ 0 ,βˆ 1 ,...,βˆ ki=1 j=0
whereαisanewhyper-parameterthatcontrolstheweightoneachpenalty
- Theelastic-netselectsvariableslikelasso,andshrinkstogetherthecoefficientsof
correlatedexplanatoryvariableslikeridge.
60/107

- Theclassicalstandardizationistosubtractthemeananddividebythestandarddeviation
forallvariables:
xi −x¯
x˜i = j j ,
j sd(x)
j
wherex¯ andsd(x)isthemeanandstandarddeviationofx,respectively
j j j
- Thisstandardizationensuresthatallexplanatoryvariableshaveameanofzeroandavariance
ofone,i.e.,theyareonthesamescale
- Protip:Withfinancialdata,itoftenmakesensetoapplystandardizationmonth-by-month
Practical considerations with ridge/lasso/elastic net
- Ridge,lasso,andelasticnetaresensitivetothescaleoftheinputs
- Forexample,ifyou’repredictingreturnsusingpastreturns(typicalvalue:0.1)andpast
marketequity(typicalvalue:1,000,000,000),thentherawOLSestimatewilldiffer
masivelyinscale,andthepenaltyaffectsthetwoestimatesunequally
- Therefore,alwaysstandardizeyourinputsbeforeusingridge/lasso/elasticnet
61/107

Practical considerations with ridge/lasso/elastic net
- Ridge,lasso,andelasticnetaresensitivetothescaleoftheinputs
- Forexample,ifyou’repredictingreturnsusingpastreturns(typicalvalue:0.1)andpast
marketequity(typicalvalue:1,000,000,000),thentherawOLSestimatewilldiffer
masivelyinscale,andthepenaltyaffectsthetwoestimatesunequally
- Therefore,alwaysstandardizeyourinputsbeforeusingridge/lasso/elasticnet
- Theclassicalstandardizationistosubtractthemeananddividebythestandarddeviation
forallvariables:
xi −x¯
x˜i = j j ,
j sd(x)
j
wherex¯ andsd(x)isthemeanandstandarddeviationofx,respectively
j j j
- Thisstandardizationensuresthatallexplanatoryvariableshaveameanofzeroandavariance
ofone,i.e.,theyareonthesamescale
- Protip:Withfinancialdata,itoftenmakesensetoapplystandardizationmonth-by-month
61/107

| Practical | considerations | with ridge/lasso/elastic | net |
| --------- | -------------- | ------------------------ | --- |
- Whenfittingaridge/lasso/elasticnetmodel,thepenaltyistypicallyonlyappliedto
| βˆ ,...,βˆ | βˆ        |     |     |
| ---------- | --------- | --- | --- |
| 1          | ,butnotto | 0   |     |
k
- Inotherwords,wetypicallydonotapplyshrinkagetotheintercept
- Instead,ifalltheexplanatoryvariableshaveameanofzero,wecanestimatethe
interceptseparatelyasthemeanofthedependentvariable:
n
1 ∑
|     |     | βˆ = y¯ = y |     |
| --- | --- | ----------- | --- |
0 i
n
i=1
- Theremainingparametersareestimatedwitharidgeregressionbyregressingthe
demeaneddependentvariableonthedemeanedexplanatoryvariableswithoutan
intercept(i.e.,weremovethecolumnofonesfromX)
62/107

| Ridge/lasso/elastic | net regression | in R |
| ------------------- | -------------- | ---- |
- Toimplementridge/lasso/elasticnetinR,Itypicallyusetheglmnetpackage
- Thefunctionglmnet()hasanargumentalpha,whichissimilartoαin(6)
- Below,Iuseglmnet()toestimatearidgeregressiononthestockdatawithλ = 0.1
63/107

| Ridge/lasso/elastic | net regression | in R |     |
| ------------------- | -------------- | ---- | --- |
- RidgeshrinkstheestimatestowardszerorelativetoOLS:
|     |     | Method: ols | ridge |
| --- | --- | ----------- | ----- |
etamitse retemaraP
0.01
0.00
−0.01
−0.02
|     | (Intercept)          |                             | rt_lg10 rt_lg11 rt_lg12 |
| --- | -------------------- | --------------------------- | ----------------------- |
|     | rt_lg1 rt_lg2 rt_lg3 | rt_lg4 rt_lg5 rt_lg6 rt_lg7 | rt_lg8 rt_lg9           |
64/107

- Forexample,implementingtheclosed-formsolutionfrom(5)withλ = 0.1doesnot
givethesameestimatesasglmnet(y = y, x = X, alpha = 0, lambda = 0.1)
- Thereasonforthisdiscrepancyisthatglmnet()usesaslightlydifferentobjective
function,andthatitdoesvariousdatatransformationsunderthehood(including
thosewediscussedinthe“Practicalconsiderations”slides)1
- It’snotthatglmnet()ortheclosed-formisinherentlybetter,rather,theyaredifferent
implementationsofthesameunderlyingidea
- Theimportantthingtoremember:Don’tassumethatλfoundusingtheclosedform
solutioncarriesthesamemeaningasλinapackage,suchasglmnet
Ridge/lasso/elastic net regression in R
- Note,glmnet()hasalotofdefaultparameters,meaningthatit’soutputisnot
necessarilywhatyouwouldexpect
1Seethisdiscussionforanexplanation:https://stats.stackexchange.com/questions/129179/
why-is-glmnet-ridge-regression-giving-me-a-different-answer-than-manual-calculat
65/107

- It’snotthatglmnet()ortheclosed-formisinherentlybetter,rather,theyaredifferent
implementationsofthesameunderlyingidea
- Theimportantthingtoremember:Don’tassumethatλfoundusingtheclosedform
solutioncarriesthesamemeaningasλinapackage,suchasglmnet
Ridge/lasso/elastic net regression in R
- Note,glmnet()hasalotofdefaultparameters,meaningthatit’soutputisnot
necessarilywhatyouwouldexpect
- Forexample,implementingtheclosed-formsolutionfrom(5)withλ = 0.1doesnot
givethesameestimatesasglmnet(y = y, x = X, alpha = 0, lambda = 0.1)
- Thereasonforthisdiscrepancyisthatglmnet()usesaslightlydifferentobjective
function,andthatitdoesvariousdatatransformationsunderthehood(including
thosewediscussedinthe“Practicalconsiderations”slides)1
1Seethisdiscussionforanexplanation:https://stats.stackexchange.com/questions/129179/
why-is-glmnet-ridge-regression-giving-me-a-different-answer-than-manual-calculat
65/107

Ridge/lasso/elastic net regression in R
- Note,glmnet()hasalotofdefaultparameters,meaningthatit’soutputisnot
necessarilywhatyouwouldexpect
- Forexample,implementingtheclosed-formsolutionfrom(5)withλ = 0.1doesnot
givethesameestimatesasglmnet(y = y, x = X, alpha = 0, lambda = 0.1)
- Thereasonforthisdiscrepancyisthatglmnet()usesaslightlydifferentobjective
function,andthatitdoesvariousdatatransformationsunderthehood(including
thosewediscussedinthe“Practicalconsiderations”slides)1
- It’snotthatglmnet()ortheclosed-formisinherentlybetter,rather,theyaredifferent
implementationsofthesameunderlyingidea
- Theimportantthingtoremember:Don’tassumethatλfoundusingtheclosedform
solutioncarriesthesamemeaningasλinapackage,suchasglmnet
1Seethisdiscussionforanexplanation:https://stats.stackexchange.com/questions/129179/
why-is-glmnet-ridge-regression-giving-me-a-different-answer-than-manual-calculat
65/107

Choosing Hyper-Parameters
66/107

Parameters vs. Hyper-Parameters
- λandαareso-calledhyper-parameters,buthowdowechoosethem?
- Leadingexample,ridgeregression, βˆridge =(X′X+λI)−1X′y
- Parametersandhyper-parameters:
is:fˆ(Xi) =f(Xi;βˆ) =Xiβˆridge
- Parameterstelluswhatf
- Hyper-parameterstellushowtofindtheparameters,e.g.,λ
- Parametersandhyper-parameters: otherexamples
| Method | Parameters | Hyper-parameters |
| ------ | ---------- | ---------------- |
Penalizedregression Regressioncoefficients,β Penaltyλforlargeβ
| Regressiontree | Treesplits   | Treedepth,etc. |
| -------------- | ------------ | -------------- |
| Neuralnetwork  | Coefficients | Layers,etc.    |
67/107

- Financeandstatisticswithmodelassessment: 2sub-samples
1. In-sample:estimateparameters
2. Out-of-sample:assessperformance
- ML:3sub-samples
1. Train:estimateparametersforeachhyper-parameter
2. Validation:pickthebest-performinghyper-parameter
3. Test:assessperformance
Training, Validation, and Testing
- Oldschoolfinanceandstatistics: 1sample(everythingin-sample)
- Whatwedidinthestockreturnexample.Notgood,asitcanleadtooverfitting
68/107

- ML:3sub-samples
1. Train:estimateparametersforeachhyper-parameter
Validation:pickthebest-performinghyper-parameter
2.
3. Test:assessperformance
| Training, | Validation, | and Testing |
| --------- | ----------- | ----------- |
- Oldschoolfinanceandstatistics: 1sample(everythingin-sample)
- Whatwedidinthestockreturnexample.Notgood,asitcanleadtooverfitting
- Financeandstatisticswithmodelassessment: 2sub-samples
| 1.  | In-sample:estimateparameters    |     |
| --- | ------------------------------- | --- |
| 2.  | Out-of-sample:assessperformance |     |
68/107

| Training, | Validation, | and Testing |
| --------- | ----------- | ----------- |
- Oldschoolfinanceandstatistics: 1sample(everythingin-sample)
- Whatwedidinthestockreturnexample.Notgood,asitcanleadtooverfitting
- Financeandstatisticswithmodelassessment: 2sub-samples
| 1.  | In-sample:estimateparameters    |     |
| --- | ------------------------------- | --- |
| 2.  | Out-of-sample:assessperformance |     |
- ML:3sub-samples
| 1.  | Train:estimateparametersforeachhyper-parameter |     |
| --- | ---------------------------------------------- | --- |
Validation:pickthebest-performinghyper-parameter
2.
| 3.  | Test:assessperformance |     |
| --- | ---------------------- | --- |
68/107

- Whatobservationsgoesintoeachsplit?
- Standard-ML:splitdatarandomlyintotrain/validation/testset
- Financial-ML:bemindfuloftimedimension
| Train-validation-test | with ridge |     |     |     |
| --------------------- | ---------- | --- | --- | --- |
- ML:exampleofridgeregression
| Train:estimateβˆridge | (X′X                | +λI)−1X′y |                 |           |
| --------------------- | ------------------- | --------- | --------------- | --------- |
| 1.                    | (λ) =               |           | foreachλ        |           |
| 2. Validation:pickλˆ  | withsmallloss,e.g., |           |                 |           |
|                       |                     |           | n ∑val(cid:16)  | (cid:17)2 |
|                       | −Xβˆridge           |           | 1 yi −xiβˆridge |           |
|                       | L[y                 | (λˆ)] =   |                 | (λˆ)      |
n
|                           |       |                             | val i=1 |     |
| ------------------------- | ----- | --------------------------- | ------- | --- |
| 3. Re-train:Re-estimateβˆ | forλˆ | withtraining+validationdata |         |     |
Test:assessperformanceofβˆridge(λˆ)
4.
69/107

| Train-validation-test | with ridge |     |     |     |
| --------------------- | ---------- | --- | --- | --- |
- ML:exampleofridgeregression
| Train:estimateβˆridge | (X′X                | +λI)−1X′y |                 |           |
| --------------------- | ------------------- | --------- | --------------- | --------- |
| 1.                    | (λ) =               |           | foreachλ        |           |
| 2. Validation:pickλˆ  | withsmallloss,e.g., |           |                 |           |
|                       |                     |           | n ∑val(cid:16)  | (cid:17)2 |
|                       | −Xβˆridge           |           | 1 yi −xiβˆridge |           |
|                       | L[y                 | (λˆ)] =   |                 | (λˆ)      |
n
|                           |       |                             | val i=1 |     |
| ------------------------- | ----- | --------------------------- | ------- | --- |
| 3. Re-train:Re-estimateβˆ | forλˆ | withtraining+validationdata |         |     |
Test:assessperformanceofβˆridge(λˆ)
4.
- Whatobservationsgoesintoeachsplit?
- Standard-ML:splitdatarandomlyintotrain/validation/testset
- Financial-ML:bemindfuloftimedimension
69/107

| Train-validation-test | split when | time is important |
| --------------------- | ---------- | ----------------- |
- Financial-ML:Bemindfuloftimedimension
- Financepapersoftenkeepthetemporalordersothevalidationsetcomesafterthetrainingset
- Notnecessarilywrongtoreverseorder
- Firstsplitdatainto3temporalsub-samples
1. Train:Firstobservationtovalidationstart
2. Validation:Validationstarttoteststart
3. Test:Teststarttoenddate
- Thenproceedinthesamestepsasbefore:
| 1. Train:estimateβˆ | foreachλinthetrainingsample |     |
| ------------------- | --------------------------- | --- |
2. Validation:pickthebest-performingλˆ
Re-train:estimateβˆ forλˆ
| 3.  | intraining+validationsample |     |
| --- | --------------------------- | --- |
4. Test:assessperformance
70/107

- Q:Whatisthebenefitofusinganexpandingvsrollingvsfixedsplit?
Rolling or expanding windows
Infinance,peopleoftenusearollingorexpandingtrainingset
- Expanding:alwaysstartfromthebeginningofthesample
- Rolling:Useafixednumberofyears(discardingtheoldestdata)
Illustrationofexpandingtrainingset:
71/107

Rolling or expanding windows
Infinance,peopleoftenusearollingorexpandingtrainingset
- Expanding:alwaysstartfromthebeginningofthesample
- Rolling:Useafixednumberofyears(discardingtheoldestdata)
Illustrationofexpandingtrainingset:
- Q:Whatisthebenefitofusinganexpandingvsrollingvsfixedsplit?
71/107

Cross-Validation
- K-foldcross-validation
- Datascarce–wanttousefulltrain+validationsampleforboth
- Splittrain+validationsampleintoK folds(subsets),butnote
- NoteK isnotthesameasthenumberofexplanatoryvariablesk
- Standardcross-validationdistributeobservationstodifferentfoldsrandomly
- Financialcross-validationdistributeobservationsfromthesamedatetothesamefold(toavoid
look-aheadbias)
- Example:5-foldvalidation
Data
| Split1 Validate | Train Train    | Train Train    |
| --------------- | -------------- | -------------- |
| Split2 Train    | Validate Train | Train Train    |
| Split3 Train    | Train Validate | Train Train    |
| Split4 Train    | Train Train    | Validate Train |
| Split5 Train    | Train Train    | Train Validate |
- Method:
1. Traink times:Foreachsplitj andeachhyper-parameter
- estimateparametersusingtrainingdatainallfolds,exceptj
- computelossinj’thfold,i.e.,thej’thvalidationperiod
2. Cross-validate:Choosehyper-parameters
- thatminimizelossacrossallvalidationperiods
3. Retrain:estimateparametersusingfulltrain+validationdata
Test:assessperformance(asalways)
4. 72/107

| How can | Ridge/Lasso | beat OLS? |
| ------- | ----------- | --------- |
TheBias-VarianceTradeoff
73/107

Notnecessarily
- Ridgeandlassoregressionsarebiasedestimators,sothey’renotintheclassof
unbiasedpredictors
- Butwhyonearthwouldweuseabiasedpredictor?
- Becauseofthebias-variancetradeoff
Wait wasn’t OLS literally the best!?
- TheGauss-Markowtheoremstatedthat,undercertainassumptions,OLSisthe
bestlinearunbiasedestimator
- Ridgeandlassoarelinearpredictors,soaretheyworsethanOLS?
74/107

- Butwhyonearthwouldweuseabiasedpredictor?
- Becauseofthebias-variancetradeoff
Wait wasn’t OLS literally the best!?
- TheGauss-Markowtheoremstatedthat,undercertainassumptions,OLSisthe
bestlinearunbiasedestimator
- Ridgeandlassoarelinearpredictors,soaretheyworsethanOLS?Notnecessarily
- Ridgeandlassoregressionsarebiasedestimators,sothey’renotintheclassof
unbiasedpredictors
74/107

- Becauseofthebias-variancetradeoff
Wait wasn’t OLS literally the best!?
- TheGauss-Markowtheoremstatedthat,undercertainassumptions,OLSisthe
bestlinearunbiasedestimator
- Ridgeandlassoarelinearpredictors,soaretheyworsethanOLS?Notnecessarily
- Ridgeandlassoregressionsarebiasedestimators,sothey’renotintheclassof
unbiasedpredictors
- Butwhyonearthwouldweuseabiasedpredictor?
74/107

| Wait wasn’t | OLS literally | the best!? |
| ----------- | ------------- | ---------- |
- TheGauss-Markowtheoremstatedthat,undercertainassumptions,OLSisthe
bestlinearunbiasedestimator
- Ridgeandlassoarelinearpredictors,soaretheyworsethanOLS?Notnecessarily
- Ridgeandlassoregressionsarebiasedestimators,sothey’renotintheclassof
unbiasedpredictors
- Butwhyonearthwouldweuseabiasedpredictor?
| - Becauseofthebias-variancetradeoff |     |     |
| ----------------------------------- | --- | --- |
74/107

The bias-variance tradeoff in darts
- WhenwecoveredtheDartsexampleearlier,itwasprettyclearthatwepreferred
Strategy1,whichwasbothcorrectonaverage(lowbias)andaccurate(lowvariance)
- However,sometimesthestrategywiththelowestbias,isnotthestrategywiththe
lowestvariance,andwefacethebias-variancetradeoff
- Forexample,whichstrategydoyouprefer?
75/107

The bias-variance tradeoff
- Let’sstartbydefiningtheprediction,outcome,anderrorasgeneralfunctionsofx:
- Prediction:yˆi =fˆ(xi)
- Outcome:yi =f(xi)+ui
- Predictionerror:uˆi =yi −yˆi,
where
- f(xi)istheexpectedvalueunderthepopulationmodel
- fˆ(xi)isyourestimatedpredictionrule
- ui isthepopulationerror
- uˆi istheresidual
76/107

- Butf(xi)couldalsobeacomplexnon-linearfunctionandfˆ(xi)aneuralnetwork
The bias-variance tradeoff
- Forconcreteness,iftheSLRmodelholdinthepopulation,then:
f(xi) = β +β xi,
0 1
andfˆ(xi)couldbetheOLSpredictionrule:
fˆ(xi) = βˆ +βˆ xi
0 1
77/107

The bias-variance tradeoff
- Forconcreteness,iftheSLRmodelholdinthepopulation,then:
f(xi) = β +β xi,
0 1
andfˆ(xi)couldbetheOLSpredictionrule:
fˆ(xi) = βˆ +βˆ xi
0 1
- Butf(xi)couldalsobeacomplexnon-linearfunctionandfˆ(xi)aneuralnetwork
77/107

The bias-variance tradeoff
- Itturnsoutthattheexpectedsquaredpredictionerror,(thinkmean-squarederror),
dependsonbias,variance,andarandomerror:
| E[(predictionerror)2] E[(yi | −yˆi)2] |     |     |     |
| --------------------------- | ------- | --- | --- | --- |
=
| = E[(f(xi)+ui |     | −fˆ(xi))2] |     |     |
| ------------- | --- | ---------- | --- | --- |
= E[(f(xi)−fˆ(xi))2]+σ2
E[f(xi)−fˆ(xi)]2+Var[f(xi)−fˆ(xi)]+σ2
=
| = E[f(xi)−fˆ(xi)]2 |     | +   | Var[fˆ(xi)] | + σ2 |
| ------------------ | --- | --- | ----------- | ---- |
(cid:124)(cid:123)(cid:122)(cid:125)
| (cid:124) | (cid:123)(cid:122) | (cid:125) | (cid:124) (cid:123)(cid:122) | (cid:125)   |
| --------- | ------------------ | --------- | ---------------------------- | ----------- |
|           | bias2              |           | variance                     | randomerror |
- Apredictionrulecan’tavoidtherandomerror,butcanreducebiasandvariance
- Manypredictionruleshavezerobias,suchasOLS,butiftherulehashighvarianceit
canbeoutperformedbyabiasedalternative,suchasridge
78/107

Becausethat’stheOLSsolution
- Similarly,pickingλ = ∞leadstoavarianceofzero. Why? Becausecoefficients
becomezeroregardlessofdata,i.e.,predictionsdoesn’tdependonsample
| Example: | Bias-variance | tradeoff | for ridge | regression |
| -------- | ------------- | -------- | --------- | ---------- |
- Thehyper-parameterλcontrolsthebias-variancetradeoffforridge
- Toseethis,considertheridgesolution:
|            |                        | βˆridge | (X′X  | +λI)−1X′y |
| ---------- | ---------------------- | ------- | ----- | --------- |
|            |                        |         | (λ) = |           |
| - Pickingλ | = 0makesridgeunbiased. |         | Why?  |           |
79/107

- Similarly,pickingλ = ∞leadstoavarianceofzero. Why? Becausecoefficients
becomezeroregardlessofdata,i.e.,predictionsdoesn’tdependonsample
| Example: | Bias-variance | tradeoff | for ridge | regression |
| -------- | ------------- | -------- | --------- | ---------- |
- Thehyper-parameterλcontrolsthebias-variancetradeoffforridge
- Toseethis,considertheridgesolution:
|     |     | βˆridge | (X′X  | +λI)−1X′y |
| --- | --- | ------- | ----- | --------- |
|     |     |         | (λ) = |           |
- Pickingλ = 0makesridgeunbiased. Why? Becausethat’stheOLSsolution
79/107

Becausecoefficients
becomezeroregardlessofdata,i.e.,predictionsdoesn’tdependonsample
| Example: | Bias-variance | tradeoff | for ridge | regression |
| -------- | ------------- | -------- | --------- | ---------- |
- Thehyper-parameterλcontrolsthebias-variancetradeoffforridge
- Toseethis,considertheridgesolution:
βˆridge (X′X +λI)−1X′y
(λ) =
- Pickingλ = 0makesridgeunbiased. Why? Becausethat’stheOLSsolution
| - Similarly,pickingλ |     | = ∞leadstoavarianceofzero. |     | Why? |
| -------------------- | --- | -------------------------- | --- | ---- |
79/107

| Example: | Bias-variance | tradeoff | for ridge | regression |
| -------- | ------------- | -------- | --------- | ---------- |
- Thehyper-parameterλcontrolsthebias-variancetradeoffforridge
- Toseethis,considertheridgesolution:
|     |     | βˆridge | (X′X  | +λI)−1X′y |
| --- | --- | ------- | ----- | --------- |
|     |     |         | (λ) = |           |
- Pickingλ = 0makesridgeunbiased. Why? Becausethat’stheOLSsolution
- Similarly,pickingλ = ∞leadstoavarianceofzero. Why? Becausecoefficients
becomezeroregardlessofdata,i.e.,predictionsdoesn’tdependonsample
79/107

| Adjusted | Standard | Errors | for Correlated | Data |
| -------- | -------- | ------ | -------------- | ---- |
80/107

Financial data is not IID
- InderivingthesamplingdistributionsfortheOLSestimators,weassumedthatthe
populationerroru wasarandomvariablefromanunderlyingnormaldistributionwith
ameanofzeroandvarianceofσ2
- Inotherwords,weassumedthatu wasindependentlyandidenticallydistributed(IID)
acrossobservations
- Inreality,thisassumptionisfrequentlyviolatedinfinancialdata
- Forexample,thereturnsofS&P500stocksinOctober-2008(onsetofthefinacial
crisis)wasnotIID:Moststockshadnegativereturns,andbankingstockswere
especiallyaffected
81/107

Why the IID assumption matters
- Intuitively,thesamplingdistributiontellsusabouttheaccuracyofourestimates,and
ourestimateswillbemoreaccurateifeachdatapointprovideindependentinformation
- Toseethis,supposeyouobservenobservationsofavariablex,andcomputeitsmean
1
x¯ = (x +x +···+x )
1 2 n
n
- Tounderstandhowaccuratethismeanestimatesthetruepopulationmean,wecan
computeitsstandarderror
- IftheobservationsareIID,thestandarderroris
(cid:114)
var(x) sd(x)
se(x¯) = = √ ,
n n
so,goingfrom,say,4to16obscutsthestandarderrorinhalf,ifreturnsareIID
82/107

- It’sunclearfornow,butwecanguess
- Usingn =4feelstoohigh,sincethereturnsoftheAandBshareinthesamemonthare
clearlynotindependent
- Ontheotherhand,n =1feelstoolow,becausereturnsinOctoberandNovemberare
closetoindependent
- Somethingliken =2,feelsappealingbecuasereturnswithitsconsistentwithperfect
correlationwithinamonth,andnocorrelationacrossmonths
| Why the | IID assumption | matters |     |     |
| ------- | -------------- | ------- | --- | --- |
- Now,supposex isthereturnofGoogle’sAandBshareforOct-2008andNov-2008:
1
|     |     | r¯ = (rA | +rB +rA | +rB )   |
| --- | --- | -------- | ------- | ------- |
|     |     |          | oct oct | nov nov |
4
- Whatistheappropriateninthestandarderrorformula?
sd(r)
|     |     |     | se(r¯) = √ | ,   |
| --- | --- | --- | ---------- | --- |
n
83/107

| Why the | IID assumption | matters |     |     |
| ------- | -------------- | ------- | --- | --- |
- Now,supposex isthereturnofGoogle’sAandBshareforOct-2008andNov-2008:
1
|     |     | r¯ = (rA | +rB +rA | +rB )   |
| --- | --- | -------- | ------- | ------- |
|     |     |          | oct oct | nov nov |
4
- Whatistheappropriateninthestandarderrorformula?
sd(r)
|     |     |     | se(r¯) = √ | ,   |
| --- | --- | --- | ---------- | --- |
n
- It’sunclearfornow,butwecanguess
- Usingn =4feelstoohigh,sincethereturnsoftheAandBshareinthesamemonthare
clearlynotindependent
- Ontheotherhand,n =1feelstoolow,becausereturnsinOctoberandNovemberare
closetoindependent
- Somethingliken =2,feelsappealingbecuasereturnswithitsconsistentwithperfect
correlationwithinamonth,andnocorrelationacrossmonths
83/107

| Methods | for adjusting | standard | errrors |
| ------- | ------------- | -------- | ------- |
- There’reseveralmethodstoadjustyourstandarderrorswhentheIIDassumptionis
violated
- Typicaladjustmentmethodsthatyou’llaccountinfinanceincludes:
| 1.  | Fama-MacBethregressions |     |     |
| --- | ----------------------- | --- | --- |
| 2.  | Clusteredstandarderrors |     |     |
| 3.  | TheNewey-Westadjustment |     |     |
- I’mgoingtocover1and2,focusingonpracticalimplementationratherthan
theoreticalunderpinning
- WeuseFama-MacBethandclusteredstandarderrorsforpaneldata(e.g,returnsofmany
asssetovertime),andtheNewey-Westadjustmentifwehaveasingletime-series(e.g.,
returnofoneassetovertime)
| -   | Foramorerigoroustreatment,IrecommendPetersen(2009) |     |     |
| --- | -------------------------------------------------- | --- | --- |
84/107

Typical residual dependence in financial data
- Typicalresidualdependenceinfinancialdata:
- Timeeffect:Residualsarecorrelatedacrossfirmswithinthesametimeperiod
- Oftenthecaseforassetreturndata
- Firmeffect:Residualsarecorrelatedacrosstimewithinthesamefirm
- Oftenthecasewhenyouregressonepersistentfirmvariable(e.g.,price-earningratio)on
anotherpersistentfirmvariable(e.g.,leverage)
- Fama-MacBethworkswellwhenthere’satimeeffect,butnofirmeffect
- Clusteredstandarderrorsareamoreflexiblewayofhandlingeitheratimeeffect,a
firmeffect,orboth
85/107

| Method | 1: Fama-MacBeth | regressions |
| ------ | --------------- | ----------- |
- Fama-MacBethregressionsareusedwhenobservationsarecorrelatedacross
observationswithinatimeperiod,but(approximately)uncorrelatedacrosstime
periods
|     | - Example:Individualstockreturns |     |
| --- | -------------------------------- | --- |
- Theprocedureisstraightforward: Insteadofestimatingoneregressionbypoolingall
stocksandtimeperiods,weestimateseparateregressionforeachtimeperiodand
averagetheseestimatesovertime
86/107

It’sthestandarderrorofthemeanwithIID
observations,soitassumesthat βˆt isindependentovertime
j
Method 1: Fama-MacBeth regressions
TheFama-MacBethalgorithm:
1. Estimatearegressioneachtime-period:
yi = βˆt +βˆtxi +uˆi, fort = 1,2...,T
t 0 1 t t
2. ComputeFama-MacBethcoefficientestimatesbyaveragingacrosstime:
βˆFMB = 1 ∑ T βˆt
j T j
t=1
3. Standarderrorofestimates:
sd(βˆt)
se(βˆFMB) = √ j
j
T
Noticesomethingaboutthisformula?
87/107

Method 1: Fama-MacBeth regressions
TheFama-MacBethalgorithm:
1. Estimatearegressioneachtime-period:
yi = βˆt +βˆtxi +uˆi, fort = 1,2...,T
t 0 1 t t
2. ComputeFama-MacBethcoefficientestimatesbyaveragingacrosstime:
βˆFMB = 1 ∑ T βˆt
j T j
t=1
3. Standarderrorofestimates:
sd(βˆt)
se(βˆFMB) = √ j
j
T
Noticesomethingaboutthisformula? It’sthestandarderrorofthemeanwithIID
observations,soitassumesthat βˆt isindependentovertime
j
87/107

Method 2: Clustered standard errors
- Clusteredstandarderrorsareamoreflexiblewayofhandlingatimeeffect,firmeffect,
orboth
- Theyworkby“clustering”yourstandarderrorsatthelevelwhereyouexpectresidual
dependence. So,forexample,ifyouexpectresidualtobecorrelatedwithinthesame
timeperiod(atimeeffect)youshouldclusterbytime
- Fama-MacBethissimilartoclusteringstandarderrorsbytime
88/107

| Clustered | standard | errors | in R |
| --------- | -------- | ------ | ---- |
- ClusteredstandarderrorsareeasytogetinRwiththefelm()functionfromthelfe
package
- Thefirstargumenttothefelm()functioniscalledformulaanditsreallya
combinationoffourinputsseparatedby“|”:
formula: y ∼ x1 +...+ xk | dum1 +... + dumN | IV | clus1 +...+ clusZ
- They ∼ x1 +...+ xkpartspecifiestheregressioninthesamewayaslm()
| -   | Thedum1 +...                                             | + dumNlet’syouincludedifferentdummyvariables |     |
| --- | -------------------------------------------------------- | -------------------------------------------- | --- |
| -   | TheIVpartstandsforinstrumentalvariable,whichwewon’tcover |                                              |     |
| -   | Theclus1 +...+                                           | clusZletsyouspecifytheclustervariables       |     |
| -   | Ifyournotusingaspecificargument,justsetitto0             |                                              |     |
- Fortheregressionofreturnattonreturnatt-1,withclusteringbytime:
felm(formula = rt∼rt_lg1 | 0 | 0 | eom, data = stock_returns)
89/107

- Clusterbytime: summary(felm(rt∼rt lg1|0|0|eom, data=stock returns))
- Clusterbyfirm: summary(felm(rt∼rt lg1|0|0|permno, data=stock returns))
|     |     |     |     |     | - Clusterbytime+firm: | summary(felm(rt∼rt | lg1|0|0|eom+permno, |
| --- | --- | --- | --- | --- | --------------------- | ------------------ | ------------------- |
data=stock returns))
- Rule-of-thumb: Ifclusteringmakesabigdifference,youshouldprobablyuseit
| Clustering | adjustment | can make | a big inferential | difference |     |     |     |
| ---------- | ---------- | -------- | ----------------- | ---------- | --- | --- | --- |
summary(lm(rt∼rt
| - Noadjustment: |     |     | lg1, data=stock | returns)) |     |     |     |
| --------------- | --- | --- | --------------- | --------- | --- | --- | --- |
90/107

- Clusterbyfirm: summary(felm(rt∼rt lg1|0|0|permno, data=stock returns))
|     |     |     |     |     | - Clusterbytime+firm: | summary(felm(rt∼rt | lg1|0|0|eom+permno, |
| --- | --- | --- | --- | --- | --------------------- | ------------------ | ------------------- |
data=stock returns))
- Rule-of-thumb: Ifclusteringmakesabigdifference,youshouldprobablyuseit
| Clustering | adjustment | can make | a big inferential | difference |     |     |     |
| ---------- | ---------- | -------- | ----------------- | ---------- | --- | --- | --- |
summary(lm(rt∼rt
| - Noadjustment: |     |     | lg1, data=stock | returns)) |     |     |     |
| --------------- | --- | --- | --------------- | --------- | --- | --- | --- |
- Clusterbytime: summary(felm(rt∼rt lg1|0|0|eom, data=stock returns))
90/107

|     |     |     |     |     | - Clusterbytime+firm: | summary(felm(rt∼rt | lg1|0|0|eom+permno, |
| --- | --- | --- | --- | --- | --------------------- | ------------------ | ------------------- |
data=stock returns))
- Rule-of-thumb: Ifclusteringmakesabigdifference,youshouldprobablyuseit
| Clustering | adjustment | can make | a big inferential | difference |     |     |     |
| ---------- | ---------- | -------- | ----------------- | ---------- | --- | --- | --- |
summary(lm(rt∼rt
| - Noadjustment: |     |     | lg1, data=stock | returns)) |     |     |     |
| --------------- | --- | --- | --------------- | --------- | --- | --- | --- |
- Clusterbytime: summary(felm(rt∼rt lg1|0|0|eom, data=stock returns))
- Clusterbyfirm: summary(felm(rt∼rt lg1|0|0|permno, data=stock returns))
90/107

- Rule-of-thumb: Ifclusteringmakesabigdifference,youshouldprobablyuseit
| Clustering | adjustment | can make | a big inferential | difference |
| ---------- | ---------- | -------- | ----------------- | ---------- |
summary(lm(rt∼rt
| - Noadjustment: |     |     | lg1, data=stock | returns)) |
| --------------- | --- | --- | --------------- | --------- |
- Clusterbytime: summary(felm(rt∼rt lg1|0|0|eom, data=stock returns))
- Clusterbyfirm: summary(felm(rt∼rt lg1|0|0|permno, data=stock returns))
| - Clusterbytime+firm: |           | summary(felm(rt∼rt | lg1|0|0|eom+permno, |     |
| --------------------- | --------- | ------------------ | ------------------- | --- |
| data=stock            | returns)) |                    |                     |     |
90/107

| Clustering | adjustment | can make | a big inferential | difference |
| ---------- | ---------- | -------- | ----------------- | ---------- |
summary(lm(rt∼rt
| - Noadjustment: |     |     | lg1, data=stock | returns)) |
| --------------- | --- | --- | --------------- | --------- |
- Clusterbytime: summary(felm(rt∼rt lg1|0|0|eom, data=stock returns))
- Clusterbyfirm: summary(felm(rt∼rt lg1|0|0|permno, data=stock returns))
| - Clusterbytime+firm: |           | summary(felm(rt∼rt | lg1|0|0|eom+permno, |     |
| --------------------- | --------- | ------------------ | ------------------- | --- |
| data=stock            | returns)) |                    |                     |     |
- Rule-of-thumb: Ifclusteringmakesabigdifference,youshouldprobablyuseit
90/107

| Adjusting | standard | errors | in practice |
| --------- | -------- | ------ | ----------- |
91/107

| Adjusting | standard | errors | in practice |
| --------- | -------- | ------ | ----------- |
92/107

Another typical IID violation: Heteroskedasticity
- TheIIDassumptionalsoimpliesthatu hasaconstantvarianceσforallobservations
(homoskedasticity),butthealternative,heteroskedasticity,ismustmorecommonin
financialdata.
- Forexample,theplotbelowshowsthestandarddeviationwithineachmonthforthe
500stocksfromthestock. Homoskedasticityimpliesthatthisnumberisconstant
overtime,whichisclearlynotthecase:
0.25
0.20
0.15
0.10
0.05
1980 1990 2000 2010 2020
snruter
kcots
fo
DS
lanoitces−ssorC
- Luckily,themethodswe’vecoveredalsoaccountforheteroskedasticity
93/107

| Model | selection: | Simplicity | versus | Complexity |
| ----- | ---------- | ---------- | ------ | ---------- |
94/107

- Financehaslongfavoredsimplemodels,suchasequityfactors,whichareessentially
simplelinearregressions
- ThefocusonsimplemethodscanbemotivatedfromOccam’sRazorwhich,loosely
speaking,saysthat
Occam’srazor
Thesimplestmodelthatfitsthedataisalsothemostplausible
QuotefromthebookLearningfromData
The Virtue of Simplicity
- Shouldyouuseasimplemodel,suchassimplelinearregression,oracomplexmodel,
suchaselasticnetwithmanyexplanatoryvariables?
95/107

- ThefocusonsimplemethodscanbemotivatedfromOccam’sRazorwhich,loosely
speaking,saysthat
Occam’srazor
Thesimplestmodelthatfitsthedataisalsothemostplausible
QuotefromthebookLearningfromData
The Virtue of Simplicity
- Shouldyouuseasimplemodel,suchassimplelinearregression,oracomplexmodel,
suchaselasticnetwithmanyexplanatoryvariables?
- Financehaslongfavoredsimplemodels,suchasequityfactors,whichareessentially
simplelinearregressions
95/107

The Virtue of Simplicity
- Shouldyouuseasimplemodel,suchassimplelinearregression,oracomplexmodel,
suchaselasticnetwithmanyexplanatoryvariables?
- Financehaslongfavoredsimplemodels,suchasequityfactors,whichareessentially
simplelinearregressions
- ThefocusonsimplemethodscanbemotivatedfromOccam’sRazorwhich,loosely
speaking,saysthat
Occam’srazor
Thesimplestmodelthatfitsthedataisalsothemostplausible
QuotefromthebookLearningfromData
95/107

The Virtue of Complexity
- Morerecently,therehasbeenapushtowardsmorecomplexmodel,andBryanKelly,
SemyonMalamud,andKangyingZhou(2024)arguesforthevirtueofcomplexity:
96/107

- A:Notreally. Occam’srazorsaysthatthesimplestmodelthatfitsthedataisalsothe
mostplausible
- Hence,Occam’srazoronlyreallytellsustopickthesimplermodelifitperformsaswellas
thecomplexone,notwhattodoifthecomplexmodelworksbetter
- Similarly,aquoteoftenattributedtoEinsteinis
Anexplanationofthedatashouldbemadeassimpleaspossible,butnosimpler
- Mypoint: Occam’srazorprovidelimitedguidanceforpickingthebestpredictionrule,
andyoushouldinsteadrelyonempiricalexperiments. Importantly,complexmodels
“always”dobetterin-samplesoit’scrucialtotestonout-of-sampledata
Simplicity vs. Complexity
- Q:IsthevirtueofcomplexityinconsistentwithOccam’srazor?
97/107

- Similarly,aquoteoftenattributedtoEinsteinis
Anexplanationofthedatashouldbemadeassimpleaspossible,butnosimpler
- Mypoint: Occam’srazorprovidelimitedguidanceforpickingthebestpredictionrule,
andyoushouldinsteadrelyonempiricalexperiments. Importantly,complexmodels
“always”dobetterin-samplesoit’scrucialtotestonout-of-sampledata
Simplicity vs. Complexity
- Q:IsthevirtueofcomplexityinconsistentwithOccam’srazor?
- A:Notreally. Occam’srazorsaysthatthesimplestmodelthatfitsthedataisalsothe
mostplausible
- Hence,Occam’srazoronlyreallytellsustopickthesimplermodelifitperformsaswellas
thecomplexone,notwhattodoifthecomplexmodelworksbetter
97/107

- Mypoint: Occam’srazorprovidelimitedguidanceforpickingthebestpredictionrule,
andyoushouldinsteadrelyonempiricalexperiments. Importantly,complexmodels
“always”dobetterin-samplesoit’scrucialtotestonout-of-sampledata
Simplicity vs. Complexity
- Q:IsthevirtueofcomplexityinconsistentwithOccam’srazor?
- A:Notreally. Occam’srazorsaysthatthesimplestmodelthatfitsthedataisalsothe
mostplausible
- Hence,Occam’srazoronlyreallytellsustopickthesimplermodelifitperformsaswellas
thecomplexone,notwhattodoifthecomplexmodelworksbetter
- Similarly,aquoteoftenattributedtoEinsteinis
Anexplanationofthedatashouldbemadeassimpleaspossible,butnosimpler
97/107

Simplicity vs. Complexity
- Q:IsthevirtueofcomplexityinconsistentwithOccam’srazor?
- A:Notreally. Occam’srazorsaysthatthesimplestmodelthatfitsthedataisalsothe
mostplausible
- Hence,Occam’srazoronlyreallytellsustopickthesimplermodelifitperformsaswellas
thecomplexone,notwhattodoifthecomplexmodelworksbetter
- Similarly,aquoteoftenattributedtoEinsteinis
Anexplanationofthedatashouldbemadeassimpleaspossible,butnosimpler
- Mypoint: Occam’srazorprovidelimitedguidanceforpickingthebestpredictionrule,
andyoushouldinsteadrelyonempiricalexperiments. Importantly,complexmodels
“always”dobetterin-samplesoit’scrucialtotestonout-of-sampledata
97/107

Example: Using advanced topics in linear regression to build optimal
| portfolios | with trading | costs |
| ---------- | ------------ | ----- |
98/107

| Machine | Learning | and the | Implementable | Efficient | Frontier |
| ------- | -------- | ------- | ------------- | --------- | -------- |
99/107

| Motivation: | ML and | Implementable | Portfolios |
| ----------- | ------ | ------------- | ---------- |
- MLmodelsaregreatatpredictingstockreturns
| - Forexample,Guetal.(2020) |     |     |     |
| -------------------------- | --- | --- | --- |
- ButmostMLpapersignoretradingcosts,implyingunrealistic
| - profitsfromilliquidstocks(Avramovetal.,2023)              |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- |
| - keycharacteristics,e.g.short-termreversal(Chenetal.,2023) |     |     |     |
- Questions:
| - CaninvestorsbenefitfromMLaftert-costs?             |     |     |     |
| ---------------------------------------------------- | --- | --- | --- |
| - Whichsignalshavegreatesteconomicfeatureimportance? |     |     |     |
| - Lessonsforassetpricing?                            |     |     |     |
100/107

| What We | Do: Theory-Guided | ML  |
| ------- | ----------------- | --- |
- Weintroducethe“Implementableefficientfrontier”(IEF)
| -   | After-cost,out-of-sampleversionofstandardefficientfrontier |     |
| --- | ---------------------------------------------------------- | --- |
- Weshowthat
| -   | StandardMLimplementationsleadstoapoorIEF |     |
| --- | ---------------------------------------- | --- |
| -   | Newtheory-guidedMLleadstoapowerfulIEF    |     |
| -   | Economicfeatureimportance:               |     |
- QualityandValue:largeimpactontheIEF
- Short-TermReversal:limitedimpactforalargeinvestor
101/107

Model
- Setup
| - N riskyassets,tradedattimest |     |     | =0,1,... |     |     |     |     |
| ------------------------------ | --- | --- | -------- | --- | --- | --- | --- |
- Eachassetshascharacteristicvectors
i,t
- Returnspredictablebygeneralfunctionofcharacteristics,E [r ] = µ(s )
|             |                     |     |     |         |     |     | t i,t+1 i,t |
| ----------- | ------------------- | --- | --- | ------- | --- | --- | ----------- |
| - Trades,τt | ,havemarketimpactof |     |     | 1 Λ tτt |     |     |             |
2
| - Investorsobjective: |     | Mean-varianceutilitywithriskaversionγ: |            |     |     |     |     |
| --------------------- | --- | -------------------------------------- | ---------- | --- | --- | --- | --- |
| - Chooseportfolioπt   |     | forallt                                | tomaximize |     |     |     |     |
1 T
|     |     | utility=     | l im ∑  | [return     | (πt )−TC | (πt,πt−1 | )−risk (πt )]    |
| --- | --- | ------------ | ------- | ----------- | -------- | -------- | ---------------- |
|     |     |              | ∞T      | t+1         |          | t        | t+1              |
|     |     |              | T → t = | 1           |          |          |                  |
|     |     | =E (cid:104) | )′πt w  |             | )′Λ(πt   |          | γ ′Σπt (cid:105) |
|     |     |              | µ(st −  | (πt −gtπt−1 |          | −gtπt−1  | )− π t ,         |
|     |     |              | 2       |             |          |          | 2                |
102/107

| Key Result: | Optimal |     | Strategy |     |     |     |     |
| ----------- | ------- | --- | -------- | --- | --- | --- | --- |
Proposition(Optimaldynamicstrategy):
Thesolutiontotheportfolioproblemis
|     |     |     | =   | +(I−m)A    |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     | π t | mg t π t−1 |     | t   |     |
withaimportfolioA
t
|     |     |     |     | ∞   | (cid:20) |     | (cid:21) |
| --- | --- | --- | --- | --- | -------- | --- | -------- |
1
|     |     |     | = (I−m)−1 | ∑ (mg¯)τcE |     | Σ−1µ(s | )   |
| --- | --- | --- | --------- | ---------- | --- | ------ | --- |
|     |     | A t |           |            | t   |        | t+τ |
γ
τ=0
|        |              |     |                  |     | (cid:124) | (cid:123)(cid:122) | (cid:125) |
| ------ | ------------ | --- | ---------------- | --- | --------- | ------------------ | --------- |
|        |              |     |                  |     |           | Markowitz          | t+τ       |
| wherec | = γmΛ−1Σandm |     | giveninthepaper. |     |           |                    |           |
w
103/107

Closed-formsolutiontoextremelyhardproblem!
-
| Implementing        | key | result: Portfolio-ML                    |        |      |
| ------------------- | --- | --------------------------------------- | ------ | ---- |
| - TofindtheoptimalA |     | t ,weproposealinearparametricportfolio: |        |      |
|                     |     | APortfolio-ML                           | =      | ∈ Rp |
|                     |     |                                         | s t β, | β    |
t
- Maximizingutilitywiththisparameterizationleadsto:
βˆ [Σ˜ ])−1E
|     |     | =   | (E    | [r˜ ] |
| --- | --- | --- | ----- | ----- |
|     |     |     | T t T | t+1   |
[Σ˜
| whereE | t ]andE | [r˜ t+1 ]canbecomputedfromobserveddata |     |     |
| ------ | ------- | -------------------------------------- | --- | --- |
T T
104/107

| Implementing        | key | result: Portfolio-ML                    |        |      |
| ------------------- | --- | --------------------------------------- | ------ | ---- |
| - TofindtheoptimalA |     | t ,weproposealinearparametricportfolio: |        |      |
|                     |     | APortfolio-ML                           | =      | ∈ Rp |
|                     |     |                                         | s t β, | β    |
t
- Maximizingutilitywiththisparameterizationleadsto:
βˆ [Σ˜ ])−1E
|     |     | =   | (E    | [r˜ ] |
| --- | --- | --- | ----- | ----- |
|     |     |     | T t T | t+1   |
[Σ˜
| whereE | t ]andE | [r˜ t+1 ]canbecomputedfromobserveddata |     |     |
| ------ | ------- | -------------------------------------- | --- | --- |
T T
- Closed-formsolutiontoextremelyhardproblem!
104/107

Implementing key result: Portfolio-ML
- Weaddacoupleof“MLmodifications”tothelinearsolution
1. MLmodification1:Addridgepenaltychosenviacross-validation
2. MLmodification2:Userandomfeaturestransformtocreateanon-linearparametric
portfolio
AP
t
ortfolio-ML =RF(s
n,t
)β
- βˆ stillhasaclosed-formsolution,thatisnowregularizedbytheridgepenaltyand
capturesnon-linearitiesviatheRFtransform
105/107

The Implementable Efficient Frontier
0.4
Without TC
0.2
Static−ML (one layer)
0.0
−0.2
0.0 0.1 0.2 0.3
Volatility
)tsoc
gnidart
fo
ten(
snruter
ssecxE
Portfolio−ML Static−ML* Factor−ML Markowitz−ML Markowitz−ML (gross)
Riskandexpectedreturnnetoft-costswithawealthof$10Bby2020
Everythingisout-of-sample:1981-2020
Dottedline:Mean-variancefrontierofriskyassets,∑ iπi =1,withoutt-costs
Markers:Relativeriskaversion(lefttoright):100⊠,20+,10□,5△,1◦
106/107

Thank you!
107/107
