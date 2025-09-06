# 0228. Summary Ranges

## Quick Facts

- URL: https://leetcode.com/problems/summary-ranges/
- Signature: `nums: list[int]` → `list[str]`
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
- Run: `pytest -q -k "0228"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0163 | Easy | [Missing Ranges](../0163-missing-ranges/readme.md) | [link](https://leetcode.com/problems/missing-ranges/) |
| 0352 | Hard | [Data Stream as Disjoint Intervals](../0352-data-stream-as-disjoint-intervals/readme.md) | [link](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) |
| 2655 | Medium | [Find Maximal Uncovered Ranges](../2655-find-maximal-uncovered-ranges/readme.md) | [link](https://leetcode.com/problems/find-maximal-uncovered-ranges/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
