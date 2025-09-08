
.PHONY: install linters precommit test lint type fmt ci \
        format-md fmt-json validate-stats validate-ids \
        tracks-report tracks-table markdown build

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

TEST_REPORT_DIR := .reports
TEST_REPORT_FILE := $(TEST_REPORT_DIR)/pytest-last.txt

test:
	@mkdir -p $(TEST_REPORT_DIR)
	@PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q > $(TEST_REPORT_FILE) 2>&1; \
	status=$$?; \
	if [ $$status -eq 0 ]; then \
	  echo "Test: all OK"; \
	else \
	  summary=$$(grep -E '^=+ .* (failed|error)' $(TEST_REPORT_FILE) | tail -n1); \
	  if [ -n "$$summary" ]; then \
	    count=$$(echo "$$summary" | grep -Eo '[0-9]+ (failed|error|errors)' | awk '{s+=$$1} END{print s+0}'); \
	  else \
	    count=$$(grep -E '^(ERROR|FAILED) ' $(TEST_REPORT_FILE) | wc -l | awk '{print $$1}'); \
	  fi; \
	  echo $$count; \
	fi; \
	exit $$status

# Optional: verbose tests for CI or local debugging
test-ci:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q

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

# Validate stats.json files against the JSON Schema
validate-stats:
	$(PYTHON) scripts/validate_stats.py

# Validate that `problems/` folder IDs and slugs match the archive metadata
validate-ids:
	$(PYTHON) scripts/validate_problem_ids.py --strict

# Generate markdown reports for tracks in tracks/
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
	@echo "--- Formatting JSON ---"
	make fmt-json
	@echo "--- Running linters ---"
	make lint
	@echo "--- Type checking ---"
	make type
# 	@echo "--- Running tests ---"
# 	make test
	@echo "--- Validating stats schema ---"
	make validate-stats
	@echo "--- Generating Markdown (tracks + README table) ---"
	make markdown
	@echo "--- Running pre-commit on all files (final step) ---"
	make precommit-all

# Target: format-md
# Automatically formats all Markdown files in the repository using mdformat.
# This target should be used locally to fix files.
format-md:
	@echo "--- Formatting Markdown files with mdformat ---"
	$(PYTHON) -m mdformat README.md docs problems tracks archive topics

# JSON formatting via pre-commit hook (pretty-format-json)
fmt-json:
	@echo "--- Formatting JSON files (pre-commit: pretty-format-json) ---"
	$(PYTHON) -m pre_commit run --hook-stage manual pretty-format-json --all-files || true

# Run all pre-commit hooks across the repo.
# - In CI (CI=true), fail if hooks find issues.
# - Locally, allow hooks to modify files; re-run once; never fail build.
precommit-all:
ifeq ($(CI),true)
	$(PYTHON) -m pre_commit run --all-files
else
	$(PYTHON) -m pre_commit run --all-files || \
	  (echo "--- Re-running pre-commit after auto-fixes ---" && $(PYTHON) -m pre_commit run --all-files) || true
endif
