# 0161. One Edit Distance

## Quick Facts

- URL: [One Edit Distance](https://leetcode.com/problems/one-edit-distance/)
- Function: `isOneEditDistance`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `0 <= s.length, t.length <= 10^4`
- `s and t consist of lowercase letters, uppercase letters, and digits.`

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
- Run: `pytest -q -k "0161"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                             | LeetCode                                                      |
| ------ | ---------- | ------------------------------------------------ | ------------------------------------------------------------- |
| 0072   | Medium     | [Edit Distance](../0072-edit-distance/readme.md) | [Edit Distance](https://leetcode.com/problems/edit-distance/) |

## Examples

### Example 1

```text
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
```

### Example 2

```text
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
```

## References

- LeetCode problem and editorial links
