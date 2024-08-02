from typing import List


class Solution:
    """
    We keep a stack in increasing order,
    Keep looping and append to the stack if the next time is higher than the top item of the stack.

    once we see item that is lower than the top item of the the stack
    we start poping the top item until the top item is lower than the current item.
    During poping out the top item, we take this opportunity to calculate the histogram of those area

    Once we done with the looping, we got a stack in increasing order, and start calculate the rest of the historram area

    NOTE: we use the trick is put the first item in the stack with height = -1 and position = -1
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        increasing_tower = [(-1, -1)]
        i = 0
        max_area = 0
        while i < len(heights):
            current_height = heights[i]
            while increasing_tower[-1][0] > current_height:
                distance_from_current_position_to_tower =  i - increasing_tower[-2][1] - 1

                area_exclue_current_tower = distance_from_current_position_to_tower * increasing_tower[-1][0]

                max_area = max(max_area, area_exclue_current_tower)

                top_tower = increasing_tower.pop()
                # print(top_tower)
                # print(distance_from_current_position_to_tower)

            area = (i - increasing_tower[-1][1]) * current_height
            max_area = max(max_area, area)

            increasing_tower.append((current_height, i))
            i += 1

        while len(increasing_tower) > 0:
            top_tower = increasing_tower.pop()
            if len(increasing_tower) != 0:
                start = increasing_tower[-1][1]
            else:
                start = -1
            distance = len(heights) - 1 - start
            area = distance * top_tower[0]
            max_area = max(area, max_area)

        return max_area


heights = [2, 2, 4]
heights = [2, 4]
heights = [3, 6, 5, 7, 4, 8, 1, 0]
heights = [2, 1, 5, 6, 2, 3]
heights = [5, 4, 1, 2]
print(Solution().largestRectangleArea(heights))
