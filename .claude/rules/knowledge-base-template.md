---
paths:
  - "output/slides/**/*.tex"
  - "scripts/**/*.R"
---

# Course Knowledge Base: MAM Intro to Statistics

## Notation Registry

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| Random variables | Uppercase Latin | $X$, $Y$, $Z$ | Lowercase $x$ for a random variable |
| Realizations / data | Lowercase Latin | $x$, $y$, $x_i$ | Uppercase $X$ for observed data |
| Parameters | Lowercase Greek | $\mu$, $\sigma^2$, $\beta$ | Latin letters for unknown parameters |
| Estimators | Hat notation | $\hat{\mu}$, $\hat{\sigma}^2$ | $\mu^*$ or $\mu_{est}$ |
| Sample size | $n$ | $n = 100$ | $N$ (reserve for population size) |
| Population size | $N$ | $N = 10{,}000$ | $n$ for population |
| Probability | $\Pr(\cdot)$ or $P(\cdot)$ | $\Pr(X > 0)$ | $prob(X > 0)$ |
| Expectation | $\E[\cdot]$ (via `\E` command) | $\E[X]$ | $E(X)$ without brackets |
| Variance | $\Var(\cdot)$ (via `\Var` command) | $\Var(X)$ | $V(X)$ or $var(X)$ |
| Covariance | $\Cov(\cdot, \cdot)$ (via `\Cov` command) | $\Cov(X, Y)$ | $C(X,Y)$ |
| Sample mean | $\bar{X}$ | $\bar{X} = \frac{1}{n}\sum X_i$ | $\hat{\mu}$ for sample mean |
| Summation index | Subscript $i$, sum over $n$ | $\sum_{i=1}^{n} x_i$ | Missing index bounds |

## Symbol Reference

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $\E$ | Expectation operator | Probability |
| $\Var$ | Variance operator | Probability |
| $\Cov$ | Covariance operator | Probability |
| $\R$ | Real numbers | Probability |
| $\mu$ | Population mean | Distributions |
| $\sigma^2$ | Population variance | Distributions |
| $\sigma$ | Population standard deviation | Distributions |
| $\bar{X}$ | Sample mean | Sampling / CLT |
| $\hat{\sigma}^2$ | Sample variance | Estimation |
| $H_0$, $H_1$ | Null and alternative hypotheses | Hypothesis testing |
| $\alpha$ | Significance level | Hypothesis testing |
| $p$ | p-value | Hypothesis testing |

## Lecture Progression

| # | Deck | Core Question | Key Notation | Key Method |
|---|------|--------------|-------------|------------|
| 1 | Probability | What are the rules of uncertainty? | $\Pr$, $\E$, $\Var$ | Axioms, Bayes' rule |
| 2 | Distributions | How do we model random phenomena? | $\mu$, $\sigma^2$, Normal | PDF, CDF, key distributions |
| 3 | Sampling & CLT | Why does averaging work? | $\bar{X}$, $n$ | LLN, CLT, sampling distributions |
| 4 | Estimation | How do we learn from data? | $\hat{\mu}$, CI | Point & interval estimation |
| 5 | Hypothesis Testing | How do we make decisions under uncertainty? | $H_0$, $p$-value, $\alpha$ | t-test, decision framework |

*Note: Deck structure is provisional — to be confirmed as content is developed.*

## Financial Applications

| Application | Dataset / Context | Deck(s) | Purpose |
|------------|-------------------|---------|---------|
| Portfolio returns | Stock return data | Probability, Distributions | Motivate expectation, variance, covariance |
| Risk measurement | VaR, volatility | Distributions | Normal distribution in finance |
| Diversification | Multi-asset portfolios | Probability | Independence, covariance |
| Market efficiency | Historical returns | Hypothesis Testing | One-sample t-test on mean returns |

## Anti-Patterns (Don't Do This)

| Anti-Pattern | What Happened | Correction |
|-------------|---------------|-----------|
| Claim returns are normal without caveat | Students assume normality always holds | State "approximately" and mention fat tails |
| Skip from definition to formula | Students memorize without understanding | Build intuition with examples first |
| Use $\sigma$ and $s$ interchangeably | Conflates population and sample quantities | Always distinguish population vs. sample |
| Present CLT without conditions | Students think it always applies | State finite variance, discuss sample size |

## R Code Pitfalls

| Bug | Impact | Fix |
|-----|--------|-----|
| `sample(x)` when `length(x) == 1` | Samples from `1:x` instead of just `x` | Use `x[sample.int(length(x), ...)]` |
| `var()` uses $n-1$ denominator | Mismatch with slide formula using $n$ | Document which convention; use `mean((x - mean(x))^2)` for population |
| `dnorm` vs `pnorm` confusion | Wrong plot (density vs. CDF) | Comment which function does what |
| Missing `set.seed()` | Non-reproducible simulations | Always call at script top |
| `rnorm(n, mean, sd)` — `sd` not `var` | Passing variance instead of SD | Double-check parameterization |
