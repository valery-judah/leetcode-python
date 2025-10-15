# 0018. 4Sum

## Quick Facts

- URL: [4Sum](https://leetcode.com/problems/4sum/)
- Function: `fourSum`
- Signature: `(nums: list[int], target: int)  -> list[list[int]]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

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
- Run: `pytest -q -k "0018"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                     | LeetCode                                                                              |
| ------ | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 0001   | Easy       | [Two Sum](../0001-two-sum/readme.md)                                     | [Two Sum](https://leetcode.com/problems/two-sum/)                                     |
| 0015   | Medium     | [3Sum](../0015-3sum/readme.md)                                           | [3Sum](https://leetcode.com/problems/3sum/)                                           |
| 0454   | Medium     | [4Sum II](../0454-4sum-ii/readme.md)                                     | [4Sum II](https://leetcode.com/problems/4sum-ii/)                                     |
| 1995   | Easy       | [Count Special Quadruplets](../1995-count-special-quadruplets/readme.md) | [Count Special Quadruplets](https://leetcode.com/problems/count-special-quadruplets/) |

## Examples

### Example 1

```text
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Example 2

```text
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

## References

- LeetCode problem and editorial links
