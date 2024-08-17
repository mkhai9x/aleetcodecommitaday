from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])

        def bfs(queue):
            visited = set()
            visited.add((queue[0][0], queue[0][1]))
            while queue:
                curr = queue.popleft()
                row = curr[0]
                col = curr[1]
                step = curr[2]

                for direction in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    drow = row + direction[0]
                    dcol = col + direction[1]
                    if (
                        drow < 0
                        or drow >= rows
                        or dcol < 0
                        or dcol >= cols
                        or rooms[drow][dcol] == -1
                        or rooms[drow][dcol] == 0
                        or (drow, dcol) in visited
                    ):
                        continue

                    visited.add((drow, dcol))
                    queue.append((drow, dcol, step + 1))
                    rooms[drow][dcol] = min(step + 1, rooms[drow][dcol])

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue = deque([(i, j, 0)])

                    bfs(queue)

        for i in range(rows):
            print(rooms[i])


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

print(Solution().wallsAndGates(rooms))
