# Plan-First Workflow

**For any non-trivial task, enter plan mode before writing code.**

## The Protocol

1. **Enter Plan Mode** — use `EnterPlanMode`
2. **Check MEMORY.md** — read any `[LEARN]` entries relevant to this task
3. **Requirements Specification (for complex/ambiguous tasks)** — see below
4. **Draft the plan** — what changes, which files, in what order
5. **Decide branching strategy:**
   - **Minor** (single file, small fix, docs): commit directly to `main`
   - **Major** (multi-file feature, risky refactor, new lecture): use a git worktree branch, then merge via PR
6. **Save to disk** — write to `quality_reports/plans/YYYY-MM-DD_short-description.md`
7. **Present to user** — wait for approval
8. **Exit plan mode** — only after approval
9. **Save initial session log** — capture goal and key context while fresh
10. **Implement via orchestrator** — see `orchestrator-protocol.md`

## Step 3: Requirements Specification (For Complex/Ambiguous Tasks)

**When to use:** task is vague, has multiple interpretations, or requires >1 hour / >3 files.
**When to skip:** task is clear, single-file, or user provided detailed requirements.

**Protocol:**
1. Use AskUserQuestion to clarify ambiguities (max 3-5 questions)
2. Create `quality_reports/specs/YYYY-MM-DD_description.md` using `templates/requirements-spec.md`
3. Mark requirements: **MUST** / **SHOULD** / **MAY**
4. Declare clarity: **CLEAR** / **ASSUMED** / **BLOCKED**
5. Get user approval, then draft the plan

## Plans on Disk

Save every plan to `quality_reports/plans/YYYY-MM-DD_short-description.md`.
Plans survive context compression. Format: status, approach, files, verification steps.

## Session Recovery

After compression or new session:
1. Read `CLAUDE.md` + most recent plan in `quality_reports/plans/`
2. Check `git log --oneline -10` and `git diff`
3. State what you understand the current task to be
