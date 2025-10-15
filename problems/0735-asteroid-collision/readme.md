# 0735. Asteroid Collision

## Quick Facts

- URL: [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
- Function: `asteroidCollision`
- Signature: `(asteroids: list[int])  -> list[int]`
- Primary pattern: **Stack**

## Constraints

- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

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
- Run: `pytest -q -k "0735"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0605   | Easy       | [Can Place Flowers](../0605-can-place-flowers/readme.md)                   | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)                   |
| 2126   | Medium     | [Destroying Asteroids](../2126-destroying-asteroids/readme.md)             | [Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/)             |
| 2211   | Medium     | [Count Collisions on a Road](../2211-count-collisions-on-a-road/readme.md) | [Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/) |
| 2751   | Hard       | [Robot Collisions](../2751-robot-collisions/readme.md)                     | [Robot Collisions](https://leetcode.com/problems/robot-collisions/)                     |

## Examples

### Example 1

```text
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

### Example 2

```text
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

### Example 3

```text
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

## References

- LeetCode problem and editorial links
