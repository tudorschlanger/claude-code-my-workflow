#!/usr/bin/env python3
"""
Project initialization script for Claude Code academic workflow.

Detects installed tools, sets up language environments (conda, renv),
saves executable paths, and fills configuration placeholders.

Usage:
    python3 scripts/src/Python/init_project.py
    make init
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys


# =============================================================================
# Utilities
# =============================================================================

def prompt(text, default=""):
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


def slugify(name):
    """'My Cool Project' -> 'my-cool-project' (for conda env names)."""
    s = name.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")


def slugify_path(name):
    """'My Cool Project' -> 'my_cool_project' (for folder names)."""
    return name.replace(" ", "_").lower()


# =============================================================================
# Tool Detection
# =============================================================================

def _run(cmd, timeout=15):
    """Run a command, return (stdout, stderr, returncode). Never raises."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip(), r.stderr.strip(), r.returncode
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "", "", 1


def _which(cmd):
    """Return absolute path to command, or None."""
    stdout, _, rc = _run(["which", cmd])
    return stdout if rc == 0 and stdout else None


def detect_python():
    path = _which("python3")
    if not path:
        return None
    stdout, _, rc = _run(["python3", "--version"])
    version = stdout.replace("Python ", "") if rc == 0 else "unknown"
    return {"path": path, "version": version}


def detect_conda():
    path = _which("conda")
    if not path:
        return None
    stdout, _, rc = _run(["conda", "--version"])
    version = stdout.replace("conda ", "") if rc == 0 else "unknown"
    return {"path": path, "version": version}


def detect_r():
    path = _which("Rscript")
    if not path:
        return None
    # Rscript --version prints to stderr
    _, stderr, rc = _run(["Rscript", "--version"])
    version = "unknown"
    if rc == 0 and stderr:
        m = re.search(r"version (\d+\.\d+\.\d+)", stderr)
        if m:
            version = m.group(1)
    return {"path": path, "version": version}


def detect_stata(custom_path=None):
    path = custom_path
    if path and os.path.isfile(path) and os.access(path, os.X_OK):
        return {"path": path, "version": "-"}
    # Try common macOS locations
    for candidate in [
        "/Applications/StataNow/StataMP.app/Contents/MacOS/stata-mp",
        "/Applications/Stata/StataMP.app/Contents/MacOS/stata-mp",
        "/usr/local/bin/stata-mp",
    ]:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return {"path": candidate, "version": "-"}
    return None


def detect_latex_tool(cmd):
    path = _which(cmd)
    if not path:
        return None
    stdout, _, rc = _run([cmd, "--version"])
    version = "unknown"
    if rc == 0 and stdout:
        first_line = stdout.split("\n")[0]
        # Extract version-like string
        m = re.search(r"(\d{4}|\d+\.\d+)", first_line)
        if m:
            version = m.group(1)
    return {"path": path, "version": version}


def detect_all_tools(selected_tools, stata_path=None):
    """Detect all tools. Returns dict of tool_name -> {path, version} or None."""
    detected = {}

    if "python" in selected_tools:
        detected["python"] = detect_python()
        detected["conda"] = detect_conda()
    if "r" in selected_tools:
        detected["r"] = detect_r()
    if "stata" in selected_tools:
        detected["stata"] = detect_stata(stata_path)

    # Always detect LaTeX
    detected["xelatex"] = detect_latex_tool("xelatex")
    detected["bibtex"] = detect_latex_tool("bibtex")
    detected["pdflatex"] = detect_latex_tool("pdflatex")

    return detected


def print_detection_summary(detected):
    print("\n  Tool Detection Results:")
    print("  " + "-" * 50)
    for name, info in detected.items():
        if info:
            print(f"  {name:<12} {info['version']:<12} {info['path']}")
        else:
            print(f"  {name:<12} {'not found':<12} -")
    print("  " + "-" * 50)
    print()


# =============================================================================
# Directory Cleanup
# =============================================================================

