from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_max = 0
        i = 0
        while i < len(nums):
            if(nums[i] != 1):
                max_ones = max(curr_max, max_ones)
                curr_max = 0
            else:
                curr_max += 1
            i += 1
        return max(curr_max, max_ones)
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))

    
