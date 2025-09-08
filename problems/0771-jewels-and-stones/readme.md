# 0771. Jewels and Stones

## Quick Facts

- URL: [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
- Function: `numJewelsInStones`
- Signature: `(jewels: str, stones: str)  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= jewels.length, stones.length <= 50`
- `jewels and stones consist of only English letters.`
- `All the characters of jewels are unique.`

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
- Run: `pytest -q -k "0771"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
```

### Example 2

```text
Input: jewels = "z", stones = "ZZ"
Output: 0
```

## References

- LeetCode problem and editorial links
