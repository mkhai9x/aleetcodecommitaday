class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        square_list = [0 for x in range(n)]
        left,right = 0, n - 1
        largest_square_tracker = n - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                square_list[largest_square_tracker] = nums[left] * nums[left]
                left += 1
            else:
                 square_list[largest_square_tracker] = nums[right] * nums[right]
                 right -= 1
            largest_square_tracker -= 1
        return square_list
