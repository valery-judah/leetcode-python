# 1345. Jump Game IV

## Quick Facts

- URL: [Jump Game IV](https://leetcode.com/problems/jump-game-iv/)
- Function: `minJumps`
- Signature: `(arr: list[int])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= arr.length <= 5 * 10^4`
- `-10^8 <= arr[i] <= 10^8`

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
- Run: `pytest -q -k "1345"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                 | LeetCode                                                                                                                          |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1871   | Medium     | [Jump Game VII](../1871-jump-game-vii/readme.md)                                                                     | [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)                                                                     |
| 2297   | Medium     | [Jump Game VIII](../2297-jump-game-viii/readme.md)                                                                   | [Jump Game VIII](https://leetcode.com/problems/jump-game-viii/)                                                                   |
| 2770   | Medium     | [Maximum Number of Jumps to Reach the Last Index](../2770-maximum-number-of-jumps-to-reach-the-last-index/readme.md) | [Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) |

## Examples

### Example 1

```text
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
```

### Example 2

```text
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
```

### Example 3

```text
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
```

## References

- LeetCode problem and editorial links
