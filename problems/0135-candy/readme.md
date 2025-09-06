# 0135. Candy

## Quick Facts

- URL: https://leetcode.com/problems/candy/
- Signature: `ratings: list[int]` → `int`
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
- Run: `pytest -q -k "0135"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2371 | Hard | [Minimize Maximum Value in a Grid](../2371-minimize-maximum-value-in-a-grid/readme.md) | [link](https://leetcode.com/problems/minimize-maximum-value-in-a-grid/) |
| 3122 | Medium | [Minimum Number of Operations to Satisfy Conditions](../3122-minimum-number-of-operations-to-satisfy-conditions/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/) |
| 3142 | Easy | [Check if Grid Satisfies Conditions](../3142-check-if-grid-satisfies-conditions/readme.md) | [link](https://leetcode.com/problems/check-if-grid-satisfies-conditions/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
