from typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        smaller_target_count = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    smaller_target_count += right - left
                    left += 1
                else:
                    right -= 1
        return smaller_target_count


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSumSmaller([-2,0,1,3],2) == 2
    assert solution.threeSumSmaller([],0) == 0
    assert solution.threeSumSmaller([0],0) == 0
    assert solution.threeSumSmaller([-1, 0, 2, 3],3) == 2
    assert solution.threeSumSmaller([-1, 4, 2, 1, 3], 5) == 4
