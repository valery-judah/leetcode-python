# 0907. Sum of Subarray Minimums

## Quick Facts

- URL: https://leetcode.com/problems/sum-of-subarray-minimums/
- Signature: `arr: list[int]` → `int`
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
- Run: `pytest -q -k "0907"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2104 | Medium | [Sum of Subarray Ranges](../2104-sum-of-subarray-ranges/readme.md) | [link](https://leetcode.com/problems/sum-of-subarray-ranges/) |
| 2281 | Hard | [Sum of Total Strength of Wizards](../2281-sum-of-total-strength-of-wizards/readme.md) | [link](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:00Z: Created scaffold.
