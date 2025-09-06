# 0050. Pow(x, n)

## Quick Facts

- URL: https://leetcode.com/problems/powx-n/
- Signature: `x: float`, `n: int` → `float`
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
- Run: `pytest -q -k "0050"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0069 | Easy | [Sqrt(x)](../0069-sqrtx/readme.md) | [link](https://leetcode.com/problems/sqrtx/) |
| 0372 | Medium | [Super Pow](../0372-super-pow/readme.md) | [link](https://leetcode.com/problems/super-pow/) |
| 2550 | Medium | [Count Collisions of Monkeys on a Polygon](../2550-count-collisions-of-monkeys-on-a-polygon/readme.md) | [link](https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
