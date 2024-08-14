from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(queue):
            while queue:
                current_item = queue.pop()
                row, col = current_item[0], current_item[1]
                for direction in directions:
                    drow = row + direction[0]
                    dcol = col + direction[1]
                    if (
                        drow < 0
                        or drow >= rows
                        or dcol < 0
                        or dcol >= cols
                        or grid[drow][dcol] == "0"
                    ):
                        continue
                    grid[drow][dcol] = "0"
                    queue.append((drow, dcol))

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    count += 1
                    queue.append((i, j))
                    bfs(queue)
        return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution().numIslands(grid))
