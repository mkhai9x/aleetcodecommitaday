from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        print(sorted_nums)
        results = []

        def twoSumWithSortedArray(left, right, target):
            current = []
            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    current.append([sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

            return current

        i = 0

        while i < len(nums) - 1:
            target = 0 - sorted_nums[i]
            others = twoSumWithSortedArray(i + 1, len(nums) - 1, target)
            if len(others) != 0:
                for other in others:
                    flag = False
                    for result in results:
                        if sorted(result) == sorted([sorted_nums[i]] + other):
                            flag = True
                    if not flag:
                        results.append([sorted_nums[i]] + other)
            i += 1

        return results


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0]
nums = [-2, 0, 1, 1, 2]
print(Solution().threeSum(nums))
