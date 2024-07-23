from typing import List
import sys


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = float("-inf")
        for house in houses:
            min_radius = min(min_radius, self.binary_search(house, heaters))
        return min_radius

    def binary_search(self, house, heaters):
        closest = sys.maxsize
        left_index = 0
        right_index = len(heaters) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            closest = min(closest, abs(heaters[mid_index] - house))
            if heaters[mid_index] > house:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
            mid_index = (left_index + right_index) // 2
        return closest


houses = [1, 5]
heaters = [1, 3, 5, 6, 12, 31]

print(Solution().binary_search(1, heaters))
