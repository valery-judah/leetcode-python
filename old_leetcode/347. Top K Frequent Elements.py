def test(f):
    print(f([1, 2, 2, 3, 3, 3, 1, 1, 1, 4, 4], 2))


@test
def topKFrequent(nums: list[int], k: int) -> list[int]:
    orderedCounter = [[] for i in range(len(nums) + 1)]

    counts = {}
    for elem in nums:
        counts[elem] = counts.get(elem, 0) + 1

    for value, count in counts.items():
        orderedCounter[count].append(value)

    out = [elem for sublist in orderedCounter for elem in sublist if sublist]
    return out[-k:]