def cleanup_unused_tools(selected_tools):
    """Delete directories for tools not selected."""
    if "stata" not in selected_tools:
        d = "scripts/src/Stata"
        if os.path.isdir(d):
            shutil.rmtree(d)
            print(f"  Removed {d}/")

    if "r" not in selected_tools:
        d = "scripts/src/R"
        if os.path.isdir(d):
            shutil.rmtree(d)
            print(f"  Removed {d}/")

    if "python" not in selected_tools:
        f = "scripts/src/Python/plot_style.py"
        if os.path.isfile(f):
            os.remove(f)
            print(f"  Removed {f}")


# =============================================================================
# Environment Setup
# =============================================================================

def setup_conda_env(project_slug, python_version, conda_path):
    """Create a conda environment. Returns env python path or None."""
    # Check if env already exists
    stdout, _, rc = _run(["conda", "env", "list", "--json"], timeout=30)
    if rc == 0:
        try:
            envs = json.loads(stdout).get("envs", [])
            if any(project_slug in e for e in envs):
                print(f"  Conda env '{project_slug}' already exists, skipping")
                # Get the python path from existing env
                py_out, _, _ = _run(
                    ["conda", "run", "-n", project_slug, "which", "python3"],
                    timeout=30,
                )
                return py_out if py_out else None
        except json.JSONDecodeError:
            pass

    # Extract major.minor from version string
    m = re.match(r"(\d+\.\d+)", python_version)
    py_ver = m.group(1) if m else "3"

    print(f"  Creating conda environment '{project_slug}' (python={py_ver})...")
    _, stderr, rc = _run(
        ["conda", "create", "-n", project_slug, f"python={py_ver}", "-y"],
        timeout=300,
    )
    if rc != 0:
        print(f"  Warning: conda create failed: {stderr[:200]}")
        return None

    # Generate environment.yml
    yml = (
        f"name: {project_slug}\n"
        f"dependencies:\n"
        f"  - python={py_ver}\n"
        f"  - matplotlib\n"
        f"  - pandas\n"
        f"  - numpy\n"
    )
    write_file("environment.yml", yml)
    print("  Created environment.yml")

    # Get conda env python path
    py_out, _, _ = _run(
        ["conda", "run", "-n", project_slug, "which", "python3"],
        timeout=30,
    )
    if py_out:
        print(f"  Conda env python: {py_out}")
    return py_out


def setup_renv(r_path):
    """Initialize renv for R. Returns True on success."""
    if os.path.isdir("renv"):
        print("  renv/ already exists, skipping")
        return True

    print("  Initializing renv...")
    cmd = (
        'options(renv.consent=TRUE); '
        'if (!requireNamespace("renv", quietly=TRUE)) '
        'install.packages("renv", repos="https://cloud.r-project.org"); '
        'renv::init(bare=TRUE)'
    )
    _, stderr, rc = _run([r_path, "-e", cmd], timeout=120)
    if rc != 0:
        print(f"  Warning: renv init failed: {stderr[:200]}")
        return False

    print("  renv initialized")

    # Add renv/ to .gitignore if not present
    update_gitignore(["renv/"])
    return True


# =============================================================================
# Configuration File Updates
# =============================================================================

def fill_claude_md(project_name, institution, branch, tool_config):
    """Replace placeholders and add tool configuration section."""
    path = "CLAUDE.md"
    content = read_file(path)

    # Standard placeholder replacements
    content = content.replace("[YOUR PROJECT NAME]", project_name)
    content = content.replace("[YOUR INSTITUTION]", institution)
    content = content.replace("[YOUR-PROJECT]", slugify_path(project_name))

    # Replace Stata placeholder with actual path (or generic message)
    stata = tool_config.get("stata")
    if stata:
        content = content.replace(
            "[PATH TO STATA - configure in .claude/settings.local.json]",
            stata["path"],
        )
        content = content.replace("[STATA PATH]", stata["path"])
    else:
        # Remove the Stata section if not using Stata
        content = re.sub(
            r"## Stata\n.*?(?=\n---|\n## )",
            "",
            content,
            flags=re.DOTALL,
        )

    # Build tool configuration section
    tool_section = _build_tool_config_section(tool_config)

    # Insert before "## Current Project State" or append
    marker = "## Current Project State"
    if "## Tool Configuration" in content:
        # Replace existing section
        content = re.sub(
            r"## Tool Configuration\n.*?(?=\n## Current Project State|\Z)",
            tool_section + "\n",
            content,
            flags=re.DOTALL,
        )
    elif marker in content:
        content = content.replace(marker, tool_section + "\n" + marker)
    else:
        content += "\n" + tool_section

    write_file(path, content)
    print(f"  Updated {path}")


