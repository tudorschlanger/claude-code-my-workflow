#!/usr/bin/env python3
"""
Project initialization script for Claude Code academic workflow.
Walks new users through customizing the template for their project.
"""

import argparse
import json
import os
import re
import sys


def prompt(text, default=""):
    """Prompt user for input with optional default."""
    suffix = f" [{default}]" if default else ""
    value = input(f"  {text}{suffix}: ").strip()
    return value if value else default


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def fill_claude_md(project_name, institution, branch):
    """Replace placeholders in CLAUDE.md."""
    path = "CLAUDE.md"
    content = read_file(path)

    replacements = [
        ("[YOUR PROJECT NAME]", project_name),
        ("[YOUR INSTITUTION]", institution),
        ("[YOUR-PROJECT]", project_name.replace(" ", "_").lower()),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    write_file(path, content)
    print(f"  Updated {path}")


def update_settings_local(stata_path=None):
    """Create or update .claude/settings.local.json with tool paths."""
    path = ".claude/settings.local.json"

    if os.path.exists(path):
        try:
            data = json.loads(read_file(path))
        except json.JSONDecodeError:
            print(f"  Warning: {path} is not valid JSON, creating fresh")
            data = {}
    else:
        data = {}

    if "env" not in data:
        data["env"] = {}

    if stata_path:
        data["env"]["STATA_PATH"] = stata_path
        print(f"  Set STATA_PATH in {path}")

    # Ensure permissions block exists
    if "permissions" not in data:
        data["permissions"] = {"allow": []}

    write_file(path, json.dumps(data, indent=2) + "\n")
    print(f"  Updated {path}")


def main():
    print("=" * 60)
    print("  Claude Code Academic Workflow - Project Init")
    print("=" * 60)
    print()

    # Step 1: Basic info
    print("Step 1: Project information")
    project_name = prompt("Project name")
    institution = prompt("Institution")
    branch = prompt("Git branch", "main")
    print()

    # Step 2: Domain
    print("Step 2: Domain (used to keep relevant tooling)")
    domain = prompt("Domain", "economics")
    print()

    # Step 3: Tools
    print("Step 3: Which tools do you use?")
    print("  Options: R, Stata, Python (comma-separated)")
    tools_input = prompt("Tools", "R, Stata, Python")
    tools = [t.strip().lower() for t in tools_input.split(",")]
    print()

    # Step 4: Stata path
    stata_path = None
    if "stata" in tools:
        default_stata = "/Applications/StataNow/StataMP.app/Contents/MacOS/stata-mp"
        stata_path = prompt("Stata executable path", default_stata)
    print()

    # Step 5: Confirm
    print("Summary:")
    print(f"  Project:    {project_name}")
    print(f"  Institution: {institution}")
    print(f"  Branch:     {branch}")
    print(f"  Domain:     {domain}")
    print(f"  Tools:      {', '.join(tools)}")
    if stata_path:
        print(f"  Stata path: {stata_path}")
    print()

    confirm = prompt("Proceed? (y/n)", "y")
    if confirm.lower() != "y":
        print("Aborted.")
        sys.exit(0)

    print()
    print("Applying configuration...")

    # Apply changes
    fill_claude_md(project_name, institution, branch)
    update_settings_local(stata_path)

    print()
    print("Done! Next steps:")
    print("  1. Add your bibliography entries to Bibliography_base.bib")
    print("  2. Place input data in input/")
    print("  3. Start Claude Code and begin working")
    print("  4. Use /context-status to check session health")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new academic project")
    parser.add_argument("--non-interactive", action="store_true", help="Use all defaults (for testing)")
    args = parser.parse_args()

    if args.non_interactive:
        # Auto-fill with defaults for testing
        fill_claude_md("My Research Project", "My University", "main")
        update_settings_local()
    else:
        main()
