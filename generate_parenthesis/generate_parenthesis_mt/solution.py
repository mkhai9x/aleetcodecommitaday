
from typing import List

'''
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

() (())
() () ()

(()) ()
(()())

((()))
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      results = []
      def dfs(open ,close , result):
         
         for open in range(1, n + 1):

            dfs(open - i,  close + i, result)





solution = Solution()

result = solution.generateParenthesis(3)

