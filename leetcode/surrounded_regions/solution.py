from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def bfs(queue):
            while queue:
                curr = queue.popleft()
                row, col = curr[0], curr[1]

                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    drow = row + direction[0]
                    dcol = col + direction[1]

                    if (
                        drow >= 0
                        and drow < rows
                        and dcol >= 0
                        and dcol < cols
                        and board[drow][dcol] == "O"
                        and (drow, dcol) not in visited
                    ):
                        visited.add((drow, dcol))
                        queue.append((drow, dcol))

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    if board[row][col] == "O" and (row, col) not in visited:
                        visited.add((row, col))
                        queue = deque([(row, col)])
                        bfs(queue)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited:
                    board[row][col] = "X"

        for row in range(rows):
            print(board[row])


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "X", "O"],
]

Solution().solve(board)
