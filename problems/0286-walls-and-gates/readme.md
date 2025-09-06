# 0286. Walls and Gates

## Quick Facts

- URL: https://leetcode.com/problems/walls-and-gates/
- Signature: `rooms: list[list[int]]` → `None`
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
- Run: `pytest -q -k "0286"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0130 | Medium | [Surrounded Regions](../0130-surrounded-regions/readme.md) | [link](https://leetcode.com/problems/surrounded-regions/) |
| 0200 | Medium | [Number of Islands](../0200-number-of-islands/readme.md) | [link](https://leetcode.com/problems/number-of-islands/) |
| 0317 | Hard | [Shortest Distance from All Buildings](../0317-shortest-distance-from-all-buildings/readme.md) | [link](https://leetcode.com/problems/shortest-distance-from-all-buildings/) |
| 0419 | Medium | [Battleships in a Board](../0419-battleships-in-a-board/readme.md) | [link](https://leetcode.com/problems/battleships-in-a-board/) |
| 0489 | Hard | [Robot Room Cleaner](../0489-robot-room-cleaner/readme.md) | [link](https://leetcode.com/problems/robot-room-cleaner/) |
| 0994 | Medium | [Rotting Oranges](../0994-rotting-oranges/readme.md) | [link](https://leetcode.com/problems/rotting-oranges/) |
| 3015 | Medium | [Count the Number of Houses at a Certain Distance I](../3015-count-the-number-of-houses-at-a-certain-distance-i/readme.md) | [link](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/) |
| 3017 | Hard | [Count the Number of Houses at a Certain Distance II](../3017-count-the-number-of-houses-at-a-certain-distance-ii/readme.md) | [link](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
