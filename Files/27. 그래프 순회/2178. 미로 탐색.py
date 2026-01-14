def bfs(sy,sx):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(sy, sx)])
    dist[sy][sx] = 1

    while queue:
        y,x = queue.popleft()

        if y == n - 1 and x == m - 1:
            return dist[y][x]

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 1 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))

    return dist[n-1][m-1]

####
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dist = [[0] * m for _ in range(n)]

print(bfs(0, 0))