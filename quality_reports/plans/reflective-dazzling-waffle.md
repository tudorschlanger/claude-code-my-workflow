# Plan: Deduplicate Always-On Configuration Files

**Status:** DRAFT
**Date:** 2026-07-03

---

## Context

Claude loads several `.md` files into its system prompt every session. Duplication across these files wastes context and creates drift risk. Each file should have exactly one unique job.

**Current always-on cost:** ~771 lines across 7 files.

---

## Target Architecture: One Job Per File

| File | Unique Job | Loaded |
|------|-----------|--------|
| **`CLAUDE.md`** | Project identity + workflow config: who, what, where, how to run things | Always |
| **`MEMORY.md`** | Accumulated learnings from corrections (summaries, not reproductions) | Always |
| **`.claude/rules/plan-first-workflow.md`** | When and how to enter plan mode, spec-then-plan protocol | Always |
| **`.claude/rules/orchestrator-protocol.md`** | The implement → verify → review → fix → score loop | Always |
| **`.claude/rules/session-logging.md`** | Three logging triggers (post-plan, incremental, end-of-session) | Always |

**DELETED:** `.claude/WORKFLOW_QUICK_REF.md` — its unique content (when-to-ask, non-negotiables, preferences) merges into CLAUDE.md.

**TRIMMED:** `.claude/rules/meta-governance.md` — cut from 252 to ~60 lines. Remove dogfooding (repeats other rules), template maintenance examples, amendment process. Keep only the core generic-vs-specific framework.

**Target always-on cost:** ~450 lines (down from ~771).

---

## Changes

### 1. Delete `.claude/WORKFLOW_QUICK_REF.md`

Its content maps to existing files:
- The Loop → `orchestrator-protocol.md` (canonical)
- Quality Gates → `CLAUDE.md` quality thresholds (canonical)
- Exploration Mode → `exploration-fast-track.md` (path-scoped, canonical)
- **Unique content to absorb into CLAUDE.md:**
  - "I Ask You When" / "I Just Execute When" (4+5 bullets)
  - "Non-Negotiables" and "Preferences" placeholder sections

### 2. Expand CLAUDE.md with Workflow Section

Add a `## Workflow` section absorbing the unique WORKFLOW_QUICK_REF content. New CLAUDE.md structure:

```
# CLAUDE.MD
**Project / Institution / Branch**

## Core Principles (existing, keep as-is)

## Folder Structure (existing, keep as-is)

## Commands (existing: LaTeX, Stata)

## Workflow                              ← NEW (from WORKFLOW_QUICK_REF)
  - When Claude asks vs. just executes
  - Non-negotiables (placeholder)
  - Preferences (placeholder)

## Quality Thresholds (existing, keep as-is)

## Skills Quick Reference (existing, keep as-is)

## Beamer Custom Environments (existing, keep as-is)

## Tool Configuration (inserted by make init)

## Current Project State (existing, keep as-is)
```

### 3. Trim `meta-governance.md` (252 → ~60 lines)

**Keep:**
- The core generic-vs-specific decision framework (~30 lines)
- The quick reference table of content types (~20 lines)
- Memory two-tier explanation (~10 lines)

**Remove:**
- "The Two Identities" extended prose (covered by the framework)
- "Dogfooding" section (just repeats plan-first, quality gates, session logging rules)
- "Template Maintenance Principles" with good/bad examples (editorial guidance, not operational)
- "When to Make Exceptions" examples
- "Amendment Process" (bureaucratic overhead)
- "Summary" section (repeats the framework)

### 4. Trim `MEMORY.md` entries that echo rules

Replace verbose entries that reproduce rule content with one-line summaries. Example:

**Before (3 lines):**
```
[LEARN:workflow] Context survival before compression: (1) Update MEMORY.md with [LEARN] entries, (2) Ensure session log current (last 10 min), (3) Active plan saved to disk, (4) Open questions documented. The pre-compact hook displays checklist.
```

**After (1 line):**
```
[LEARN:workflow] Context survival: MEMORY.md + session log + plan must be on disk before compression. See plan-first-workflow.md.
```

### 5. Trim `plan-first-workflow.md` (84 → ~50 lines)

Remove the "Context Management" section (lines 64-83) which duplicates what the pre-compact hook already enforces. Keep the protocol steps and session recovery.

### 6. Update README.md

Add a section explaining the configuration file hierarchy and each file's unique role.

### 7. Update `settings.json`

Remove the hook reference to WORKFLOW_QUICK_REF.md if any hooks reference it.

---

## Files Modified

| File | Action |
|------|--------|
| `.claude/WORKFLOW_QUICK_REF.md` | DELETE |
| `CLAUDE.md` | Add `## Workflow` section |
| `.claude/rules/meta-governance.md` | Trim 252 → ~60 lines |
| `.claude/rules/plan-first-workflow.md` | Trim 84 → ~50 lines |
| `MEMORY.md` | Trim verbose entries to summaries |
| `README.md` | Add configuration file hierarchy section |

---

## Verification

1. Count total always-on lines before and after
2. Grep for WORKFLOW_QUICK_REF references — update any that remain
3. Verify no unique content was lost in deletions
4. `make help` still works
