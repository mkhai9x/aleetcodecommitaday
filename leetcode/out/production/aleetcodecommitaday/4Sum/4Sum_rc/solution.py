from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n <= 2:
            return []
        nums.sort()
        quadruple_list = []
        first_left,  right = 0, n - 1
        while first_left < n - 3:
            if first_left > 0 and nums[first_left] == nums[first_left - 1]:
                first_left += 1
                continue
            second_left = first_left + 1
            while second_left < n - 2:
                if nums[second_left] == nums[second_left - 1] and second_left > first_left + 1:
                    second_left += 1
                    continue
                self.twoSum(nums,target,nums[first_left],nums[second_left],quadruple_list,second_left + 1, right)
                second_left += 1
            first_left += 1
        return quadruple_list

    def twoSum(self, nums: List[int], target: int, first_left_number: int, second_left_number: int,  quadruple_list: List[List[int]],left: int, right: int):
        while left < right:
            total_sum = first_left_number + second_left_number + nums[left] + nums[right]
            if total_sum == target:
                quadruple_list.append([first_left_number,second_left_number,nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
            elif total_sum > target:
                right -= 1
            else:
                left += 1



if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([1,0,-1,0,-2,2],0))
    print(solution.fourSum([2,2,2,2,2],0))
    print(solution.fourSum([4, 1, 2, -1, 1, -3], 1))
    print(solution.fourSum([2,2,2,2,2], 8))
