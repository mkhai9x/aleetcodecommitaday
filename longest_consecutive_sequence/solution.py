from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn nums to a set
        nums_set = set(nums)
        # Create a visit set
        visited = set()

        i = 0
        longest = 0
        while i < len(nums):
            if nums[i] not in visited:
                current_num = nums[i]

                visited.add(current_num)

                current_length = 1
                while True:
                    current_num += 1
                    if current_num in nums_set:
                        visited.add(current_num)
                        current_length += 1
                    else:
                        break
                current_num = nums[i]
                while True:
                    current_num -= 1
                    if current_num in nums_set:
                        visited.add(current_num)
                        current_length += 1
                    else:
                        break

                longest = max(longest, current_length)

            i += 1
        return longest


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [100, 4, 200, 1, 3, 2]

print(Solution().longestConsecutive(nums))
