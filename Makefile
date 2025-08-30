
.PHONY: install linters precommit test lint type fmt ci

install:
	python -m pip install -r requirements-dev.txt

linters:  # alias
	make lint

precommit:
	pre-commit install

test:
	PYTHONDONTWRITEBYTECODE=1 python -m pytest -q

lint:
	ruff check .
	black --check .

fmt:
	ruff check . --fix
	black .

type:
	mypy tasks || true  # tasks may contain stubs early

ci: test lint type
