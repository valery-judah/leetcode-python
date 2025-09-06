# 0162. Find Peak Element

## Quick Facts

- URL: https://leetcode.com/problems/find-peak-element/
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
- Run: `pytest -q -k "0162"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0852 | Medium | [Peak Index in a Mountain Array](../0852-peak-index-in-a-mountain-array/readme.md) | [link](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |
| 1901 | Medium | [Find a Peak Element II](../1901-find-a-peak-element-ii/readme.md) | [link](https://leetcode.com/problems/find-a-peak-element-ii/) |
| 2137 | Medium | [Pour Water Between Buckets to Make Water Levels Equal](../2137-pour-water-between-buckets-to-make-water-levels-equal/readme.md) | [link](https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/) |
| 2210 | Easy | [Count Hills and Valleys in an Array](../2210-count-hills-and-valleys-in-an-array/readme.md) | [link](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/) |
| 2951 | Easy | [Find the Peaks](../2951-find-the-peaks/readme.md) | [link](https://leetcode.com/problems/find-the-peaks/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:51Z: Created scaffold.
