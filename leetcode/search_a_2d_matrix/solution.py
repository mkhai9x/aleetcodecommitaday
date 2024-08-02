from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        low = 0
        high = (n_rows - 1) * n_cols + (n_cols - 1)

        while low <= high:
            mid = low + (high - low) // 2
            value = matrix[mid // n_cols][mid % n_cols]
            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

matrix = [[1, 1]]
target = 4

print(Solution().searchMatrix(matrix, target))
