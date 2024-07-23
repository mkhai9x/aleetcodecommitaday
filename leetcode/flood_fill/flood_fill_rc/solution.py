from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_color = image[sr][sc]
        if source_color == color:
            return image
        row = len(image)
        col = len(image[0])
        visited = [[False for i in range(col)] for j in range(row)]
        neighbours = deque([(sr,sc)])

        while neighbours:
            x, y = neighbours.popleft()
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            if image[x][y] == source_color:
                image[x][y] = color
                neighbours.extend([(x + 1,y)])
                neighbours.extend([(x - 1, y)])
                neighbours.extend([(x, y + 1)])
                neighbours.extend([(x, y - 1)])
        return image

if __name__ == '__main__':
    solution = Solution()
    print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
    print(solution.floodFill([[0,0,0],[0,0,0]],0,0,0))
