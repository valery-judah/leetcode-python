# 0502. IPO

## Quick Facts

- URL: [IPO](https://leetcode.com/problems/ipo/)
- Function: `findMaximizedCapital`
- Signature: `(k: int, w: int, profits: list[int], capital: list[int])  -> int`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= k <= 10^5`
- `0 <= w <= 10^9`
- `n == profits.length`
- `n == capital.length`
- `1 <= n <= 10^5`
- `0 <= profits[i] <= 10^4`
- `0 <= capital[i] <= 10^9`

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
- Run: `pytest -q -k "0502"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2542 | Medium | [Maximum Subsequence Score](../2542-maximum-subsequence-score/readme.md) | [Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/) |
| 2813 | Hard | [Maximum Elegance of a K-Length Subsequence](../2813-maximum-elegance-of-a-k-length-subsequence/readme.md) | [Maximum Elegance of a K-Length Subsequence](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/) |

## Examples

### Example 1

```text
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
```

### Example 2

```text
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
```

## References

- LeetCode problem and editorial links
