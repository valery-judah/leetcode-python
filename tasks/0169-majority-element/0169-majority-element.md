---
category: arrays-hashing
difficulty: easy
status: todo
attempts: 0
last_solved: null
solution_path: repos/leetcode-python-project/tasks/0169-majority-element/solutions.py
tags:
- leetcode
- array
- hash-table
- divide-and-conquer
- sorting
- counting
pattern: []
created: 2025-09-01
updated: 2025-09-01
leetcode_link: https://leetcode.com/problems/majority-element/
task_dir: repos/leetcode-python-project/tasks/0169-majority-element
---

# Majority Element

## Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```bash
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```bash
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Stub

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
```

## Solutions

### Approach 1: Brute Force

#### Intuition

We can exhaust the search space in quadratic time by checking whether each element is the majority element.

#### Algorithm

The brute force algorithm iterates over the array, and then iterates again for each number to count its occurrences. As soon as a number is found to have appeared more than any other can possibly have appeared, return it.

#### Implementation

```python
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
```

#### Complexity Analysis

- **Time complexity:** O(n^2)
The brute force algorithm contains two nested `for` loops that each run for n iterations, adding up to quadratic time complexity.
- **Space complexity:** O(1)
The brute force solution does not allocate additional space proportional to the input size.

---

### Approach 2: HashMap

#### Intuition

We know that the majority element occurs more than `⌊n / 2⌋` times, and a `HashMap` allows us to count element occurrences efficiently.

#### Algorithm

We can use a `HashMap` that maps elements to counts in order to count occurrences in linear time by looping over `nums`. Then, we simply return the key with maximum value.

#### Implementation

```python
import collections

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

#### Complexity Analysis

- **Time complexity:** O(n)
We iterate over `nums` once and make a constant time `HashMap` insertion on each iteration. Therefore, the algorithm runs in O(n) time.
- **Space complexity:** O(n)
At most, the `HashMap` can contain n - `⌊n / 2⌋` associations, so it occupies O(n) space.

---

### Approach 3: Sorting

#### Intuition

If the elements are sorted in monotonically increasing (or decreasing) order, the majority element can be found at index `n // 2`.

#### Algorithm

For this algorithm, we simply sort `nums`, and return the element at index `n // 2`.

#### Implementation

```python
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
```

#### Complexity Analysis

- **Time complexity:** O(n log n)
Sorting the array costs O(n log n) time in Python and Java, so it dominates the overall runtime.
- **Space complexity:** O(1) or O(n)
We sorted `nums` in place here - if that is not allowed, then we must spend linear additional space on a copy of `nums` and sort the copy instead.

---

### Approach 4: Boyer-Moore Voting Algorithm

#### Intuition

If we had some way of counting instances of the majority element as +1 and instances of any other element as -1, summing them would make it obvious that the majority element is indeed the majority element.

#### Algorithm

Essentially, what Boyer-Moore does is look for a suffix of `nums` where the majority element is `candidate`. To do this, we maintain a `count`, which is incremented whenever we see an instance of our current `candidate` for majority element and decremented whenever we see anything else. Whenever `count` equals 0, we effectively forget about everything in `nums` up to the current index and consider the current number as the new candidate.

