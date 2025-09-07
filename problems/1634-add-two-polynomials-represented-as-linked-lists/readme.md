# 1634. Add Two Polynomials Represented as Linked Lists

## Quick Facts

- URL: [Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/)
- Function: `addPoly`
- Signature: `(poly1: list[list[int]], poly2: list[list[int]])  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `0 <= n <= 10^4`
- `-10^9 <= PolyNode.coefficient <= 10^9`
- `PolyNode.coefficient != 0`
- `0 <= PolyNode.power <= 10^9`
- `PolyNode.power > PolyNode.next.power`

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
- Run: `pytest -q -k "1634"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0002 | Medium | [Add Two Numbers](../0002-add-two-numbers/readme.md) | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |
| 0021 | Easy | [Merge Two Sorted Lists](../0021-merge-two-sorted-lists/readme.md) | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |
| 0445 | Medium | [Add Two Numbers II](../0445-add-two-numbers-ii/readme.md) | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) |

## Examples

### Example 1

```text
Input: poly1 = [[1,1]], poly2 = [[1,0]]
Output: [[1,1],[1,0]]
Explanation: poly1 = x. poly2 = 1. The sum is x + 1.
```

### Example 2

```text
Input: poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
Output: [[5,2],[2,0]]
Explanation: poly1 = 2x2 + 4x + 3. poly2 = 3x2 - 4x - 1. The sum is 5x2 + 2. Notice that we omit the "0x" term.
```

### Example 3

```text
Input: poly1 = [[1,2]], poly2 = [[-1,2]]
Output: []
Explanation: The sum is 0. We return an empty list.
```

## References

- LeetCode problem and editorial links
