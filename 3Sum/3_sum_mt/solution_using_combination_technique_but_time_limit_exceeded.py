from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_track(current_result, current_index):
            if len(current_result) == 3:
                if sum(current_result) == 0:
                    for result in results:
                        if sorted(result) == sorted(current_result):
                            return
                    results.append(current_result[:])
                return
            i = current_index
            while i < len(nums):
                current_result.append(nums[i])
                back_track(current_result, i + 1)
                current_result.pop()
                i += 1

        back_track([], 0)
        print(results)
        return results


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
