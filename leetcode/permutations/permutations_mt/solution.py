
from typing import List

'''
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


class Solution():
  def permute(self, nums: List[int]) -> List[List[int]]:
    results = []

    def backtrack(result):
      if len(result) == len(nums):
        results.append(result[:])
        return 
      for num in nums:
        if num not in result:
          result.append(num)
          backtrack(result)
          result.remove(num)
    
    backtrack([])
    return results


solution = Solution()
permutations = solution.permute([1,2,3])

print(permutations)


