import heapq


def lastStoneWeight(stones: list[int]) -> int:
    stones = [-n for n in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first_stone = -heapq.heappop(stones)
        second_stone = -heapq.heappop(stones)
        diff = first_stone - second_stone
        if diff > 0:
            heapq.heappush(stones, -diff)
    if len(stones) == 1:
        return -stones[0]
    else:
        return 0


if __name__ == "__main__":
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
