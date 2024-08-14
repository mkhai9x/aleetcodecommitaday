from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        visited = set()

        def bfs(queue):
            current_area = 0
            while queue:
                current_item = queue.pop()
                current_area += 1
                row = current_item[0]
                col = current_item[1]

                for direction in directions:
                    drow = row + direction[0]
                    dcol = col + direction[1]
                    if (
                        drow < 0
                        or drow >= rows
                        or dcol < 0
                        or dcol >= cols
                        or (drow, dcol) in visited
                        or grid[drow][dcol] == 0
                    ):
                        continue

                    visited.add((drow, dcol))
                    queue.append((drow, dcol))

            return current_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    queue = deque()
                    queue.append((i, j))
                    max_area = max(max_area, bfs(queue))
        return max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))
