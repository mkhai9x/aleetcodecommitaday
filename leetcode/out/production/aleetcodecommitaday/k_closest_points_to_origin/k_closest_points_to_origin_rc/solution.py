from typing import List
from heapq import *
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(k):
            x,y = points[i]
            distance = sqrt(y**2 + x**2)
            heappush(max_heap, (-distance, x, y))

        for i in range(k, len(points)):
            x, y = points[i]
            distance = sqrt(y**2 + x**2)
            if -distance > max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-distance, x, y))
        k_nearest = []
        for point in max_heap:
            k_nearest.append([point[1], point[2]])
        return k_nearest


if __name__ == '__main__':
    solution = Solution()

    points = [[-10,-10],[10,10],[10,-10],[-2, 2],[1, 3], [-2, -2],[2,2]]
    k = 1

    print(solution.kClosest(points,3))


