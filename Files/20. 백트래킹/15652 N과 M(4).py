import sys

def backtrack(depth):
    if len(path) == m:
        print(*path)
        return
    for i in range(depth, n + 1):
        path.append(i)
        backtrack(i )
        path.pop()


n, m = map(int, sys.stdin.readline().split())

path = []

backtrack(1)