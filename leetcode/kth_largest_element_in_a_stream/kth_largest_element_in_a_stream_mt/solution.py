from typing import List
from heapq import heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
