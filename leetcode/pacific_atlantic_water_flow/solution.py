from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []

        def bfs(queue):
            visited = set()
            visited.add((queue[0][0], queue[0][1]))
            root = [queue[0][0], queue[0][1]]

            pacific_ocean_flag = False
            atlantic_ocean_flag = False

            while queue:
                curr = queue.popleft()
                row, col = curr[0], curr[1]
                curr_height = heights[row][col]

                for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    drow = row + direction[0]
                    dcol = col + direction[1]

                    if drow < 0 or dcol < 0:
                        pacific_ocean_flag = True
                        continue
                    if drow >= rows or dcol >= cols:
                        atlantic_ocean_flag = True
                        continue

                    if (drow, dcol) in visited:
                        continue

                    height = heights[drow][dcol]
                    if height <= curr_height:
                        queue.append((drow, dcol))

                        visited.add((drow, dcol))
                if pacific_ocean_flag and atlantic_ocean_flag:
                    result.append(root)
                    break

        for i in range(rows):
            for j in range(cols):
                queue = deque([(i, j)])
                bfs(queue)
        return result


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

heights = [[1]]
heights = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(Solution().pacificAtlantic(heights))
