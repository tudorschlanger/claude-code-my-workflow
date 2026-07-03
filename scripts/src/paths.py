"""
Central path definitions — two data tiers.

  EXTERNAL   Large/shared upstream data (read-only, lives OUTSIDE the project)
             e.g., WRDS extracts, Census files, shared Dropbox research data.
             Configure via RESEARCH_DATA below or environment variable.

  RAW        Small, project-specific data (lives INSIDE the project at data/raw/)
             e.g., hand-collected CSVs, survey exports, small public datasets.
             Never modify raw files — all transformations go to DERIVED.

  DERIVED    ALL intermediates (parquet, dta, rds) → data/derived/

  OUTPUT     Figures, tables, logs → output/

Usage:
    from scripts.src.paths import ROOT, RAW, DERIVED, OUTPUT, TABLE, FIG
"""

import os
from pathlib import Path

ROOT     = Path(__file__).resolve().parent.parent.parent
DATA     = ROOT / "data"
RAW      = DATA / "raw"
DERIVED  = DATA / "derived"
OUTPUT   = ROOT / "output"

# ─────────────────────────────────────────────────────────────────────────────
# EXTERNAL — large/shared upstream data (read-only, outside the project)
# ─────────────────────────────────────────────────────────────────────────────
# Set RESEARCH_DATA to your shared data directory. This keeps large datasets
# out of the git repo while making them accessible via a stable path.
#
# Option 1: Set here directly
#   RESEARCH_DATA = Path.home() / "Dropbox" / "research_data"
#
# Option 2: Set via environment variable (recommended for portability)
#   export RESEARCH_DATA="$HOME/Dropbox/research_data"
#
RESEARCH_DATA = Path(os.environ.get("RESEARCH_DATA", ""))

# Pin versions per source so re-runs always read the same inputs.
# Bump a value when that source is refreshed.
# VERSIONS = {"compustat": "202606", "crsp": "202606"}

# ─────────────────────────────────────────────────────────────────────────────
# Project-specific raw (data/raw/) — small files only
# ─────────────────────────────────────────────────────────────────────────────
# Add paths to small, project-specific data here, e.g.:
# RAW_SURVEY = RAW / "survey_2026.csv"

# ─────────────────────────────────────────────────────────────────────────────
# Derived intermediates (data/derived/)
# ─────────────────────────────────────────────────────────────────────────────
# Add paths to derived/processed data here, e.g.:
# CLEAN_PANEL = DERIVED / "panel_clean.parquet"

# ─────────────────────────────────────────────────────────────────────────────
# Outputs (figures / tables)
# ─────────────────────────────────────────────────────────────────────────────
TABLE = OUTPUT / "tables"
FIG   = OUTPUT / "figures"

