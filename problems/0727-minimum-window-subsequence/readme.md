# 0727. Minimum Window Subsequence

## Quick Facts

- URL: [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
- Function: `minWindow`
- Signature: `(s1: str, s2: str)  -> str`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= s1.length <= 2 * 10^4`
- `1 <= s2.length <= 100`
- `s1 and s2 consist of lowercase English letters.`

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
- Run: `pytest -q -k "0727"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0076 | Hard | [Minimum Window Substring](../0076-minimum-window-substring/readme.md) | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| 0674 | Easy | [Longest Continuous Increasing Subsequence](../0674-longest-continuous-increasing-subsequence/readme.md) | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) |

## Examples

### Example 1

```text
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
```

### Example 2

```text
Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
```

## References

- LeetCode problem and editorial links
