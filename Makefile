.RECIPEPREFIX := >
.PHONY: deps fmt lint type test check docs docs-serve tracks validate tree new-problem

# Tooling
deps:
> python -m pip install -U pip
> pip install -r requirements-dev.txt

fmt:
> black .
> ruff format .

lint:
> ruff check .

type:
> mypy .

test:
> pytest -q

check: fmt lint type test

# Docs
docs:
> mkdocs build --strict

docs-serve:
> mkdocs serve -a 0.0.0.0:8000


# Repo-specific scripts
tracks:
> python scripts/generate_track_reports.py
> python scripts/update_tracks_table.py

validate:
> python scripts/validate_stats.py

new-problem:
> python scripts/new_problem.py

# Utility
tree:
> python - <<'PY' > project_tree.txt
> import os
> for root, dirs, files in os.walk('.', topdown=True):
>     dirs[:] = [d for d in dirs if d not in {'.git', '.devcontainer', '.venv', 'venv', '__pycache__', '.pytest_cache'}]
>     level = root.count(os.sep)
>     indent = '    ' * level
>     if level == 0:
>         print('.')
>     else:
>         print(f"{indent}└── {os.path.basename(root)}")
>     for f in sorted(files):
>         print(f"{indent}    ├── {f}")
PY
