# 0518. Coin Change II

## Quick Facts

- URL: https://leetcode.com/problems/coin-change-ii/
- Signature: `amount: int`, `coins: list[int]` → `int`
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
- Run: `pytest -q -k "0518"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2218 | Hard | [Maximum Value of K Coins From Piles](../2218-maximum-value-of-k-coins-from-piles/readme.md) | [link](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) |
| 2585 | Hard | [Number of Ways to Earn Points](../2585-number-of-ways-to-earn-points/readme.md) | [link](https://leetcode.com/problems/number-of-ways-to-earn-points/) |
| 2902 | Hard | [Count of Sub-Multisets With Bounded Sum](../2902-count-of-sub-multisets-with-bounded-sum/readme.md) | [link](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) |
| 2915 | Medium | [Length of the Longest Subsequence That Sums to Target](../2915-length-of-the-longest-subsequence-that-sums-to-target/readme.md) | [link](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) |
| 3183 | Medium | [The Number of Ways to Make the Sum](../3183-the-number-of-ways-to-make-the-sum/readme.md) | [link](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) |
| 3592 | Medium | [Inverse Coin Change](../3592-inverse-coin-change/readme.md) | [link](https://leetcode.com/problems/inverse-coin-change/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:57Z: Created scaffold.
