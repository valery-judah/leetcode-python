# CI Workflow Improvements (Future Work)

This document captures proposed improvements to our GitHub Actions workflow for better security, speed, signal quality, and maintainability. It references the current workflow at `.github/workflows/ci.yml`.

## Goals

- Reduce supply‑chain risk and over‑privileged permissions.
- Speed up PR feedback and reduce CI costs.
- Increase signal quality (fail clearly on type/coverage regressions).
- Keep deployment isolated and predictable.

## Security

- Least privilege: move `permissions` from workflow to job level; grant `pages/id-token: write` only to the deploy job.
- Pin actions by commit SHA instead of floating tags (e.g., `actions/checkout@<sha>`).
- Add per‑job `timeout-minutes` (e.g., 10–15) to prevent hung runs.

## Speed & Cost

- Split CI into `build` (test/lint/type) and `deploy` jobs; run `deploy` only on pushes to `main`.
- Use a Python matrix (baseline 3.11 + optional 3.12). Upload artifacts and deploy only once (e.g., 3.11) to avoid duplication.
- Expand pip cache dependency paths to include `requirements.txt` and `requirements-dev.txt` (already done).
- Use `paths-ignore` for PRs to skip heavy jobs on docs‑only changes.

## Reliability & Signal

- Separate strict CI targets:
  - `test-ci` with coverage threshold (e.g., `--cov-fail-under=85`).
  - `type-ci` that fails on mypy errors (keep local `type` lenient if desired).
- Add `check-latest: true` to `actions/setup-python` to receive latest patch releases.
- Add a short job summary (coverage %, lint/type status) for quick PR triage.
- Optionally run `pre-commit` via `pre-commit/action` to mirror local hooks.

## Maintainability

- Attach the `github-pages` environment only to the deploy job.
- Reduce artifact retention (e.g., 14 days) to save storage.
- Keep step names concise and consistent; avoid redundant rebuilds (reuse coverage to build badge/HTML).

## Implementation Sketch

1) Makefile additions (keep existing local targets unchanged):

```Makefile
# Fail CI if coverage drops below threshold
test-ci:
 PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q \
  --cov=tasks --cov-report=term-missing \
  --cov-report=xml:coverage.xml --cov-fail-under=85

# Strict mypy for CI (no "|| true")
type-ci:
 mypy tasks
```

2) Split workflow into build and deploy jobs with job‑level permissions and matrix:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    paths-ignore:
      - 'docs/**'
      - 'README.md'
  workflow_dispatch:

jobs:
  build:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    timeout-minutes: 15
    strategy:
      matrix:
        python-version: [ '3.11', '3.12' ]
    steps:
      - uses: actions/checkout@<sha>
      - uses: actions/setup-python@<sha>
        with:
          python-version: ${{ matrix.python-version }}
          check-latest: true
          cache: pip
          cache-dependency-path: |
            requirements.txt
            requirements-dev.txt
      - name: Restore tool caches
        uses: actions/cache@<sha>
        with:
          path: |
            .mypy_cache
            .ruff_cache
            .pytest_cache
          key: tools-${{ runner.os }}-py${{ matrix.python-version }}-${{ hashFiles('pyproject.toml') }}
          restore-keys: |
            tools-${{ runner.os }}-py${{ matrix.python-version }}-
      - name: Install dependencies
        run: make install
      - name: Lint
        run: make lint
      - name: Type check (CI)
        run: make type-ci
      - name: Test (CI)
        run: make test-ci
      - name: Upload coverage artifacts
        if: always() && matrix.python-version == '3.11'
        uses: actions/upload-artifact@<sha>
        with:
          name: coverage
          path: |
            coverage.xml
            docs/badges/coverage.svg
            htmlcov
          if-no-files-found: ignore
          retention-days: 14
      - name: Build static site
        if: matrix.python-version == '3.11' && github.event_name == 'push' && github.ref == 'refs/heads/main'
        run: python scripts/build_pages.py
      - name: Upload Pages artifact
        if: matrix.python-version == '3.11' && github.event_name == 'push' && github.ref == 'refs/heads/main'
        uses: actions/upload-pages-artifact@<sha>
        with:
          path: site

  deploy:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: build
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@<sha>
```

3) Optional extras

- Pre-commit in CI:

```yaml
- uses: actions/checkout@<sha>
- uses: actions/setup-python@<sha>
- uses: pre-commit/action@<sha>
  with:
    extra_args: --all-files
```

- Job summary (after tests): use `actions/github-script` to parse `coverage.xml` and append a brief summary to `$GITHUB_STEP_SUMMARY`.

## Adoption Plan

- Add `test-ci` and `type-ci` targets to `Makefile`.
- Refactor `.github/workflows/ci.yml` using the sketch above; keep behavior identical for non‑deploy PRs.
- Pin actions to SHAs in the refactor PR; follow up to tune thresholds/timeouts as needed.
