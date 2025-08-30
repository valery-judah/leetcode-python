from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            median = int((r + l) / 2)
            print(f"l: {l}, median: {median}, r: {r}")
            if target > nums[median]:
                l = median
            elif target == nums[median]:
                return median
            else:
                r = median
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
