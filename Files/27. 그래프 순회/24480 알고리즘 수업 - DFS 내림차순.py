import sys

sys.setrecursionlimit(10 ** 6)


def sol():
    n,m,r = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for idx in range(1,n+1):
        graph[idx].sort(reverse=True)

    visited = [0] * (n+1)

    order = 1
    visited[r] = order
    order += 1

    def dfs(node):
        nonlocal order

        for idx in graph[node]:
            if visited[idx] == 0:
                visited[idx] = order
                order += 1
                dfs(idx)

    dfs(r)

    for i in range(1,n+1):
        print(visited[i])


sol()
