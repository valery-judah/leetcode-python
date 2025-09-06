# 0560. Subarray Sum Equals K

## Quick Facts

- URL: https://leetcode.com/problems/subarray-sum-equals-k/
- Signature: `nums: list[int]`, `k: int` → `int`
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
- Run: `pytest -q -k "0560"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0001 | Easy | [Two Sum](../0001-two-sum/readme.md) | [link](https://leetcode.com/problems/two-sum/) |
| 0523 | Medium | [Continuous Subarray Sum](../0523-continuous-subarray-sum/readme.md) | [link](https://leetcode.com/problems/continuous-subarray-sum/) |
| 0713 | Medium | [Subarray Product Less Than K](../0713-subarray-product-less-than-k/readme.md) | [link](https://leetcode.com/problems/subarray-product-less-than-k/) |
| 0724 | Easy | [Find Pivot Index](../0724-find-pivot-index/readme.md) | [link](https://leetcode.com/problems/find-pivot-index/) |
| 0974 | Medium | [Subarray Sums Divisible by K](../0974-subarray-sums-divisible-by-k/readme.md) | [link](https://leetcode.com/problems/subarray-sums-divisible-by-k/) |
| 1658 | Medium | [Minimum Operations to Reduce X to Zero](../1658-minimum-operations-to-reduce-x-to-zero/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |
| 2090 | Medium | [K Radius Subarray Averages](../2090-k-radius-subarray-averages/readme.md) | [link](https://leetcode.com/problems/k-radius-subarray-averages/) |
| 2219 | Medium | [Maximum Sum Score of Array](../2219-maximum-sum-score-of-array/readme.md) | [link](https://leetcode.com/problems/maximum-sum-score-of-array/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:58Z: Created scaffold.
