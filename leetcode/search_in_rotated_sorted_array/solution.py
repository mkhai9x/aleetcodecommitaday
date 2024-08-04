import re
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the index of the smallest num
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        pivot = high

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            real_mid = (pivot + mid) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif target > nums[real_mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
target = 1

print(Solution().search(nums, target))
