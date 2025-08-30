

def topKFrequent(nums: list[int], k: int) -> list[int]:
    orderedCounter = [[] for i in range(len(nums) + 1)]

    counts = {}
    for elem in nums:
        counts[elem] = counts.get(elem, 0) + 1

    for value, count in counts.items():
        orderedCounter[count].append(value)
    print(orderedCounter)

    out = [elem for sublist in orderedCounter for elem in sublist if sublist]
    print(f"flattened: {out}")
    print(f"out: {out[-k:]}")
    res = []
    for i in range(len(nums) - 1, 0, -1):
        for n in orderedCounter[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))
