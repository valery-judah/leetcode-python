# 0518. Coin Change II

## Quick Facts

- URL: [Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- Function: `change`
- Signature: `(amount: int, coins: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- `All the values of coins are unique.`
- `0 <= amount <= 5000`

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
| 1393 | Hard | [Maximum Value of K Coins From Piles](../1393-maximum-value-of-k-coins-from-piles/readme.md) | [Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) |
| 2648 | Hard | [Number of Ways to Earn Points](../2648-number-of-ways-to-earn-points/readme.md) | [Number of Ways to Earn Points](https://leetcode.com/problems/number-of-ways-to-earn-points/) |
| 3091 | Hard | [Count of Sub-Multisets With Bounded Sum](../3091-count-of-sub-multisets-with-bounded-sum/readme.md) | [Count of Sub-Multisets With Bounded Sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) |
| 3106 | Medium | [Length of the Longest Subsequence That Sums to Target](../3106-length-of-the-longest-subsequence-that-sums-to-target/readme.md) | [Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) |
| 3489 | Medium | [The Number of Ways to Make the Sum](../3489-the-number-of-ways-to-make-the-sum/readme.md) | [The Number of Ways to Make the Sum](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) |
| 3903 | Medium | [Inverse Coin Change](../3903-inverse-coin-change/readme.md) | [Inverse Coin Change](https://leetcode.com/problems/inverse-coin-change/) |

## Examples

### Example 1

```text
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

### Example 2

```text
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

### Example 3

```text
Input: amount = 10, coins = [10]
Output: 1
```

## References

- LeetCode problem and editorial links
