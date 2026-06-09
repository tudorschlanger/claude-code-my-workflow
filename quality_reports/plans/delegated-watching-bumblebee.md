# Template Readiness Assessment & Improvement Plan

**Status:** COMPLETED
**Date:** 2026-06-09
**Goal:** Evaluate this repo as a starting folder for economics research/teaching projects and identify what to add or subtract.

---

## Context

This repo is a fork of `hsantanna88/claude-code-my-workflow` — a Claude Code infrastructure template originally built for Econ 730 at Emory. The user wants to use it as the default starting point for all research and teaching projects. Current state: 17 rules, 7 agents, 7 hooks, 13 local skills, 9 external skills (locked), LaTeX preambles, quality scoring, and a 2200-line guide.

---

## Assessment: Is This Ready to Use?

**Short answer:** The Claude Code infrastructure (rules, agents, hooks, skills) is strong and immediately useful. But there are structural gaps and mismatches that will cause errors on first use. A new project cloned from this template will hit problems immediately without fixes.

**Strengths:**
- Best-in-class Claude Code workflow (orchestrator, quality gates, plan-first)
- 7 specialized agents covering slides, code, pedagogy, TikZ, and domain review
- 13 local skills + 9 external — comprehensive coverage
- Hooks for context survival, file protection, verification reminders
- Quality scoring script ready to use
- LaTeX preambles with Okabe-Ito colors and econ-specific math shortcuts

**Critical issues (will cause errors):**
1. **Path mismatches between rules and actual folder structure** — see below
2. **CLAUDE.md has unfilled placeholders** — Beamer environments table is empty
3. **`explorations/` directory missing** — referenced by 2 rules but doesn't exist
4. **Stata path hardcoded in CLAUDE.md** — machine-specific, should be local

---

## What to Subtract / Fix

### 1. Path mismatches between rules and folder structure

Several rules reference paths that don't match the actual directory layout:

| Rule file | References | Actual path | Fix |
|---|---|---|---|
| `single-source-of-truth.md` | `Figures/**/*` | `output/figures/` | Update rule paths |
| `tikz-visual-quality.md` | `Figures/**/*.tex` | `output/figures/` | Update rule paths |
| `verification-protocol.md` | `Slides/**/*.tex` | `output/slides/` | Update rule paths |
| `pdf-processing.md` | `master_supporting_docs/**` | (doesn't exist) | Remove or redirect to `input/` |

**Action:** Update the 4 affected rule files to use the correct `output/` paths, or decide on canonical naming.

### 2. CLAUDE.md placeholders

- `[YOUR PROJECT NAME]`, `[YOUR INSTITUTION]` — acceptable for a template, but the Beamer custom environments table is completely empty. Fill it with the 7 box environments from `header_slides.tex` (questionbox, answerbox, insightbox, definitionbox, methodbox, quotebox, keybox) so new users see a working example.

**Action:** Fill the Beamer custom environments table with actual entries from the preamble.

### 3. Machine-specific Stata path in CLAUDE.md

The Stata executable path `/Applications/StataNow/StataMP.app/Contents/MacOS/stata-mp` is in the committed CLAUDE.md. Per the meta-governance rule, this should be local.

**Action:** Move Stata path to a comment or to `.claude/settings.local.json` template. Replace in CLAUDE.md with a placeholder: `[PATH TO STATA - configure locally]`.

### 4. `docs/` subdirectory structure is premature

`docs/emails/`, `docs/papers/`, `docs/technical/` — three empty dirs with no README. Either add READMEs explaining their purpose or flatten to just `docs/`.

**Action:** Add a `docs/README.md` explaining what goes in each subdirectory (or flatten).

### 5. Bibliography is empty and protected

`Bibliography_base.bib` is empty (just comments) but protected by `protect-files.sh`. New users can't add entries without removing the protection first.

**Action:** Add 2-3 example bib entries so the file isn't empty, or update the protection hook to allow additions.

---

## What to Add

### 1. `explorations/` directory (HIGH priority)

Two rules reference it (`exploration-folder-protocol.md`, `exploration-fast-track.md`) but the directory doesn't exist. This will confuse Claude when those rules load.

**Action:** Create `explorations/` with a `README.md` using the `templates/exploration-readme.md` template as example content.

### 2. Project init script (HIGH priority)

The user wants an interactive setup script. This walks a new user through:
- Project name and institution (fills CLAUDE.md)
- Domain selection (economics is default)
- Tool selection (which of R/Stata/Python they use)
- Stata path (if applicable, save to settings.local.json)
- Optional: populate Bibliography_base.bib with example entries

**Action:** Create `scripts/init_project.py` — a Python script that reads CLAUDE.md, replaces placeholders interactively, and sets up local config.

### 3. Makefile / task runner (MEDIUM priority)

No build system exists. Common operations (compile slides, run quality checks, clean build artifacts) require typing long commands. A Makefile standardizes these.

**Action:** Create a `Makefile` with targets:
- `make compile FILE=output/slides/Lecture01.tex` — 3-pass XeLaTeX
- `make quality FILE=output/slides/Lecture01.tex` — run quality_score.py
- `make clean` — remove LaTeX build artifacts
- `make verify FILE=output/slides/Lecture01.tex` — compile + quality check
- `make init` — run init script

### 4. `input/README.md` data documentation template (MEDIUM priority)

The `input/` directory is empty with no guidance on how to document data sources.

**Action:** Add `input/README.md` template with fields: source name, URL, access date, format, variable count, license/terms.

### 5. Fill CLAUDE.md project state table (LOW priority)

The "Current Project State" table at the bottom of CLAUDE.md has placeholder rows. Either remove it (it's session-specific, not template material) or replace with a clear instruction to fill it in.

**Action:** Replace the example rows with a comment: "Update this table as you add lectures/content."

---

## Summary of Changes

| Priority | Action | Type | Files affected |
|---|---|---|---|
| HIGH | Fix path mismatches in rules | Fix | 4 rule files in `.claude/rules/` |
| HIGH | Create `explorations/` directory | Add | `explorations/`, `explorations/README.md` |
| HIGH | Create project init script | Add | `scripts/init_project.py` |
| MEDIUM | Fill Beamer environments table in CLAUDE.md | Fix | `CLAUDE.md` |
| MEDIUM | Move Stata path to local config | Fix | `CLAUDE.md` |
| MEDIUM | Add Makefile | Add | `Makefile` |
| MEDIUM | Add `input/README.md` template | Add | `input/README.md` |
| LOW | Add `docs/README.md` | Add | `docs/README.md` |
| LOW | Fix bibliography protection or add example entries | Fix | `Bibliography_base.bib` or `.claude/hooks/protect-files.sh` |
| LOW | Clean up CLAUDE.md project state table | Fix | `CLAUDE.md` |

---

## Verification

After implementation:
1. Run `scripts/init_project.py` on a fresh clone — verify it fills placeholders correctly
2. Check that all rule paths now match actual directory structure (grep for `Figures/`, `Slides/`, `master_supporting_docs/`)
3. Verify `make compile`, `make quality`, `make clean` work
4. Confirm `explorations/` rules no longer reference a missing directory
5. Run `/review-repo-structure` to catch any remaining inconsistencies
