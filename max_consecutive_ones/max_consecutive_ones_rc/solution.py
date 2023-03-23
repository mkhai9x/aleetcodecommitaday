from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length, window_start = 0,0
        for window_end in range(len(nums)):
            number = nums[window_end]
            if number == 0:
                window_end += 1
                window_start = window_end
            else:
                max_length = max(max_length, window_end - window_start + 1)

        return max_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert solution.findMaxConsecutiveOnes([0,0,0,0,0,0,0,0,0,0]) == 0
    assert solution.findMaxConsecutiveOnes([]) == 0