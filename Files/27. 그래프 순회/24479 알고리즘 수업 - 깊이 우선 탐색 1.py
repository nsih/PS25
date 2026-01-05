import sys

sys.setrecursionlimit(10 ** 6)

def solve():
    #정점 수, 간선 수, 시작 정점
    n, m, r = map(int, sys.stdin.readline().split())

    #n+1 길이의 그래프
    graph = [[] for _ in range(n + 1)]

    #간선수 만큼 graph[u](정점)에 연결된 다른 정점(간선)정보를 추가한다.
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    #정점에 연결된 정점(간선정보)들 정렬
    for i in range(1, n + 1):
        graph[i].sort()
    
    
    #그래프 크기의 방문순서 정보 리스트
    visited = [0] * (n + 1)

    #순서
    order = 1

    def dfs(node):
        nonlocal order

        #시작정점 r 부터 시작해서 순서를 늘려간다.
        visited[node] = order
        order += 1

        #정점마다 정점에 이러진 애들 돌면서
        #이어진 간선이 방문한적 없으면 dfs(재귀)
        #이어진 간선이 방문한적 있으면 return
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                dfs(neighbor)

    dfs(r)

    sys.stdout.write('\n'.join(map(str, visited[1:])) + '\n')

solve()

#DFS는 스택