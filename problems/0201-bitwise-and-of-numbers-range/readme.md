# 0201. Bitwise AND of Numbers Range

## Quick Facts

- URL: [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
- Function: `rangeBitwiseAnd`
- Signature: `(left: int, right: int)  -> int`
- Primary pattern: **Bit Manipulation**

## Constraints

- `0 <= left <= right <= 2^31 - 1`

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
- Run: `pytest -q -k "0201"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2478 | Medium | [Longest Nice Subarray](../2478-longest-nice-subarray/readme.md) | [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) |

## Examples

### Example 1

```text
Input: left = 5, right = 7
Output: 4
```

### Example 2

```text
Input: left = 0, right = 0
Output: 0
```

### Example 3

```text
Input: left = 1, right = 2147483647
Output: 0
```

## References

- LeetCode problem and editorial links
