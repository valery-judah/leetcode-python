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

**Follow-up:** Solve it in linear time and `O(1)` space.

## Recommended Solution (Boyer–Moore)

The Boyer–Moore majority vote algorithm runs in O(n) time and O(1) space by maintaining a candidate and a vote margin (count). Each non-candidate cancels one vote from the candidate; a true majority cannot be fully canceled.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate
```

### Why it works (pair-cancellation intuition)

- Maintain `(candidate, count)` for the processed prefix.
- If `count == 0`, start a new phase with the current element as `candidate` and `count = 1`.
- If the next item equals `candidate`, increment; otherwise decrement (`cancel a pair`).
- Deleting unequal pairs never changes whether a majority exists; if a majority exists overall, it must be the final `candidate`.

Note: In problems without the “majority always exists” guarantee, add a verification pass to confirm the final candidate appears more than `n/2` times.

## Alternative Approaches

### Approach 1: Brute Force

#### Intuition

Check every element and count its occurrences; return the first that exceeds `n/2`.

#### Algorithm

Iterate over `nums`; for each value, do a full pass to count its occurrences. If the count exceeds `n/2`, return it.

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
Two nested loops over `n` elements lead to quadratic time.
- **Space complexity:** O(1)
No extra space proportional to input size.

---

### Approach 2: Hash Map / Counter

#### Intuition

The majority element occurs more than `⌊n / 2⌋` times; counting with a map is straightforward and linear time.

#### Algorithm

Use a map from value → count while scanning; return the key with the maximum count.

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
Single pass to count; `max` over keys is linear in distinct values.
- **Space complexity:** O(n)
Up to `O(n)` distinct keys in the map.

---

### Approach 3: Sorting

#### Intuition

When sorted, the majority element must occupy index `n // 2`.

#### Algorithm

Sort `nums` and return the element at index `n // 2`.

#### Implementation

```python
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
```

#### Complexity Analysis

- **Time complexity:** O(n log n)
Sorting dominates the runtime.
- **Space complexity:** O(1) or O(n)
In-place sort is `O(1)` extra; copying to sort is `O(n)`.

---

### Approach 4: Boyer–Moore Voting (expanded)

#### Intuition

Count the majority as +1 and others as −1; the surplus that survives pairwise cancellation identifies the majority.

#### Algorithm

Maintain `candidate` and `count` as a running vote margin. If `count == 0`, start a new phase with the current element as `candidate`; otherwise increment/decrement based on match. A true majority cannot be completely canceled.

#### Implementation

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate
```

#### Complexity Analysis

- **Time complexity:** O(n)
Constant work per element.
- **Space complexity:** O(1)
Constant extra memory.

---

### Approach 5: Bit Manipulation

#### Intuition

For each bit position, count how many numbers have that bit set. If the count exceeds `n/2`, set that bit in the answer. This reconstructs the majority value bit by bit.

#### Algorithm

Scan all 32 bit positions (fits the constraints). If `ones > n/2` for a bit, set it in the result. Handle the sign bit for negatives using 32-bit two’s complement.

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        for b in range(32):
            ones = 0
            mask = 1 << b
            for x in nums:
                if x & mask:
                    ones += 1
            if ones > n // 2:
                result |= mask
        # Convert to signed 32-bit if needed
        if result >= 1 << 31:
            result -= 1 << 32
        return result
```

#### Complexity Analysis

- **Time complexity:** O(32 · n) = O(n)
- **Space complexity:** O(1)

---

### Approach 6: Divide and Conquer

#### Intuition

If we know the majority element in the left and right halves of an array, we can determine which is the global majority element in linear time.

#### Algorithm

Recurse on left and right halves; if both sides agree, return that value. Otherwise, count both candidates across the current range and return the one with higher frequency.

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def majority(lo: int, hi: int) -> int:
            if lo == hi:
                return nums[lo]
            mid = (lo + hi) // 2
            left = majority(lo, mid)
            right = majority(mid + 1, hi)
            if left == right:
                return left
            # Count both in current segment
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
            return left if left_count >= right_count else right
        return majority(0, len(nums) - 1)
```

#### Complexity Analysis

- **Time complexity:** O(n log n)
- **Space complexity:** O(log n) due to recursion stack.

---

### Approach 7: Randomization

#### Intuition

Since more than half the positions contain the majority, a random index equals the majority with probability > 1/2.

#### Algorithm

Repeat: pick a random index, count occurrences of that value; if it exceeds `n/2`, return it; otherwise try again.

#### Complexity Analysis

- **Time complexity:** Expected O(n). Each trial costs O(n) to verify, and the expected number of trials is < 2.
- **Space complexity:** O(1)

## Pitfalls

- Forgetting that the majority element is guaranteed to exist.
- Not considering the time and space complexity constraints mentioned in the follow-up.

## Tests / Edge Cases

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
