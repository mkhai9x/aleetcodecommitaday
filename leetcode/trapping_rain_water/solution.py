from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_height_on_the_right = [-1] * len(height)
        right = len(height) - 2
        current_height = height[-1]
        while right >= 0:
            max_height_on_the_right[right] = current_height
            current_height = max(current_height, height[right])
            right -= 1

        max_height_on_the_left = [-1] * len(height)
        left = 1
        current_height = height[0]
        while left < len(height):
            max_height_on_the_left[left] = current_height
            current_height = max(current_height, height[left])
            left += 1

        # print(max_height_on_the_left)
        # print(max_height_on_the_right)

        result = [0] * len(height)
        i = 0
        while i < len(height):
            if height[i] < min(max_height_on_the_right[i], max_height_on_the_left[i]):
                result[i] = min(max_height_on_the_right[i], max_height_on_the_left[i]) - height[i]
            i += 1

        return sum(result)

print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4,2,0,3,2,5]))
