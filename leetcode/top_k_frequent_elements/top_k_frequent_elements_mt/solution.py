from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequently = Counter(nums)
        array = [(-(value), key) for key, value in frequently.items()]

        heapq.heapify(array)

        top_k = [heapq.heappop(array)[1] for _ in range(k)]

        print(top_k)
        return top_k


solution = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
