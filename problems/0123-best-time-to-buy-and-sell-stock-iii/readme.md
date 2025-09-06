# 0123. Best Time to Buy and Sell Stock III

## Quick Facts

- URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
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
- Run: `pytest -q -k "0123"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0121 | Easy | [Best Time to Buy and Sell Stock](../0121-best-time-to-buy-and-sell-stock/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 0122 | Medium | [Best Time to Buy and Sell Stock II](../0122-best-time-to-buy-and-sell-stock-ii/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |
| 0188 | Hard | [Best Time to Buy and Sell Stock IV](../0188-best-time-to-buy-and-sell-stock-iv/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) |
| 0689 | Hard | [Maximum Sum of 3 Non-Overlapping Subarrays](../0689-maximum-sum-of-3-non-overlapping-subarrays/readme.md) | [link](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) |
| 2291 | Medium | [Maximum Profit From Trading Stocks](../2291-maximum-profit-from-trading-stocks/readme.md) | [link](https://leetcode.com/problems/maximum-profit-from-trading-stocks/) |
| 2555 | Medium | [Maximize Win From Two Segments](../2555-maximize-win-from-two-segments/readme.md) | [link](https://leetcode.com/problems/maximize-win-from-two-segments/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
