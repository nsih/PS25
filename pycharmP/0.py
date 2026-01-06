import sys

sys.setrecursionlimit(10 ** 6)

def solve():
    n, m, r = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        graph[i].sort()

    visited = [0]*(n+1)
    order = 1
    visited[r] = order

    def dfs(r):
        nonlocal order
        order += 1

        for item in graph[r]:
            if visited[item] == 0:
                visited[item] = order
                dfs(item)

    dfs(r)

    for i in range(1,n+1):
        print(visited[i],end='\n')

solve()