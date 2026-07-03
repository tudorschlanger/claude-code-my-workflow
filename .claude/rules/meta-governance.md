# Meta-Governance: Generic vs. Specific

This repository is both a working project and a template others can fork.
When creating or modifying content, ask: **"Is this generic or specific?"**

---

## Generic (commit to repo)

- Workflow patterns (plan-first, quality gates, orchestrator)
- Templates, skills, rules, agents, hooks
- Documentation standards
- MEMORY.md entries (learnings that help any user)

## Specific (keep local, gitignore)

- Machine-specific paths, tool versions
- Institutional requirements (your university's format)
- Personal preferences (custom quality thresholds)
- API keys, credentials
- `.claude/state/personal-memory.md` (gitignored)

---

## Two-Tier Memory

| Layer | File | Committed? | Purpose |
|-------|------|-----------|---------|
| Generic | `MEMORY.md` | Yes | Learnings useful to any user (< 200 lines) |
| Personal | `.claude/state/personal-memory.md` | No (gitignored) | Machine-specific setup, personal prefs |

Generic patterns sync via git. Personal patterns stay local.

---

## Content Type Reference

| Content | Commit? | Location |
|---------|---------|----------|
| Workflow patterns | Yes | MEMORY.md |
| Templates, skills, rules | Yes | .claude/, templates/ |
| Session logs, plans | Yes | quality_reports/ |
| Machine paths, local settings | No | .claude/settings.local.json |
| Build artifacts | No | .gitignore |

**When in doubt:** Would someone forking this repo for a different field benefit from this? If yes, commit. If no, keep local.
