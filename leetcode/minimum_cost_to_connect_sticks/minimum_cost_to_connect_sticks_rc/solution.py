from heapq import *
from typing import  List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        total_cost, temp = 0, 0
        while len(sticks) > 1:
            temp = heappop(sticks) + heappop(sticks)
            total_cost += temp
            heappush(sticks,temp)
        print(total_cost)
        return total_cost


if __name__ == "__main__":
    solution = Solution()
    solution.connectSticks([1,8,3,5])