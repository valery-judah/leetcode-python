# Foundations — Arrays, Hashing, Two-Pointers, Prefix, Stack

Track: `track_0_foundations`

Core patterns for fast ramp-up. Focus on invariants, O(n) scans, and state compression.

See generation instructions in ../README.md.

## Problems

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Contains Duplicate](../problems/0217-contains-duplicate/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Valid Anagram](../problems/0242-valid-anagram/readme.md)</span> | Easy | ✅ | ✖️ | ✅ |  | 0 | 2 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Two Sum](../problems/0001-two-sum/readme.md)</span> | Easy | ✖️ | ✖️ | ✅ |  | 0 | 2 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Group Anagrams](../problems/0049-group-anagrams/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Top K Frequent Elements](../problems/0347-top-k-frequent-elements/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Product of Array Except Self](../problems/0238-product-of-array-except-self/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Valid Sudoku](../problems/0036-valid-sudoku/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Longest Consecutive Sequence](../problems/0128-longest-consecutive-sequence/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Encode and Decode Strings](../problems/0271-encode-and-decode-strings/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Valid Palindrome](../problems/0125-valid-palindrome/readme.md)</span> | Easy | ✅ | ✖️ | ✅ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Two Sum II - Input Array Is Sorted](../problems/0167-two-sum-ii-input-array-is-sorted/readme.md)</span> | Medium | ✅ | ✖️ | ✅ |  | 0 | 2 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[3Sum](../problems/0015-3sum/readme.md)</span> | Medium | ✅ | ✖️ | ✅ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Container With Most Water](../problems/0011-container-with-most-water/readme.md)</span> | Medium | ✅ | ✖️ | ✅ |  | 2 | 2 | ✖️ | ✖️ | ✖️ | ✖️                 | ✅ |  |
| <span style="display:inline-block; min-width: 260px;">[Subarray Sum Equals K](../problems/0560-subarray-sum-equals-k/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Valid Parentheses](../problems/0020-valid-parentheses/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Min Stack](../problems/0155-min-stack/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Daily Temperatures](../problems/0739-daily-temperatures/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Isomorphic Strings](../problems/0205-isomorphic-strings/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Ransom Note](../problems/0383-ransom-note/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Majority Element](../problems/0169-majority-element/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Squares of a Sorted Array](../problems/0977-squares-of-a-sorted-array/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Duplicates from Sorted Array](../problems/0026-remove-duplicates-from-sorted-array/readme.md)</span> | Easy | ✅ | ✖️ | ✅ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Move Zeroes](../problems/0283-move-zeroes/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Merge Sorted Array](../problems/0088-merge-sorted-array/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Implement Queue using Stacks](../problems/0232-implement-queue-using-stacks/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
