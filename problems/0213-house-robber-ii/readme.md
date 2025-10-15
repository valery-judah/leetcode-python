# 0213. House Robber II

## Quick Facts

- URL: [House Robber II](https://leetcode.com/problems/house-robber-ii/)
- Function: `rob`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

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
- Run: `pytest -q -k "0213"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                               | LeetCode                                                                                                                        |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 0198   | Medium     | [House Robber](../0198-house-robber/readme.md)                                                                     | [House Robber](https://leetcode.com/problems/house-robber/)                                                                     |
| 0256   | Medium     | [Paint House](../0256-paint-house/readme.md)                                                                       | [Paint House](https://leetcode.com/problems/paint-house/)                                                                       |
| 0276   | Medium     | [Paint Fence](../0276-paint-fence/readme.md)                                                                       | [Paint Fence](https://leetcode.com/problems/paint-fence/)                                                                       |
| 0337   | Medium     | [House Robber III](../0337-house-robber-iii/readme.md)                                                             | [House Robber III](https://leetcode.com/problems/house-robber-iii/)                                                             |
| 0600   | Hard       | [Non-negative Integers without Consecutive Ones](../0600-non-negative-integers-without-consecutive-ones/readme.md) | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) |
| 0656   | Hard       | [Coin Path](../0656-coin-path/readme.md)                                                                           | [Coin Path](https://leetcode.com/problems/coin-path/)                                                                           |

## Examples

### Example 1

```text
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

### Example 2

```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 3

```text
Input: nums = [1,2,3]
Output: 3
```

## References

- LeetCode problem and editorial links
