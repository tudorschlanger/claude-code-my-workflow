"""
Central path definitions — three data tiers.

  RAW      project-downloaded raw data         → data/raw/     (never modify)
  DERIVED  ALL intermediates (parquet, dta)     → data/derived/
  OUTPUT   figures, tables, logs               → output/

Usage:
    from scripts.src.paths import ROOT, RAW, DERIVED, OUTPUT, TABLE, FIG

To add an external upstream data source (e.g., WRDS, FRED), define a
RESEARCH_DATA path and pin versions:

    RESEARCH_DATA = Path("/path/to/shared/research_data")
    VERSIONS = {"compustat": "202606", "crsp": "202606"}
"""

from pathlib import Path

ROOT     = Path(__file__).resolve().parent.parent.parent
DATA     = ROOT / "data"
RAW      = DATA / "raw"
DERIVED  = DATA / "derived"
OUTPUT   = ROOT / "output"

# ─────────────────────────────────────────────────────────────────────────────
# Project-downloaded raw (data/raw/)
# ─────────────────────────────────────────────────────────────────────────────
# Add paths to raw data files here, e.g.:
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

