# 0767. Reorganize String

## Quick Facts

- URL: [Reorganize String](https://leetcode.com/problems/reorganize-string/)
- Function: `reorganizeString`
- Signature: `(s: str)  -> str`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= s.length <= 500`
- `s consists of lowercase English letters.`

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
- Run: `pytest -q -k "0767"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0358 | Hard | [Rearrange String k Distance Apart](../0358-rearrange-string-k-distance-apart/readme.md) | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) |
| 0621 | Medium | [Task Scheduler](../0621-task-scheduler/readme.md) | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) |
| 1405 | Medium | [Longest Happy String](../1405-longest-happy-string/readme.md) | [Longest Happy String](https://leetcode.com/problems/longest-happy-string/) |

## Examples

### Example 1

```text
Input: s = "aab"
Output: "aba"
```

### Example 2

```text
Input: s = "aaab"
Output: ""
```

## References

- LeetCode problem and editorial links
