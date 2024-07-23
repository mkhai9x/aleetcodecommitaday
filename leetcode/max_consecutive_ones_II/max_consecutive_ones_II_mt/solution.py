from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        new_array = []
        accumulate = 0
        i = 0
        while i < len(nums):
            if (nums[i] == 0) and accumulate != 0:
                new_array.append(accumulate)
                new_array.append(0)
                accumulate = 0
            elif (nums[i] == 0) and accumulate == 0:
                new_array.append(0)
            else:
                accumulate += 1
            print(accumulate)
            i += 1
        if (accumulate != 0):
            new_array.append(accumulate)
        i = 0
        max_ones = 0
        print(new_array)
        if (len(new_array) == 1):
            return new_array[0] if new_array[0] != 0 else 1
        while i < len(new_array):
            if i == 0:
                prev = 0
            else:
                prev = new_array[i-1]
            if i == len(new_array) - 1:
                nxt = 0
            else:
                nxt = new_array[i+1]

            if (new_array[i] == 0):
                max_ones = max(new_array[i] + prev + nxt + 1, max_ones)
            i += 1

        return max_ones


if __name__ == "__main__":

    solution = Solution()
    print(solution.findMaxConsecutiveOnes([0]))
