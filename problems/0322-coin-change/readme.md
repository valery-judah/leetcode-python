# 0322. Coin Change

## Quick Facts

- URL: [Coin Change](https://leetcode.com/problems/coin-change/)
- Function: `coinChange`
- Signature: `(coins: list[int], amount: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

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
- Run: `pytest -q -k "0322"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1025 | Medium | [Minimum Cost For Tickets](../1025-minimum-cost-for-tickets/readme.md) | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) |
| 1393 | Hard | [Maximum Value of K Coins From Piles](../1393-maximum-value-of-k-coins-from-piles/readme.md) | [Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) |
| 2345 | Easy | [Minimum Number of Operations to Convert Time](../2345-minimum-number-of-operations-to-convert-time/readme.md) | [Minimum Number of Operations to Convert Time](https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/) |
| 2633 | Hard | [Minimum Cost to Split an Array](../2633-minimum-cost-to-split-an-array/readme.md) | [Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) |
| 3091 | Hard | [Count of Sub-Multisets With Bounded Sum](../3091-count-of-sub-multisets-with-bounded-sum/readme.md) | [Count of Sub-Multisets With Bounded Sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) |
| 3106 | Medium | [Length of the Longest Subsequence That Sums to Target](../3106-length-of-the-longest-subsequence-that-sums-to-target/readme.md) | [Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) |
| 3231 | Medium | [Minimum Number of Coins to be Added](../3231-minimum-number-of-coins-to-be-added/readme.md) | [Minimum Number of Coins to be Added](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/) |
| 3273 | Medium | [Most Expensive Item That Can Not Be Bought](../3273-most-expensive-item-that-can-not-be-bought/readme.md) | [Most Expensive Item That Can Not Be Bought](https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/) |
| 3903 | Medium | [Inverse Coin Change](../3903-inverse-coin-change/readme.md) | [Inverse Coin Change](https://leetcode.com/problems/inverse-coin-change/) |

## Examples

### Example 1

```text
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

### Example 2

```text
Input: coins = [2], amount = 3
Output: -1
```

### Example 3

```text
Input: coins = [1], amount = 0
Output: 0
```

## References

- LeetCode problem and editorial links
