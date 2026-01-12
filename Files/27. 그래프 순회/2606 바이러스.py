import sys
from collections import deque

def sol():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (n+1)

    cnt = 1
    visited[1] = cnt

    queue = deque([1])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                cnt += 1
                queue.append(neighbor)

    print(cnt-1)

sol()
