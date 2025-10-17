# 0034. Find First and Last Position of Element in Sorted Array

## Quick Facts

- URL:
  [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- Function: `searchRange`
- Signature: `(nums: list[int], target: int)  -> list[int]`
- Primary pattern: **Binary Search**

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums is a non-decreasing array.`
- `-10^9 <= target <= 10^9`

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

### Alternative Binary Search Variations

Beyond the iterative implementations, several other variations of binary search are worth knowing:

1.  **Recursive Binary Search**:
    *   **Idea**: Uses function calls to recursively narrow the search space instead of a `while` loop.
    *   **Pros**: Can be more intuitive and elegant.
    *   **Cons**: Less efficient in Python due to function call overhead and potential for recursion depth errors.

2.  **Using Python's `bisect` Module**:
    *   **Idea**: Leverages the highly optimized `bisect_left` and `bisect_right` functions.
    *   **Pros**: The most "Pythonic" and efficient approach. It's concise, fast, and less error-prone.
    *   **Cons**: Relies on a standard library, so it doesn't demonstrate an understanding of the underlying algorithm.

3.  **Exponential Search**:
    *   **Idea**: Finds a range where the target is likely to be by checking indices `1, 2, 4, 8, ...` and then performs a binary search within that range.
    *   **Pros**: Useful for unbounded or infinite sorted arrays.
    *   **Cons**: More complex and not a direct replacement for standard binary search.

4.  **Interpolation Search**:
    *   **Idea**: Makes an educated guess about the target's position based on its value relative to the start and end of the array.
    *   **Pros**: Can be faster than binary search (O(log log n)) for uniformly distributed data.
    *   **Cons**: Worst-case performance is O(n) if the data is not uniformly distributed.

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
- Run: `pytest -q -k "0034"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                 | LeetCode                                                                                                          |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 0278   | Easy       | [First Bad Version](../0278-first-bad-version/readme.md)                                             | [First Bad Version](https://leetcode.com/problems/first-bad-version/)                                             |
| 2055   | Medium     | [Plates Between Candles](../2055-plates-between-candles/readme.md)                                   | [Plates Between Candles](https://leetcode.com/problems/plates-between-candles/)                                   |
| 2089   | Easy       | [Find Target Indices After Sorting Array](../2089-find-target-indices-after-sorting-array/readme.md) | [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |

## Examples

### Example 1

```text
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2

```text
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3

```text
Input: nums = [], target = 0
Output: [-1,-1]
```

## References

- LeetCode problem and editorial links
