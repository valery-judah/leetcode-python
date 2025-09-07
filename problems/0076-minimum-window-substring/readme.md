# 0076. Minimum Window Substring

## Quick Facts

- URL: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- Function: `minWindow`
- Signature: `(s: str, t: str)  -> str`
- Primary pattern: **Sliding Window**

## Constraints

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s and t consist of uppercase and lowercase English letters.`

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
- Run: `pytest -q -k "0076"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0030 | Hard | [Substring with Concatenation of All Words](../0030-substring-with-concatenation-of-all-words/readme.md) | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |
| 0209 | Medium | [Minimum Size Subarray Sum](../0209-minimum-size-subarray-sum/readme.md) | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 0239 | Hard | [Sliding Window Maximum](../0239-sliding-window-maximum/readme.md) | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 0567 | Medium | [Permutation in String](../0567-permutation-in-string/readme.md) | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) |
| 0632 | Hard | [Smallest Range Covering Elements from K Lists](../0632-smallest-range-covering-elements-from-k-lists/readme.md) | [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) |
| 0727 | Hard | [Minimum Window Subsequence](../0727-minimum-window-subsequence/readme.md) | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) |
| 3572 | Hard | [Count Substrings That Can Be Rearranged to Contain a String II](../3572-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/readme.md) | [Count Substrings That Can Be Rearranged to Contain a String II](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) |
| 3573 | Medium | [Count Substrings That Can Be Rearranged to Contain a String I](../3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/readme.md) | [Count Substrings That Can Be Rearranged to Contain a String I](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/) |

## Examples

### Example 1

```text
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2

```text
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3

```text
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## References

- LeetCode problem and editorial links
