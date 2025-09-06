# 0295. Find Median from Data Stream

## Quick Facts

- URL: https://leetcode.com/problems/find-median-from-data-stream/
- Signature: `...` → `bool`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0295"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0480 | Hard | [Sliding Window Median](../0480-sliding-window-median/readme.md) | [link](https://leetcode.com/problems/sliding-window-median/) |
| 1825 | Hard | [Finding MK Average](../1825-finding-mk-average/readme.md) | [link](https://leetcode.com/problems/finding-mk-average/) |
| 2102 | Hard | [Sequentially Ordinal Rank Tracker](../2102-sequentially-ordinal-rank-tracker/readme.md) | [link](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/) |
| 3107 | Medium | [Minimum Operations to Make Median of Array Equal to K](../3107-minimum-operations-to-make-median-of-array-equal-to-k/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/) |
| 3422 | Medium | [Minimum Operations to Make Subarray Elements Equal](../3422-minimum-operations-to-make-subarray-elements-equal/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/) |
| 3505 | Hard | [Minimum Operations to Make Elements Within K Subarrays Equal](../3505-minimum-operations-to-make-elements-within-k-subarrays-equal/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
