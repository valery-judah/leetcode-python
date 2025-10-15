# 0252. Meeting Rooms

## Quick Facts

- URL: [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- Function: `canAttendMeetings`
- Signature: `(intervals: list[list[int]])  -> bool`
- Primary pattern: **Sorting**

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti < endi <= 10^6`

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
- Run: `pytest -q -k "0252"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                 | LeetCode                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 0056   | Medium     | [Merge Intervals](../0056-merge-intervals/readme.md)                                 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                 |
| 0253   | Medium     | [Meeting Rooms II](../0253-meeting-rooms-ii/readme.md)                               | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)                               |
| 2402   | Hard       | [Meeting Rooms III](../2402-meeting-rooms-iii/readme.md)                             | [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)                             |
| 2848   | Easy       | [Points That Intersect With Cars](../2848-points-that-intersect-with-cars/readme.md) | [Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## Examples

### Example 1

```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

### Example 2

```text
Input: intervals = [[7,10],[2,4]]
Output: true
```

## References

- LeetCode problem and editorial links
