# Input Data

This directory holds all data sources from outside the project. Document each dataset here.

## Data Inventory

| File | Source | Date accessed | Format | Variables | Notes |
|------|--------|---------------|--------|-----------|-------|
| `[your_data.csv]` | `[URL or description]` | `[YYYY-MM-DD]` | `[csv/dta/xlsx]` | `[N]` | `[Any access terms or restrictions]` |

## Guidelines

- Never modify raw data files — all transformations happen in `scripts/`
- Document provenance: where the data came from, when it was accessed, any license terms
- If data is restricted, note the access conditions and do not commit sensitive files
- Use `.gitignore` for large binary files — consider git-lfs or store externally
