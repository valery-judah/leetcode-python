# 0132. Palindrome Partitioning II

## Quick Facts

- URL: [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)
- Function: `minCut`
- Signature: `(s: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= s.length <= 2000`
- `s consists of lowercase English letters only.`

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
- Run: `pytest -q -k "0132"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                 | LeetCode                                                                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0131   | Medium     | [Palindrome Partitioning](../0131-palindrome-partitioning/readme.md)                                                                 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)                                                                 |
| 1745   | Hard       | [Palindrome Partitioning IV](../1745-palindrome-partitioning-iv/readme.md)                                                           | [Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv/)                                                           |
| 2472   | Hard       | [Maximum Number of Non-overlapping Palindrome Substrings](../2472-maximum-number-of-non-overlapping-palindrome-substrings/readme.md) | [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) |
| 2518   | Hard       | [Number of Great Partitions](../2518-number-of-great-partitions/readme.md)                                                           | [Number of Great Partitions](https://leetcode.com/problems/number-of-great-partitions/)                                                           |

## Examples

### Example 1

```text
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

### Example 2

```text
Input: s = "a"
Output: 0
```

### Example 3

```text
Input: s = "ab"
Output: 1
```

## References

- LeetCode problem and editorial links
