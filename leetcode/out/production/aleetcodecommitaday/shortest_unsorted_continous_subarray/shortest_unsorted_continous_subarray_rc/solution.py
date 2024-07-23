from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < n:
            if left > 0 and nums[left] < nums[left - 1]:
                left -= 1
                break
            left += 1
        while right >=0:
            if right < n - 1 and nums[right] > nums[right + 1]:
                right += 1
                break
            right -= 1
        if left == n:
            return 0
        # find the maximum and minimum within this sub array
        maximum_subarray = max(nums[left:right+1])
        minimum_subarray = min(nums[left:right+1])
        for i in range(left - 1,-1,-1):
            if nums[i] > minimum_subarray:
                left = i
            elif nums[i] == minimum_subarray and i != left - 1:
                left = i
        for i in range(right + 1, n):
            if nums[i] < maximum_subarray:
                right = i
            elif nums[i] == minimum_subarray and i != right + 1:
                right = i
        return right - left + 1
if __name__ == '__main__':
    solution = Solution()
    print(solution.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(solution.findUnsortedSubarray([1,2,3,4]))
    print(solution.findUnsortedSubarray([1]))
    print(solution.findUnsortedSubarray([1, 2, 5, 3, 7, 10, 9, 12]))
    print(solution.findUnsortedSubarray([1, 3, 2, 0, -1, 7, 10]))
    print(solution.findUnsortedSubarray([3, 2, 1]))

