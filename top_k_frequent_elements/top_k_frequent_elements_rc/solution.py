from typing import  List
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}
        min_heap = []
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        for (num,frequency) in frequency.items():
            heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heappop(min_heap)

        frequent_numbers = [i[1] for i in min_heap]
        return frequent_numbers





if __name__ == '__main__':
    solution = Solution()
    solution.topKFrequent([1,1,1,2,2,3],2)