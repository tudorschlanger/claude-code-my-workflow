# Raw Data

Small, project-specific data files. Large or shared datasets belong **outside** this project — see `scripts/src/paths.py` for the `RESEARCH_DATA` path.

## Rules

- **Never modify** raw data files — all transformations happen in `scripts/` and output to `data/derived/`
- **Only small text files** belong here (CSV, TSV, JSON). Binary formats (.dta, .parquet, .xlsx) and PDFs go in `RESEARCH_DATA` or `data/derived/`
- **Classify every dataset** as `public` or `proprietary` in the inventory below
- **Git pre-commit hook** blocks commits of files > 5 MB, binary data formats, and PDFs

## Data Inventory

Every dataset in this directory must be documented here. Claude reads this file when working with data.

| File | Classification | Source | Date Accessed | Description |
|------|---------------|--------|---------------|-------------|
<!-- Example:
| `firm_returns.csv` | public | CRSP via WRDS | 2026-06-15 | Monthly stock returns, 2000-2025 |
| `survey_responses.csv` | proprietary | Field experiment (IRB #2026-001) | 2026-05-01 | Treatment/control outcomes, de-identified |
-->

### Classification Guide

- **`public`** — freely available data (FRED, Census public-use, published datasets). Claude can read, analyze, and reference freely.
- **`proprietary`** — licensed, restricted, or IRB-governed data. Claude can process it for analysis, but remember: anything Claude reads is sent to Anthropic's API. For truly confidential data, use local models or keep it in `RESEARCH_DATA` outside the project.

## Large / External Data

For large datasets (> 5 MB) or shared data used across projects:

1. Store in a directory outside this repo (e.g., `~/Dropbox/research_data/`)
2. Set the path in `scripts/src/paths.py` or via environment variable:
   ```bash
   export RESEARCH_DATA="/Users/you/Dropbox/research_data"
   ```
3. Reference in your scripts: `from scripts.src.paths import RESEARCH_DATA`
