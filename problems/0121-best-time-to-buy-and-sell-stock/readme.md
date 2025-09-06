# 0121. Best Time to Buy and Sell Stock

## Quick Facts

- URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Signature: `prices: list[int]` → `int`
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
- Run: `pytest -q -k "0121"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0053 | Medium | [Maximum Subarray](../0053-maximum-subarray/readme.md) | [link](https://leetcode.com/problems/maximum-subarray/) |
| 0122 | Medium | [Best Time to Buy and Sell Stock II](../0122-best-time-to-buy-and-sell-stock-ii/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |
| 0123 | Hard | [Best Time to Buy and Sell Stock III](../0123-best-time-to-buy-and-sell-stock-iii/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |
| 0188 | Hard | [Best Time to Buy and Sell Stock IV](../0188-best-time-to-buy-and-sell-stock-iv/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) |
| 0309 | Medium | [Best Time to Buy and Sell Stock with Cooldown](../0309-best-time-to-buy-and-sell-stock-with-cooldown/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| 2012 | Medium | [Sum of Beauty in the Array](../2012-sum-of-beauty-in-the-array/readme.md) | [link](https://leetcode.com/problems/sum-of-beauty-in-the-array/) |
| 2016 | Easy | [Maximum Difference Between Increasing Elements](../2016-maximum-difference-between-increasing-elements/readme.md) | [link](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |
| 2291 | Medium | [Maximum Profit From Trading Stocks](../2291-maximum-profit-from-trading-stocks/readme.md) | [link](https://leetcode.com/problems/maximum-profit-from-trading-stocks/) |
| 3573 | Medium | [Best Time to Buy and Sell Stock V](../3573-best-time-to-buy-and-sell-stock-v/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
