
# 217. Contains Duplicate

**URL**: <https://leetcode.com/problems/contains-duplicate/>

**Difficulty**: easy

**Tags**: #array, #hash-set

## Clarifying questions

- Input shape, ranges, constraints?
- Duplicates, negatives, empty input?
- Mutations allowed? Sorted? Streaming?

## Examples

- Add 2–3 examples and edge cases.

## Approach

- Brute force -> improved -> optimal.
- Data structures considered.
- Proof of correctness sketch.

## Complexity

- Time: O(...)
- Space: O(...)

## Checklist

- [ ] Restate problem
- [ ] Small example walkthrough
- [ ] Choose DS/algorithm
- [ ] Dry-run core loop
- [ ] Code cleanly
- [ ] Test edge cases

See also: `docs/interview-framework.md`.

# Flow / How I solved it

## Step-by-Step Reasoning

1) Restate the problem clearly

- Input: an array of integers `nums`.
- Output: `True` if any value appears at least twice; otherwise `False`.
- Clarify: allowed to mutate input? input size range? negative values? empty input?

2) Establish a baseline (brute force)

- Idea: for each index `i`, scan only elements to the right (`j > i`).
- Why only to the right: anything to the left was already compared when that element was the “current”.
- Early exit: return `True` on the first match; return `False` if no matches after all scans.
- Complexity: time `O(n^2)`, space `O(1)`.

3) Improve with sorting

- Intuition: duplicates become adjacent after sorting; then a single pass finds any equal neighbors.
- Implementation: sort (or use a sorted copy) and check `nums[i] == nums[i-1]` while scanning.
- Complexity: time `O(n log n)` (sorting dominates), space `O(1)` extra if in-place, `O(n)` if copied.
- Caveat: sorting mutates input unless you work on a copy, which may be undesirable.

4) Optimal approach with a set (one pass)

- Invariant: the `seen` set contains exactly the values to the left of the current index.
- Algorithm: for each `x` in `nums` → if `x in seen` return `True`; otherwise `seen.add(x)`; after loop return `False`.
- Complexity: average-case time `O(n)`, space `O(n)`.
- Real-world note: for very small `n`, the constant factors of hashing can make it similar to or slower than sorting; asymptotically it wins.

5) Validate with quick examples

- `[1, 2, 3, 1]` → set path: add 1,2,3; see 1 again → `True`.
- `[1, 2, 3, 4]` → exhaust loop with no repeats → `False`.
- `[]` / single element → `False`.

6) Choose by constraints

- Prefer the set approach for typical constraints (cleanest, fastest on average).
- Prefer sorting when memory is tight and mutation is acceptable (or copy if not).
- Use brute force only for tiny inputs or when both extra memory and mutation are disallowed.

## Common Pitfalls and How to Fix Them

- Scanning the wrong range: scanning both left and right is redundant. Fix by scanning only `j > i` or use a set.
- Forgetting the final `False`: after a full pass with no duplicates, explicitly return `False`.
- Using a list for membership tests: `x in list` is `O(n)`, making the pass `O(n^2)`. Use a `set` for `O(1)` average membership.
- Mutating input while sorting: if callers expect `nums` unchanged, use `sorted(nums)` and scan the copy.
- Building a new set on every iteration: avoid patterns like repeatedly doing `set(nums[:i])`. Maintain a single `seen` set incrementally.
- Misplacing the add-check order: always check `if x in seen: return True` before `seen.add(x)`.
- Misinterpreting “duplicate” semantics: this problem ignores positions; any repeated value counts. Don’t overconstrain with index differences (that’s a different variant).
- Assuming set conversion is space-free: `len(set(nums)) != len(nums)` is concise and correct, but still `O(n)` extra space and no early exit.

## Reference Implementations (Python)

All implementations live in `solutions.py` and expose `.solve(nums) -> bool`:

Brute force (reference; intentionally flawed for matrix demonstration):

```python
class BruteForce:
    def solve(self, nums: list[int]) -> bool:
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                if v == nums[j]:
                    return True
        return False
```

- Note: this compares each element with itself at `j == i`, so it returns `True` for any non-empty input. Tests mark this class as an expected failure to illustrate the reporting matrix; see `test_0217_contains_duplicate.py`.

Hash set (optimal average case; default export via `Solution = SetBased`):

```python
class SetBased:
    def solve(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

Sorting (non-mutating; scans adjacent after copy sort):

```python
class Sorting:
    def solve(self, nums: list[int]) -> bool:
        nums_sorted = sorted(nums)
        return any(
            nums_sorted[i] == nums_sorted[i - 1]
            for i in range(1, len(nums_sorted))
        )
```

Direct code anchors (commit-pinned):

- BruteForce class: https://github.com/valery-judah/leetcode-python-project/blob/e0d064588ad7b5b99f1fe7282eab5859644ac41f/tasks/0217-contains-duplicate/solutions.py#L4
- SetBased class: https://github.com/valery-judah/leetcode-python-project/blob/e0d064588ad7b5b99f1fe7282eab5859644ac41f/tasks/0217-contains-duplicate/solutions.py#L13
- Sorting class: https://github.com/valery-judah/leetcode-python-project/blob/e0d064588ad7b5b99f1fe7282eab5859644ac41f/tasks/0217-contains-duplicate/solutions.py#L23

## How to Think Through Errors

- Unexpected `False` with known duplicates: add prints or a quick trace to confirm you’re adding to `seen` after checking membership, not before.
- Input changes after call: if using sorting, verify whether you mutated `nums`. Switch to a copied sort (`sorted(nums)`) when mutation is not acceptable.
- Performance too slow on large inputs: confirm you’re not using a list for membership or rebuilding sets repeatedly. Use a single `set` and early exit.
- Memory pressure: if `set` size is an issue, prefer the sorting approach; if even that is too large, consider chunked/external strategies (out of scope for this kata).

## Extension Notes

- Variants like “Contains Duplicate II” add index-distance constraints (e.g., `|i - j| <= k`). Those require tracking indices (e.g., hashmap or sliding window set), not just values. Keep this README focused on the base problem.

## Cross-Links

- Solution code: `tasks/0217-contains-duplicate/solutions.py`
- Unit tests: `tasks/0217-contains-duplicate/test_0217_contains_duplicate.py`
- Property tests: `tasks/0217-contains-duplicate/test_properties.py`
- Related variant: `tasks/0219-contains-duplicate-ii/README.md`
- Interview framework: `docs/interview-framework.md`
- API docs (mkdocs): `docs/reference/0217-contains-duplicate.md`
