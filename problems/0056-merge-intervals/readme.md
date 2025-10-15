# 0056. Merge Intervals

## Quick Facts

- URL: [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- Function: `merge`
- Signature: `(intervals: list[list[int]])  -> list[list[int]]`
- Primary pattern: **Sorting**

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

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
- Run: `pytest -q -k "0056"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                 | LeetCode                                                                                                                          |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0057   | Medium     | [Insert Interval](../0057-insert-interval/readme.md)                                                                 | [Insert Interval](https://leetcode.com/problems/insert-interval/)                                                                 |
| 0252   | Easy       | [Meeting Rooms](../0252-meeting-rooms/readme.md)                                                                     | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)                                                                     |
| 0253   | Medium     | [Meeting Rooms II](../0253-meeting-rooms-ii/readme.md)                                                               | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)                                                               |
| 0495   | Easy       | [Teemo Attacking](../0495-teemo-attacking/readme.md)                                                                 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/)                                                                 |
| 0616   | Medium     | [Add Bold Tag in String](../0616-add-bold-tag-in-string/readme.md)                                                   | [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/)                                                   |
| 0715   | Hard       | [Range Module](../0715-range-module/readme.md)                                                                       | [Range Module](https://leetcode.com/problems/range-module/)                                                                       |
| 0759   | Hard       | [Employee Free Time](../0759-employee-free-time/readme.md)                                                           | [Employee Free Time](https://leetcode.com/problems/employee-free-time/)                                                           |
| 0763   | Medium     | [Partition Labels](../0763-partition-labels/readme.md)                                                               | [Partition Labels](https://leetcode.com/problems/partition-labels/)                                                               |
| 0986   | Medium     | [Interval List Intersections](../0986-interval-list-intersections/readme.md)                                         | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)                                         |
| 2158   | Hard       | [Amount of New Area Painted Each Day](../2158-amount-of-new-area-painted-each-day/readme.md)                         | [Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/)                         |
| 2213   | Hard       | [Longest Substring of One Repeating Character](../2213-longest-substring-of-one-repeating-character/readme.md)       | [Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)       |
| 2276   | Hard       | [Count Integers in Intervals](../2276-count-integers-in-intervals/readme.md)                                         | [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/)                                         |
| 2406   | Medium     | [Divide Intervals Into Minimum Number of Groups](../2406-divide-intervals-into-minimum-number-of-groups/readme.md)   | [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)   |
| 2446   | Easy       | [Determine if Two Events Have Conflict](../2446-determine-if-two-events-have-conflict/readme.md)                     | [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/)                     |
| 2580   | Medium     | [Count Ways to Group Overlapping Ranges](../2580-count-ways-to-group-overlapping-ranges/readme.md)                   | [Count Ways to Group Overlapping Ranges](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/)                   |
| 2848   | Easy       | [Points That Intersect With Cars](../2848-points-that-intersect-with-cars/readme.md)                                 | [Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)                                 |
| 3169   | Medium     | [Count Days Without Meetings](../3169-count-days-without-meetings/readme.md)                                         | [Count Days Without Meetings](https://leetcode.com/problems/count-days-without-meetings/)                                         |
| 3323   | Medium     | [Minimize Connected Groups by Inserting Interval](../3323-minimize-connected-groups-by-inserting-interval/readme.md) | [Minimize Connected Groups by Inserting Interval](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) |

## Examples

### Example 1

```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

### Example 2

```text
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Example 3

```text
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
```

## References

- LeetCode problem and editorial links
