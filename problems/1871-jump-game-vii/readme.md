# 1871. Jump Game VII

## Quick Facts

- URL: [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)
- Function: `canReach`
- Signature: `(s: str, minJump: int, maxJump: int)  -> bool`
- Primary pattern: **Sliding Window**

## Constraints

- `2 <= s.length <= 10^5`
- `s[i] is either '0' or '1'.`
- `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`

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
- Run: `pytest -q -k "1871"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                 | LeetCode                                                                                                                          |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0045   | Medium     | [Jump Game II](../0045-jump-game-ii/readme.md)                                                                       | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                                                       |
| 0055   | Medium     | [Jump Game](../0055-jump-game/readme.md)                                                                             | [Jump Game](https://leetcode.com/problems/jump-game/)                                                                             |
| 1306   | Medium     | [Jump Game III](../1306-jump-game-iii/readme.md)                                                                     | [Jump Game III](https://leetcode.com/problems/jump-game-iii/)                                                                     |
| 1345   | Hard       | [Jump Game IV](../1345-jump-game-iv/readme.md)                                                                       | [Jump Game IV](https://leetcode.com/problems/jump-game-iv/)                                                                       |
| 1340   | Hard       | [Jump Game V](../1340-jump-game-v/readme.md)                                                                         | [Jump Game V](https://leetcode.com/problems/jump-game-v/)                                                                         |
| 1696   | Medium     | [Jump Game VI](../1696-jump-game-vi/readme.md)                                                                       | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)                                                                       |
| 1871   | Medium     | [Jump Game VII](readme.md)                                                                                           | [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)                                                                     |
| 2297   | Medium     | [Jump Game VIII](../2297-jump-game-viii/readme.md)                                                                   | [Jump Game VIII](https://leetcode.com/problems/jump-game-viii/)                                                                   |
| 2559   | Medium     | [Count Vowel Strings in Ranges](../2559-count-vowel-strings-in-ranges/readme.md)                                     | [Count Vowel Strings in Ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges/)                                     |
| 2770   | Medium     | [Maximum Number of Jumps to Reach the Last Index](../2770-maximum-number-of-jumps-to-reach-the-last-index/readme.md) | [Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) |

## Examples

### Example 1

```text
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.
```

### Example 2

```text
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
```

## References

- LeetCode problem and editorial links
