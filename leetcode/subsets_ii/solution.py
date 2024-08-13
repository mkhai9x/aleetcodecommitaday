from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def backtrack(current_result, index, length):
            if len(current_result) == length:
                result.append(current_result[:])
                return
            if len(current_result) > length:
                return
            i = index
            while i < len(nums):
                current_result.append(nums[i])
                backtrack(current_result, i + 1, length)
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                current_result.pop()
                i += 1

        for length in range(len(nums) + 1):
            backtrack([], 0, length)
        return result


nums = [1, 2, 2, 3, 4]
print(Solution().subsetsWithDup(nums))
