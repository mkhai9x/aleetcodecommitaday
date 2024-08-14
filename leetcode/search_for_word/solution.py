from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        result = False

        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(row, col, index):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
                or (row, col) in visited
            ):
                return False

            if board[row][col] == word[index] and index == len(word) - 1:
                return True

            current_result = False
            for direction in directions:
                drow = row + direction[0]
                dcol = col + direction[1]
                visited.add((row, col))
                back_track_result = backtrack(drow, dcol, index + 1)
                current_result = current_result or back_track_result # need OR operation here

                visited.remove((row, col))

            return current_result

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    result = result or backtrack(i, j, 0)

        return result


board = [["A", "B", "C", "D"], ["S", "A", "A", "A"], ["A", "C", "A", "T"]]

word = "CAT"

board=[["C","A","A"],["A","A","A"],["B","C","D"]]
word="AAB"

print(Solution().exist(board, word))
