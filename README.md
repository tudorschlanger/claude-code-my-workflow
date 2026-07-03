# Claude Code for Academic Economists

A ready-to-use Claude Code template for research and teaching projects. Designed for economists who use **Stata, R, Python, and LaTeX** — but the patterns work for any academic field.

**Last Updated:** 2026-07-03

---

## Quick Start (5 minutes)

### 0. Prerequisites

> **Platform:** This setup is designed for **macOS**. Most components work on Linux with minor path adjustments. Windows users should use WSL.

| Tool | Required For | Install |
|------|-------------|---------|
| [Claude Code](https://code.claude.com/docs/en/overview) | Everything | `npm install -g @anthropic-ai/claude-code` |
| [Node.js](https://nodejs.org/) (v18+) | Claude Code | `brew install node` |
| [Git](https://git-scm.com/) | Version control | `brew install git` |
| [MacTeX](https://www.tug.org/mactex/) | LaTeX compilation | `brew install --cask mactex` |
| [Python 3](https://www.python.org/) + [Conda](https://docs.conda.io/) | Analysis, env management | `brew install --cask miniconda` |
| [R](https://www.r-project.org/) | Statistical analysis | `brew install --cask r` |
| [Stata](https://www.stata.com/) | Econometric analysis | Requires license (optional) |

`make init` will detect which of these are installed, set up conda/renv environments, and save all executable paths. You only need to install the tools you plan to use — Python and LaTeX are the only ones required by the infrastructure itself.

### 1. Create Your Project

**Option A: GitHub template** (recommended)
Click **"Use this template"** on the GitHub repo page, name your new repo, then clone it:
```bash
git clone https://github.com/YOUR_USERNAME/my-project.git
cd my-project
```

**Option B: Manual clone**
```bash
git clone https://github.com/tudorschlanger/claude-code-my-workflow.git my-project
cd my-project
rm -rf .git
git init && git add . && git commit -m "Initial project setup"
```

### 2. Initialize Your Project

```bash
make init
```

This runs an interactive wizard that:
- Detects installed tools (Python, R, Stata, LaTeX) and saves their paths
- Creates a **conda environment** for Python and initializes **renv** for R
- Removes directories for tools you don't use
- Fills in your project name, institution, and domain across all config files

### 3. Start Claude Code

```bash
claude
```

Paste this prompt:

> I am starting to work on **[PROJECT NAME]** in this repo. **[Describe your project in 2-3 sentences.]** Please read the configuration files and adapt them for my project.

Claude reads all configuration files, adapts to your project, and enters contractor mode — planning, implementing, reviewing, and verifying autonomously. You approve the plan and Claude handles the rest.

---

## How It Works

### Contractor Mode

You describe a task. For complex or ambiguous requests, Claude first creates a requirements specification with MUST/SHOULD/MAY priorities and clarity status (CLEAR/ASSUMED/BLOCKED). You approve the spec, then Claude plans the approach, implements it, runs specialized review agents, fixes issues, re-verifies, and scores against quality gates — all autonomously. You see a summary when the work meets quality standards.

### The Core Loop

```
Your instruction
    |
[PLAN] (if multi-file or ambiguous) --> Your approval
    |
[EXECUTE] Implement --> Verify (compile/run) --> Review (agents)
    |
[REPORT] Summary + quality score
    |
Score >= 80? --> Commit.  Score < 80? --> Fix --> Re-verify (max 5 rounds)
```

### Specialized Agents

7 focused agents each check one dimension:

- **proofreader** — grammar, typos, consistency
- **slide-auditor** — visual layout, overflow, spacing
- **pedagogy-reviewer** — narrative arc, pacing, notation clarity
- **domain-reviewer** — field-specific correctness (template — customize for your field)
- **r-reviewer** — R code quality, reproducibility
- **tikz-reviewer** — TikZ diagram visual critique
- **verifier** — end-to-end task completion verification

### Quality Gates

Every file gets a score (0-100). Scores below threshold block the action:
- **80** — commit threshold
- **90** — PR threshold
- **95** — excellence (aspirational)

### Context Survival

Plans, specifications, and session logs survive auto-compression and session boundaries. The PreCompact hook saves a context snapshot before Claude's auto-compression triggers. MEMORY.md accumulates learning across sessions.

---

## Workflows

### Research Workflow

| Phase | Skill | What It Does |
|-------|-------|-------------|
| 1. Ideate | `/interview-me` | Formalize research question into structured spec |
| | `/research-brainstorm` | Multi-turn idea development and stress-testing |
| 2. Survey | `/lit-review` | Structured literature search + synthesis |
| 3. Data | `/find-data` | Identify and catalog relevant datasets |
| | `/create-codebook` | Auto-generate codebooks from .dta files |
| 4. Analyze | Write Stata/R/Python | Claude writes + runs code |
| | `/review-metrics` | Catch econometric errors (clustering, controls, specification) |
| | `/review-data-pipeline` | Audit variable construction + sample restrictions |
| 5. Format | `/format-tables-reg` | Publication-ready regression tables (Stata) |
| | `/format-tables` | Summary statistics + other tables |
| | `/format-graphs` | Consistent figure styling (Okabe-Ito palette) |
| 6. Write | `/review-paper` | Simulated adversarial referee review |
| 7. Ship | `/commit` | Stage, commit, push |

### Teaching Workflow

| Phase | Skill | What It Does |
|-------|-------|-------------|
| 1. Prepare | Drop papers into `docs/papers/` | Reference materials |
| 2. Create | `/create-lecture` | Guided slide creation from papers |
| 3. Review | `/slide-excellence` | Multi-agent review (visual + pedagogy + proofread) |
| | `/devils-advocate` | Challenge pedagogical choices |
| 4. Compile | `/compile-beamer` | 3-pass XeLaTeX + bibtex |
| 5. Ship | `/commit` | Stage, commit, push |

---

## Folder Structure

```
your-project/
├── CLAUDE.md                    # Project config (filled by make init)
├── README.md                    # This file
├── MEMORY.md                    # Persistent learnings across sessions
├── Makefile                     # Task automation
├── .gitignore                   # LaTeX, R, Python, Stata
│
├── .claude/                     # Claude Code infrastructure
│   ├── settings.json            # Permissions + hooks
│   ├── agents/                  # 9 review agents
│   ├── rules/                   # 19 workflow rules
│   ├── skills/                  # 28 skills
│   └── hooks/                   # 7 lifecycle hooks
│
├── data/                        # Three-tier data pipeline
│   ├── raw/                     # External data (never modify)
│   └── derived/                 # All intermediates (.dta, .parquet, .rds)
│
├── docs/                        # Reference materials (inputs to your work)
│   ├── papers/                  # Source PDFs
│   ├── emails/                  # Correspondence
│   └── technical/               # Tool guides, setup notes
│
├── drafts/                      # Work in progress (your source files)
│   ├── documents/               # Paper drafts (.tex)
│   ├── slides/                  # Lecture slides (.tex)
│   └── latex_files/             # Preambles, .bib, .bst
│
├── output/                      # Generated artifacts
│   ├── figures/                 # Plots (.pdf, .png, .svg)
│   ├── tables/                  # Tables (.tex, .csv)
│   └── logs/                    # Compilation + execution logs
│
├── scripts/                     # All code
│   └── src/
│       ├── paths.py             # Central path definitions
│       ├── Python/              # Python scripts
│       ├── R/                   # R scripts
│       └── Stata/               # Stata do-files
│
├── quality_reports/             # QA artifacts
│   ├── plans/                   # Approved plans
│   ├── session_logs/            # Work session records
│   ├── specs/                   # Requirements specs
│   └── merges/                  # Merge quality reports
│
└── templates/                   # Templates for QA documents
```

---

## What's Included

### Agents (`.claude/agents/`)

| Agent | What It Does |
|-------|-------------|
| `proofreader` | Grammar, typos, overflow, consistency review |
| `slide-auditor` | Visual layout audit (overflow, font consistency, spacing) |
| `pedagogy-reviewer` | 13-pattern pedagogical review (narrative arc, notation, pacing) |
| `r-reviewer` | R code quality, reproducibility, and domain correctness |
| `tikz-reviewer` | TikZ diagram visual critique |
| `stata-reviewer` | Stata do-file quality, reproducibility, econometric specification |
| `python-reviewer` | Python script quality, data pipeline correctness, figure standards |
| `verifier` | End-to-end task completion verification |
| `domain-reviewer` | **Template** for your field-specific substance reviewer |

### Skills (`.claude/skills/`)

| Skill | What It Does |
|-------|-------------|
| `/commit` | Stage, commit, and push to main |
| `/compile-beamer` | Compile Beamer slides (3-pass XeLaTeX + bibtex) |
| `/compile-paper` | Compile LaTeX paper with pdflatex |
| `/context-status` | Show session health and context usage |
| `/create-codebook` | Auto-generate codebook from Stata .dta file |
| `/create-lecture` | Guided lecture creation from papers |
| `/devils-advocate` | Challenge slide design (5-7 questions) |
| `/extract-tikz` | TikZ to PDF to SVG pipeline |
| `/find-data` | Identify datasets for empirical research |
| `/format-graphs` | Consistent matplotlib figure style |
| `/format-tables` | LaTeX table formatting |
| `/format-tables-reg` | Regression table formatting (Stata) |
| `/interview-me` | Formalize a research idea interactively |
| `/learn` | Extract reusable knowledge into a skill |
| `/lit-review` | Literature search + synthesis |
| `/pdf` | Read, merge, split, extract PDFs |
| `/proofread` | Grammar and consistency review |
| `/research-brainstorm` | Multi-turn idea stress-testing |
| `/review-data-pipeline` | Adversarial data audit |
| `/review-metrics` | Adversarial econometrics review |
| `/review-paper` | Simulated referee review |
| `/review-r` | R code review |
| `/review-slides-pedagogy` | Pedagogical review |
| `/slide-excellence` | Multi-agent combined review |
| `/validate-bib` | Cross-reference citations vs bibliography |
| `/visual-audit` | Visual layout audit |

### Rules (`.claude/rules/`)

Rules use path-scoped loading: **always-on** rules load every session; **path-scoped** rules load only when Claude works on matching files.

| Rule | What It Enforces |
|------|-----------------|
| `plan-first-workflow` | Plan mode for non-trivial tasks + context preservation |
| `orchestrator-protocol` | Contractor mode: implement, verify, review, fix, score |
| `session-logging` | Three logging triggers: post-plan, incremental, end-of-session |
| `quality-gates` | 80/90/95 thresholds with scoring rubrics |
| `r-code-conventions` | Reproducibility, naming, visual identity |
| `replication-protocol` | Replicate-first methodology with tolerance thresholds |
| `confidential-data` | Never commit raw restricted data |
| `knowledge-base-template` | Notation registry, conventions (customize for your field) |

### Templates (`templates/`)

| Template | What It Does |
|----------|-------------|
| `session-log.md` | Structured session logging format |
| `quality-report.md` | Merge-time quality report |
| `requirements-spec.md` | MUST/SHOULD/MAY requirements with clarity status |
| `constitutional-governance.md` | Define non-negotiable principles vs. preferences |
| `skill-template.md` | Create new domain-specific skills |
| `exploration-readme.md` | Template for experimental work |
| `archive-readme.md` | Document abandoned explorations |

---

## How Claude Uses These Files

Claude loads configuration files at different times to minimize context usage. Each file has one unique job — no duplication.

### Always Loaded (every session)

| File | Job | Lines |
|------|-----|-------|
| `CLAUDE.md` | Project identity: name, folders, commands, tools, skills, workflow preferences | ~150 |
| `MEMORY.md` | Accumulated learnings from corrections (`[LEARN:category]` entries) | <200 |

### Always-On Rules (`.claude/rules/`, no `paths:` scope)

| File | Job |
|------|-----|
| `plan-first-workflow.md` | When and how to enter plan mode, spec-then-plan protocol |
| `orchestrator-protocol.md` | The implement → verify → review → fix → score loop |
| `session-logging.md` | Three logging triggers: post-plan, incremental, end-of-session |
| `meta-governance.md` | Generic vs. specific content — what to commit vs. keep local |

### Path-Scoped Rules (loaded only when working on matching files)

| File | Triggers on |
|------|------------|
| `quality-gates.md` | `drafts/slides/**/*.tex` |
| `r-code-conventions.md` | `scripts/src/**/*.R` |
| `knowledge-base-template.md` | `drafts/slides/**/*.tex` |
| `no-pause-beamer.md` | `drafts/slides/**/*.tex` |
| `verification-protocol.md` | `drafts/slides/**/*.tex` |
| `confidential-data.md` | `data/**` |
| `replication-protocol.md` | `scripts/src/**` |

### Agents (loaded only when spawned by a skill)

Each agent checks one dimension: proofreading, visual layout, pedagogy, domain correctness, R code, TikZ, or verification. They load on demand, not every session.

### Skills (loaded only when invoked)

Each `/skill-name` loads its `SKILL.md` file only when triggered. Zero cost when not in use.

### Templates (never auto-loaded)

Read on demand when creating session logs, quality reports, or specs.

---

## Tips for Working with Claude Code

| Command | What It Does |
|---------|-------------|
| `/btw` | Ask a side question without adding to context history — keeps your session clean |
| `/rewind` or `Esc+Esc` | Restore conversation and code to any previous checkpoint |
| `/compact Focus on X` | Manually compress context, keeping what you specify |
| `/goal` | Set a condition Claude keeps working toward until it holds |
| `/rename` | Name your session (e.g., `data-cleaning`) so you can resume it later |
| `/clear` | Reset context between unrelated tasks — do this often |
| `claude --continue` | Resume your most recent session |
| `claude --resume` | Pick a session to resume from a list |
| `claude -p "prompt"` | Run Claude non-interactively (for scripts, CI, batch jobs) |
| `/plugin` | Browse and install community plugins (e.g., code intelligence for typed languages) |

**When Claude goes off track:** correct early. After two failed corrections, `/clear` and write a better prompt incorporating what you learned. A clean session with a better prompt beats a long session with accumulated corrections.

---

## Adapting for Your Field

1. **Fill in the knowledge base** (`.claude/rules/knowledge-base-template.md`) with your notation, applications, and anti-patterns
2. **Customize the domain reviewer** (`.claude/agents/domain-reviewer.md`) with review lenses specific to your field
3. **Add field-specific R pitfalls** to `.claude/rules/r-code-conventions.md`
4. **Set your non-negotiables and preferences** in the `## Workflow` section of `CLAUDE.md`
5. **Update LaTeX preambles** (`drafts/latex_files/`) with your institutional theme

---

## Community & Extensions

As of 2026, **15+ research groups** across economics, energy, political science, and engineering have forked and adapted this workflow. The infrastructure transfers without modification.

**Extended workflows:**

- **[clo-author](https://github.com/hsantanna88/clo-author)** by Hugo Sant'Anna (UAB) — Paper-centric research workflows with 17 specialized agents, simulated blind peer review, AEA replication compliance
- **[claudeblattman](https://github.com/chrisblattman/claudeblattman)** by Chris Blattman (U Chicago) — Comprehensive guide for non-technical academics: executive assistant workflows, proposal writing, agent debates
- **[MixtapeTools](https://github.com/scunning1975/MixtapeTools)** by Scott Cunningham (Baylor) — The Rhetoric of Decks: philosophy and practice of beautiful academic presentations
- **[autoresearch](https://github.com/karpathy/autoresearch)** by Andrej Karpathy — Constraint-based autonomous research with `program.md` as constitutional document
- **[ClaudeCodeTools](https://github.com/aspi6246/ClaudeCodeTools)** — "The Editor" persona: seven-audit sequential paper review protocol

---

## Additional Resources

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Writing a Good CLAUDE.md](https://code.claude.com/docs/en/memory) — official guidance on project memory

---

## License

MIT License. See [LICENSE](LICENSE).
