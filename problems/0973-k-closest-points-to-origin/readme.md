# 0973. K Closest Points to Origin

## Quick Facts

- URL: [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- Function: `kClosest`
- Signature: `(points: list[list[int]], k: int)  -> list[list[int]]`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

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
- Run: `pytest -q -k "0973"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0215 | Medium | [Kth Largest Element in an Array](../0215-kth-largest-element-in-an-array/readme.md) | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |
| 0347 | Medium | [Top K Frequent Elements](../0347-top-k-frequent-elements/readme.md) | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| 0692 | Medium | [Top K Frequent Words](../0692-top-k-frequent-words/readme.md) | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) |
| 1779 | Easy | [Find Nearest Point That Has the Same X or Y Coordinate](../1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/readme.md) | [Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) |
| 3111 | Medium | [Minimum Rectangles to Cover Points](../3111-minimum-rectangles-to-cover-points/readme.md) | [Minimum Rectangles to Cover Points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/) |
| 3275 | Medium | [K-th Nearest Obstacle Queries](../3275-k-th-nearest-obstacle-queries/readme.md) | [K-th Nearest Obstacle Queries](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) |

## Examples

### Example 1

```text
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

### Example 2

```text
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## References

- LeetCode problem and editorial links
