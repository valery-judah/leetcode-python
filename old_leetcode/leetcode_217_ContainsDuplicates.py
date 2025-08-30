def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    duplicates = {}
    for i, elem in enumerate(nums):
        if elem in duplicates:
            j = duplicates[elem]
            if abs(i - j) <= k:
                return True
            else:
                duplicates[elem] = i
        else:
            duplicates[elem] = i
    return False


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    duplicates = {}
    for i, elem in enumerate(nums):
        if elem in duplicates and i - duplicates[elem] <= k:
            return True
        duplicates[elem] = i
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 2
    print(containsNearbyDuplicate(nums, k))

    indexDiff = 3
    valueDiff = 0
    print(containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
