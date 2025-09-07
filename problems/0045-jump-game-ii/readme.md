# 0045. Jump Game II

## Quick Facts

- URL: [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- Function: `jump`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Greedy**

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- `It's guaranteed that you can reach nums[n - 1].`

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
- Run: `pytest -q -k "0045"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0055 | Medium | [Jump Game](../0055-jump-game/readme.md) | [Jump Game](https://leetcode.com/problems/jump-game/) |
| 1428 | Medium | [Jump Game III](../1428-jump-game-iii/readme.md) | [Jump Game III](https://leetcode.com/problems/jump-game-iii/) |
| 2001 | Medium | [Jump Game VII](../2001-jump-game-vii/readme.md) | [Jump Game VII](https://leetcode.com/problems/jump-game-vii/) |
| 2056 | Medium | [Jump Game VIII](../2056-jump-game-viii/readme.md) | [Jump Game VIII](https://leetcode.com/problems/jump-game-viii/) |
| 2697 | Hard | [Minimum Number of Visited Cells in a Grid](../2697-minimum-number-of-visited-cells-in-a-grid/readme.md) | [Minimum Number of Visited Cells in a Grid](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) |
| 2855 | Medium | [Maximum Number of Jumps to Reach the Last Index](../2855-maximum-number-of-jumps-to-reach-the-last-index/readme.md) | [Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) |
| 2893 | Medium | [Visit Array Positions to Maximize Score](../2893-visit-array-positions-to-maximize-score/readme.md) | [Visit Array Positions to Maximize Score](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) |

## Examples

### Example 1

```text
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2

```text
Input: nums = [2,3,0,1,4]
Output: 2
```

## References

- LeetCode problem and editorial links
