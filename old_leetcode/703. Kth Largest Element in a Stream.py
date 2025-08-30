import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


if __name__ == "__main__":
    getter = KthLargest(3, [1, 3, 4, 5, 5, 5, 6])
    print(getter.add(10))
    print(getter.add(10))
    print(getter.add(10))
    print(getter.add(10))
