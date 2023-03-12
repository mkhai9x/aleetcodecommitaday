from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islands = 0
        for i in [0, row - 1]:
            for j in range(col):
                if grid[i][j] == 0:
                    self.findLand(grid, i, j)

        for i in range(row):
            for j in [0, col - 1]:
                if grid[i][j] == 0:
                    self.findLand(grid, i,j)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    islands += 1
                    self.findLand(grid, i, j)
        return islands


    def findLand(self, grid: List[List[int]], x: int, y: int):
        neighbours = deque([(x,y)])
        while neighbours:
            row, col = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == 0:
                grid[row][col] = 1
                neighbours.extend([(row + 1,col)])
                neighbours.extend([(row - 1, col)])
                neighbours.extend([(row, col + 1)])
                neighbours.extend([(row, col - 1)])



if __name__ == '__main__':
    solution = Solution()
    grid1 = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    assert solution.closedIsland(grid1) == 2

    grid2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    assert solution.closedIsland(grid2) == 1