# 0253. Meeting Rooms II

## Quick Facts

- URL: https://leetcode.com/problems/meeting-rooms-ii/
- Signature: `intervals: list[list[int]]` → `int`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
| 0056 | Medium | [Merge Intervals](../0056-merge-intervals/readme.md) | [link](https://leetcode.com/problems/merge-intervals/) |
| 0252 | Easy | [Meeting Rooms](../0252-meeting-rooms/readme.md) | [link](https://leetcode.com/problems/meeting-rooms/) |
| 0452 | Medium | [Minimum Number of Arrows to Burst Balloons](../0452-minimum-number-of-arrows-to-burst-balloons/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) |
| 1094 | Medium | [Car Pooling](../1094-car-pooling/readme.md) | [link](https://leetcode.com/problems/car-pooling/) |
| 2251 | Hard | [Number of Flowers in Full Bloom](../2251-number-of-flowers-in-full-bloom/readme.md) | [link](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |
| 2402 | Hard | [Meeting Rooms III](../2402-meeting-rooms-iii/readme.md) | [link](https://leetcode.com/problems/meeting-rooms-iii/) |
| 2462 | Medium | [Total Cost to Hire K Workers](../2462-total-cost-to-hire-k-workers/readme.md) | [link](https://leetcode.com/problems/total-cost-to-hire-k-workers/) |
| 2848 | Easy | [Points That Intersect With Cars](../2848-points-that-intersect-with-cars/readme.md) | [link](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:54Z: Created scaffold.
