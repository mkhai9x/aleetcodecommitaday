from collections import deque
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        traversal_pattern = set()
        row = len(grid)
        col = len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] is False:
                    islands_type = self.traverseGrid(grid, visited, i, j, "0")
                    traversal_pattern.add(islands_type)
        print(len(traversal_pattern))


    def traverseGrid(self, grid: List[List[int]], visited: List[List[int]], x: int, y: int, direction : str):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return ""
        if grid[x][y] == 0 or visited[x][y]:
            return ""
        islandTraversal = direction
        visited[x][y] = True
        islandTraversal += self.traverseGrid(grid, visited, x + 1 , y, "D")
        islandTraversal += self.traverseGrid(grid, visited, x - 1, y, "U")
        islandTraversal += self.traverseGrid(grid, visited, x, y + 1, "R")
        islandTraversal += self.traverseGrid(grid, visited, x, y - 1, "L")
        islandTraversal += "B"
        return islandTraversal

if __name__ == '__main__':
    solution = Solution()
    # solution.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])

    grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    solution.numDistinctIslands(grid)
