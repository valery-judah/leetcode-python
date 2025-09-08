# 0265. Paint House II

## Quick Facts

- URL: [Paint House II](https://leetcode.com/problems/paint-house-ii/)
- Function: `minCostII`
- Signature: `(costs: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `costs.length == n`
- `costs[i].length == k`
- `1 <= n <= 100`
- `2 <= k <= 20`
- `1 <= costs[i][j] <= 20`

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
- Run: `pytest -q -k "0265"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0238 | Medium | [Product of Array Except Self](../0238-product-of-array-except-self/readme.md) | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| 0239 | Hard | [Sliding Window Maximum](../0239-sliding-window-maximum/readme.md) | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 0256 | Medium | [Paint House](../0256-paint-house/readme.md) | [Paint House](https://leetcode.com/problems/paint-house/) |
| 0276 | Medium | [Paint Fence](../0276-paint-fence/readme.md) | [Paint Fence](https://leetcode.com/problems/paint-fence/) |

## Examples

### Example 1

```text
Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
```

### Example 2

```text
Input: costs = [[1,3],[2,4]]
Output: 5
```

## References

- LeetCode problem and editorial links
