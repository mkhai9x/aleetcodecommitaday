from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_islands = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    total_islands += 1
                    # self.visitIsland(x,y,grid)
                    self.visitIslandDFS(x,y,grid)
        return total_islands

    def visitIsland(self, x: int, y: int, grid: List[List[str]]):
        neighbours = deque([(x, y)])
        while neighbours:
            row, col = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == '1':
                grid[row][col] = '0'
                neighbours.extend([(row + 1, col)])
                neighbours.extend([(row - 1, col)])
                neighbours.extend([(row, col + 1)])
                neighbours.extend([(row, col - 1)])

    def visitIslandDFS(self, x: int, y: int, grid: List[List[str]]):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if (grid[x][y] == "0"):
            return
        if (grid[x][y] == "1"):
            grid[x][y] = "0"
            self.visitIslandDFS(x + 1, y, grid)
            self.visitIslandDFS(x - 1, y, grid)
            self.visitIslandDFS(x, y + 1, grid)
            self.visitIslandDFS(x, y - 1, grid)



if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

    print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))