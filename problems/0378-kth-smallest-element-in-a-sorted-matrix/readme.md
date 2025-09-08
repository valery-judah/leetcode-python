# 0378. Kth Smallest Element in a Sorted Matrix

## Quick Facts

- URL: [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- Function: `kthSmallest`
- Signature: `(matrix: list[list[int]], k: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- `All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.`
- `1 <= k <= n^2`

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
- Run: `pytest -q -k "0378"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0373 | Medium | [Find K Pairs with Smallest Sums](../0373-find-k-pairs-with-smallest-sums/readme.md) | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) |
| 0668 | Hard | [Kth Smallest Number in Multiplication Table](../0668-kth-smallest-number-in-multiplication-table/readme.md) | [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) |
| 0719 | Hard | [Find K-th Smallest Pair Distance](../0719-find-k-th-smallest-pair-distance/readme.md) | [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) |
| 0786 | Medium | [K-th Smallest Prime Fraction](../0786-k-th-smallest-prime-fraction/readme.md) | [K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/) |

## Examples

### Example 1

```text
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

### Example 2

```text
Input: matrix = [[-5]], k = 1
Output: -5
```

## References

- LeetCode problem and editorial links
