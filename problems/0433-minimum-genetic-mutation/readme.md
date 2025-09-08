# 0433. Minimum Genetic Mutation

## Quick Facts

- URL: [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)
- Function: `minMutation`
- Signature: `(startGene: str, endGene: str, bank: list[str])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `0 <= bank.length <= 10`
- `startGene.length == endGene.length == bank[i].length == 8`
- `startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].`

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
- Run: `pytest -q -k "0433"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0127 | Hard | [Word Ladder](../0127-word-ladder/readme.md) | [Word Ladder](https://leetcode.com/problems/word-ladder/) |

## Examples

### Example 1

```text
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
```

### Example 2

```text
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

## References

- LeetCode problem and editorial links
