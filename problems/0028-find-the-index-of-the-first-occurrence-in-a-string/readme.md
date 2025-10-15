# 0028. Find the Index of the First Occurrence in a String

## Quick Facts

- URL:
  [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- Function: `strStr`
- Signature: `(haystack: str, needle: str)  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack and needle consist of only lowercase English characters.`

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
- Run: `pytest -q -k "0028"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0214   | Hard       | [Shortest Palindrome](../0214-shortest-palindrome/readme.md)               | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)               |
| 0459   | Easy       | [Repeated Substring Pattern](../0459-repeated-substring-pattern/readme.md) | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |

## Examples

### Example 1

```text
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

### Example 2

```text
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## References

- LeetCode problem and editorial links
