# Plan: Adapt Workflow Configuration for MAM Intro to Statistics

**Date:** 2026-06-16
**Status:** COMPLETED

---

## Context

This repo contains the Claude Code academic workflow template, already stripped of Quarto content (as of 2026-06-08). It needs to be configured for a specific project: a 3-hour introductory Probability & Statistics session for Yale School of Management's Master of Asset Management (MAM) program. The session prepares students for a subsequent linear regression course. Content will be multiple Beamer decks (one per topic block) with R code for simulations/visualizations.

---

## Changes

### 1. CLAUDE.md — Fill placeholders & customize
**File:** `CLAUDE.md`

- Line 8: `[YOUR PROJECT NAME]` → `MAM Intro to Statistics`
- Line 9: `[YOUR INSTITUTION]` → `Yale University, School of Management`
- Line 27: `[YOUR-PROJECT]` → `MAM-Intro-to-Statistics`
- Keep Stata section (user wants it available)
- Update Current Project State table with planned multi-deck structure (initially empty, but with column descriptions that reflect this project)

### 2. Domain Reviewer Agent — Customize for stats/finance
**File:** `.claude/agents/domain-reviewer.md`

- Persona: probability/statistics expert with asset management applications lens
- Lens 1 (Assumptions): probability axioms, distribution parameter assumptions, independence/iid conditions, CLT applicability, sample size adequacy, finite variance requirements
- Lens 4 (Code-Theory): R-specific pitfalls for statistical simulations (seed reproducibility, vectorization correctness, distribution function usage)
- Lens 3 (Citations): cross-reference with Bibliography_base.bib and docs/papers/
- Add finance-application checks: are financial data examples realistic? Do stated properties (e.g., "stock returns are approximately normal") come with appropriate caveats?

### 3. Knowledge Base — Pre-populate for probability/statistics
**File:** `.claude/rules/knowledge-base-template.md`

- Course name: MAM Intro to Statistics
- Notation registry: conventions for probability (P, E, Var, Cov), random variables (uppercase X vs lowercase x for realizations), estimators (hat notation), parameters (Greek letters)
- Symbol reference: key symbols with their meaning
- Lecture progression: placeholder rows for the planned topic decks (probability, distributions, sampling/CLT, estimation, hypothesis testing — to be confirmed with user)
- Anti-patterns: common intro-stats presentation mistakes

### 4. R Code Conventions — Yale palette & stats pitfalls
**File:** `.claude/rules/r-code-conventions.md`

- Visual identity: Yale blue (#00356b), Yale gray (#4a4a4a), accent colors appropriate for the School of Management
- Common pitfalls table: add stats-specific entries (e.g., `sample()` without `replace`, `dnorm` vs `pnorm` vs `qnorm` confusion, `var()` using n-1 denominator, forgetting `set.seed()` before simulations)

### 5. Quality Gates — Fill tolerance thresholds
**File:** `.claude/rules/quality-gates.md`

- Fill tolerance thresholds for simulation-based teaching (point estimates, Monte Carlo variability, coverage rates)

### 6. Save Memories
**Directory:** `/Users/schl/.claude/projects/-Users-schl-Dropbox--Personal--teaching-2026-2027-MAM-Intro-to-Statistics/memory/`

- **User memory:** Tudor Schlanger, Yale SOM faculty, teaching MAM Intro to Statistics, prefers structured/rigorous collaboration, R + Beamer stack
- **Project memory:** Single 3h session, multiple Beamer decks by topic, preps students for linear regression course, audience is MAM practitioners

---

## Files Modified

| File | Action |
|------|--------|
| `CLAUDE.md` | Fill placeholders, update project state |
| `.claude/agents/domain-reviewer.md` | Customize for probability/statistics + finance |
| `.claude/rules/knowledge-base-template.md` | Pre-populate notation and course structure |
| `.claude/rules/r-code-conventions.md` | Yale palette, stats pitfalls |
| `.claude/rules/quality-gates.md` | Fill tolerance thresholds |
| Memory files (2) | Save user and project context |

## Files NOT Modified

- `.claude/settings.json` — hooks and permissions are already correct
- `.claude/settings.local.json` — Stata path already configured
- `scripts/latex_preambles/header_slides.tex` — functional as-is (comment path is cosmetic)
- All other rules/agents — generic and work as-is

---

## Verification

1. Read back each modified file to confirm placeholders are gone
2. Confirm CLAUDE.md is under ~150 lines
3. Confirm knowledge-base notation matches header_slides.tex math commands
4. Verify memory files are properly indexed in MEMORY.md
