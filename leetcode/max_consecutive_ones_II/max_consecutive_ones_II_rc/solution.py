from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_tracker = {0:0}
        window_start, max_length = 0, 0
        for window_end in range(len(nums)):
            number = nums[window_end]
            if number == 0:
                zero_tracker[number] += 1
                if zero_tracker[number] > 1:
                    while nums[window_start] != 0:
                        window_start += 1
                    zero_tracker[number] -= 1
                    window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMaxConsecutiveOnes([1,0,1,1,0]) == 4
    assert solution.findMaxConsecutiveOnes([1,0,1,1,0,1]) == 4
    assert solution.findMaxConsecutiveOnes([1,1,1,1,0,1]) == 6
    assert solution.findMaxConsecutiveOnes([0, 0, 0, 0, 0, 1]) == 2
    assert solution.findMaxConsecutiveOnes([0, 0, 0, 0, 0, 0]) == 1
    assert solution.findMaxConsecutiveOnes([]) == 0
