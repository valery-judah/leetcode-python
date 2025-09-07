# 0358. Rearrange String k Distance Apart

## Quick Facts

- URL: [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)
- Function: `rearrangeString`
- Signature: `(s: str, k: int)  -> str`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s consists of only lowercase English letters.`
- `0 <= k <= s.length`

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
- Run: `pytest -q -k "0358"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0621 | Medium | [Task Scheduler](../0621-task-scheduler/readme.md) | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) |
| 0778 | Medium | [Reorganize String](../0778-reorganize-string/readme.md) | [Reorganize String](https://leetcode.com/problems/reorganize-string/) |
| 2300 | Medium | [Construct String With Repeat Limit](../2300-construct-string-with-repeat-limit/readme.md) | [Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit/) |

## Examples

### Example 1

```text
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
```

### Example 2

```text
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
```

### Example 3

```text
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
```

## References

- LeetCode problem and editorial links