def _build_tool_config_section(tool_config):
    """Build the ## Tool Configuration markdown section."""
    lines = [
        "## Tool Configuration",
        "",
        "| Tool | Version | Path |",
        "|------|---------|------|",
    ]

    display_names = {
        "python": "Python",
        "conda": "Conda",
        "r": "R (Rscript)",
        "stata": "Stata",
        "xelatex": "XeLaTeX",
        "bibtex": "BibTeX",
        "pdflatex": "pdflatex",
    }

    for key in ["python", "conda", "r", "stata", "xelatex", "bibtex", "pdflatex"]:
        info = tool_config.get(key)
        if info:
            name = display_names.get(key, key)
            lines.append(f"| {name} | {info['version']} | `{info['path']}` |")

    # Add run commands
    lines.append("")
    lines.append("### Run Commands")
    lines.append("")
    lines.append("```bash")

    if tool_config.get("python"):
        conda_env = None
        if tool_config.get("conda"):
            conda_env = tool_config.get("_conda_env_name")
        if conda_env:
            lines.append(f"# Python (conda env)")
            lines.append(
                f"conda run -n {conda_env} python3 scripts/src/Python/script.py"
            )
        else:
            lines.append(f"# Python")
            lines.append(
                f"{tool_config['python']['path']} scripts/src/Python/script.py"
            )

    if tool_config.get("r"):
        lines.append(f"# R")
        lines.append(f"{tool_config['r']['path']} scripts/src/R/script.R")

    if tool_config.get("stata"):
        lines.append(f"# Stata")
        lines.append(
            f"{tool_config['stata']['path']} -b do scripts/src/Stata/script.do"
        )

    if tool_config.get("xelatex"):
        bibtex_path = tool_config.get("bibtex", {}).get("path", "bibtex")
        lines.append(f"# Compile slides")
        lines.append(
            f"cd drafts/slides && TEXINPUTS=../latex_files:$TEXINPUTS "
            f"{tool_config['xelatex']['path']} -interaction=nonstopmode file.tex"
        )
        lines.append(
            f"BIBINPUTS=../latex_files:$BIBINPUTS {bibtex_path} file"
        )

    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def fill_latex_headers(project_name):
    """Replace [YOUR PROJECT NAME] in LaTeX preambles."""
    for path in [
        "drafts/latex_files/header_slides.tex",
        "drafts/latex_files/header_doc.tex",
    ]:
        if os.path.isfile(path):
            content = read_file(path)
            content = content.replace("[YOUR PROJECT NAME]", project_name)
            write_file(path, content)
            print(f"  Updated {path}")


def fill_domain_reviewer(domain):
    """Replace [YOUR DOMAIN] in domain-reviewer agent."""
    path = ".claude/agents/domain-reviewer.md"
    if os.path.isfile(path):
        content = read_file(path)
        content = content.replace("[YOUR DOMAIN]", domain)
        write_file(path, content)
        print(f"  Updated {path}")


def fill_knowledge_base(project_name):
    """Replace [YOUR PROJECT NAME] in knowledge-base template."""
    path = ".claude/rules/knowledge-base-template.md"
    if os.path.isfile(path):
        content = read_file(path)
        content = content.replace("[YOUR PROJECT NAME]", project_name)
        write_file(path, content)
        print(f"  Updated {path}")


# =============================================================================
# Settings & Gitignore
# =============================================================================

