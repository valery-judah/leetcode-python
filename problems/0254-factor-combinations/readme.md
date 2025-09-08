# 0254. Factor Combinations

## Quick Facts

- URL: [Factor Combinations](https://leetcode.com/problems/factor-combinations/)
- Function: `getFactors`
- Signature: `(n: int)  -> list[list[int]]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= n <= 10^7`

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
- Run: `pytest -q -k "0254"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0039 | Medium | [Combination Sum](../0039-combination-sum/readme.md) | [Combination Sum](https://leetcode.com/problems/combination-sum/) |

## Examples

### Example 1

```text
Input: n = 1
Output: []
```

### Example 2

```text
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
```

### Example 3

```text
Input: n = 37
Output: []
```

## References

- LeetCode problem and editorial links
