from typing import  List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start, max_length,window_ones = 0,0,0

        for window_end in range(len(nums)):
            number = nums[window_end]
            if number == 1:
                window_ones += 1

            # the current window needs more than k replacements of 0s
            while window_end - window_start + 1 - window_ones > k:
                if nums[window_start] == 1:
                    window_ones -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length





if __name__ == '__main__':
    solution = Solution()
    assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10