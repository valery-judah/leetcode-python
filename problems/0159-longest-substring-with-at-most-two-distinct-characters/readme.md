# 0159. Longest Substring with At Most Two Distinct Characters

## Quick Facts

- URL: [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- Function: `lengthOfLongestSubstringTwoDistinct`
- Signature: `(s: str)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= s.length <= 10^5`
- `s consists of English letters.`

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
- Run: `pytest -q -k "0159"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0003 | Medium | [Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/readme.md) | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 0239 | Hard | [Sliding Window Maximum](../0239-sliding-window-maximum/readme.md) | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 0340 | Medium | [Longest Substring with At Most K Distinct Characters](../0340-longest-substring-with-at-most-k-distinct-characters/readme.md) | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| 1034 | Hard | [Subarrays with K Different Integers](../1034-subarrays-with-k-different-integers/readme.md) | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) |

## Examples

### Example 1

```text
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
```

### Example 2

```text
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
```

## References

- LeetCode problem and editorial links
