from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplet_list = []
        for i in range(n):
            curr_number = nums[i]
            right = n - 1
            left = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.search_pair(left,right,triplet_list,curr_number, nums)
        return triplet_list

    def search_pair(self, left: int, right: int, triplet_list: List[List[int]], curr_number: int, nums: List[List[int]] ):
        while left < right:
            curr_sum = curr_number + nums[left] + nums[right]
            if curr_sum == 0:
                triplet_list.append([curr_number, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1
if __name__ == '__main__':
    solution = Solution()
    # Test Case 1
    triplets = solution.threeSum([-1,0,1,2,-1,-4])
    assert triplets == [[-1,-1,2],[-1,0,1]]

    # Test Case 2
    triplets = solution.threeSum([0,1,1])
    assert triplets == []

    # Test Case 3
    triplets = solution.threeSum([0,0,0])
    assert triplets == [[0,0,0]]