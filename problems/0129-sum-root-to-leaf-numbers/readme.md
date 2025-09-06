# 0129. Sum Root to Leaf Numbers

## Quick Facts

- URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
- Signature: `root: TreeNode | None` → `int`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0129"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0064 | Easy | [Path Sum](../0064-path-sum/readme.md) | [link](https://leetcode.com/problems/path-sum/) |
| 0124 | Hard | [Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/readme.md) | [link](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |
| 0988 | Medium | [Smallest String Starting From Leaf](../0988-smallest-string-starting-from-leaf/readme.md) | [link](https://leetcode.com/problems/smallest-string-starting-from-leaf/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
