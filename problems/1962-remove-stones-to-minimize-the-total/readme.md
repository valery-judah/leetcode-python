# 1962. Remove Stones to Minimize the Total

## Quick Facts

- URL: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
- Signature: `piles: list[int]`, `k: int` → `int`
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
- Run: `pytest -q -k "1962"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2208 | Medium | [Minimum Operations to Halve Array Sum](../2208-minimum-operations-to-halve-array-sum/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) |
| 2530 | Medium | [Maximal Score After Applying K Operations](../2530-maximal-score-after-applying-k-operations/readme.md) | [link](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) |
| 2558 | Easy | [Take Gifts From the Richest Pile](../2558-take-gifts-from-the-richest-pile/readme.md) | [link](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:02Z: Created scaffold.
