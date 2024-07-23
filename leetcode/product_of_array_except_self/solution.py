from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1 for i in nums]
        right_product = [1 for i in nums]

        left_index, current_left_product = 1, 1
        while left_index < len(nums):
            current_left_product = current_left_product * nums[left_index - 1]
            left_product[left_index] = current_left_product
            left_index += 1

        right_index, current_right_product = len(nums) - 2, 1
        while right_index >= 0:
            current_right_product = current_right_product * nums[right_index + 1]
            right_product[right_index] = current_right_product
            right_index -= 1

        result = []
        i = 0
        while i < len(nums):
            result.append(left_product[i] * right_product[i])
            i += 1

        return result


nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]

print(Solution().productExceptSelf(nums))
