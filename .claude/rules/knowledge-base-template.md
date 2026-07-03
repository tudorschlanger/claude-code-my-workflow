---
paths:
  - "drafts/slides/**/*.tex"
  - "scripts/src/**/*.R"
---

# Course Knowledge Base: [YOUR PROJECT NAME]

<!-- CUSTOMIZE: Fill in your project's notation conventions, lecture progression,
     and domain-specific anti-patterns. The structure below shows examples from
     an introductory statistics course — replace with your own content. -->

## Notation Registry

<!-- Define your notation conventions here. Consistency across lectures is critical. -->

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
<!-- Example rows — replace with your conventions:
| Random variables | Uppercase Latin | $X$, $Y$, $Z$ | Lowercase $x$ for a random variable |
| Parameters | Lowercase Greek | $\mu$, $\sigma^2$, $\beta$ | Latin letters for unknown parameters |
| Estimators | Hat notation | $\hat{\mu}$, $\hat{\sigma}^2$ | $\mu^*$ or $\mu_{est}$ |
| Sample size | $n$ | $n = 100$ | $N$ (reserve for population size) |
-->

## Symbol Reference

<!-- Track which symbols are introduced in which lecture to maintain consistency. -->

| Symbol | Meaning | Introduced |
|--------|---------|------------|
<!-- Add your symbols here -->

## Lecture Progression

<!-- Map your lecture sequence to track flow and dependencies. -->

| # | Deck | Core Question | Key Notation | Key Method |
|---|------|--------------|-------------|------------|
<!-- Add your lectures here -->

## Domain Applications

<!-- How does your subject connect to real-world applications? -->

| Application | Dataset / Context | Deck(s) | Purpose |
|------------|-------------------|---------|---------|
<!-- Add your applications here -->

## Anti-Patterns (Don't Do This)

<!-- Document common mistakes and their corrections. These accumulate over time. -->

| Anti-Pattern | What Happened | Correction |
|-------------|---------------|-----------|
<!-- Add domain-specific anti-patterns here -->

## R Code Pitfalls

| Bug | Impact | Fix |
|-----|--------|-----|
| `sample(x)` when `length(x) == 1` | Samples from `1:x` instead of just `x` | Use `x[sample.int(length(x), ...)]` |
| `var()` uses $n-1$ denominator | Mismatch with slide formula using $n$ | Document which convention; use `mean((x - mean(x))^2)` for population |
| `dnorm` vs `pnorm` confusion | Wrong plot (density vs. CDF) | Comment which function does what |
| Missing `set.seed()` | Non-reproducible simulations | Always call at script top |
| `rnorm(n, mean, sd)` — `sd` not `var` | Passing variance instead of SD | Double-check parameterization |
