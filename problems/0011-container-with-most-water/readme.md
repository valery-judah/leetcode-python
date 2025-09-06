# 0011. Container With Most Water

## Quick Facts

- URL: https://leetcode.com/problems/container-with-most-water/
- Signature: `height: list[int]` → `int`
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
- Run: `pytest -q -k "0011"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0042 | Hard | [Trapping Rain Water](../0042-trapping-rain-water/readme.md) | [link](https://leetcode.com/problems/trapping-rain-water/) |
| 2517 | Medium | [Maximum Tastiness of Candy Basket](../2517-maximum-tastiness-of-candy-basket/readme.md) | [link](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/) |
| 2560 | Medium | [House Robber IV](../2560-house-robber-iv/readme.md) | [link](https://leetcode.com/problems/house-robber-iv/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
