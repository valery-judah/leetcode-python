
.PHONY: install linters precommit test lint type fmt ci badge cov-html

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
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --cov=tasks --cov-report=term-missing --cov-report=xml:coverage.xml

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
	$(PYTHON) -m mypy tasks || true  # tasks may contain stubs early

ci: test lint type

cov-html:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --cov=tasks --cov-report=html
