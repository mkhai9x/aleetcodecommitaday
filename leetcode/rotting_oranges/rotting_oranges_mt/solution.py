from collections import deque
from typing import List

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    rotten_queue = deque()
    fresh_counts = 0

    minutues = 0

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 2:
          rotten_queue.append((i, j))
        elif grid[i][j] == 1:
          fresh_counts += 1
    
    while rotten_queue and fresh_counts > 0:
      # now loop all the items in the queue at once and rotten other cells, increment minutues by one
      for _ in range(len(rotten_queue)): # here we do not use rotten_orange in rotten_queue cause we dynamically update the queue
        # get coordinates
        row, col =  rotten_queue.popleft()
        for each in [(0,1), (0, -1), (1, 0), (-1,0)]:
          new_row = row + each[0]
          new_col = col + each[1]
          if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
            grid[new_row][new_col] == 2
            fresh_counts -= 1
            rotten_queue.append((new_row, new_col))
      minutues += 1
    
    return minutues if fresh_counts == 0 else -1;
  

    