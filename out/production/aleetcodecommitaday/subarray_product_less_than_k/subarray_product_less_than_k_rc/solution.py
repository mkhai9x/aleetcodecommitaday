from typing import List
from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        current_product = 1
        subarray_count = 0
        left = 0
        for right,val in enumerate(nums):
            current_product *= val
            while current_product >= k:
                current_product /= nums[left]
                left += 1
            subarray_count += right - left + 1
        return subarray_count

# This function will let you print out the actual subarrays
# def find_subarrays(arr,target):
#     result = []
#     product = 1
#     left = 0
#     for right in range(len(arr)):
#         product *= arr[right]
#         while product >= target and left < len(arr):
#             product /= arr[left]
#             left += 1
#         temp_list = deque()
#         for i in range(right,left - 1, -1):
#             temp_list.appendleft(arr[i])
#             result.append(list(temp_list))
#     return result
if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10,5,2,6],100))
    print(solution.numSubarrayProductLessThanK([1,2,3],0))
    print(solution.numSubarrayProductLessThanK([1, 1, 1], 2))


    # print(find_subarrays([10,5,2,6],100))
