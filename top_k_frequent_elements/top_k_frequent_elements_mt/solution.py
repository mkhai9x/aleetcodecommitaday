from heapq import *
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      heapify(nums)
      print(nums)

solution = Solution().topKFrequent([6, 7, 9, 4, 3, 5, 8, 10, 1], 3)
