# 0986. Interval List Intersections

## Quick Facts

- URL: [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- Function: `intervalIntersection`
- Signature: `(firstList: list[list[int]], secondList: list[list[int]])  -> list[list[int]]`
- Primary pattern: **Two Pointers**

## Constraints

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= starti < endi <= 10^9`
- `endi < starti+1`
- `0 <= startj < endj <= 10^9`
- `endj < startj+1`

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
- Run: `pytest -q -k "0986"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                     | LeetCode                                                                                                              |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 0056   | Medium     | [Merge Intervals](../0056-merge-intervals/readme.md)                                                     | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                                     |
| 0088   | Easy       | [Merge Sorted Array](../0088-merge-sorted-array/readme.md)                                               | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)                                               |
| 0759   | Hard       | [Employee Free Time](../0759-employee-free-time/readme.md)                                               | [Employee Free Time](https://leetcode.com/problems/employee-free-time/)                                               |
| 2410   | Medium     | [Maximum Matching of Players With Trainers](../2410-maximum-matching-of-players-with-trainers/readme.md) | [Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) |

## Examples

### Example 1

```text
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

### Example 2

```text
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

## References

- LeetCode problem and editorial links
