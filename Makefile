
.PHONY: install linters precommit test lint type fmt ci badge cov-html \
        format-md lint-md fix-md validate-stats tracks-report tracks-table markdown build

# Prefer project venv Python, then python3, then python
PYTHON := $(shell if [ -x "./venv/bin/python" ]; then echo "./venv/bin/python"; \
                  elif command -v python3 >/dev/null 2>&1; then command -v python3; \
                  elif command -v python >/dev/null 2>&1; then command -v python; \
                  else echo python; fi)

install:
	$(PYTHON) -m pip install -r requirements.txt -r requirements-dev.txt

linters:  # alias
	make lint

precommit:
	pre-commit install

test:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --cov=problems --cov-report=term-missing --cov-report=xml:coverage.xml

badge:
	@mkdir -p docs/badges
	PYTHONWARNINGS="ignore::UserWarning" genbadge coverage -i coverage.xml -o docs/badges/coverage.svg \
		|| echo "Install dev deps first: make install"

lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m black --check .

fmt:
	$(PYTHON) -m ruff check . --fix
	$(PYTHON) -m black .

# Optional: run linters on legacy code too
lint-legacy:
	$(PYTHON) -m ruff check old_leetcode
	$(PYTHON) -m black --check old_leetcode

fmt-legacy:
	$(PYTHON) -m ruff check old_leetcode --fix || true
	$(PYTHON) -m black old_leetcode || true

type:
	$(PYTHON) -m mypy common || true  # problems may contain stubs early

ci: test lint type validate-stats

cov-html:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --cov=problems --cov-report=html

# Validate stats.json files against the JSON Schema
validate-stats:
	$(PYTHON) scripts/validate_stats.py

# Generate markdown reports for all tracks
tracks-report:
	$(PYTHON) scripts/generate_track_reports.py

# Update README tracks table from tracks/*.md
tracks-table:
	$(PYTHON) scripts/update_tracks_table.py

# Markdown docs pipeline: generate track reports and update README table
markdown: tracks-report tracks-table

# Build: run formatters, linters, type checks, tests, stats validation, and track reports
build:
	@echo "--- Running code formatters ---"
	make fmt
	@echo "--- Formatting Markdown ---"
	make format-md
	@echo "--- Running linters ---"
	make lint
	@echo "--- Linting Markdown ---"
	make lint-md || true
	@echo "--- Type checking ---"
	make type
	@echo "--- Running tests ---"
	make test
	@echo "--- Validating stats schema ---"
	make validate-stats
	@echo "--- Generating Markdown (tracks + README table) ---"
	make markdown
	@echo "--- Build complete ---"

# Target: format-md
# Automatically formats all Markdown files in the repository using mdformat.
# This target should be used locally to fix files.
format-md:
	@echo "--- Formatting Markdown files with mdformat ---"
	$(PYTHON) -m mdformat .

# Target: fix-md
# Automatically fixes all supported Markdown linting issues using markdownlint.
# Respects the .gitignore file. This target should be used locally.
fix-md:
	@echo "--- Fixing Markdown files with markdownlint ---"
	markdownlint --fix "**/*.md" --ignore-path .gitignore .

# Target: lint-md
# Checks Markdown files for formatting and style issues without modifying them.
# Ideal for CI pipelines. Fails if any issues are found.
lint-md:
	@echo "--- Checking Markdown formatting (mdformat) ---"
	$(PYTHON) -m mdformat --check .
	@echo "--- Linting Markdown files (markdownlint) ---"
	markdownlint --ignore-path .gitignore . --config .markdownlint.json
