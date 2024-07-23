from collections import deque
from typing import List

'''
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]
'''

class Solution():
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    max_area = 0
    visited = set()

    for i in range(rows):
      for j in range(columns):
        if grid[i][j] == 1 and (i, j) not in visited:
          queue = deque()
          queue.append((i, j))
          current_area = 0
          visited.add((i, j))
          while queue: # process each cell
            current_area += 1
            row, col = queue.popleft()
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
              new_row = row +x
              new_col = col + y
              if 0<= new_row < rows and 0<= new_col < columns and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
      max_area = max(max_area, current_area)
    return max_area

