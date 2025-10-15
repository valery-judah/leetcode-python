# Solving LeetCode 128: Longest Consecutive Sequence (An Interview Guide)

This document provides a systematic approach to analyzing, solving, and presenting the “Longest Consecutive
Sequence” problem in a senior-level software engineering interview.

- **Identifier:** LC-0128
- **Title:** Longest Consecutive Sequence
- **Aliases/Patterns:** Hash Set, Unordered Set, Sequence Building
- **Category:** arrays, hash-table
- **Difficulty:** medium
- **Link:** https://leetcode.com/problems/longest-consecutive-sequence/description/
- **Function:** `longestConsecutive(nums: list[int]) -> int`

---

## 1) Problem Restatement

Given an unsorted list of integers, return the length of the longest sequence of consecutive integers that
appear in the list. Consecutive means values increase by exactly 1 each step. Duplicates may exist and should
not extend the length.

---

## 2) Clarifying Questions and Assumptions

- **Input size and range** → **Assume** up to `1e5` elements; Python `int` is unbounded for this task.
- **Order significance** → **Assume** order is irrelevant; only membership matters.
- **Duplicates** → **Assume** allowed; they do not increase run length.
- **Negative numbers** → **Assume** allowed and treated the same as positives.
- **Empty input** → **Assume** result is `0`.

> **Reflection:** These assumptions push us toward set reasoning rather than index-based DP.

---

## 3) Solution Discovery Path

- **Initial Observation.** We need runs like `…, k, k+1, …`. Only membership matters, not positions.
- **Naive Idea & Failure Mode.** Sort and scan to count consecutive runs. Correct, `O(n log n)` time, `O(1)`
  extra if in-place. Fails target linear time for large `n`.
- **Aha! Insight.** If we know whether a number has a predecessor (`x-1`), then only numbers **without** a
  predecessor can start runs. From each start, count forward `x+1, x+2, …` using `O(1)` membership checks in a
  hash set.
- **Core Plan (one sentence).** Insert all numbers in a set; for each `x` with no `x-1` in the set, walk
  upward while `x+len` exists; track the max length.
- **Micro Walkthrough.** For `[100,4,200,1,3,2]`, the starts are `100` (no `99`), `1` (no `0`), `200` (no
  `199`). Their runs are `100`→len 1, `1,2,3,4`→len 4, `200`→len 1. Answer `4`.

---

## 4) Algorithms and Trade-offs

1. **Sorting + linear scan**\
   **Idea:** sort, then count streaks where `a[i] == a[i-1]+1` (skip duplicates).\
   **Correctness:** consecutive after sort gives runs.\
   **Time/Space:** `O(n log n)` / `O(1)` extra if in-place; `O(n)` extra if copying required.\
   **Choose when:** hashing unavailable, memory-tight languages, or when `n` small.

1. **Hash-set starts (recommended)**\
   **Idea:** put all numbers in a set; for each `x` with `x-1` not in set, grow `x, x+1, …`.\
   **Correctness:** every run is discovered exactly once, from its unique smallest element.\
   **Time/Space:** expected `O(n)` / `O(n)`.\
   **Choose when:** standard interview constraints; Python/C++ average-case hashing.

1. **Union–Find (DSU)**\
   **Idea:** union adjacent numbers; length of largest component is answer.\
   **Correctness:** components correspond to consecutive blocks.\
   **Time/Space:** ~`O(n α(n))` / `O(n)` but heavier constants and maps.\
   **Choose when:** you need dynamic union queries or to illustrate DSU.

> **Recommendation:** Hash-set starts. Single pass, minimal code, linear average time.

---

## 5) Correctness

- **Dominance intuition.** If `x-1` exists, then any run containing `x` will be discovered starting at `x-1`
  (or earlier). So counting from `x` would be redundant. Limiting starts to numbers with no predecessor
  ensures each maximal run is explored once.
- **Invariant (formal).** While iterating the array, the set `S` equals the input’s distinct elements. For any
  `x ∈ S`, if `x-1 ∉ S`, then the loop that increments `y = x, x+1, …` visits exactly the elements of the
  unique maximal run containing `x`. No other start can visit these elements because any other candidate `z`
  in the run has `z-1 ∈ S`. Therefore the maximum length observed equals the true maximum.

---

## 6) Complexity and Resource Analysis

- **Time:** Expected `O(n)` with hash set membership (`n` insertions + each element’s membership tested a
  constant number of times; each element participates in at most one forward walk).
