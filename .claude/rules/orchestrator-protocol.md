# Orchestrator Protocol: Contractor Mode

**After a plan is approved, the orchestrator takes over autonomously.**

## The Loop

```
Plan approved → orchestrator activates
  │
  Step 1: BRANCH — If major change, create worktree branch
  │
  Step 2: IMPLEMENT — Execute plan steps
  │
  Step 3: VERIFY — Compile, render, check outputs
  │         If verification fails → fix → re-verify
  │
  Step 4: REVIEW — Run review agents (by file type)
  │
  Step 5: FIX — Apply fixes (critical → major → minor)
  │
  Step 6: RE-VERIFY — Confirm fixes are clean
  │
  Step 7: SCORE — Apply quality-gates rubric
  │
  └── Score >= threshold?
        YES → Commit and present summary
              If on branch → push branch, create PR (score >= 90)
              If on main → push to main (score >= 80)
        NO  → Loop back to Step 4 (max 5 rounds)
              After max rounds → present with remaining issues
```

## Branching Strategy (decided during planning)

**Minor changes** — commit directly to `main`:
- Single file edits, small fixes, documentation updates
- Score threshold: 80/100

**Major changes** — use a git worktree branch, then PR:
- Multi-file features, new lectures, risky refactors, new analysis pipelines
- Branch name: `<type>/<short-description>` (e.g., `feat/lecture-5-iv`, `fix/panel-clustering`)
- Score threshold for PR: 90/100
- After PR is created, present the URL to the user

## PR Creation

When work is on a branch and score >= 90:
1. Push branch: `git push -u origin <branch-name>`
2. Create PR with `gh pr create`:
   - Title: conventional commit format (e.g., `feat: add Lecture 5 on IV estimation`)
   - Body: summary of changes, files modified, quality score, review agent findings
3. Present the PR URL to the user
4. User decides whether to merge immediately or request further review

## Limits

- **Main loop:** max 5 review-fix rounds
- **Critic-fixer sub-loop:** max 5 rounds
- **Verification retries:** max 2 attempts
- Never loop indefinitely

## "Just Do It" Mode

When user says "just do it" / "handle it":
- Skip final approval pause
- Auto-commit if score >= 80 (main) or auto-PR if score >= 90 (branch)
- Still run the full verify-review-fix loop
- Still present the summary
