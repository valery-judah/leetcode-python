# LeetCode Python Workspace

Track-first workflow for interview prep. Organize your practice into curated “tracks,” solve problems, and watch your progress update automatically in the README.

This repo ships with predefined tracks you can use out of the box, and you can also create your own. See [Tracks](#tracks) to view progress, copy built-in tracks, and build custom ones.

All problems live under `problems/`. Each problem folder contains the description, solution(s), reasoning, and progress stats. Example: `problems/0169-majority-element/readme.md`.

## Quick start

Common tasks

- Create a new problem: `python scripts/new_problem.py <slug> <id> [--difficulty ... --tags ... --url ...]`
- Run tests: `make test` (pytest, no `__pycache__`)
- Lint/format: `make lint` / `make fmt`
- Type check: `make type`
- Generate track reports and update README table: `make markdown`
- Full build (format → lint → type → test → validate stats → reports): `make build`

# Tracks

Tracks are curated problem lists that drive your learning plan and progress tracking.

- Define tracks in `tracks/*.yaml` (custom or copied from predefined ones).
- Generate per-track reports and the README table from your problem stats.
- “Done” is counted from each problem’s `stats.json` (`optimal_solution: true`).

Current tracks and progress:

<!-- BEGIN_TRACKS_TABLE -->
| Track | Main | Ext | Total | Done | Progress | Linked | Unlinked |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Foundations — Arrays, Hashing, Two-Pointers, Prefix, Stack](tracks/track_0_foundations.md) | 17 | 8 | 25 | 0 | 0%                 | 25 | 0 |
| [Hard Mix — Integration and Advanced Data Structures](tracks/track_10_hard_mix.md) | 13 | 6 | 19 | 0 | 0%                 | 14 | 5 |
| [Sliding Window — Fixed and Dynamic](tracks/track_1_sliding_window.md) | 12 | 6 | 18 | 0 | 0%                 | 10 | 8 |
| [Two Pointers — Advanced and In‑Place Transforms](tracks/track_2_two_pointers_advanced.md) | 12 | 8 | 20 | 0 | 0%                 | 17 | 3 |
| [Binary Search — Predicates, Partitions, and Heaps](tracks/track_3_binary_search_heaps.md) | 12 | 6 | 18 | 0 | 0%                 | 12 | 6 |
| [Intervals — Sorting, Merging, and Greedy Scheduling](tracks/track_4_intervals.md) | 12 | 10 | 22 | 0 | 0%                 | 14 | 8 |
| [Linked Lists — Invariants, Rewiring, and Structural Tricks](tracks/track_5_linked_lists.md) | 12 | 9 | 21 | 0 | 0%                 | 19 | 2 |
| [Trees — Traversals, BST Properties, and LCA](tracks/track_6_trees_basics.md) | 14 | 11 | 25 | 0 | 0%                 | 22 | 3 |
| [Graphs — BFS/DFS, Topo Sort, Union‑Find, Shortest Paths](tracks/track_7_graphs_basics.md) | 14 | 10 | 24 | 0 | 0%                 | 18 | 6 |
| [Dynamic Programming I — 1D States, Rolling Arrays, Greedy vs DP](tracks/track_8_dynamic_programming_i.md) | 12 | 7 | 19 | 0 | 0%                 | 17 | 2 |
| [Dynamic Programming II — 2D Tables, Sequences, and Palindromes](tracks/track_9_dynamic_programming_ii.md) | 14 | 9 | 23 | 0 | 0%                 | 21 | 2 |
<!-- END_TRACKS_TABLE -->

> Manage tracks in `tracks/*.yaml`. Generate reports and update this table with `make markdown` (or run the full pipeline with `make build`).

## Working With Tracks

- Create or update problems under `problems/NNNN-slug/`.
- Mark progress in `stats.json` (set `optimal_solution: true` when you’ve reached your target solution).
- Generate per-track reports and update the README progress table:
  - `make tracks-report` → updates `tracks/*.md`
  - `make tracks-table` → refreshes the table in this README
  - `make markdown` → runs both

### Use Predefined Tracks

Predefined track blueprints live in `archive/` (e.g., sliding window, two-pointers advanced, binary search & heaps, intervals, DP, graphs, trees, etc.). To use one:

1. Copy a YAML into `tracks/` (keep the name or rename):

   `cp archive/track_1_sliding_window.yaml tracks/`

1. Generate reports and update progress:

   `make markdown`

You’ll get a `tracks/track_1_sliding_window.md` report and an updated table here.

Optional: build a convenience list of problem IDs across the predefined tracks:

- `python extract_track_ids.py` → writes `track_ids.txt`

### Create Your Own Track

Create a minimal file like `tracks/my_track.yaml`:

