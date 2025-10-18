# Two Pointers — Advanced and In‑Place Transforms

Track: `track_2_two_pointers_advanced`

Master slow–fast scans, 3‑way partitions, backscans, reverse/backfill tricks, and cycle detection.

See generation instructions in ../README.md.

## Problems

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Remove Duplicates from Sorted Array](../problems/0026-remove-duplicates-from-sorted-array/readme.md)</span> | Easy | ✅ | ✖️ | ✅ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Move Zeroes](../problems/0283-move-zeroes/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Sort Colors](../problems/0075-sort-colors/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[3Sum Closest](../problems/0016-3sum-closest/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[4Sum](../problems/0018-4sum/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Is Subsequence](../problems/0392-is-subsequence/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Backspace String Compare](../problems/0844-backspace-string-compare/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Rotate Array](../problems/0189-rotate-array/readme.md)</span> | Medium | ✅ | ✖️ | ✅ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Nth Node From End of List](../problems/0019-remove-nth-node-from-end-of-list/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Linked List Cycle](../problems/0141-linked-list-cycle/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Find the Duplicate Number](../problems/0287-find-the-duplicate-number/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Trapping Rain Water](../problems/0042-trapping-rain-water/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Valid Palindrome II](../problems/0680-valid-palindrome-ii/readme.md)</span> | Easy | ✅ | ✖️ | ✅ |  | 0 | 2 | ✖️ | ✖️ | ✖️ | ✖️                 | ✅ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Duplicates from Sorted Array II](../problems/0080-remove-duplicates-from-sorted-array-ii/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Element](../problems/0027-remove-element/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Sort Array By Parity](../problems/0905-sort-array-by-parity/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Shortest Unsorted Continuous Subarray](../problems/0581-shortest-unsorted-continuous-subarray/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Reverse Words in a String II](../problems/0186-reverse-words-in-a-string-ii/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Minimum Window Subsequence](../problems/0727-minimum-window-subsequence/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Partition List](../problems/0086-partition-list/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
