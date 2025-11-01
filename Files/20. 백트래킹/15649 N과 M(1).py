import sys


def backtrack(depth):
    if depth == m:
        print(*path)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(depth + 1)
            path.pop()
            visited[i] = False


n, m = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
path = []

backtrack(0)