#### Implementation

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, res = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
```

#### Complexity Analysis

- **Time complexity:** O(n)
Boyer-Moore performs constant work exactly n times, so the algorithm runs in linear time.
- **Space complexity:** O(1)
Boyer-Moore allocates only constant additional memory.

---

### Approach 5: Bit Manipulation

#### Intuition

If an element `majority_element` occurs more than `⌊n / 2⌋` times, then there are at least `⌊n / 2⌋` + 1 elements of identical values with `num` at each bit. That is, we can reconstruct the exact value of `num` by combining the most frequent value (0 or 1) at each bit.

#### Algorithm

Starting from the least significant bit, we enumerate each bit to determine which value is the majority at this bit, 0 or 1, and put this value to the corresponding bit of the result. Finally, we end up with the most least significant bit of all elements and return the result.

#### Complexity Analysis

- **Time complexity:** O(n * log C) where C is the max absolute value in `nums`.
- **Space complexity:** O(1)

---

### Approach 6: Divide and Conquer

#### Intuition

If we know the majority element in the left and right halves of an array, we can determine which is the global majority element in linear time.

#### Algorithm

We apply a classical divide & conquer approach that recurses on the left and right halves of an array until an answer can be trivially achieved for a length-1 array. If the left and right halves agree on the majority element, then that is the answer. If they disagree, we count the occurrences of each candidate and return the winner.

#### Complexity Analysis

- **Time complexity:** O(n log n)
- **Space complexity:** O(log n) due to recursion stack.

---

### Approach 7: Randomization

#### Intuition

Because more than `⌊n / 2⌋` array indices are occupied by the majority element, a random array index is likely to contain the majority element.

#### Algorithm

Select a random index, check whether its value is the majority element, return if it is, and repeat if it is not.

#### Complexity Analysis

- **Time complexity:** O(∞) in the worst case, but O(n) on average.
- **Space complexity:** O(1)

## pitfalls

- Forgetting that the majority element is guaranteed to exist.
- Not considering the time and space complexity constraints mentioned in the follow-up.

## tests / edge cases

- `[3,2,3]` -> `3`
- `[2,2,1,1,1,2,2]` -> `2`
- `[1]` -> `1`

## Companies

| Company | Company | Company |
| :--- | :--- | :--- |
| Amazon | Google | Bloomberg |
| Microsoft | Meta | Oracle |
| Qualcomm | TCS | Adobe |
| Apple | Accenture | Yahoo |
| DE Shaw | IBM | Zoho |
| Uber | Nvidia | |

## Related Questions

- [Majority Element II](https://leetcode.com/problems/majority-element-ii/) (Medium)
- [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy)
- [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) (Easy)
- [Minimum Index of a Valid Split](https://leetcode.com/problems/minimum-index-of-a-valid-split/) (Medium)
- [Minimum Operations to Exceed Threshold Value I](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) (Easy)
- [Find the Most Common Response](https://leetcode.com/problems/find-the-most-common-response/) (Medium)
- [Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/) (Easy)

## Editorial / Discussions

**User (date unknown):**
> All those upvotes are for sure done by nerds who used either an extra O(n) space or extra time complexity which maybe n^2 or nlogn.
> But guys be honest did anyone solve it O(n) time and O(1) space. who has solved it like this?
> I'm here sitting for an hour to figure out this.

---
**An-Wen Deng** (Feb 11, 2024):
> Have a good day.
> key word "Boyer–Moore majority vote algorithm"
> Other quick solution fit the requirement is to use bit manipulation.

---
**Margad B Jantsan** (May 12, 2023):
> I don't understand why people are sorting and returning the middle element. Although it is a valid solution, the follow-up of the question is asking us to solve the problem in Linear time and not O(nlogn) time.

---
**iL YDOC** (Nov 17, 2015):
> if I have [1,1,1,2,2,2], why is 1 the majority number and not 2?

---
**User (date unknown):**
> I found nobody using bit-Operation for this question.
>
> I will try make up a O(n) time bit operation solution.
>
> **No** Boyer-Moore Majority Vote Algorithm
> **No** Hashing table

---
**User (date unknown):**
> I have problem coming up with the divide and conquer solution. Assume the base case contains only one element, which is the majority element for the base case. Now suppose we have two elements, each one returning from the base case. Say they are 1 2. There is clearly no majority element in this two-element array. If the whole input array is 1 2 2 and you divide the problem into 1 2 and 2. Of course you pick 2 in the right half. But what to pick in the left half?

---
**User (date unknown):**
> Why did they put this problem under "Bit Manipulation" when none of the 6 solutions use bit operators?

---
**User (date unknown):**
> This has to be a medium question considering you want time complexity of O(n) and space complexity of O(1). How anyone supposed to come up with Moore's algorithm?
