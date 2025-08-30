import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    if len(points) <= k:
        return points

    minHeap = []
    for i in range(len(points)):
        dist = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
        minHeap.append((dist, points[i]))
    heapq.heapify(minHeap)

    res = []
    while k > 0:
        d, point = heapq.heappop(minHeap)
        res.append(point)
        k -= 1
    return res


if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(kClosest(points, k))
