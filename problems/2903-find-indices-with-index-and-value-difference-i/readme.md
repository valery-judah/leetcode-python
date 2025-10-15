# 2903. Find Indices With Index and Value Difference I

## Quick Facts

- URL:
  [Find Indices With Index and Value Difference I](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/)
- Function: `findIndices`
- Signature: `(nums: list[int], indexDifference: int, valueDifference: int)  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= n == nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= indexDifference <= 100`
- `0 <= valueDifference <= 50`

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
- Run: `pytest -q -k "2903"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                           | LeetCode                                                                                                                                                    |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2817   | Medium     | [Minimum Absolute Difference Between Elements With Constraint](../2817-minimum-absolute-difference-between-elements-with-constraint/readme.md) | [Minimum Absolute Difference Between Elements With Constraint](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/) |
| 2905   | Medium     | [Find Indices With Index and Value Difference II](../2905-find-indices-with-index-and-value-difference-ii/readme.md)                           | [Find Indices With Index and Value Difference II](https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/)                           |

## Examples

### Example 1

```text
Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
Output: [0,3]
Explanation: In this example, i = 0 and j = 3 can be selected.
abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
Hence, a valid answer is [0,3].
[3,0] is also a valid answer.
```

### Example 2

```text
Input: nums = [2,1], indexDifference = 0, valueDifference = 0
Output: [0,0]
Explanation: In this example, i = 0 and j = 0 can be selected.
abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
Hence, a valid answer is [0,0].
Other valid answers are [0,1], [1,0], and [1,1].
```

### Example 3

```text
Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
Output: [-1,-1]
Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
Hence, [-1,-1] is returned.
```

## References

- LeetCode problem and editorial links
