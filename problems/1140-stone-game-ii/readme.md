# 1140. Stone Game II

## Quick Facts

- URL: [Stone Game II](https://leetcode.com/problems/stone-game-ii/)
- Function: `stoneGameII`
- Signature: `(piles: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10^4`

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
- Run: `pytest -q -k "1140"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1563 | Hard | [Stone Game V](../1563-stone-game-v/readme.md) | [Stone Game V](https://leetcode.com/problems/stone-game-v/) |
| 1686 | Medium | [Stone Game VI](../1686-stone-game-vi/readme.md) | [Stone Game VI](https://leetcode.com/problems/stone-game-vi/) |
| 1690 | Medium | [Stone Game VII](../1690-stone-game-vii/readme.md) | [Stone Game VII](https://leetcode.com/problems/stone-game-vii/) |
| 1872 | Hard | [Stone Game VIII](../1872-stone-game-viii/readme.md) | [Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) |
| 2029 | Medium | [Stone Game IX](../2029-stone-game-ix/readme.md) | [Stone Game IX](https://leetcode.com/problems/stone-game-ix/) |

## Examples

None

## References

- LeetCode problem and editorial links
