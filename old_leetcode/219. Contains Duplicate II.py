# tags: #duplicates #hashmap


def test(f):
    print(f([1, 2, 3, 4, 1, 5, 1], 3))


@test
def containsNearbyDuplicate_steps(nums: list[int], k: int) -> bool:
    indexes = {}
    for i, value in enumerate(nums):
        # if already seen
        if value in indexes:
            prev_index = indexes[value]
            if i - prev_index <= k:
                return True
        # else add to seen values
        indexes[value] = i
    return False

