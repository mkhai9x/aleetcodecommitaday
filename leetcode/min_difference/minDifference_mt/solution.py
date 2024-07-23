from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        n = len(nums)
        case1 = nums[n-4] - nums[0]
        case2 = nums[n-3] - nums[1]
        case3 = nums[n-2] - nums[2]
        case4 = nums[n-1] - nums[3]
        return min(min(case1, case2), min(case3, case4))

if __name__ == '__main__':
    
    solution = Solution()
    print("hello world")

    print(solution.minDifference([1,5,0,10,14]))
