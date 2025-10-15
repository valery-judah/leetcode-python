# 0853. Car Fleet

## Quick Facts

- URL: [Car Fleet](https://leetcode.com/problems/car-fleet/)
- Function: `carFleet`
- Signature: `(target: int, position: list[int], speed: list[int])  -> int`
- Primary pattern: **Stack**

## Constraints

- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- `All the values of position are unique.`
- `0 < speed[i] <= 10^6`

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
- Run: `pytest -q -k "0853"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 1776   | Hard       | [Car Fleet II](../1776-car-fleet-ii/readme.md)                             | [Car Fleet II](https://leetcode.com/problems/car-fleet-ii/)                             |
| 2211   | Medium     | [Count Collisions on a Road](../2211-count-collisions-on-a-road/readme.md) | [Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/) |

## Examples

None

## References

- LeetCode problem and editorial links
