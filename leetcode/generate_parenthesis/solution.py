from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open, close):
            if len(current) == 2 * n:
                result.append(current)
            if open < n:
                backtrack(current + "(", open + 1, close)
            if open > 0 and close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)
        return result


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
