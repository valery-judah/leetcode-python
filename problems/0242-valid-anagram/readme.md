# 242. Find Resultant Array After Removing Anagrams

- **URL**: <https://leetcode.com/problems/valid-anagram/>
- **Difficulty**: easy
- **Tags**: Hash Table, String, Sorting

## Files

- [solutions.py](solutions.py): Implementations (single or multi-variant via `ALL_SOLUTIONS`) and
  `TEST_CASES`.

## Similar Questions

- [Medium] [Group Anagrams](../0049-group-anagrams/readme.md)
- [Easy] [Palindrome Permutation](../0266-palindrome-permutation/readme.md)
- [Medium] [Find All Anagrams in a String](../0438-find-all-anagrams-in-a-string/readme.md)
- [Easy]
  [Find Resultant Array After Removing Anagrams](../2273-find-resultant-array-after-removing-anagrams/readme.md)

# Additional content from an LLM model

## 1. Problem Statement

Given two strings, `s` and `t`, determine if `t` is an anagram of `s`. An anagram is a word or phrase formed
by rearranging the letters of a different word or phrase, typically using all the original letters exactly
once.

## 2. Core Intuition: Canonical Representation

The fundamental insight is that the order of characters in a string is irrelevant when checking for an
anagram. We only care about the characters themselves and their frequencies. This suggests that if we can
convert a string into a **canonical representation** that ignores order, we can solve the problem with a
simple comparison.

- **Definition**: Two strings `s` and `t` are anagrams if and only if their character multisets (sets that
  allow for duplicate elements) are identical.

- **Canonical Forms**: We can represent this multiset in two primary ways:
    1. A sorted sequence of its characters.
    1. A frequency map (or histogram) of its characters.

If the canonical forms of `s` and `t` are equal, they are anagrams.

## 3. Approaches

### Approach 1: Sorting

This is the most direct implementation of the first canonical form. We sort both strings and check if the
results are identical.

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

- **Space Complexity**: **O(N)** in Python, as strings are immutable and `sorted()` creates new lists. In a
  language that allows in-place sorting of character arrays, it could be O(1) or O(log N) depending on the
  sort implementation's space requirements.

### Approach 2: Frequency Counter (Optimal)

This approach uses the second canonical form. We count the frequency of each character in both strings and
compare the resulting frequency maps.

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

- **Time Complexity**: **O(N)**, where N is the length of the strings. We perform a single pass over each
  string to build the maps.

- **Space Complexity**: **O(k)**, where `k` is the number of unique characters in the alphabet.

#### 2b. Using an Array (Optimized for Constraints)

The problem states that inputs consist of "lowercase English letters." This is a critical constraint. Knowing
the character set is fixed and small (26 letters) allows for a highly efficient array-based frequency map.

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

- **Space Complexity**: **O(1)**, as the array size (26) is constant and does not depend on the input string
  length.

## 4. Key Pitfalls and Discussion Points

1. **Ignoring Character Frequencies**: A common mistake is only checking for character *presence*,
   not *count*. This fails for cases like `s = "aab"`, `t = "abc"`.

1. **Forgetting the Length Check**: Always start with `if len(s) != len(t): return False`. It's a simple,
   highly effective optimization that handles many negative cases instantly.

1. **Overlooking Constraints (The Character Set Discussion)**:
    - **Lowercase English (as per problem)**: An array of size 26 is the most optimal data structure. This
      demonstrates attention to detail and performance.

    - **Full ASCII**: An array of size 256 would be appropriate.

    - **Unicode**: The character set is vast and sparse. Using an array would be impractical due to its
      enormous size. A **hash map** is the correct and necessary choice here. A strong candidate can discuss
      these trade-offs.

1. **Choosing a Suboptimal Approach**: While the sorting solution is correct, a candidate should recognize and
   explain why the frequency counter approach is asymptotically more efficient (O(N) vs. O(N log N)).

# Complexity Reasoning

Complexity Analysis (Formal Summary)

- **Time Complexity: O(N+M)**
    - We iterate through string `s` once to build its frequency map. This takes O(N) time, where N is the
      length of `s`.

    - We then iterate through string `t` once to build its frequency map. This takes O(M) time, where M is the
      length of `t`.

    - Comparing the two maps takes time proportional to the number of unique keys. Since the character set is
      fixed to 26 lowercase English letters, this comparison is O(26), which is constant time, i.e., O(1).

    - The total time complexity is O(N+M+1)=O(N+M). If both strings have a similar length `L`, this is often
      simplified to O(L).

- **Space Complexity: O(1)**
    - The space is determined by the storage required for the frequency maps.

    - In the worst case, each map will store one entry for each unique character in the alphabet.

    - Since the alphabet is fixed at 26, the maximum size of each map is 26. This is a constant amount of
      space. Therefore, the space complexity is O(1).
