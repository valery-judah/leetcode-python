# 0009. Palindrome Number

## Quick Facts

- URL: [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- Function: `isPalindrome`
- Signature: `(x: int)  -> bool`
- Primary pattern: **Math**

## Constraints

- `-2^31 <= x <= 2^31 - 1`

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
- Run: `pytest -q -k "0009"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                       | LeetCode                                                                                                                |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 0234   | Easy       | [Palindrome Linked List](../0234-palindrome-linked-list/readme.md)                                         | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                                         |
| 2217   | Medium     | [Find Palindrome With Fixed Length](../2217-find-palindrome-with-fixed-length/readme.md)                   | [Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length/)                   |
| 2396   | Medium     | [Strictly Palindromic Number](../2396-strictly-palindromic-number/readme.md)                               | [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/)                               |
| 2843   | Easy       | [Count Symmetric Integers](../2843-count-symmetric-integers/readme.md)                                     | [Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers/)                                     |
| 3272   | Hard       | [Find the Count of Good Integers](../3272-find-the-count-of-good-integers/readme.md)                       | [Find the Count of Good Integers](https://leetcode.com/problems/find-the-count-of-good-integers/)                       |
| 3260   | Hard       | [Find the Largest Palindrome Divisible by K](../3260-find-the-largest-palindrome-divisible-by-k/readme.md) | [Find the Largest Palindrome Divisible by K](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/) |

## Examples

### Example 1

```text
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Example 2

```text
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3

```text
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## References

- LeetCode problem and editorial links
