---
paths:
  - "**/*.R"
  - "output/figures/**/*.R"
  - "scripts/**/*.R"
---

# R Code Standards

**Standard:** Senior Principal Data Engineer + PhD researcher quality

---

## 1. Reproducibility

- `set.seed()` called ONCE at top (YYYYMMDD format)
- All packages loaded at top via `library()` (not `require()`)
- All paths relative to repository root
- `dir.create(..., recursive = TRUE)` for output directories

## 2. Function Design

- `snake_case` naming, verb-noun pattern
- Roxygen-style documentation
- Default parameters, no magic numbers
- Named return values (lists or tibbles)

## 3. Domain Correctness

<!-- Customize for your field's known pitfalls -->
- Verify estimator implementations match slide formulas
- Check known package bugs (document below in Common Pitfalls)

## 4. Visual Identity

```r
# --- Okabe-Ito colorblind-friendly palette ---
oi_black      <- "#000000"
oi_orange     <- "#E69F00"
oi_sky_blue   <- "#56B4E9"
oi_green      <- "#009E73"
oi_yellow     <- "#F0E442"
oi_blue       <- "#0072B2"
oi_vermillion <- "#D55E00"
oi_purple     <- "#CC79A7"

# --- Base colors ---
black        <- "#000000"
white        <- "#FFFFFF"
gray_light1  <- "#D9D9D9"
```

### Custom Theme
```r
theme_custom <- function() {
  theme_minimal() %+replace%
    theme(
      text             = element_text(face = "plain", lineheight = 1.2),
      panel.background = element_rect(fill = white, color = white, linewidth = 0.5, linetype = "solid"),
      panel.grid.major = element_line(color = gray_light1, linewidth = 0.3, linetype = 2),
      panel.grid.minor = element_blank(),
      panel.border     = element_rect(fill = NA, color = black, linewidth = 0.5, linetype = "solid"),
      plot.background  = element_rect(fill = white, color = white),
      legend.title     = element_blank(),
      legend.text      = element_text(size = 9.5, color = black),
      legend.key.width = unit(1, "cm"),
      legend.key       = element_rect(fill = "transparent", color = "transparent"),
      axis.title       = element_text(size = 10, color = black),
      axis.text        = element_text(size = 9, color = black),
      plot.title       = element_text(size = 10, face = "bold", color = black),
      complete         = TRUE
    )
}
```

### Figure Dimensions for Beamer
```r
ggsave(filepath, width = 12, height = 5, bg = "transparent")
```

## 5. RDS Data Pattern

**Heavy computations saved as RDS; slide rendering loads pre-computed data.**

```r
saveRDS(result, file.path(out_dir, "descriptive_name.rds"))
```

## 6. Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Missing `bg = "transparent"` | White boxes on slides | Always include in ggsave() |
| Hardcoded paths | Breaks on other machines | Use relative paths |
| `sample(x)` when `length(x)==1` | Samples from `1:x` silently | Use `x[sample.int(length(x), ...)]` |
| `var()` uses n-1 denominator | Mismatch with population formula on slides | Document convention; use `mean((x-mean(x))^2)` for population variance |
| Confusing `dnorm`/`pnorm`/`qnorm` | Wrong plot or calculation | Comment: density / CDF / quantile |
| `rnorm(n, mean, sd)` takes sd not var | Passing σ² instead of σ | Always pass `sd = sqrt(variance)` |
| Missing `set.seed()` | Non-reproducible simulation output | Call once at script top, YYYYMMDD format |

## 7. Line Length & Mathematical Exceptions

**Standard:** Keep lines <= 100 characters.

**Exception: Mathematical Formulas** -- lines may exceed 100 chars **if and only if:**

1. Breaking the line would harm readability of the math (influence functions, matrix ops, finite-difference approximations, formula implementations matching paper equations)
2. An inline comment explains the mathematical operation:
   ```r
   # Sieve projection: inner product of residuals onto basis functions P_k
   alpha_k <- sum(r_i * basis[, k]) / sum(basis[, k]^2)
   ```
3. The line is in a numerically intensive section (simulation loops, estimation routines, inference calculations)

**Quality Gate Impact:**
- Long lines in non-mathematical code: minor penalty (-1 to -2 per line)
- Long lines in documented mathematical sections: no penalty

## 8. Code Quality Checklist

```
[ ] Packages at top via library()
[ ] set.seed() once at top
[ ] All paths relative
[ ] Functions documented (Roxygen)
[ ] Figures: transparent bg, explicit dimensions
[ ] RDS: every computed object saved
[ ] Comments explain WHY not WHAT
```