- **Space:** `O(n)` for the set of distinct elements.
- **Constant factors:** Using local variables and `while` loops keeps Python overhead low; avoid repeated `in`
  checks with recomputed expressions where possible.

---

## 7) Implementation (Python)

```python
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    Return the length of the longest consecutive-elements sequence.
    Expected O(n) time using a hash set; O(n) space.

    Rules:
      - Duplicates do not extend length.
      - Negative numbers are allowed.
    """
    if not nums:
        return 0

    s = set(nums)
    best = 0

    for x in s:
        # Only start counting at the beginning of a run
        if x - 1 not in s:
            y = x
            # Walk forward through this run
            while y in s:
                y += 1
            best = max(best, y - x)

    return best
```

---

## 8) Tests (pytest)

Create `tests/test_longest_consecutive.py`.

```python
import random
from typing import List
from solution import longestConsecutive  # adjust import to your module


def oracle_sorting(nums: List[int]) -> int:
    """O(n log n) oracle using sorting; correct but slower."""
    if not nums:
        return 0
    a = sorted(set(nums))
    if not a:
        return 0
    best = 1
    cur = 1
    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best


# Deterministic unit tests

def test_empty_and_singleton():
    assert longestConsecutive([]) == 0
    assert longestConsecutive([7]) == 1


def test_duplicates_only():
    assert longestConsecutive([2, 2, 2]) == 1


def test_canonical_examples():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_negatives_and_mixed():
    assert longestConsecutive([-1, -2, -3, 10]) == 3  # [-3,-2,-1]
    assert longestConsecutive([10, -1, 0, 1, 2, 50]) == 4  # [-1,0,1,2]


def test_gaps_and_blocks():
    assert longestConsecutive([1, 9, 3, 10, 4, 20, 2]) == 4  # [1,2,3,4]
    assert longestConsecutive([1, 2, 2, 3]) == 3


# Randomized differential tests

def test_random_against_oracle_small():
    random.seed(13)
    for _ in range(200):
        n = random.randint(0, 40)
        arr = [random.randint(-20, 20) for _ in range(n)]
        assert longestConsecutive(arr) == oracle_sorting(arr)


# Scale sanity (not strict timing, but exercises asymptotics)

def test_scale_constant_stride():
    # Two large blocks; answer equals length of bigger block
    n1, n2 = 5000, 8000
    block1 = list(range(100000, 100000 + n1))
    block2 = list(range(-20000, -20000 + n2))
    arr = block1 + block2
    assert longestConsecutive(arr) == max(n1, n2)
```

---

## 9) Pitfalls Checklist

- Counting from every element instead of only starts → `O(n^2)` worst-case.
- Forgetting to deduplicate before scanning in sorting oracle → breaks runs with duplicates.
- Off-by-one on length: run length is `y - x` after walking `y` to first missing.
- Mutating the set during iteration → undefined behavior; iterate over a fixed set.
- Assuming positivity; negative values and zero are valid consecutive integers.

---

## 10) Interview Guidance

- **Talk-track (≈25s).** “I want linear time. Sorting works in `O(n log n)` but we can do better. Put all
  numbers in a set. A consecutive run must start at a number with no predecessor `x-1`. For each such start,
  walk upward while `x+1, x+2, …` are in the set and track the max length. Each element belongs to exactly one
  forward walk, so expected `O(n)`. Duplicates are ignored by the set. Empty input returns 0.”
- **What to implement first.** Sorting oracle to lock down correctness, then the set-based optimal.
- **Follow-ups.**
    - Streaming data → maintain a disjoint-set or map of segment endpoints to merge on the fly.
    - Memory limits → external sort then one pass.
    - Need actual sequence, not length → record `(start, len)` and reconstruct.

---

## 11) Reflection Prompts

- What exact invariant ensures we explore each run exactly once?
- Provide a counterexample that would double-count runs if we didn’t check `x-1 ∉ S`.
- Why does the average-case hashing assumption matter for `O(n)`?
- When would you prefer the sorting solution despite higher asymptotics?
- How would you adapt the solution to return the sequence itself?

---

## 12) Extensions

- **LC-0129 variant idea:** Return the **longest k-consecutive** where gaps up to `k` are allowed → sliding
  window over sorted unique values.
- **Disjoint sequences with updates:** Support insert/delete and query max run length → interval map or
  union-find with hash maps.
- **2D generalization:** Longest consecutive path in a grid with 4-connectivity → graph traversal, not a set
  lookup.
