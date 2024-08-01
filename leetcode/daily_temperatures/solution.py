from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        not_yet_found = []
        result = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            current_temp = temperatures[i]
            # Check if the current_temp is greater then the top of the stack
            # The current_temp could be greater than multiple element in the stack so we make a while condition here
            while not_yet_found and current_temp > not_yet_found[-1][0]:
                lower_temp = not_yet_found.pop()
                difference = i - lower_temp[1]
                result[lower_temp[1]] = difference

            not_yet_found.append([current_temp, i])
            i += 1

        return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(Solution().dailyTemperatures(temperatures=temperatures))
