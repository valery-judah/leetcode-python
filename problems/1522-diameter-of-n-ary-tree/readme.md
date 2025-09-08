# 1522. Diameter of N-Ary Tree

## Quick Facts

- URL: [Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/)
- Function: `diameter`
- Signature: `(root: int)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The depth of the n-ary tree is less than or equal to 1000.`
- `The total number of nodes is between [1, 10^4].`

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
- Run: `pytest -q -k "1522"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0543 | Easy | [Diameter of Binary Tree](../0543-diameter-of-binary-tree/readme.md) | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) |

## Examples

### Example 1

```text
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
```

### Example 2

```text
Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
```

### Example 3

```text
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
```

## References

- LeetCode problem and editorial links
