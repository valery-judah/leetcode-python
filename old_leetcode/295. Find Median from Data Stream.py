import heapq


class MedianFinder:
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        self.median = []
        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)
        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            elem = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, elem)
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

        print(f"heaps: left: {self.leftHeap}, right: {self.rightHeap}")

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        elif len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        else:
            return self.rightHeap[0]


class MedianFinderMy:
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        self.median = []
        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        print(
            f"before: n: {num},    left: {self.leftHeap}, "
            f"median:{self.median}, right: {self.rightHeap}"
        )
        if not self.median:
            self.median.append(num)
        elif len(self.median) == 1:
            if num > self.median[0]:
                heapq.heappush(self.rightHeap, num)
                self.median.append(heapq.heappop(self.rightHeap))
            else:
                heapq.heappush(self.leftHeap, -num)
                self.median.append(-heapq.heappop(self.leftHeap))
        elif len(self.median) == 2:
            if num < self.median[0]:
                heapq.heappush(self.leftHeap, -num)
                heapq.heappush(self.rightHeap, self.median[1])
                self.median.pop()
            elif self.median[0] < num < self.median[1]:
                heapq.heappush(self.leftHeap, -self.median[0])
                heapq.heappush(self.rightHeap, self.median[1])
                self.median = [num]
            else:
                heapq.heappush(self.leftHeap, -self.median[0])
                heapq.heappush(self.rightHeap, num)
                self.median.pop(0)

        print(
            f"after: n: {num},   left: {self.leftHeap}, "
            f"median:{self.median}, right: {self.rightHeap}"
        )

    def findMedian(self) -> float:
        return sum(self.median) / len(self.median)


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
    medianFinder.addNum(4)
    print(medianFinder.findMedian())
    medianFinder.addNum(-11)
    print(medianFinder.findMedian())
    medianFinder.addNum(5)
    print(medianFinder.findMedian())
    medianFinder.addNum(6)
    print(medianFinder.findMedian())