def update_settings_local(tool_paths):
    """Write detected tool paths to .claude/settings.local.json."""
    path = ".claude/settings.local.json"

    if os.path.exists(path):
        try:
            data = json.loads(read_file(path))
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    if "env" not in data:
        data["env"] = {}
    if "permissions" not in data:
        data["permissions"] = {"allow": []}

    # Merge tool paths (only set keys with values)
    for key, value in tool_paths.items():
        if value:
            data["env"][key] = value

    # Enable sandbox by default with raw data protection
    if "sandbox" not in data:
        data["sandbox"] = {}
    data["sandbox"]["enabled"] = True
    if "filesystem" not in data["sandbox"]:
        data["sandbox"]["filesystem"] = {}
    deny_write = data["sandbox"]["filesystem"].get("denyWrite", [])
    if "./data/raw" not in deny_write:
        deny_write.append("./data/raw")
        data["sandbox"]["filesystem"]["denyWrite"] = deny_write
    # Exclude tools that break under sandbox
    if "excludedCommands" not in data["sandbox"]:
        data["sandbox"]["excludedCommands"] = []
    excluded = data["sandbox"]["excludedCommands"]
    if "gh *" not in excluded:
        excluded.append("gh *")

    write_file(path, json.dumps(data, indent=2) + "\n")
    print(f"  Updated {path}")


def install_git_hooks():
    """Copy git hooks from .claude/hooks/ to .git/hooks/."""
    hooks = [
        ("git-pre-commit", "pre-commit"),
        ("git-commit-msg", "commit-msg"),
    ]
    git_hooks_dir = ".git/hooks"
    if not os.path.isdir(git_hooks_dir):
        print("  Warning: .git/hooks/ not found — skipping hook installation")
        return

    for src_name, dst_name in hooks:
        src = os.path.join(".claude", "hooks", src_name)
        dst = os.path.join(git_hooks_dir, dst_name)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            os.chmod(dst, 0o755)
    print("  Installed git hooks (pre-commit quality gate + conventional commits)")


