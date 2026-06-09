---
paths:
  - "output/figures/**/*"
  - "output/slides/**/*.tex"
---

# Single Source of Truth: Enforcement Protocol

**The Beamer `.tex` file is the authoritative source for ALL content.** Everything else is derived.

## The SSOT Chain

```
Beamer .tex (SOURCE OF TRUTH)
  ├── extract_tikz.tex → PDF → SVGs (derived)
  ├── Bibliography_base.bib (shared)
  └── output/figures/LectureN/*.rds → plots (data source)

NEVER edit derived artifacts independently.
ALWAYS propagate changes from source → derived.
```
