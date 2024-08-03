from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            print(f"low: {low}, mid {mid}, high {high}")
            print(f"low: {nums[low]}, mid {nums[mid]}, high {nums[high]}\n")

            # it means the mid could be the smallest or there will be a smaller before the mid, so we continue looking for the smallest on the left, include the mid
            if nums[mid] < nums[high]:
                high = mid
            # it means the nums[mid] > nums[hight] and because we are loooking for the smallest so there must be a smaller num in the right part, exclude the mid
            else:
                low = mid + 1
        return nums[high]


nums = [4, 5, 1, 2, 3]

nums = [11, 13, 15, 17]

nums = [3, 4, 5, 1, 2]
nums = [4, 5, 6, 7, 0, 1, 2]

nums = [1]

print(Solution().findMin(nums))
