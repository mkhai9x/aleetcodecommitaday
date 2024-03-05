from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts nums in place - do not return anything
        :param nums:
        :return:
        """
        # everything to the left of low is 0, everything to the right of high is 2
        low,high = 0, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i],nums[low] = nums[low],nums[i]
                low += 1
                i += 1
            elif nums[i] == 1:
                 i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1



if __name__ == "__main__":
    solution = Solution()
    x = [1, 0, 2, 1, 0]
    solution.sortColors(x)
    print(x)