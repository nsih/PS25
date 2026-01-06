import sys

sys.setrecursionlimit(10 ** 6)

def solve():
    n, m, r = map(int, sys.stdin.readline().split())

    #for로 해야 리스트 내부에 독립적인 리스트가 생긴다.
    graph = [[] for _ in range(n+1)]

    #간선추가
    for _ in range(m):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    #정점에 붙은 간선정보를 오름차순으로 정렬
    for i in range(1, n+1):
        graph[i].sort()
    
    #방문순서 데이터
    visited = [0]*(n+1)
    
    #첫 방문은 초기화
    order = 1
    visited[r] = order

    def dfs(node):
        nonlocal order
        order += 1

        #간선을 타고 정점을 돌면서 오름차순으로 dfs
        for item in graph[node]:
            if visited[item] == 0:
                visited[item] = order
                dfs(item)

    dfs(r)

    for i in range(1,n+1):
        print(visited[i],end='\n')

#main
solve()