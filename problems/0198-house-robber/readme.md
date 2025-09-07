# 0198. House Robber

## Quick Facts

- URL: [House Robber](https://leetcode.com/problems/house-robber/)
- Function: `rob`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

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
- Run: `pytest -q -k "0198"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0152 | Medium | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md) | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |
| 0213 | Medium | [House Robber II](../0213-house-robber-ii/readme.md) | [House Robber II](https://leetcode.com/problems/house-robber-ii/) |
| 0256 | Medium | [Paint House](../0256-paint-house/readme.md) | [Paint House](https://leetcode.com/problems/paint-house/) |
| 0276 | Medium | [Paint Fence](../0276-paint-fence/readme.md) | [Paint Fence](https://leetcode.com/problems/paint-fence/) |
| 0337 | Medium | [House Robber III](../0337-house-robber-iii/readme.md) | [House Robber III](https://leetcode.com/problems/house-robber-iii/) |
| 0600 | Hard | [Non-negative Integers without Consecutive Ones](../0600-non-negative-integers-without-consecutive-ones/readme.md) | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) |
| 0656 | Hard | [Coin Path](../0656-coin-path/readme.md) | [Coin Path](https://leetcode.com/problems/coin-path/) |
| 0740 | Medium | [Delete and Earn](../0740-delete-and-earn/readme.md) | [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) |
| 2140 | Medium | [Solving Questions With Brainpower](../2140-solving-questions-with-brainpower/readme.md) | [Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) |
| 2320 | Medium | [Count Number of Ways to Place Houses](../2320-count-number-of-ways-to-place-houses/readme.md) | [Count Number of Ways to Place Houses](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) |
| 2560 | Medium | [House Robber IV](../2560-house-robber-iv/readme.md) | [House Robber IV](https://leetcode.com/problems/house-robber-iv/) |
| 2611 | Medium | [Mice and Cheese](../2611-mice-and-cheese/readme.md) | [Mice and Cheese](https://leetcode.com/problems/mice-and-cheese/) |
| 2789 | Medium | [Largest Element in an Array after Merge Operations](../2789-largest-element-in-an-array-after-merge-operations/readme.md) | [Largest Element in an Array after Merge Operations](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 2

```text
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## References

- LeetCode problem and editorial links