def exclude_git_from_dropbox():
    """On macOS, mark .git/ as ignored by Dropbox to prevent sync conflicts."""
    import platform
    if platform.system() != "Darwin":
        return
    if not os.path.isdir(".git"):
        return
    try:
        result = subprocess.run(
            ["xattr", "-w", "com.dropbox.ignored", "1", ".git"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            print("  Excluded .git/ from Dropbox sync (prevents corruption)")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass


def update_gitignore(entries):
    """Add entries to .gitignore if not already present."""
    path = ".gitignore"
    content = read_file(path) if os.path.isfile(path) else ""

    added = []
    for entry in entries:
        if entry not in content:
            added.append(entry)

    if added:
        if not content.endswith("\n"):
            content += "\n"
        content += "\n# Environment (added by init)\n"
        for entry in added:
            content += entry + "\n"
        write_file(path, content)
        for entry in added:
            print(f"  Added '{entry}' to .gitignore")


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 60)
    print("  Claude Code Academic Workflow — Project Init")
    print("=" * 60)
    print()

    # --- Phase 1: Gather input ---
    print("Step 1: Project information")
    project_name = prompt("Project name")
    institution = prompt("Institution")
    branch = prompt("Git branch", "main")
    print()

    print("Step 2: Domain")
    domain = prompt("Domain (e.g., economics, finance, political science)", "economics")
    print()

    print("Step 3: Which tools do you use?")
    print("  Options: R, Stata, Python (comma-separated)")
    tools_input = prompt("Tools", "R, Stata, Python")
    tools = [t.strip().lower() for t in tools_input.split(",")]
    print()

    # --- Phase 2: Detect tools ---
    print("Step 4: Detecting installed tools...")
    detected = detect_all_tools(tools)

    # If Stata selected but not auto-detected, prompt for path
    stata_path = None
    if "stata" in tools and not detected.get("stata"):
        print("  Stata not found at common locations.")
        stata_path = prompt("Stata executable path (or leave blank to skip)", "")
        if stata_path:
            detected["stata"] = detect_stata(stata_path)
        print()
    print_detection_summary(detected)

    # Warn about missing tools
    for tool in tools:
        if tool in detected and detected[tool] is None:
            print(f"  Warning: {tool} selected but not found on this machine")

    # --- Summary & confirm ---
    print("Summary:")
    print(f"  Project:     {project_name}")
    print(f"  Institution: {institution}")
    print(f"  Branch:      {branch}")
    print(f"  Domain:      {domain}")
    print(f"  Tools:       {', '.join(tools)}")
    if "python" in tools and detected.get("conda"):
        print(f"  Conda env:   {slugify(project_name)}")
    if "r" in tools and detected.get("r"):
        print(f"  R env:       renv (bare init)")
    print()

    confirm = prompt("Proceed? (y/n)", "y")
    if confirm.lower() != "y":
        print("Aborted.")
        sys.exit(0)

    print()
    print("Applying configuration...")
    print()

    # --- Phase 3: Cleanup ---
    cleanup_unused_tools(tools)

    # --- Phase 4: Set up environments ---
    conda_env_python = None
    conda_env_name = None
    if "python" in tools and detected.get("conda"):
        conda_env_name = slugify(project_name)
        python_ver = detected["python"]["version"] if detected.get("python") else "3"
        conda_env_python = setup_conda_env(conda_env_name, python_ver, detected["conda"]["path"])

    if "r" in tools and detected.get("r"):
        setup_renv(detected["r"]["path"])

    print()

    # --- Phase 5: Build paths dict ---
    tool_paths = {}
    if detected.get("python"):
        tool_paths["PYTHON_PATH"] = detected["python"]["path"]
    if detected.get("conda"):
        tool_paths["CONDA_PATH"] = detected["conda"]["path"]
    if conda_env_name:
        tool_paths["CONDA_ENV"] = conda_env_name
    if conda_env_python:
        tool_paths["CONDA_PYTHON_PATH"] = conda_env_python
    if detected.get("r"):
        tool_paths["R_PATH"] = detected["r"]["path"]
    if detected.get("stata"):
        tool_paths["STATA_PATH"] = detected["stata"]["path"]
    if detected.get("xelatex"):
        tool_paths["XELATEX_PATH"] = detected["xelatex"]["path"]
    if detected.get("bibtex"):
        tool_paths["BIBTEX_PATH"] = detected["bibtex"]["path"]
    if detected.get("pdflatex"):
        tool_paths["PDFLATEX_PATH"] = detected["pdflatex"]["path"]

    # --- Phase 6: Update config files ---
    # Attach conda env name for CLAUDE.md run commands
    tool_config = dict(detected)
    if conda_env_name:
        tool_config["_conda_env_name"] = conda_env_name

    fill_claude_md(project_name, institution, branch, tool_config)
    fill_latex_headers(project_name)
    fill_domain_reviewer(domain)
    fill_knowledge_base(project_name)
    update_settings_local(tool_paths)
    install_git_hooks()
    exclude_git_from_dropbox()

    print()
    print("Done! Next steps:")
    print("  1. Add bibliography entries to drafts/latex_files/Bibliography_base.bib")
    print("  2. Place input data in data/raw/")
    if conda_env_name:
        print(f"  3. Activate conda: conda activate {conda_env_name}")
    print("  4. Start Claude Code: claude")
    print("  5. Run /sandbox and select auto-allow for hands-free Bash commands")
    print("  6. Use /context-status to check session health")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new academic project")
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Fill placeholders with defaults only (no env setup, no cleanup)",
    )
    args = parser.parse_args()

    if args.non_interactive:
        # Safe mode: fill placeholders only, detect tools, no destructive ops
        detected = detect_all_tools(["python", "r"], stata_path=None)
        tool_config = dict(detected)

        tool_paths = {}
        for key, name in [
            ("python", "PYTHON_PATH"),
            ("r", "R_PATH"),
            ("xelatex", "XELATEX_PATH"),
            ("bibtex", "BIBTEX_PATH"),
            ("pdflatex", "PDFLATEX_PATH"),
        ]:
            if detected.get(key):
                tool_paths[name] = detected[key]["path"]

        fill_claude_md("My Research Project", "My University", "main", tool_config)
        fill_latex_headers("My Research Project")
        fill_domain_reviewer("economics")
        fill_knowledge_base("My Research Project")
        update_settings_local(tool_paths)
    else:
        main()
