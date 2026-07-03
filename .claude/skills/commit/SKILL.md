---
name: commit
description: Stage, commit, and push to main. Use for the standard commit cycle.
argument-hint: "[optional: commit message]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Commit and Push

Stage changes, commit with a descriptive message, and push to main.

## Steps

1. **Check current state:**

```bash
git status
git diff --stat
git log --oneline -5
```

2. **Stage files** — add specific files (never use `git add -A`):

```bash
git add <file1> <file2> ...
```

Do NOT stage `.claude/settings.local.json` or any files containing secrets.

3. **Commit** with a conventional commit message:

If `$ARGUMENTS` is provided, use it as the commit message. Otherwise, analyze the staged changes and write a message using [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>[(scope)]: <description>
```

**Types:**
- `feat` — new feature or capability
- `fix` — bug fix
- `docs` — documentation changes
- `refactor` — code restructuring without behavior change
- `test` — adding or modifying tests
- `style` — formatting, whitespace, no logic change
- `chore` — maintenance, dependencies, config
- `perf` — performance improvement
- `data` — data additions or transformations
- `slides` — lecture slide creation or modification

**Scope** (optional): a noun in parentheses describing the area — e.g., `fix(panel):`, `feat(api):`, `slides(lecture3):`

```bash
git commit -m "$(cat <<'EOF'
<type>: <description>
EOF
)"
```

4. **Push to main:**

```bash
git push origin main
```

5. **Report** what was committed and pushed.

## Important

- Commit directly to `main` for minor changes (single file, small fix)
- For major changes (multi-file, new feature, risky refactor), use a worktree branch — this is decided during plan mode
- Exclude `settings.local.json` and sensitive files from staging
- If the commit message from `$ARGUMENTS` is provided, use it exactly
- If the push is rejected (diverged history), ask the user whether to pull first or force-push
