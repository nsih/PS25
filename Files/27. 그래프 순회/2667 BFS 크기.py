def bfs(sy,sx):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(sy, sx)])
    visited[sy][sx] = 1
    cnt = 1

    while queue:
        y,x = queue.popleft()

        for dy,dx in directions:
            ny = y + dy
            nx = x + dx

            if 0 <= nx < n and 0 <= ny < n:
                if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                    queue.append((ny,nx))
                    visited[ny][nx] = 1
                    cnt += 1
    bfsCnt.append(cnt)

####
import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

bfsCnt = []
visited = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1 and visited[y][x] == 0:
            bfs(y, x)

print(len(bfsCnt))
bfsCnt.sort()
for item in bfsCnt:
    print(item)