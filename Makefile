# Makefile for Claude Code Academic Workflow
# Usage: make compile FILE=output/slides/Lecture01.tex

# Default values (override with: make compile FILE=path/to/file.tex)
FILE ?=
QUALITY_SCRIPT := scripts/quality_score.py
TEX_INPUTS := TEXINPUTS=../scripts/latex_preambles:$$TEXINPUTS
BIB_INPUTS := BIBINPUTS=..:$$BIBINPUTS
STATA := $(shell python3 -c "import json; d=json.load(open('.claude/settings.local.json')); print(d.get('env',{}).get('STATA_PATH','stata-mp'))" 2>/dev/null || echo stata-mp)

.PHONY: compile quality clean verify init help

help:
	@echo "Available targets:"
	@echo "  make compile FILE=output/slides/Lecture01.tex   Compile Beamer slides (3-pass XeLaTeX + bibtex)"
	@echo "  make quality FILE=output/slides/Lecture01.tex     Run quality scoring on a file"
	@echo "  make verify FILE=output/slides/Lecture01.tex      Compile + quality check"
	@echo "  make clean                                        Remove LaTeX build artifacts"
	@echo "  make init                                          Run project initialization script"
	@echo "  make stata FILE=scripts/do_file.do                Run a Stata do-file"

# Compile Beamer slides (3-pass XeLaTeX + bibtex)
compile:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make compile FILE=output/slides/Lecture01.tex"; exit 1; fi
	@echo "Compiling $(FILE)..."
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) xelatex -interaction=nonstopmode $$(basename $(FILE))
	cd $$(dirname $(FILE)) && $(BIB_INPUTS) bibtex $$(basename $(FILE) .tex)
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) xelatex -interaction=nonstopmode $$(basename $(FILE))
	cd $$(dirname $(FILE)) && $(TEX_INPUTS) xelatex -interaction=nonstopmode $$(basename $(FILE))
	@echo "Done. Output: $$(dirname $(FILE))/$$(basename $(FILE) .tex).pdf"

# Run quality scoring
quality:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make quality FILE=output/slides/Lecture01.tex"; exit 1; fi
	python3 $(QUALITY_SCRIPT) $(FILE)

# Compile + quality check
verify: compile quality

# Run a Stata do-file
stata:
	@if [ -z "$(FILE)" ]; then echo "Error: FILE is required. Usage: make stata FILE=scripts/file.do"; exit 1; fi
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
	python3 scripts/init_project.py
