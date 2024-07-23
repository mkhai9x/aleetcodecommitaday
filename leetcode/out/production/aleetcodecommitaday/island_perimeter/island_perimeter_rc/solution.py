from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        perimeter = 0
        found_island = False
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter = self.traverseIsland(grid, visited, i, j)
                    found_island = True
                    break
            if found_island:
                break
        return perimeter

    def traverseIsland(self, grid: List[List[int]], visited: List[List[int]], x: int, y: int):
        neighbours = deque([(x, y)])
        perimeter = 0
        while neighbours:
            row, col = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                perimeter += 1
            elif grid[row][col] == 0:
                perimeter += 1
            elif grid[row][col] == 1 and visited[row][col] is False:
                visited[row][col] = True
                neighbours.extend([(row + 1, col)])
                neighbours.extend([(row - 1, col)])
                neighbours.extend([(row, col + 1)])
                neighbours.extend([(row, col - 1)])
        return perimeter

if __name__ == '__main__':
    solution = Solution()
    grid = [[1]]
    print(solution.islandPerimeter(grid))

    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(solution.islandPerimeter(grid))

    grid = [[1,0]]
    print(solution.islandPerimeter(grid))