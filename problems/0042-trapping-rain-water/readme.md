# 0042. Trapping Rain Water

## Quick Facts

- URL: [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- Function: `trap`
- Signature: `(height: list[int])  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

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
- Run: `pytest -q -k "0042"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                               | LeetCode                                                                                                        |
| ------ | ---------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 0011   | Medium     | [Container With Most Water](../0011-container-with-most-water/readme.md)                           | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                           |
| 0238   | Medium     | [Product of Array Except Self](../0238-product-of-array-except-self/readme.md)                     | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)                     |
| 0407   | Hard       | [Trapping Rain Water II](../0407-trapping-rain-water-ii/readme.md)                                 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)                                 |
| 0755   | Medium     | [Pour Water](../0755-pour-water/readme.md)                                                         | [Pour Water](https://leetcode.com/problems/pour-water/)                                                         |
| 2874   | Medium     | [Maximum Value of an Ordered Triplet II](../2874-maximum-value-of-an-ordered-triplet-ii/readme.md) | [Maximum Value of an Ordered Triplet II](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) |

## Examples

### Example 1

```text
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2

```text
Input: height = [4,2,0,3,2,5]
Output: 9
```

## References

- LeetCode problem and editorial links
