

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      board = [[0 for _ in range(0, n)] for _ in range(0, m)]
      for i in range(0, m):
         board[i][0] = 1
      for i in range(0, n):
         board[0][i] = 1
      
      i = 1
      while i < m:
        j = 1
        while j < n:
          board[i][j] = board[i-1][j] + board[i][j-1]
          j+=1
        i+=1
      return board[m-1][n-1]

solution = Solution()
print(solution.uniquePaths(3, 7))

