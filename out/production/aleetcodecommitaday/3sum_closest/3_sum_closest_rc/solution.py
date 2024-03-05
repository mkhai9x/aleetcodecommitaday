
from typing import  List
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        target_distance = math.inf
        n = len(nums)
        for i in range(n-2):
            left , right = i + 1, n -1
            while left < right:
                target_difference = target -  nums[i] - nums[left] - nums[right]
                if target_difference == 0:
                    return target
                if abs(target_difference) < abs(target_distance) or (abs(target_difference) == abs(target_distance) and target_difference > target_distance): # second part of the if condition is used to handle negative numbers with the same distance, i.e target_difference = 10 and target_distance = -10
                    target_distance = target_difference
                if target_difference > 0:
                    left += 1
                else:
                    right -= 1
        return target - target_distance


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSumClosest([-1,2,1,-4],1) == 2
    assert solution.threeSumClosest([0,0,0],1) == 0
    assert solution.threeSumClosest([-3, -1, 1, 2], 1) == 0
    assert solution.threeSumClosest([-2, 0, 1, 2], 2) == 1
    assert solution.threeSumClosest([1, 0, 1, 1],100) == 3
    assert solution.threeSumClosest([0, 0, 1, 1, 2, 6], 5) == 4



