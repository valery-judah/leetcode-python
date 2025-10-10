# 0125. Valid Palindrome

## Quick Facts

- URL: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- Function: `isPalindrome`
- Signature: `(s: str)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s consists only of printable ASCII characters.`

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
- Run: `pytest -q -k "0125"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0234 | Easy | [Palindrome Linked List](../0234-palindrome-linked-list/readme.md) | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) |
| 0680 | Easy | [Valid Palindrome II](../0680-valid-palindrome-ii/readme.md) | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) |
| 2002 | Medium | [Maximum Product of the Length of Two Palindromic Subsequences](../2002-maximum-product-of-the-length-of-two-palindromic-subsequences/readme.md) | [Maximum Product of the Length of Two Palindromic Subsequences](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) |
| 2108 | Easy | [Find First Palindromic String in the Array](../2108-find-first-palindromic-string-in-the-array/readme.md) | [Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |
| 2330 | Medium | [Valid Palindrome IV](../2330-valid-palindrome-iv/readme.md) | [Valid Palindrome IV](https://leetcode.com/problems/valid-palindrome-iv/) |
| 3035 | Medium | [Maximum Palindromes After Operations](../3035-maximum-palindromes-after-operations/readme.md) | [Maximum Palindromes After Operations](https://leetcode.com/problems/maximum-palindromes-after-operations/) |

## Examples

### Example 1

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2

```text
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3

```text
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Essential notes

The core problem arises when an inner "seeking" loop, designed to find a valid item, runs unchecked and moves a pointer past the array's boundaries or past its counterpart pointer.

The overarching strategy is to ensure that any sub-operation (like an inner seeking loop) is strictly constrained by the rules, or invariants, of its parent operation (the main loop). An inner process should never be allowed to violate the boundaries established by the outer process.

## Tactics for Prevention

To augment your `example-construction-bias.md` note, adopt the following recommendations:

- **Adopt an Adversarial Mindset:** Shift the goal of testing from _confirming_ that code works on expected inputs to actively trying to _falsify_ it by finding inputs where it fails.

- **Systematize with Equivalence Classes:** Instead of constructing ad-hoc examples, partition all possible inputs into logical classes. This forces consideration of non-obvious categories.

- **Prioritize Antagonistic Classes:** Consciously create test cases from the classes your bias makes you likely to ignore. For any given problem, always include:

  - The **Zero-Element Class:** Inputs with no valid data (e.g., `""`, `",.!;"`).

  - The **Singleton Class:** Inputs with exactly one valid data point (e.g., `"-a-"`).

  - The **Boundary Class:** Inputs where valid data is at the absolute edges (e.g., `"a,,,,,"`, `",,,,,a"`).

- **Formalize into a Checklist:** Convert this process into a repeatable checklist. Before committing code, verify that you have written a test case for each non-obvious equivalence class. This transforms the mitigation of bias from a hope into a defined engineering step.

# Attempt 2

- forgot about guard close and ".," test case

* used phased approach
