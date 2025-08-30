from typing import List


def test(f):
    print(f([1, 2, 3, 4], 6))


@test
def twoSum_brute_force(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if n + nums[j] == target:
                return [i, j]


@test
def twoSum_brute_hashmap(nums: List[int], target: int) -> List[int]:
    sum_to_target = {}
    for i, n in enumerate(nums):
        if n not in sum_to_target.keys():
            sum_to_target[target - n] = i
        else:
            return [sum_to_target[n], i]
