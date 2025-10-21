# 0278. First Bad Version

## Quick Facts

- URL: [First Bad Version](https://leetcode.com/problems/first-bad-version/)
- Function: `firstBadVersion`
- Signature: `(n: int, bad: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= bad <= n <= 2^31 - 1`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| # | Idea | When to use | Correctness invariant | Time | Space |
|---|------|-------------|-----------------------|------|-------|
| A | [primary idea] | [scenario] | [invariant] | O(n) | O(n) |
| B | [alternative] | [scenario] | [invariant] | O(n log n) | O(1) |
| C | [reject] | [why not] | [violated invariant] | - | - |

## Edge Cases Checklist

- [case 1]
- [case 2]
- [case 3]

## Correctness Sketch

[state the invariant and why it guarantees correctness]

## Implementation

- `solutions.py` should expose:
  - `ALL_SOLUTIONS = {"...": fn, "...": fn}`
  - Short notes on tradeoffs and pitfalls.

## Tests

- Deterministic cases covering all edge cases above
- Optional fuzz/property checks as applicable
- Run: `pytest -q -k "0278"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0034 | Medium | [Find First and Last Position of Element in Sorted Array](../0034-find-first-and-last-position-of-element-in-sorted-array/readme.md) | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 0035 | Easy | [Search Insert Position](../0035-search-insert-position/readme.md) | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) |
| 0374 | Easy | [Guess Number Higher or Lower](../0374-guess-number-higher-or-lower/readme.md) | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) |

## Examples

### Example 1

```text
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

### Example 2

```text
Input: n = 1, bad = 1
Output: 1
```

## References

- LeetCode problem and editorial links
