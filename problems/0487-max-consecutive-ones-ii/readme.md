# 0487. Max Consecutive Ones II

## Quick Facts

- URL: https://leetcode.com/problems/max-consecutive-ones-ii/
- Signature: `nums: list[int]` → `int`
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
- Run: `pytest -q -k "0487"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0485 | Easy | [Max Consecutive Ones](../0485-max-consecutive-ones/readme.md) | [link](https://leetcode.com/problems/max-consecutive-ones/) |
| 1004 | Medium | [Max Consecutive Ones III](../1004-max-consecutive-ones-iii/readme.md) | [link](https://leetcode.com/problems/max-consecutive-ones-iii/) |
| 2155 | Medium | [All Divisions With the Highest Score of a Binary Array](../2155-all-divisions-with-the-highest-score-of-a-binary-array/readme.md) | [link](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:57Z: Created scaffold.
