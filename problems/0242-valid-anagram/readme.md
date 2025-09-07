# 0242. Valid Anagram

## Quick Facts

- URL: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- Function: `isAnagram`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s and t consist of lowercase English letters.`

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
- Run: `pytest -q -k "0242"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0049 | Medium | [Group Anagrams](../0049-group-anagrams/readme.md) | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| 0266 | Easy | [Palindrome Permutation](../0266-palindrome-permutation/readme.md) | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) |
| 0438 | Medium | [Find All Anagrams in a String](../0438-find-all-anagrams-in-a-string/readme.md) | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |
| 2273 | Easy | [Find Resultant Array After Removing Anagrams](../2273-find-resultant-array-after-removing-anagrams/readme.md) | [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |

## Examples

None

## References

- LeetCode problem and editorial links

## 1. Problem Statement

Given two strings, `s` and `t`, determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## 2. Core Intuition: Canonical Representation

The fundamental insight is that the order of characters in a string is irrelevant when checking for an anagram. We only care about the characters themselves and their frequencies. This suggests that if we can convert a string into a **canonical representation** that ignores order, we can solve the problem with a simple comparison.

- **Definition**: Two strings `s` and `t` are anagrams if and only if their character multisets (sets that allow for duplicate elements) are identical.

- **Canonical Forms**: We can represent this multiset in two primary ways:

    1. A sorted sequence of its characters.

    2. A frequency map (or histogram) of its characters.

If the canonical forms of `s` and `t` are equal, they are anagrams.

## 3. Approaches

### Approach 1: Sorting

This is the most direct implementation of the first canonical form. We sort both strings and check if the results are identical.

```python
class SolutionSort:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimization: Anagrams must have the same length.
        if len(s) != len(t):
            return False
        # Convert to sorted lists of characters and compare.
        return sorted(s) == sorted(t)
```

- **Time Complexity**: **O(N log N)**, dominated by the sorting algorithm.

- **Space Complexity**: **O(N)** in Python, as strings are immutable and `sorted()` creates new lists. In a language that allows in-place sorting of character arrays, it could be O(1) or O(log N) depending on the sort implementation's space requirements.

### Approach 2: Frequency Counter (Optimal)

This approach uses the second canonical form. We count the frequency of each character in both strings and compare the resulting frequency maps.

#### 2a. Using a Hash Map (General Purpose)

A hash map is a robust choice that works for any character set (ASCII, Unicode, etc.).

```python
from collections import Counter

class SolutionFrequencyCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # The Counter class builds the frequency map automatically.
        return Counter(s) == Counter(t)
```

- **Time Complexity**: **O(N)**, where N is the length of the strings. We perform a single pass over each string to build the maps.

- **Space Complexity**: **O(k)**, where `k` is the number of unique characters in the alphabet.

#### 2b. Using an Array (Optimized for Constraints)

The problem states that inputs consist of "lowercase English letters." This is a critical constraint. Knowing the character set is fixed and small (26 letters) allows for a highly efficient array-based frequency map.

```python
class SolutionArrayCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        ord_a = ord('a')

        for char in s:
            counts[ord(char) - ord_a] += 1

        for char in t:
            counts[ord(char) - ord_a] -= 1
            # Optimization: If a count goes below zero, they can't be anagrams.
            if counts[ord(char) - ord_a] < 0:
                return False

        # If all counts are zero, the final array will be all zeros.
        # This check is implicitly handled by the loop. If we finish, it's True.
        return True
```

- **Time Complexity**: **O(N)**.

- **Space Complexity**: **O(1)**, as the array size (26) is constant and does not depend on the input string length.

## 4. Key Pitfalls and Discussion Points

1. **Ignoring Character Frequencies**: A common mistake is only checking for character _presence_, not _count_. This fails for cases like `s = "aab"`, `t = "abc"`.

2. **Forgetting the Length Check**: Always start with `if len(s) != len(t): return False`. It's a simple, highly effective optimization that handles many negative cases instantly.

3. **Overlooking Constraints (The Character Set Discussion)**:

    - **Lowercase English (as per problem)**: An array of size 26 is the most optimal data structure. This demonstrates attention to detail and performance.

    - **Full ASCII**: An array of size 256 would be appropriate.

    - **Unicode**: The character set is vast and sparse. Using an array would be impractical due to its enormous size. A **hash map** is the correct and necessary choice here. A strong candidate can discuss these trade-offs.

4. **Choosing a Suboptimal Approach**: While the sorting solution is correct, a candidate should recognize and explain why the frequency counter approach is asymptotically more efficient (O(N) vs. O(N log N)).

# Complexity Reasoning

Complexity Analysis (Formal Summary)

- **Time Complexity: O(N+M)**

  - We iterate through string `s` once to build its frequency map. This takes O(N) time, where N is the length of `s`.

  - We then iterate through string `t` once to build its frequency map. This takes O(M) time, where M is the length of `t`.

  - Comparing the two maps takes time proportional to the number of unique keys. Since the character set is fixed to 26 lowercase English letters, this comparison is O(26), which is constant time, i.e., O(1).

  - The total time complexity is O(N+M+1)=O(N+M). If both strings have a similar length `L`, this is often simplified to O(L).

- **Space Complexity: O(1)**

  - The space is determined by the storage required for the frequency maps.

  - In the worst case, each map will store one entry for each unique character in the alphabet.

  - Since the alphabet is fixed at 26, the maximum size of each map is 26. This is a constant amount of space. Therefore, the space complexity is O(1).
