# 0276. Paint Fence

## Quick Facts

- URL: [Paint Fence](https://leetcode.com/problems/paint-fence/)
- Function: `numWays`
- Signature: `(n: int, k: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= n <= 50`
- `1 <= k <= 10^5`
- `The testcases are generated such that the answer is in the range [0, 2^31 - 1] for the given n and k.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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
- Run: `pytest -q -k "0276"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                 | LeetCode                                                          |
| ------ | ---------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 0198   | Medium     | [House Robber](../0198-house-robber/readme.md)       | [House Robber](https://leetcode.com/problems/house-robber/)       |
| 0213   | Medium     | [House Robber II](../0213-house-robber-ii/readme.md) | [House Robber II](https://leetcode.com/problems/house-robber-ii/) |
| 0256   | Medium     | [Paint House](../0256-paint-house/readme.md)         | [Paint House](https://leetcode.com/problems/paint-house/)         |
| 0265   | Hard       | [Paint House II](../0265-paint-house-ii/readme.md)   | [Paint House II](https://leetcode.com/problems/paint-house-ii/)   |

## Examples

### Example 1

```text
Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
```

### Example 2

```text
Input: n = 1, k = 1
Output: 1
```

### Example 3

```text
Input: n = 7, k = 2
Output: 42
```

## References

- LeetCode problem and editorial links
