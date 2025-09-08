# 0844. Backspace String Compare

## Quick Facts

- URL: [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
- Function: `backspaceCompare`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length, t.length <= 200`
- `s and t only contain lowercase letters and '#' characters.`

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
- Run: `pytest -q -k "0844"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1598 | Easy | [Crawler Log Folder](../1598-crawler-log-folder/readme.md) | [Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/) |
| 2390 | Medium | [Removing Stars From a String](../2390-removing-stars-from-a-string/readme.md) | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/) |

## Examples

### Example 1

```text
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

### Example 2

```text
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

### Example 3

```text
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

## References

- LeetCode problem and editorial links
