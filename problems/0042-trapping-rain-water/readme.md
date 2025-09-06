# 0042. Trapping Rain Water

## Quick Facts

- URL: https://leetcode.com/problems/trapping-rain-water/
- Signature: `height: list[int]` → `int`
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
- Run: `pytest -q -k "0042"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0011 | Medium | [Container With Most Water](../0011-container-with-most-water/readme.md) | [link](https://leetcode.com/problems/container-with-most-water/) |
| 0238 | Medium | [Product of Array Except Self](../0238-product-of-array-except-self/readme.md) | [link](https://leetcode.com/problems/product-of-array-except-self/) |
| 0407 | Hard | [Trapping Rain Water II](../0407-trapping-rain-water-ii/readme.md) | [link](https://leetcode.com/problems/trapping-rain-water-ii/) |
| 0755 | Medium | [Pour Water](../0755-pour-water/readme.md) | [link](https://leetcode.com/problems/pour-water/) |
| 2874 | Medium | [Maximum Value of an Ordered Triplet II](../2874-maximum-value-of-an-ordered-triplet-ii/readme.md) | [link](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
