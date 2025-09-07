# 0003. Longest Substring Without Repeating Characters

## Quick Facts

- URL: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- Function: `lengthOfLongestSubstring`
- Signature: `(s: str)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s consists of English letters, digits, symbols and spaces.`

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
- Run: `pytest -q -k "0003"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0159 | Medium | [Longest Substring with At Most Two Distinct Characters](../0159-longest-substring-with-at-most-two-distinct-characters/readme.md) | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| 0340 | Medium | [Longest Substring with At Most K Distinct Characters](../0340-longest-substring-with-at-most-k-distinct-characters/readme.md) | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| 1034 | Hard | [Subarrays with K Different Integers](../1034-subarrays-with-k-different-integers/readme.md) | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) |
| 1813 | Medium | [Maximum Erasure Value](../1813-maximum-erasure-value/readme.md) | [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) |
| 2209 | Medium | [Number of Equal Count Substrings](../2209-number-of-equal-count-substrings/readme.md) | [Number of Equal Count Substrings](https://leetcode.com/problems/number-of-equal-count-substrings/) |
| 2338 | Medium | [Minimum Consecutive Cards to Pick Up](../2338-minimum-consecutive-cards-to-pick-up/readme.md) | [Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) |
| 2478 | Medium | [Longest Nice Subarray](../2478-longest-nice-subarray/readme.md) | [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) |
| 2487 | Medium | [Optimal Partition of String](../2487-optimal-partition-of-string/readme.md) | [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) |
| 2856 | Medium | [Count Complete Subarrays in an Array](../2856-count-complete-subarrays-in-an-array/readme.md) | [Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) |
| 3266 | Medium | [Find Longest Special Substring That Occurs Thrice II](../3266-find-longest-special-substring-that-occurs-thrice-ii/readme.md) | [Find Longest Special Substring That Occurs Thrice II](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/) |
| 3267 | Medium | [Find Longest Special Substring That Occurs Thrice I](../3267-find-longest-special-substring-that-occurs-thrice-i/readme.md) | [Find Longest Special Substring That Occurs Thrice I](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/) |

## Examples

### Example 1

```text
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2

```text
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3

```text
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## References

- LeetCode problem and editorial links
