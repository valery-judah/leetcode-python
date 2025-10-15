# 0228. Summary Ranges

## Quick Facts

- URL: [Summary Ranges](https://leetcode.com/problems/summary-ranges/)
- Function: `summaryRanges`
- Signature: `(nums: list[int])  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `All the values of nums are unique.`
- `nums is sorted in ascending order.`

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
- Run: `pytest -q -k "0228"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                     | LeetCode                                                                                              |
| ------ | ---------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 0163   | Easy       | [Missing Ranges](../0163-missing-ranges/readme.md)                                       | [Missing Ranges](https://leetcode.com/problems/missing-ranges/)                                       |
| 0352   | Hard       | [Data Stream as Disjoint Intervals](../0352-data-stream-as-disjoint-intervals/readme.md) | [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) |
| 2655   | Medium     | [Find Maximal Uncovered Ranges](../2655-find-maximal-uncovered-ranges/readme.md)         | [Find Maximal Uncovered Ranges](https://leetcode.com/problems/find-maximal-uncovered-ranges/)         |

## Examples

### Example 1

```text
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

### Example 2

```text
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

## References

- LeetCode problem and editorial links
