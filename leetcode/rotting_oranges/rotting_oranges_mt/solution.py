from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        total_fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        if total_fresh == 0:
            return 0

        while queue:
            length = len(queue)

            count += 1
            for _ in range(length):
                rotten = (
                    queue.popleft()
                )  # need to use popleft, in order to have a correct bfs order
                row = rotten[0]
                col = rotten[1]

                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    drow = row + direction[0]
                    dcol = col + direction[1]

                    if (
                        drow < 0
                        or drow >= rows
                        or dcol < 0
                        or dcol >= cols
                        or grid[drow][dcol] == 2
                        or grid[drow][dcol] == 0
                    ):
                        continue

                    grid[drow][dcol] = 2
                    queue.append((drow, dcol))
                    total_fresh -= 1
                    if total_fresh == 0:
                        return count

        return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


print(Solution().orangesRotting(grid))
