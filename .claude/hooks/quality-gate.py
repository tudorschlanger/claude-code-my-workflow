#!/usr/bin/env python3
"""
Quality Gate Stop Hook for Claude Code

Blocks Claude from stopping if any .tex or .R file modified in this session
scores below the commit threshold (80/100). Runs quality_score.py on
modified files and reports failures.

Only fires once per session to avoid infinite loops — after blocking once,
it lets Claude proceed on the next stop attempt.

Usage (in .claude/settings.json):
    "Stop": [{ "hooks": [{ "type": "command",
      "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/quality-gate.py" }] }]
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


THRESHOLD = 80


def get_state_path() -> Path:
    """Get state file path keyed by project."""
    import os
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        state_dir = Path.home() / ".claude" / "sessions" / "default"
    else:
        project_hash = hashlib.md5(project_dir.encode()).hexdigest()[:8]
        state_dir = Path.home() / ".claude" / "sessions" / project_hash
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir / "quality-gate-state.json"


def load_state(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"blocked_once": False}


def save_state(path: Path, state: dict):
    path.write_text(json.dumps(state))


def get_modified_files(project_dir: str) -> list[str]:
    """Get .tex and .R files modified (staged or unstaged) since last commit."""
    files = []
    for cmd in [
        ["git", "diff", "--name-only", "--diff-filter=ACMR"],
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
    ]:
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=10, cwd=project_dir
            )
            if result.returncode == 0:
                files.extend(result.stdout.strip().split("\n"))
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    # Deduplicate and filter to scorable files (exclude infrastructure scripts)
    skip = {"scripts/src/Python/init_project.py", "scripts/src/Python/quality_score.py"}
    seen = set()
    scorable = []
    for f in files:
        f = f.strip()
        if f and f not in seen and f not in skip and f.endswith((".tex", ".R", ".py", ".do")):
            seen.add(f)
            scorable.append(f)
    return scorable


def score_file(project_dir: str, filepath: str) -> dict | None:
    """Run quality_score.py on a file. Returns parsed JSON or None."""
    script = Path(project_dir) / "scripts" / "src" / "Python" / "quality_score.py"
    if not script.exists():
        return None

    try:
        result = subprocess.run(
            ["python3", str(script), filepath, "--json"],
            capture_output=True, text=True, timeout=30, cwd=project_dir
        )
        if result.returncode <= 1 and result.stdout.strip():
            data = json.loads(result.stdout)
            if isinstance(data, list) and data:
                return data[0]
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        pass
    return None


def main():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        hook_input = {}

    # If stop_hook_active, Claude is already retrying after a block — let it stop
    if hook_input.get("stop_hook_active", False):
        sys.exit(0)

    project_dir = hook_input.get("cwd", "")
    if not project_dir:
        sys.exit(0)

    state_path = get_state_path()
    state = load_state(state_path)

    # Only block once per session to avoid infinite loops
    if state.get("blocked_once", False):
        sys.exit(0)

    modified = get_modified_files(project_dir)
    if not modified:
        sys.exit(0)

    # Score each modified file
    failures = []
    for filepath in modified:
        full_path = Path(project_dir) / filepath
        if not full_path.exists():
            continue
        result = score_file(project_dir, filepath)
        if result and result.get("score", 100) < THRESHOLD:
            failures.append(f"  {filepath}: {result['score']}/100")

    if not failures:
        sys.exit(0)

    # Block and report
    state["blocked_once"] = True
    save_state(state_path, state)

    failure_list = "\n".join(failures)
    output = {
        "decision": "block",
        "reason": (
            f"QUALITY GATE: {len(failures)} file(s) below {THRESHOLD}/100 commit threshold:\n"
            f"{failure_list}\n"
            f"Fix the issues above before finishing."
        ),
    }
    json.dump(output, sys.stdout)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Fail open — never block Claude due to a hook bug
        sys.exit(0)
