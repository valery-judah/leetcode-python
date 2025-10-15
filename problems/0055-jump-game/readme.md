# 0055. Jump Game

## Quick Facts

- URL: [Jump Game](https://leetcode.com/problems/jump-game/)
- Function: `canJump`
- Signature: `(nums: list[int])  -> bool`
- Primary pattern: **Greedy**

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

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
- Run: `pytest -q -k "0055"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                       | LeetCode                                                                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 0045   | Medium     | [Jump Game II](../0045-jump-game-ii/readme.md)                                                                             | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                                                             |
| 1306   | Medium     | [Jump Game III](../1306-jump-game-iii/readme.md)                                                                           | [Jump Game III](https://leetcode.com/problems/jump-game-iii/)                                                                           |
| 1871   | Medium     | [Jump Game VII](../1871-jump-game-vii/readme.md)                                                                           | [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)                                                                           |
| 2297   | Medium     | [Jump Game VIII](../2297-jump-game-viii/readme.md)                                                                         | [Jump Game VIII](https://leetcode.com/problems/jump-game-viii/)                                                                         |
| 2617   | Hard       | [Minimum Number of Visited Cells in a Grid](../2617-minimum-number-of-visited-cells-in-a-grid/readme.md)                   | [Minimum Number of Visited Cells in a Grid](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/)                   |
| 2789   | Medium     | [Largest Element in an Array after Merge Operations](../2789-largest-element-in-an-array-after-merge-operations/readme.md) | [Largest Element in an Array after Merge Operations](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) |

## Examples

### Example 1

```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2

```text
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## References

- LeetCode problem and editorial links
