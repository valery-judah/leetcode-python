
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
	ruff check .
	black --check .

fmt:
	ruff check . --fix
	black .

# Optional: run linters on legacy code too
lint-legacy:
	ruff check old_leetcode
	black --check old_leetcode

fmt-legacy:
	ruff check old_leetcode --fix || true
	black old_leetcode || true

type:
	mypy tasks || true  # tasks may contain stubs early

ci: test badge lint type

cov-html:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --cov=tasks --cov-report=html
