# 0253. Meeting Rooms II

## Quick Facts

- URL: [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- Function: `minMeetingRooms`
- Signature: `(intervals: list[list[int]])  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= starti < endi <= 10^6`

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
- Run: `pytest -q -k "0253"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0056 | Medium | [Merge Intervals](../0056-merge-intervals/readme.md) | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |
| 0252 | Easy | [Meeting Rooms](../0252-meeting-rooms/readme.md) | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) |
| 0452 | Medium | [Minimum Number of Arrows to Burst Balloons](../0452-minimum-number-of-arrows-to-burst-balloons/readme.md) | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) |
| 1184 | Medium | [Car Pooling](../1184-car-pooling/readme.md) | [Car Pooling](https://leetcode.com/problems/car-pooling/) |
| 2334 | Hard | [Number of Flowers in Full Bloom](../2334-number-of-flowers-in-full-bloom/readme.md) | [Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |
| 2479 | Hard | [Meeting Rooms III](../2479-meeting-rooms-iii/readme.md) | [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) |
| 2553 | Medium | [Total Cost to Hire K Workers](../2553-total-cost-to-hire-k-workers/readme.md) | [Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) |
| 3034 | Easy | [Points That Intersect With Cars](../3034-points-that-intersect-with-cars/readme.md) | [Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## Examples

### Example 1

```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

### Example 2

```text
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## References

- LeetCode problem and editorial links
