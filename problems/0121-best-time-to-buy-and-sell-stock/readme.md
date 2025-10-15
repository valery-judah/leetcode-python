# 0121. Best Time to Buy and Sell Stock

## Quick Facts

- URL: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- Function: `maxProfit`
- Signature: `(prices: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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

| Number | Difficulty | Name                                                                                                               | LeetCode                                                                                                                        |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 0053   | Medium     | [Maximum Subarray](../0053-maximum-subarray/readme.md)                                                             | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                                             |
| 0122   | Medium     | [Best Time to Buy and Sell Stock II](../0122-best-time-to-buy-and-sell-stock-ii/readme.md)                         | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)                         |
| 0123   | Hard       | [Best Time to Buy and Sell Stock III](../0123-best-time-to-buy-and-sell-stock-iii/readme.md)                       | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)                       |
| 0188   | Hard       | [Best Time to Buy and Sell Stock IV](../0188-best-time-to-buy-and-sell-stock-iv/readme.md)                         | [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)                         |
| 0309   | Medium     | [Best Time to Buy and Sell Stock with Cooldown](../0309-best-time-to-buy-and-sell-stock-with-cooldown/readme.md)   | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)   |
| 2012   | Medium     | [Sum of Beauty in the Array](../2012-sum-of-beauty-in-the-array/readme.md)                                         | [Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array/)                                         |
| 2016   | Easy       | [Maximum Difference Between Increasing Elements](../2016-maximum-difference-between-increasing-elements/readme.md) | [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |
| 2291   | Medium     | [Maximum Profit From Trading Stocks](../2291-maximum-profit-from-trading-stocks/readme.md)                         | [Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks/)                         |
| 3573   | Medium     | [Best Time to Buy and Sell Stock V](../3573-best-time-to-buy-and-sell-stock-v/readme.md)                           | [Best Time to Buy and Sell Stock V](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/)                           |

## Examples

### Example 1

```text
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2

```text
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## References

- LeetCode problem and editorial links
