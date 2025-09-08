# 0131. Palindrome Partitioning

## Quick Facts

- URL: [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- Function: `partition`
- Signature: `(s: str)  -> list[list[str]]`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= s.length <= 16`
- `s contains only lowercase English letters.`

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
- Run: `pytest -q -k "0131"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0132 | Hard | [Palindrome Partitioning II](../0132-palindrome-partitioning-ii/readme.md) | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |
| 1745 | Hard | [Palindrome Partitioning IV](../1745-palindrome-partitioning-iv/readme.md) | [Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv/) |
| 2472 | Hard | [Maximum Number of Non-overlapping Palindrome Substrings](../2472-maximum-number-of-non-overlapping-palindrome-substrings/readme.md) | [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) |

## Examples

### Example 1

```text
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2

```text
Input: s = "a"
Output: [["a"]]
```

## References

- LeetCode problem and editorial links
