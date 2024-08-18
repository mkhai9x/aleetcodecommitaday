from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            # push to the heap first
            heappush(heap, num)
            while len(heap) > k:
                heappop(heap)
        return heap[0]
