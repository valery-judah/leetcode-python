# 0269. Alien Dictionary

## Quick Facts

- URL: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- Function: `alienOrder`
- Signature: `(words: list[str])  -> str`
- Primary pattern: **Graph**

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i] consists of only lowercase English letters.`

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
- Run: `pytest -q -k "0269"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0210 | Medium | [Course Schedule II](../0210-course-schedule-ii/readme.md) | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |

## Examples

### Example 1

```text
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

### Example 2

```text
Input: words = ["z","x"]
Output: "zx"
```

### Example 3

```text
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## References

- LeetCode problem and editorial links
