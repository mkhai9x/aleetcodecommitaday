from collections import deque
from typing import  List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        cycles = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] is False:
                    cycles = self.traverseGrid(grid,visited,i,j, grid[i][j])
                    if cycles is True:
                        return True
        return False

    def traverseGrid(self, grid: List[List[int]], visited: List[List[int]], x: int, y: int, letter: str, prev_x = - 1, prev_y = - 1):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] != letter:
            return False
        if visited[x][y] is True:
            return True
        visited[x][y] = True

        if x + 1 != prev_x  and self.traverseGrid(grid,visited,x + 1, y, letter, x, y):
            return True
        if x - 1 != prev_x and self.traverseGrid(grid, visited, x - 1, y, letter, x, y):
            return True
        if y + 1 != prev_y and self.traverseGrid(grid, visited, x, y + 1, letter, x, y):
            return True
        if y - 1 != prev_y and self.traverseGrid(grid, visited, x, y - 1, letter, x, y):
            return True

        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    print(solution.containsCycle(
        [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    print(solution.containsCycle(
        [["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]))