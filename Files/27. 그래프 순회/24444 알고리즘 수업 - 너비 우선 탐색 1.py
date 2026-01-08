import sys
from collections import deque

def sol():
    n,m,r = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for idx in range(1,n+1):
        graph[idx].sort()

    visited = [0] * (n+1)

    order = 1
    visited[r] = order

    queue = deque([r])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                order += 1
                visited[neighbor] = order
                queue.append(neighbor)

    for i in range(1,n+1):
        print(visited[i])

sol()
