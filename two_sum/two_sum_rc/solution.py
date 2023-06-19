from typing import  List

# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_indicies = {}
        for i in range(0, len(nums)):
            number_indicies[nums[i]] = i
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in number_indicies and number_indicies[remainder] != index:
                return [index, number_indicies[remainder]]

