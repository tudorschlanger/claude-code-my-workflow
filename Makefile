# Makefile for Claude Code Academic Workflow
# Usage: make compile FILE=drafts/slides/Lecture01.tex

# Default values (override with: make compile FILE=path/to/file.tex)
FILE ?=
QUALITY_SCRIPT := scripts/src/Python/quality_score.py

# Tool paths from .claude/settings.local.json (with fallback defaults)
_read_setting = $(shell python3 -c "import json; print(json.load(open('.claude/settings.local.json')).get('env',{}).get('$(1)','$(2)'))" 2>/dev/null || echo $(2))
PYTHON   := $(call _read_setting,PYTHON_PATH,python3)
RSCRIPT  := $(call _read_setting,R_PATH,Rscript)
STATA    := $(call _read_setting,STATA_PATH,stata-mp)
XELATEX  := $(call _read_setting,XELATEX_PATH,xelatex)
BIBTEX   := $(call _read_setting,BIBTEX_PATH,bibtex)
PDFLATEX := $(call _read_setting,PDFLATEX_PATH,pdflatex)

TEX_INPUTS := TEXINPUTS=../latex_files:$$TEXINPUTS
BIB_INPUTS := BIBINPUTS=../latex_files:$$BIBINPUTS BSTINPUTS=../latex_files:$$BSTINPUTS

.PHONY: compile quality clean verify init install-hooks help

help:
	@echo "Available targets:"
	@echo "  make compile FILE=drafts/slides/Lecture01.tex    Compile Beamer slides (3-pass XeLaTeX + bibtex)"
	@echo "  make quality FILE=drafts/slides/Lecture01.tex   Run quality scoring on a file"
	@echo "  make verify FILE=drafts/slides/Lecture01.tex    Compile + quality check"
	@echo "  make clean                                      Remove LaTeX build artifacts"
	@echo "  make init                                       Run project initialization script"
	@echo "  make stata FILE=scripts/src/Stata/analysis.do   Run a Stata do-file"
	@echo "  make install-hooks                               Install git hooks (quality gate + commit format)"

# Compile Beamer slides (3-pass XeLaTeX + bibtex)
compile:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make compile FILE=drafts/slides/Lecture01.tex"; exit 1; fi
	@echo "Compiling $(FILE)..."
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) $(XELATEX) -interaction=nonstopmode $$(basename $(FILE))
	cd $$(dirname $(FILE)) && $(BIB_INPUTS) $(BIBTEX) $$(basename $(FILE) .tex)
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) $(XELATEX) -interaction=nonstopmode $$(basename $(FILE))
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) $(XELATEX) -interaction=nonstopmode $$(basename $(FILE))
	@echo "Done. Output: $$(dirname $(FILE))/$$(basename $(FILE) .tex).pdf"

# Run quality scoring
quality:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make quality FILE=drafts/slides/Lecture01.tex"; exit 1; fi
	$(PYTHON) $(QUALITY_SCRIPT) $(FILE)

# Compile + quality check
verify: compile quality

# Run a Stata do-file
stata:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make stata FILE=scripts/src/Stata/analysis.do"; exit 1; fi
	$(STATA) -b do $(FILE)
	@echo "Stata log: $$(basename $(FILE) .do).log"

# Clean build artifacts
clean:
	find . -name "*.aux" -delete
	find . -name "*.bbl" -delete
	find . -name "*.blg" -delete
	find . -name "*.fls" -delete
	find . -name "*.fdb_latexmk" -delete
	find . -name "*.log" -not -name "*.Stata.log" -delete
	find . -name "*.nav" -delete
	find . -name "*.out" -delete
	find . -name "*.snm" -delete
	find . -name "*.toc" -delete
	find . -name "*.vrb" -delete
	find . -name "*.synctex.gz" -delete
	find . -name "*-blx.bib" -delete
	@echo "Cleaned build artifacts."

# Run project initialization
init:
	python3 scripts/src/Python/init_project.py

# Install git hooks (pre-commit quality gate + conventional commit format)
install-hooks:
	cp .claude/hooks/git-pre-commit .git/hooks/pre-commit
	cp .claude/hooks/git-commit-msg .git/hooks/commit-msg
	chmod +x .git/hooks/pre-commit .git/hooks/commit-msg
	@echo "Git hooks installed: pre-commit (quality gate) + commit-msg (conventional format)"
