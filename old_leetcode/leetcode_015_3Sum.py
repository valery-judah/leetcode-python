from dataclasses import dataclass
from unittest import TestCase


@dataclass
class TestData:
    name: str
    numbers: list[int]
    expected: list[list[int]]


class TestSolution(TestCase):
    def test_3_sum(self):
        testcases = [
            TestData(name="case 0", numbers=[-1, 0, 1, 2, -1, -4], expected=[[-1, -1, 2], [-1, 0, 1]]),
            TestData(name="case 0", numbers=[0, 0, 0], expected=[[0, 0, 0]])
        ]
        for case in testcases:
            actual = Solution.three_sum_sorted(nums=case.numbers)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}",
            )


# reuse 2 sum that it can return all pairs


class Solution:
    # solution when we can sort the input array
    @staticmethod
    def three_sum_sorted(nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                Solution.two_sum_pointers(nums, i, triplets)
        return triplets

    @staticmethod
    def two_sum_pointers(nums: list[int], i: int, triplets: list[list[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            current_sum = nums[lo] + nums[hi] + nums[i]
            if current_sum == 0:
                triplets.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
            elif current_sum < 0:
                lo += 1
            else:
                hi -= 1
