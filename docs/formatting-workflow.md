# Formatting & Linting Workflow

This guide shows how to format, lint, and quickly find issues.

## Single File

- Format + auto-fix:
  - `ruff check <path> --fix && black <path>`
- Verify clean:
  - `ruff check <path> && black --check <path>`
- Explain a specific rule:
  - `ruff rule E741` (replace `E741` with any rule code)

## Whole Repo

- Auto-fix + format everything:
  - `make fmt`
- Check only (no writes):
  - `make lint`
- Run tests:
  - `make test`

## Tasks Only (skip legacy noise)

- Fix current tasks code:
  - `ruff check tasks --fix && black tasks`
- Check tasks only:
  - `ruff check tasks && black --check tasks`

## Capture What’s Wrong (log to a file)

- Full repository log:
  - `ruff check . | tee fmt_errors.md && echo "\n--- BLACK ---" | tee -a fmt_errors.md && black --check . |& tee -a fmt_errors.md`
- Tasks-only log:
  - `ruff check tasks | tee fmt_errors.md && black --check tasks |& tee -a fmt_errors.md`

## Triage Tips

- Focus on one file:
  - `ruff check <file>`
- Filter by rule family:
  - `ruff check . --select E741` (or `UP`, `SIM`, `PT`, etc.)
- After auto-fixes, re-run to see remaining manual repairs:
  - `ruff check .`

## Optional

- Run pre-commit hooks across the repo:
  - `pre-commit run --all-files`
- Stop on first failing test (fast feedback):
  - `pytest -x -q`
