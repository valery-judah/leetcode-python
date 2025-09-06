# 0015. 3Sum

## Quick Facts

- URL: https://leetcode.com/problems/3sum/
- Signature: `nums: list[int]` → `list[list[int]]`
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
- Run: `pytest -q -k "0015"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0001 | Easy | [Two Sum](../0001-two-sum/readme.md) | [link](https://leetcode.com/problems/two-sum/) |
| 0016 | Medium | [3Sum Closest](../0016-3sum-closest/readme.md) | [link](https://leetcode.com/problems/3sum-closest/) |
| 0018 | Medium | [4Sum](../0018-4sum/readme.md) | [link](https://leetcode.com/problems/4sum/) |
| 0259 | Medium | [3Sum Smaller](../0259-3sum-smaller/readme.md) | [link](https://leetcode.com/problems/3sum-smaller/) |
| 2367 | Easy | [Number of Arithmetic Triplets](../2367-number-of-arithmetic-triplets/readme.md) | [link](https://leetcode.com/problems/number-of-arithmetic-triplets/) |
| 2908 | Easy | [Minimum Sum of Mountain Triplets I](../2908-minimum-sum-of-mountain-triplets-i/readme.md) | [link](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/) |
| 2909 | Medium | [Minimum Sum of Mountain Triplets II](../2909-minimum-sum-of-mountain-triplets-ii/readme.md) | [link](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
