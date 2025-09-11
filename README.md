# LeetCode Python Workspace

Track-first workflow for interview prep. Organize your practice into curated “tracks,” solve problems, and watch your progress update automatically in the README.

This repo ships with predefined tracks you can use out of the box, and you can also create your own. See [Tracks](#tracks) to view progress, copy built-in tracks, and build custom ones.

All problems live under `problems/`. Each problem folder contains the description, solution(s), reasoning, and progress stats. Example: [`problems/0169-majority-element/readme.md`](/problems/0169-majority-element/readme.md).

# Tracks

Tracks are curated problem lists that drive your learning plan and progress tracking.

- Define tracks in `tracks/*.yaml` (custom or copied from predefined ones in [archive folder](/archive/)).
- Generate per-track reports and the README table from your problem stats.
- “Done” is counted from each problem’s `stats.json` (`optimal_solution: true`).

Current tracks and progress:

<!-- BEGIN_TRACKS_TABLE -->
| Track | Main | Ext | Total | Done | Progress | Linked | Unlinked |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Foundations — Arrays, Hashing, Two-Pointers, Prefix, Stack](tracks/track_0_foundations.md) | 17 | 8 | 25 | 2 | 8%                 | 25 | 0 |
| [Sliding Window — Fixed and Dynamic](tracks/track_1_sliding_window.md) | 12 | 6 | 18 | 0 | 0%                 | 16 | 2 |
| [Two Pointers — Advanced and In‑Place Transforms](tracks/track_2_two_pointers_advanced.md) | 12 | 8 | 20 | 0 | 0%                 | 20 | 0 |
| [Binary Search — Predicates, Partitions, and Heaps](tracks/track_3_binary_search_heaps.md) | 12 | 6 | 18 | 0 | 0%                 | 18 | 0 |
| [Intervals — Sorting, Merging, and Greedy Scheduling](tracks/track_4_intervals.md) | 12 | 10 | 22 | 0 | 0%                 | 22 | 0 |
| [NeetCode 250 — Arrays & Hashing](tracks/track_neetcode_0_arrays_hashing.md) | 22 | 0 | 22 | 1 | 5%                 | 22 | 0 |
| [NeetCode 250 — Two Pointers](tracks/track_neetcode_1_two_pointers.md) | 13 | 0 | 13 | 1 | 8%                 | 13 | 0 |
| [NeetCode 250 — Sliding Window](tracks/track_neetcode_2_sliding_window.md) | 9 | 0 | 9 | 0 | 0%                 | 9 | 0 |
| [NeetCode 250 — Stack](tracks/track_neetcode_3_stack.md) | 15 | 0 | 15 | 0 | 0%                 | 15 | 0 |
| [NeetCode 250 — Binary Search](tracks/track_neetcode_4_binary_search.md) | 14 | 0 | 14 | 0 | 0%                 | 14 | 0 |
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

<!-- - How to trigger:

  - Run tests for a specific problem: `pytest -q -k "0001-two-sum"`
  - Or run the full suite: `make test`
  - On success, you’ll see a note like: “Updated stats.json fields for: 0001-two-sum”.
  - Then regenerate reports/tables: `make markdown` -->

Example:

```bash
make install            # ensure dev deps (jsonschema, PyYAML)
python scripts/new_problem.py contains-duplicate 217 --full-rewrite
make validate-stats
make tracks-report
code tracks/track_0_foundations.md
```
