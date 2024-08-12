from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[grid[0][0]] * len(grid[0]) for i in range(len(grid))]
        # fill all the top row
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # fill all the first column
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] = min(
                    dp[row - 1][col] + grid[row][col], dp[row][col - 1] + grid[row][col]
                )

        return dp[len(grid) - 1][len(grid[0]) - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid=grid))
