from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        total_oranges = 0
        neighbours = deque()
        rotting_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_oranges += 1
                elif grid[i][j] == 2:
                    total_oranges += 1
                    neighbours.extend([(i,j,0)])
        max_level = 0
        while neighbours:
            row, col, level = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if (grid[row][col] == 1 or grid[row][col] == 2) and visited[row][col] is False:
                visited[row][col] = True
                grid[row][col] = 2
                rotting_oranges += 1
                max_level = max(max_level,level)
                neighbours.extend([(row + 1, col, level + 1)])
                neighbours.extend([(row - 1, col, level + 1)])
                neighbours.extend([(row, col + 1, level + 1)])
                neighbours.extend([(row , col - 1, level + 1)])

        # print(max_level, rotting_oranges, total_oranges)
        if rotting_oranges < total_oranges:
            return - 1
        return max_level


if __name__ == '__main__':
    solution = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(solution.orangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(solution.orangesRotting(grid))

    grid = [[0]]
    print(solution.orangesRotting(grid))

    grid = [[0,2]]
    print(solution.orangesRotting(grid))

    grid = [[2,1,1],[1,1,1],[0,1,2]]
    print(solution.orangesRotting(grid))



