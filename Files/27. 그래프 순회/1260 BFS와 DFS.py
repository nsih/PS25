import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


def sol():
    n, m, r = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for item in graph:
        item.sort()

    #
    visited_dfs = [0] * (n + 1)
    dLst = []

    def dfs(node):
        visited_dfs[node] = 1
        dLst.append(node)

        for item in graph[node]:
            if visited_dfs[item] == 0:
                dfs(item)
                
    #
    visited_bfs = [0] * (n + 1)
    bLst = []
    def bfs(node):
        queue = deque([r])
        visited_bfs[r] = 1

        while queue:
            cur = queue.popleft()
            bLst.append(cur)

            for item in graph[cur]:
                if visited_bfs[item] == 0:
                    visited_bfs[item] = 1
                    queue.append(item)

    dfs(r)
    bfs(r)

    print(*dLst)
    print(*bLst)


sol()
