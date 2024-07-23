from typing import List
from heapq import  heappush, heappop
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency = {}
        for num in arr:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        distinct_num = 0
        non_distinct_nums = []
        for (number, count) in frequency.items():
            heappush(non_distinct_nums, (count,number))
            distinct_num += 1

        while non_distinct_nums:
            (frequency, number) = heappop(non_distinct_nums)
            if frequency <= k:
                k = k - frequency
                distinct_num -= 1
            else:
                break

        return distinct_num

if __name__ == '__main__':
    solution = Solution()

    print(solution.findLeastNumOfUniqueInts([5,5,4], 1))
    print(solution.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))



