# 0014. Longest Common Prefix

## Quick Facts

- URL: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- Function: `longestCommonPrefix`
- Signature: `(strs: list[str])  -> str`
- Primary pattern: **Array**

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i] consists of only lowercase English letters if it is non-empty.`

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
- Run: `pytest -q -k "0014"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2996 | Easy | [Smallest Missing Integer Greater Than Sequential Prefix Sum](../2996-smallest-missing-integer-greater-than-sequential-prefix-sum/readme.md) | [Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |
| 3043 | Medium | [Find the Length of the Longest Common Prefix](../3043-find-the-length-of-the-longest-common-prefix/readme.md) | [Find the Length of the Longest Common Prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) |
| 3093 | Hard | [Longest Common Suffix Queries](../3093-longest-common-suffix-queries/readme.md) | [Longest Common Suffix Queries](https://leetcode.com/problems/longest-common-suffix-queries/) |
| 3460 | Medium | [Longest Common Prefix After at Most One Removal](../3460-longest-common-prefix-after-at-most-one-removal/readme.md) | [Longest Common Prefix After at Most One Removal](https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/) |

## Examples

### Example 1

```text
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2

```text
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## References

- LeetCode problem and editorial links
