from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], 0, result)
    def backtrack(self, candidates: List[int], target: int, comb: List[int], index: int, result: List[List[int]]):
        if target == 0:
            result.append(list(comb))
            return
        for i in range(index, len(candidates)):
            if target < candidates[i]:
                continue
            comb.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], comb, i, result)
            comb.pop()


if __name__ == '__main__':
    solution = Solution()
    solution.combinationSum([2,3,6,7], 7)