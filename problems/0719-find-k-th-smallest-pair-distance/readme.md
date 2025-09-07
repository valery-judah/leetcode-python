# 0719. Find K-th Smallest Pair Distance

## Quick Facts

- URL: [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)
- Function: `smallestDistancePair`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `n == nums.length`
- `2 <= n <= 10^4`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= n * (n - 1) / 2`

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
- Run: `pytest -q -k "0719"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0373 | Medium | [Find K Pairs with Smallest Sums](../0373-find-k-pairs-with-smallest-sums/readme.md) | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) |
| 0378 | Medium | [Kth Smallest Element in a Sorted Matrix](../0378-kth-smallest-element-in-a-sorted-matrix/readme.md) | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |
| 0658 | Medium | [Find K Closest Elements](../0658-find-k-closest-elements/readme.md) | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) |
| 0668 | Hard | [Kth Smallest Number in Multiplication Table](../0668-kth-smallest-number-in-multiplication-table/readme.md) | [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) |
| 0786 | Medium | [K-th Smallest Prime Fraction](../0786-k-th-smallest-prime-fraction/readme.md) | [K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/) |
| 3134 | Hard | [Find the Median of the Uniqueness Array](../3134-find-the-median-of-the-uniqueness-array/readme.md) | [Find the Median of the Uniqueness Array](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) |
| 3281 | Medium | [Maximize Score of Numbers in Ranges](../3281-maximize-score-of-numbers-in-ranges/readme.md) | [Maximize Score of Numbers in Ranges](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/) |

## Examples

### Example 1

```text
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
```

### Example 2

```text
Input: nums = [1,1,1], k = 2
Output: 0
```

### Example 3

```text
Input: nums = [1,6,1], k = 3
Output: 5
```

## References

- LeetCode problem and editorial links
