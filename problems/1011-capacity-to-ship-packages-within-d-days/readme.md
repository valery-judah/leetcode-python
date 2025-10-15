# 1011. Capacity To Ship Packages Within D Days

## Quick Facts

- URL:
  [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- Function: `shipWithinDays`
- Signature: `(weights: list[int], days: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

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
- Run: `pytest -q -k "1011"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                               | LeetCode                                                                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0410   | Hard       | [Split Array Largest Sum](../0410-split-array-largest-sum/readme.md)                                                               | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)                                                               |
| 1231   | Hard       | [Divide Chocolate](../1231-divide-chocolate/readme.md)                                                                             | [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/)                                                                             |
| 1891   | Medium     | [Cutting Ribbons](../1891-cutting-ribbons/readme.md)                                                                               | [Cutting Ribbons](https://leetcode.com/problems/cutting-ribbons/)                                                                               |
| 2064   | Medium     | [Minimized Maximum of Products Distributed to Any Store](../2064-minimized-maximum-of-products-distributed-to-any-store/readme.md) | [Minimized Maximum of Products Distributed to Any Store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) |
| 2279   | Medium     | [Maximum Bags With Full Capacity of Rocks](../2279-maximum-bags-with-full-capacity-of-rocks/readme.md)                             | [Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)                             |
| 2463   | Hard       | [Minimum Total Distance Traveled](../2463-minimum-total-distance-traveled/readme.md)                                               | [Minimum Total Distance Traveled](https://leetcode.com/problems/minimum-total-distance-traveled/)                                               |

## Examples

### Example 1

```text
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```

### Example 2

```text
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

### Example 3

```text
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

## References

- LeetCode problem and editorial links
