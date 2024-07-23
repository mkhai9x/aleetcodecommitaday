from typing import List
from heapq import heappop,heappush
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for i in range(k):
            distance = abs(arr[i] - x)
            heappush(max_heap, (-distance, arr[i]))
        for i in range(k, len(arr)):
            distance = abs(arr[i] - x)
            if -distance > max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-distance, arr[i]))
        sorted_list = []
        while max_heap:
            sorted_list.append(heappop(max_heap)[1])
        sorted_list.sort()
        return sorted_list


if __name__ == '__main__':
    solution = Solution()

    solution.findClosestElements([1,2,3,4,5],4,3)
    solution.findClosestElements([1, 2, 3, 4, 5], 4, -1)
