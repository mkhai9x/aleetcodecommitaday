
from collections import deque
from types import List

class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    visited = set()
    visited.add((0,0, grid[0][0]))
    queue = deque((0, 0, 0))
    minimum = 999999999

    while queue:
      row, col, current_length = queue.popleft()

      for x, y in [(0, 1), (0, -1), (1, 0), (-1,0)]:
        next_row = row + x
        next_col = col + y
        if 0<= next_row < len(grid) and 0<= next_col < len(grid[0]) and 