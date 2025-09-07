# 0100. Same Tree

## Quick Facts

- URL: [Same Tree](https://leetcode.com/problems/same-tree/)
- Function: `isSameTree`
- Signature: `(p: TreeNode | None, q: TreeNode | None)  -> bool`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in both trees is in the range [0, 100].`
- `-10^4 <= Node.val <= 10^4`

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
- Run: `pytest -q -k "0100"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Example 2

```text
Input: p = [1,2], q = [1,null,2]
Output: false
```

### Example 3

```text
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## References

- LeetCode problem and editorial links