```yaml
track: my_track
title: My Custom Track
description: Focused list for my next 2–3 weeks.
problems:
  - slug: two-sum
  - slug: group-anagrams
extensions:
  optional:
    - slug: valid-parentheses
```

Then generate the report and update the README table:

`make markdown`

## How to create a problem snapshot

```bash
# 1) Create a new problem skeleton (example)
python scripts/new_problem.py two-sum 1

# 2) Run tests and style checks
make test          # pytest (no __pycache__ written)
make lint          # ruff + black --check
make type          # mypy
```

Folders are created under `problems/NNNN-slug/`. Each contains:

- `readme.md` with clarifying questions, examples, approach, and complexity
- `solutions.py` starter (exports `Solution`, optionally `ALL_SOLUTIONS`)
- `stats.json` to fix information about progress for the task

## Stats and Track Reports

- Stats file: Each problem folder contains a `stats.json` scaffold (created by `scripts/new_problem.py`) that follows a strict JSON Schema (`templates/stats.schema.json`).

  - Validate across the repo: `make validate-stats`
  - Schema source: `templates/stats.schema.json`

- Track reports: Generate Markdown reports for all tracks in `tracks/` based on your `stats.json` progress.

  - Generate: `make tracks-report`
  - Output: `tracks/<track_name>.md` beside each YAML, e.g. `tracks/track_0_foundations.md`
  - Template: `templates/track_report.md.tpl`
  - Links in the reports are relative to the report location and point to `problems/NNNN-slug/readme.md`.

## Test-Driven Progress Updates

- Auto-baseline on pass: After pytest finishes, any problem whose default cases all pass gets `baseline_impl: true` written into its `problems/NNNN-slug/stats.json`.

  - Applies only to problems with a non-empty `TEST_CASES` in `solutions.py`.
  - Never downgrades or edits unrelated fields; only sets missing booleans to true.

- Optional auto-optimal: Opt in per problem by adding this to `solutions.py`:

  ```python
  # Mark this problem as optimal in stats.json when all default tests pass
  TEST_MARK_OPTIMAL_ON_PASS = True
  ```

- How to trigger:

  - Run tests for a specific problem: `pytest -q -k "0001-two-sum"`
  - Or run the full suite: `make test`
  - On success, you’ll see a note like: “Updated stats.json fields for: 0001-two-sum”.
  - Then regenerate reports/tables: `make markdown`

Example:

```bash
make install            # ensure dev deps (jsonschema, PyYAML)
python scripts/new_problem.py contains-duplicate 217 --full-rewrite
make validate-stats
make tracks-report
code tracks/track_0_foundations.md
```

## Tracks Format

- Location: define tracks in `tracks/*.yaml`; each YAML generates a sibling Markdown report (`tracks/*.md`).
- Core keys: `track` (id), `title`, `description`, `problems` (list), `extensions.optional` (list).
- Problem entry: `slug` (required), optional `title`, `difficulty`, and notes. The `slug` maps to `problems/*-<slug>/`.
- Links: report rows link to `problems/NNNN-slug/readme.md` when that directory exists; otherwise they render as plain text.
- Done calculation (README table): counts problems with `optimal_solution: true` in `problems/*-slug/stats.json`; includes both `problems` and `extensions.optional`.
- Totals (Main/Ext): derived from the generated track Markdown tables, so run `make markdown` (which runs reports first) to keep counts correct.
- Fallback: if a track has no YAML, the README table estimates progress from linked rows in the track Markdown.

Predefined tracks are available under `archive/`. Copy any `archive/track_*.yaml` into `tracks/` and run `make markdown` to activate it.

### Optional alias files (local convenience)

- Prefer a symlink alias which is resides in taks folder per problem, e.g. `0169.readme.md` → `readme.md`.
- Create with: `ln -s readme.md 0169.readme.md`.

### Multi-variant mode (compare approaches)

If you want to implement and compare multiple approaches for a problem:

```bash
python scripts/new_problem.py contains-duplicate 217 --multi
```

This scaffolds a consolidated `problems/0217-contains-duplicate/solutions.py` where you can define multiple classes (e.g., `BruteForce`, `SetBased`) and list them in `ALL_SOLUTIONS = [BruteForce, SetBased]`. The test file auto-discovers each class and runs the same cases for all variants. You can also optionally set `Solution = SetBased` as a default alias.

### Problem file conventions

- Header docstring at top of `solutions.py` for consistency:

  ```python
  """
  Problem 1: Two Sum
  https://leetcode.com/problems/two-sum/
  Difficulty: easy
  Tags: array,hash-map
  """
  ```

