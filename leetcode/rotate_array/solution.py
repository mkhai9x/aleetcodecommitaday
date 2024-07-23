from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        count = 0
        start = 0
        if k == 0:
            return

        start = nums[count]
        start_index = count
        while count < len(nums):
            start_cycle = start_index
            while True:
                next_index = (start_index + k) % len(nums)
                temp = nums[next_index]
                start_index = next_index

                nums[next_index] = start
                count += 1

                start = temp
                if start_index == start_cycle:
                    break

            start_index += 1
            start = nums[start_index]


original1 = [1, 23, 31]


k1 = 2
print(f"original array {original1}")
Solution().rotate(original1, k1)
print(f"rotated array {original1}")
