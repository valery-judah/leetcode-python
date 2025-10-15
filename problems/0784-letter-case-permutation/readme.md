# 0784. Letter Case Permutation

## Quick Facts

- URL: [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)
- Function: `letterCasePermutation`
- Signature: `(s: str)  -> list[str]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= s.length <= 12`
- `s consists of lowercase English letters, uppercase English letters, and digits.`

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
- Run: `pytest -q -k "0784"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                 | LeetCode                                                          |
| ------ | ---------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 0078   | Medium     | [Subsets](../0078-subsets/readme.md)                 | [Subsets](https://leetcode.com/problems/subsets/)                 |
| 1087   | Medium     | [Brace Expansion](../1087-brace-expansion/readme.md) | [Brace Expansion](https://leetcode.com/problems/brace-expansion/) |

## Examples

### Example 1

```text
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```

### Example 2

```text
Input: s = "3z4"
Output: ["3z4","3Z4"]
```

## References

- LeetCode problem and editorial links
