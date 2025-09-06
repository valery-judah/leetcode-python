# 0124. Binary Tree Maximum Path Sum

## Quick Facts

- URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
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
- Run: `pytest -q -k "0124"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0064 | Easy | [Path Sum](../0064-path-sum/readme.md) | [link](https://leetcode.com/problems/path-sum/) |
| 0129 | Medium | [Sum Root to Leaf Numbers](../0129-sum-root-to-leaf-numbers/readme.md) | [link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) |
| 0666 | Medium | [Path Sum IV](../0666-path-sum-iv/readme.md) | [link](https://leetcode.com/problems/path-sum-iv/) |
| 0687 | Medium | [Longest Univalue Path](../0687-longest-univalue-path/readme.md) | [link](https://leetcode.com/problems/longest-univalue-path/) |
| 1376 | Medium | [Time Needed to Inform All Employees](../1376-time-needed-to-inform-all-employees/readme.md) | [link](https://leetcode.com/problems/time-needed-to-inform-all-employees/) |
| 2538 | Hard | [Difference Between Maximum and Minimum Price Sum](../2538-difference-between-maximum-and-minimum-price-sum/readme.md) | [link](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
