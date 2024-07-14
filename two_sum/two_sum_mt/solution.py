from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_table = defaultdict(int)
        for index, num in enumerate(nums):
            remain = target - num
            print(index, num)
            if num in track_table:
                return [track_table[num], index]
            else:
                track_table[remain] = index
            print(track_table)
        return []


nums = [2, 7, 11, 15]
target = 9

nums = [3, 2, 4]
target = 6


print(Solution().twoSum(nums, target))

