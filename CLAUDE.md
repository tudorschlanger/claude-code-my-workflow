# CLAUDE.MD -- Academic Project Development with Claude Code

<!-- HOW TO USE: Run `make init` to fill placeholders, or replace [BRACKETS] manually.
     This file loads every session — keep it under ~150 lines.
     
     File roles (each has one unique job, no duplication):
       CLAUDE.md              — Project identity, commands, workflow, skills
       MEMORY.md              — Accumulated learnings from corrections
       rules/plan-first-*     — When and how to plan
       rules/orchestrator-*   — The implement-verify-review-fix loop
       rules/session-logging  — When and where to log
       rules/meta-governance  — Generic vs. specific content decisions
     See README.md "How Claude Uses These Files" for the full hierarchy.  -->

**Project:** [YOUR PROJECT NAME]
**Institution:** [YOUR INSTITUTION]
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **When compacting** -- always preserve: list of modified files, current plan path, test/compile commands, and any open questions
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- Beamer `.tex` is authoritative
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
[YOUR-PROJECT]/
├── CLAUDE.md                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── data/
│   ├── raw/                     # External data (never modify, document provenance)
│   └── derived/                 # All intermediates (.dta, .parquet, .rds)
├── docs/                        # Reference papers, emails, technical docs
├── drafts/
│   ├── documents/               # Paper drafts (.tex)
│   ├── slides/                  # Lecture slides (.tex)
│   └── latex_files/             # Preambles, .bib, .bst
├── output/
│   ├── figures/                 # Generated figures
│   ├── tables/                  # Generated tables
│   └── logs/                    # Compilation + execution logs
├── scripts/src/                 # All code (Python/, R/, Stata/)
├── quality_reports/             # Plans, session logs, merge reports
└── templates/                   # Session log, quality report templates
```

---

## Commands

```bash
# LaTeX (3-pass, XeLaTeX only) — run from the directory containing your .tex file
cd drafts/slides && TEXINPUTS=../latex_files:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
BIBINPUTS=../latex_files:$BIBINPUTS bibtex file
TEXINPUTS=../latex_files:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
TEXINPUTS=../latex_files:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
```

### LaTeX Headers
- Slides: always use `drafts/latex_files/header_slides.tex`
- Documents: always use `drafts/latex_files/header_doc.tex`


## Stata
- Always run Stata to verify code and table output rather than generating blindly
- Stata executable path: `[PATH TO STATA - configure in .claude/settings.local.json]`
- Run do-files with: `[STATA PATH] -b do filename.do`
- Logs are written to the same directory as the do-file; always check the `.log` file for errors after running

---

## Workflow

### Claude asks when:
- Design forks with multiple valid approaches
- Spec is unclear or ambiguous
- Scope question (also do Y, or focus on X?)

### Claude just executes when:
- Code fix is obvious (bug, pattern application)
- Verification (compilation, tests, tolerance checks)
- Documentation (session logs, commits)
- Plotting (per established standards)

### Non-Negotiables

<!-- Replace with YOUR project's locked-in preferences -->

- [YOUR PATH CONVENTION] (e.g., `here::here()` for R, relative paths for LaTeX)
- [YOUR SEED CONVENTION] (e.g., `set.seed()` once at top for stochastic code)
- [YOUR FIGURE STANDARDS] (e.g., white bg, 300 DPI, custom theme)
- [YOUR COLOR PALETTE] (e.g., Okabe-Ito)

### Preferences

<!-- Fill in as you discover your working style -->

- **Reporting:** [Concise bullets? Detailed prose?]
- **Replication:** [How strict? Flag near-misses?]

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/commit [msg]` | Stage, commit, and push to main |
| `/compile-beamer [file]` | Compile Beamer slide deck with XeLaTeX (3 passes + bibtex) |
| `/compile-paper [file]` | Compile LaTeX paper/document with pdflatex |
| `/context-status` | Show session health and context usage |
| `/create-codebook [file]` | Auto-generate codebook from Stata .dta file |
| `/create-lecture` | Create new Beamer lecture from papers and materials |
| `/devils-advocate` | Challenge slide design with 5-7 pedagogical questions |
| `/extract-tikz [file]` | Extract TikZ diagrams from Beamer source, compile to PDF, convert to SVG |
| `/find-data [topic]` | Identify and catalog relevant datasets for empirical research |
| `/format-graphs` | Apply consistent matplotlib figure style (Okabe-Ito palette) |
| `/format-tables` | Apply consistent LaTeX table style for table output |
| `/format-tables-reg` | Apply consistent LaTeX regression table style for Stata output |
| `/interview-me [topic]` | Interactive interview to formalize a research idea |
| `/learn [skill-name]` | Extract reusable knowledge into a persistent skill |
| `/lit-review [topic]` | Structured literature search and synthesis with citation extraction |
| `/pdf [file]` | Read, merge, split, extract, or annotate PDFs |
| `/proofread [file]` | Grammar, typo, overflow, consistency review (produces report) |
| `/research-brainstorm [topic]` | Multi-turn research idea development and stress-testing |
| `/review-data-pipeline` | Adversarial audit of variable construction and sample restrictions |
| `/review-metrics` | Adversarial econometrics review (clustering, specification, controls) |
| `/review-paper [file]` | Simulated adversarial referee review of manuscripts |
| `/review-r [file]` | R code quality, reproducibility, and domain correctness review |
| `/review-slides-pedagogy [file]` | Holistic pedagogical review: narrative arc, prerequisites, notation, pacing |
| `/slide-excellence [file]` | Multi-agent slide review (visual, pedagogy, proofreading) |
| `/validate-bib` | Cross-reference citations against bibliography |
| `/visual-audit [file]` | Adversarial visual audit: overflow, font consistency, box fatigue |

---

## Beamer Custom Environments

| Environment | Effect | Use Case |
|---|---|---|
| `questionbox` | Orange background box | Pose questions to the audience |
| `answerbox` | Green border box | Highlight answers or solutions |
| `insightbox` | Orange left-accent bar | Key insights and takeaways |
| `definitionbox[Title]` | Blue bordered titled box | Formal definitions and theorems |
| `methodbox` | Sky blue background box | Methodology or estimation approach |
| `quotebox` | Purple left-accent bar | Quotes, citations, references |

---

## Current Project State

<!-- Update this table as you add lectures/content. -->

| Deck | Beamer | Key Content |
|------|--------|-------------|
| | | *(to be filled as decks are created)* |
