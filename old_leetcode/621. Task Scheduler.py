import heapq
from collections import Counter, deque


def leastInterval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    print(count)

    maxHeap = [-c for c in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    queue = deque()
    while maxHeap or queue:
        time += 1
        cnt = -heapq.heappop(maxHeap)

        queue.append((cnt - 1, time + 1))


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval(tasks, n))
