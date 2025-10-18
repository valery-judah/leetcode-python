# Sliding Window — Fixed and Dynamic

Track: `track_1_sliding_window`

Master fixed-size and variable-size windows. Learn frequency maps, expansion/contraction logic, and deque optimization.

See generation instructions in ../README.md.

## Problems

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Best Time to Buy and Sell Stock](../problems/0121-best-time-to-buy-and-sell-stock/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Longest Substring Without Repeating Characters](../problems/0003-longest-substring-without-repeating-characters/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Longest Repeating Character Replacement](../problems/0424-longest-repeating-character-replacement/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Minimum Window Substring](../problems/0076-minimum-window-substring/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Permutation in String](../problems/0567-permutation-in-string/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Find All Anagrams in a String](../problems/0438-find-all-anagrams-in-a-string/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Maximum Number of Vowels in a Substring of Given Length](../problems/1456-maximum-number-of-vowels-in-a-substring-of-given-length/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Sliding Window Maximum](../problems/0239-sliding-window-maximum/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Max Consecutive Ones III](../problems/1004-max-consecutive-ones-iii/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">Fruit Into Baskets (0904-fruit-into-baskets)</span> | Medium |  |  |  |  |  |  |  |  |  |                  |  |  |
| <span style="display:inline-block; min-width: 260px;">[Binary Subarrays With Sum](../problems/0930-binary-subarrays-with-sum/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Subarrays with K Different Integers](../problems/0992-subarrays-with-k-different-integers/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Subarray Product Less Than K](../problems/0713-subarray-product-less-than-k/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">Longest Subarray of 1s After Deleting One</span> | Medium |  |  |  |  |  |  |  |  |  |                  |  |  |
| <span style="display:inline-block; min-width: 260px;">[Longest Substring with At Most K Distinct Characters](../problems/0340-longest-substring-with-at-most-k-distinct-characters/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Longest Substring with At Most Two Distinct Characters](../problems/0159-longest-substring-with-at-most-two-distinct-characters/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Shortest Subarray with Sum at Least K](../problems/0862-shortest-subarray-with-sum-at-least-k/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Maximum Erasure Value](../problems/1695-maximum-erasure-value/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
