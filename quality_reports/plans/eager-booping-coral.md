# Plan: Remove All Quarto Content, Restructure as Beamer-Only

## Context

The project currently supports a dual Beamer + Quarto (RevealJS) workflow. The user wants to remove all Quarto support entirely and restructure for a Beamer-only workflow. This affects ~47 files across agents, skills, rules, scripts, docs, the guide, and configuration.

## Phase 1: Delete Purely Quarto Files

**Agents (3):** `.claude/agents/quarto-critic.md`, `quarto-fixer.md`, `beamer-translator.md`
**Skills (3 directories):** `.claude/skills/translate-to-quarto/`, `qa-quarto/`, `deploy/`
**Rules (1):** `.claude/rules/beamer-quarto-sync.md`
**Scripts:** `scripts/sync_to_docs.sh`
**Guide dir:** `guide/workflow-guide.qmd`, `guide/_quarto.yml`, `guide/custom.scss`, `guide/.gitignore`, `guide/workflow-guide.html`
**Docs dir:** `docs/` (entire directory)

## Phase 2: Heavy Cleanup (many Quarto references)

- **CLAUDE.md** -- Remove Quarto from folder structure, SSOT line, commands, skills table (3 rows), CSS classes section, lecture mapping (Quarto column)
- **`.claude/rules/verification-protocol.md`** -- Remove `.qmd`/`docs/` from paths, delete "For Quarto/HTML Slides" and "For TikZ Diagrams in HTML/Quarto" sections
- **`.claude/rules/single-source-of-truth.md`** -- Remove `.qmd` from paths, delete TikZ freshness protocol, environment parity section, content fidelity checklist
- **`.claude/rules/quality-gates.md`** -- Remove `.qmd` from paths, delete "Quarto Slides (.qmd)" rubric
- **`.claude/agents/slide-auditor.md`** -- Remove environment parity, Plotly quality, and "For Quarto" sections
- **`.claude/agents/verifier.md`** -- Remove `.qmd` verification section, deployment check section
- **`scripts/quality_score.py`** -- Remove `QUARTO_RUBRIC`, `check_quarto_compilation`, `check_quarto_citations`, `score_quarto`, `.qmd` dispatch
- **`README.md`** -- Remove 3 agent rows, 3 skill rows, `beamer-quarto-sync` rule row, Quarto prerequisite, update rule trigger paths, update counts

## Phase 3: Light Cleanup (few Quarto references)

18 files with 1-3 references each:
- **Rules:** `proofreading-protocol.md`, `knowledge-base-template.md`, `meta-governance.md` (remove `.qmd` from paths, replace Quarto examples)
- **Config:** `settings.json` (remove `quarto render` and `sync_to_docs.sh` permissions), `.gitignore` (remove `.quarto/` entries)
- **Hooks:** `verify-reminder.py` (remove `.qmd` entry)
- **Skills (9):** `slide-excellence`, `visual-audit`, `create-lecture`, `deep-audit`, `pedagogy-review`, `proofread`, `data-analysis`, `review-paper`, `validate-bib`
- **Agents (3):** `proofreader.md`, `pedagogy-reviewer.md`, `r-reviewer.md`
- **Templates (2):** `skill-template.md` (line 118, 406), `constitutional-governance.md` (lines 32, 38, 94)

## Phase 4: Adapt `extract-tikz` Skill

Remove Step 5 (sync_to_docs.sh call), renumber steps, update description.

## Phase 5: Convert Guide to Markdown

Create `guide/workflow-guide.md` from `guide/workflow-guide.qmd`:
- Strip Quarto YAML frontmatter
- Remove all Quarto-specific sections (Beamer-to-Quarto pipeline, CSS classes, RevealJS config, deploy/QA docs, Plotly sections)
- Convert Quarto callout syntax to plain markdown
- Update file paths from `.qmd` to `.tex`
- Update agent/skill/rule counts: 7 agents, 21 skills, 17 rules, 7 hooks

## Phase 6: Delete `docs/`

Delete entire `docs/` directory. Update README to remove GitHub Pages references.

## Phase 7: Update MEMORY.md

Remove `(no Quarto)` parenthetical from design principle.

## Phase 8: Verification

1. Grep for remaining `.qmd`, `Quarto`, `sync_to_docs`, `RevealJS` references
2. Verify deleted files are gone
3. Verify counts consistent across CLAUDE.md, README.md, guide
4. Test `python3 scripts/quality_score.py --help`
5. Validate `settings.json` is valid JSON
