from dataclasses import dataclass
from unittest import TestCase

# Main things: we need to find 2 elements. By traversing a massive in various ways.
#
# There is 3 solutions to this question:
# 1. Nested loops. Time = O(N^2), Space = O(1)
# 2. Sorted array. Time = O(N * log(N)), Space = O(1)
# 3. Hash table. Time = O(N). Space = O(N).
#
#


@dataclass
class TestData:
    name: str
    numbers: list[int]
    target: int
    expected: list[int]


class Solution:
    @staticmethod
    def two_sum(numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers) - 1):
            first_num = numbers[i]
            for j in range(i + 1, len(numbers)):
                second_num = numbers[j]
                if first_num + second_num == target:
                    return [i, j]
        return []

    @staticmethod
    def two_sum_sorted(nums: list[int], target: int) -> list[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == target:
                return [left, right]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return []

    @staticmethod
    def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
        complements = {}
        for i in range(len(nums)):
            cur_number = nums[i]
            addition = target - cur_number
            if addition in complements:
                return [complements[addition], i]
            else:
                complements[cur_number] = i
        return []


class TestSolution(TestCase):
    def test_two_sum(self):
        testcases = [
            TestData(name="case 9", numbers=[2, 7, 11, 15], target=9, expected=[0, 1]),
            TestData(name="case null", numbers=[2, 7, 11, 15], target=0, expected=[]),
        ]
        for case in testcases:
            actual = Solution.two_sum_sorted(case.numbers, case.target)
            assert case.expected == actual, f"failed test {case.name}"
