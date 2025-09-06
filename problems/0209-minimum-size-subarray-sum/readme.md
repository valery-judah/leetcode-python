# 0209. Minimum Size Subarray Sum

## Quick Facts

- URL: https://leetcode.com/problems/minimum-size-subarray-sum/
- Signature: `target: int`, `nums: list[int]` → `int`
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
- Run: `pytest -q -k "0209"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0076 | Hard | [Minimum Window Substring](../0076-minimum-window-substring/readme.md) | [link](https://leetcode.com/problems/minimum-window-substring/) |
| 0325 | Medium | [Maximum Size Subarray Sum Equals k](../0325-maximum-size-subarray-sum-equals-k/readme.md) | [link](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) |
| 0718 | Medium | [Maximum Length of Repeated Subarray](../0718-maximum-length-of-repeated-subarray/readme.md) | [link](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |
| 1658 | Medium | [Minimum Operations to Reduce X to Zero](../1658-minimum-operations-to-reduce-x-to-zero/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |
| 2090 | Medium | [K Radius Subarray Averages](../2090-k-radius-subarray-averages/readme.md) | [link](https://leetcode.com/problems/k-radius-subarray-averages/) |
| 2233 | Medium | [Maximum Product After K Increments](../2233-maximum-product-after-k-increments/readme.md) | [link](https://leetcode.com/problems/maximum-product-after-k-increments/) |
| 3095 | Easy | [Shortest Subarray With OR at Least K I](../3095-shortest-subarray-with-or-at-least-k-i/readme.md) | [link](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) |
| 3364 | Easy | [Minimum Positive Sum Subarray](../3364-minimum-positive-sum-subarray/readme.md) | [link](https://leetcode.com/problems/minimum-positive-sum-subarray/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