- Quick-run tests from a problem file directly (runs generic spec filtered to that problem):

  ```python
  if __name__ == "__main__":
      import subprocess, sys
      from pathlib import Path
      problem_dir = Path(__file__).parent
      root = problem_dir.parent
      problem_name = problem_dir.name
      subprocess.run([sys.executable, "-m", "pytest", "-q", str(root), "-k", problem_name], check=False)
  ```

- Canonical test cases live in `solutions.py` as `TEST_CASES`:

  - Implemented problems: `(label, arg1, ..., expected)`
  - Stub problems: `(label, args_tuple, kwargs_dict)` and `TEST_EXPECT_EXCEPTION = NotImplementedError`

## Developer workflow

- Lint: `make lint` (runs `ruff check .` and `black --check .`).
- Auto-fix: `make fmt` (runs `ruff check . --fix` and `black .`).
- Type check: `make type` (mypy on `problems/`).
- Tests: `make test` (runs `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q`).
  - To run manually without cache files: `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q`.
- Pre-commit: `make precommit` to install hooks; `pre-commit run --all-files` to run manually.
- VS Code Problems: Command Palette → “Problems: Run Problem” → `Test`, `Test: Active File`, or `New problem` (see `.vscode/problems.json`).
- Python Test Explorer: Enabled for pytest; discovery is configured in `.vscode/settings.json`.

Notes on multi-variant tests:

- Tests load `solutions.py` and read `ALL_SOLUTIONS` to parametrize variants. If `ALL_SOLUTIONS` is absent, they will use a single exported `Solution` class from `solutions.py`.

Key configs:

- Ruff/Black/Mypy: `pyproject.toml`.
- Pytest defaults: `pytest.ini`.
- Git hooks: `.pre-commit-config.yaml`.
- Editor problems/settings: `.vscode/problems.json`, `.vscode/settings.json`.
- Terminal bootstrap: `scripts/setup_terminal.sh` (creates venv, installs deps).

CI:

- GitHub Actions runs lint, type check, and tests on push/PR (`.github/workflows/ci.yml`).
- GitHub Pages: on pushes to `main`, CI builds `site/` and deploys it via Pages. Enable once in Settings → Pages → Build and deployment → Source: GitHub Actions. Site URL: `https://<your-username>.github.io/<this-repo>/` (or see Actions → Deployments → Pages for the exact link).

## Project Architecture

- Overview of structure, testing, and conventions: `docs/architecture.md`
- Workflow templates: `docs/cline-workflow-template.md`
- Patterns and active notes: `memory-bank/`

## Cline Assistant Workflow

This project is configured with a `.clinerules` file that enables a proactive assistant workflow with Cline. You can ask Cline to review your work, and it will act as an automated code reviewer to ensure your solution meets the project's standards.

## How to Use

1. **Implement Your Solution**: Complete your solution in the `solution.py` file and update the problem `readme.md` with your approach and complexity analysis.
1. **Request a Review**: In the chat, ask Cline to review your work. You can say something like:
   - "Cline, please review my solution for the two-sum problem."
   - "Can you check my work for `0001-two-sum`?"
1. **Review the Feedback**: Cline will perform the following checks and provide you with a summary of the results.

### Review Criteria

When you request a review, I will check your solution against the following criteria:

1. **Code Quality**: I will run the project's quality gates to ensure the code is clean and well-formatted.

   - `make fmt`: Checks for and fixes any formatting issues.
   - `make lint`: Checks for any linting errors.
   - `make type`: Performs static type checking.

1. **Correctness**: I will run the test suite to ensure that your solution is correct and passes all test cases.

   - `make test`: Executes the `pytest` test suite.

1. **Complexity Analysis**: I will check the problem `readme.md` to ensure that you have provided a clear and accurate analysis of the time and space complexity of your solution.

1. **Documentation**: I will verify that the solution is well-documented.

   - **Solution Docstring**: I will check for a comprehensive docstring in the `solve` method in `solution.py`.
   - **Approach Documentation**: I will check that the problem `readme.md` contains a clear explanation of your approach.

1. **Pattern Recognition**: I will remind you to consider if the solution uses a common pattern that should be added to the `memory-bank/patterns.md` file to help you build your collection of reusable patterns.

This workflow helps maintain code quality and ensures that all necessary documentation and logging are completed for each problem.

# Other: Markdown Formatting

You can use `markdownlint --fix "**/*.md" --ignore-path .gitignore .` command.

## Optional cool-off when enriching problems

```bash
python enrich_problem.py --start 1 --end 3700 --max-problems 300 --per-problem-sleep-min 15 --per-problem-sleep-max 25 --long-break-every 20 --long-break-sleep-min 180 --long-break-sleep-max 360 --micro-delay-min 2 --micro-delay-max 4 --backoff-base 30 --retries 3 --cool-off-threshold 2 --cool-off-sleep-min 600 --cool-off-sleep-max 900 --log-file enrich.log --log-level INFO
```
