# 0712. Minimum ASCII Delete Sum for Two Strings

## Quick Facts

- URL:
  [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
- Function: `minimumDeleteSum`
- Signature: `(s1: str, s2: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= s1.length, s2.length <= 1000`
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
- Run: `pytest -q -k "0712"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                   | LeetCode                                                                                            |
| ------ | ---------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 0072   | Medium     | [Edit Distance](../0072-edit-distance/readme.md)                                       | [Edit Distance](https://leetcode.com/problems/edit-distance/)                                       |
| 0300   | Medium     | [Longest Increasing Subsequence](../0300-longest-increasing-subsequence/readme.md)     | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)     |
| 0583   | Medium     | [Delete Operation for Two Strings](../0583-delete-operation-for-two-strings/readme.md) | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |

## Examples

### Example 1

```text
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

### Example 2

```text
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```

## References

- LeetCode problem and editorial links
