# 0735. Asteroid Collision

## Quick Facts

- URL: https://leetcode.com/problems/asteroid-collision/
- Signature: `asteroids: list[int]` → `list[int]`
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
- Run: `pytest -q -k "0735"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0605 | Easy | [Can Place Flowers](../0605-can-place-flowers/readme.md) | [link](https://leetcode.com/problems/can-place-flowers/) |
| 2126 | Medium | [Destroying Asteroids](../2126-destroying-asteroids/readme.md) | [link](https://leetcode.com/problems/destroying-asteroids/) |
| 2211 | Medium | [Count Collisions on a Road](../2211-count-collisions-on-a-road/readme.md) | [link](https://leetcode.com/problems/count-collisions-on-a-road/) |
| 2751 | Hard | [Robot Collisions](../2751-robot-collisions/readme.md) | [link](https://leetcode.com/problems/robot-collisions/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:59Z: Created scaffold.
