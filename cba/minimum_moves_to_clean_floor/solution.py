def solution(plan):
    n = len(plan)
    m = len(plan[0])
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    robots = 0

    def is_valid(x, y):
        # return plan[x][y] != "#" and not visited[x][y]
        return x >=0 and x < n and y >=0 and y < m and plan[x][y] != "#" and not visited[x][y]

    def bfs(x, y):
        visited[x][y] = True
        queue.append((x, y))
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if plan[i][j] == "*" and not visited[i][j]:
                bfs(i, j)
                robots += 1

    return robots


plan = ["##########", "#....*.**#", "##########"]
plan = ["..####", "..#.*#", "###*.#", "#.####", "#.#...", "###..."]
plan = ["..####", "..#.*#", "###..#", "#*####", "#.#...", "###..."]
print(solution(plan))
