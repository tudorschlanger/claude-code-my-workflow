---
name: lit-review
description: Structured literature search and synthesis with citation extraction and gap identification. Searches local papers and uses web search for broader context.
argument-hint: "[topic or research question]"
---

# Literature Review

## Instructions

1. **Scan local papers** -- Read files in `doc/papers/` for directly relevant work.

2. **Web search** -- Use WebSearch to find related academic papers, working papers, and preprints
   - **Finance journals** -- Search in Journal of Finance, Journal of Financial Economics, Review of Financial Studies 
   - **Economics journals** -- Search in American Economic Review (including P&P), Quarterly Journal of Economics, Journal of Political Economy, Econometrica, Review of Economic Studies, Review of Economics and Statistics, Journal of Monetary Economics 
   - **Working papers** -- Search in NBER Working Papers, and SSRN 

3. **Organize findings** into categories:
   - **Theoretical foundation** -- Papers that establish the theoretical framework
   - **Empirical evidence** -- Papers with related empirical findings
   - **Methodological** -- Papers with relevant identification strategies
   - **Debates** -- Conflicting findings or methodological disagreements

4. **For each paper, extract:**
   - Citation (author, year, journal)
   - Key finding relevant to this project
   - Identification strategy used
   - Data source
   - How it relates to our work

5. **Identify gaps** -- What questions remain unanswered? Where can this project contribute?

6. **Save report** to `quality_reports/lit-review_YYYY-MM-DD_topic.md`

## Examples

**User says:** `/lit-review partisan bias in economic expectations`
**Action:** Search local papers + web, synthesize findings, identify gaps.

## Validity Checks
   - Ensure that every paper has a URL link or PDF (no fake citations!)


## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "No local papers match" | Topic not in existing library | Rely on web search, suggest relevant papers to add |
| "Too many results" | Broad topic | Ask user to narrow scope |
