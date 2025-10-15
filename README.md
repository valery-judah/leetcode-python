# LeetCode Python Workspace

> This repository is a Work in Progress.

Track-first workflow for interview prep. Organize your practice into curated “tracks,” solve problems, and
watch your progress update automatically in the README.

This repo ships with predefined tracks you can use out of the box, and you can also create your own. See
[Tracks](#tracks) to view progress, copy built-in tracks, and build custom ones.

All problems live under `problems/`. Each problem folder contains the description, solution(s), reasoning, and
progress stats. Example:
[`problems/0169-majority-element/readme.md`](/problems/0169-majority-element/readme.md).

# Tracks

Tracks are curated problem lists that drive your learning plan and progress tracking.

- Define tracks in `tracks/*.yaml` (custom or copied from predefined ones in [archive folder](/archive/)).
- Generate per-track reports and the README table from your problem stats.
- “Done” is counted from each problem’s `stats.json` (`optimal_solution: true`).

Current tracks and progress:

<!-- BEGIN_TRACKS_TABLE -->

| Track                                                                                       | Main | Ext | Total | Done | Progress | Linked | Unlinked |
| ------------------------------------------------------------------------------------------- | ---: | --: | ----: | ---: | -------: | -----: | -------: |
| [Foundations — Arrays, Hashing, Two-Pointers, Prefix, Stack](tracks/track_0_foundations.md) |   17 |   8 |    25 |    7 |      28% |     25 |        0 |
| [Sliding Window — Fixed and Dynamic](tracks/track_1_sliding_window.md)                      |   12 |   6 |    18 |    0 |       0% |     16 |        2 |
| [Two Pointers — Advanced and In‑Place Transforms](tracks/track_2_two_pointers_advanced.md)  |   12 |   8 |    20 |    3 |      15% |     20 |        0 |
| [Binary Search — Predicates, Partitions, and Heaps](tracks/track_3_binary_search_heaps.md)  |   12 |   6 |    18 |    0 |       0% |     18 |        0 |
| [Intervals — Sorting, Merging, and Greedy Scheduling](tracks/track_4_intervals.md)          |   12 |  10 |    22 |    0 |       0% |     22 |        0 |
| [NeetCode 250 — Arrays & Hashing](tracks/track_neetcode_0_arrays_hashing.md)                |   22 |   0 |    22 |    2 |       9% |     22 |        0 |
| [NeetCode 250 — Two Pointers](tracks/track_neetcode_1_two_pointers.md)                      |   13 |   0 |    13 |   10 |      77% |     13 |        0 |
| [NeetCode 250 — Sliding Window](tracks/track_neetcode_2_sliding_window.md)                  |    9 |   0 |     9 |    0 |       0% |      9 |        0 |
| [NeetCode 250 — Stack](tracks/track_neetcode_3_stack.md)                                    |   15 |   0 |    15 |    0 |       0% |     15 |        0 |
| [NeetCode 250 — Binary Search](tracks/track_neetcode_4_binary_search.md)                    |   14 |   0 |    14 |    1 |       7% |     14 |        0 |

<!-- END_TRACKS_TABLE -->

> Manage tracks in `tracks/*.yaml`. Generate reports and update this table with `make markdown` (or run the
> full pipeline with `make build`).

## Working With Tracks

- Create or update problems under `problems/NNNN-slug/`.
- Mark progress in `stats.json` (set `optimal_solution: true` when you’ve reached your target solution).
- Generate per-track reports and update the README progress table:
    - `make tracks-report` → updates `tracks/*.md`
    - `make tracks-table` → refreshes the table in this README
    - `make markdown` → runs both

### Use Predefined Tracks

Predefined track blueprints live in `archive/` (e.g., sliding window, two-pointers advanced, binary search &
heaps, intervals, DP, graphs, trees, etc.). To use one:

1. Copy a YAML into `tracks/` (keep the name or rename):

    `cp archive/track_1_sliding_window.yaml tracks/`

1. Generate reports and update progress:

    `make markdown`

You’ll get a `tracks/track_1_sliding_window.md` report and an updated table here.
