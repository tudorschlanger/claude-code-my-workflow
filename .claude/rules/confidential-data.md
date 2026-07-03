---
paths:
  - "data/**"
  - "**/*.dta"
  - "**/*.sav"
  - "**/raw/**"
  - "**/restricted/**"
  - "**/confidential/**"
---

# Data Use Protocol

## Two-Tier Data Model

- **External data** (large, shared): lives OUTSIDE the project in `RESEARCH_DATA` (see `scripts/src/paths.py`). Not tracked by git. Examples: WRDS extracts, Census files, administrative records.
- **Project data** (`data/raw/`): small, project-specific files only. CSV, TSV, JSON. No binary formats, no PDFs. Must be documented in `data/raw/README.md`.

## Classification Requirement

Every dataset must be classified in `data/raw/README.md`:

- **`public`** — freely available (FRED, Census public-use, published datasets). Claude can read and reference freely.
- **`proprietary`** — licensed, restricted, or IRB-governed. Claude can process it, but anything Claude reads is sent to Anthropic's API.

**Before working with any data file, check its classification in `data/raw/README.md`.** If a dataset is marked `proprietary`, warn the user before reading it.

## The Four Hard Rules

1. **Never commit raw confidential data.** Raw microdata, identifiers, and provider-supplied files do not belong in git. The pre-commit hook blocks binary data formats (.dta, .parquet, .xlsx, .pdf) and files > 5 MB.
2. **Anything Claude reads is sent to the API.** Sandboxing limits what Claude can *do*, not what it can *see*. For truly confidential datasets: keep them in `RESEARCH_DATA` outside the project, or use local models.
3. **Nothing leaves without disclosure clearance.** Any table, figure, coefficient, or count built on restricted data must pass disclosure-avoidance review before publication.
4. **Access is per-person, per-agreement.** A co-author without the DUA cannot receive the data or outputs that fail disclosure rules.

## What the Pre-Commit Hook Blocks

- Binary data formats: `.dta`, `.sav`, `.parquet`, `.feather`, `.rds`, `.RData`, `.xlsx`, `.xls`, `.h5`, `.sqlite`
- PDFs: `.pdf`
- Archives: `.zip`, `.gz`, `.tar`, `.7z`
- Any file > 5 MB

Override with `--no-verify` (not recommended).
