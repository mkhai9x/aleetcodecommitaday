from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        number_frequency = {}
        window_start = 0
        for window_end in range(len(nums)):
            right_number = nums[window_end]
            if right_number not in number_frequency:
                number_frequency[right_number] = 1
            else:
                return True
            while len(number_frequency) > k:
                left_number = nums[window_start]
                del number_frequency[left_number]
                window_start += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.containsNearbyDuplicate([1,2,3,1], 3) is True