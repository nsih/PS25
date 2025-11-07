import sys


def dfs(depth, cur, a, s, m, d):
    global maxv, minv

    if depth == n:
        maxv = max(maxv, cur)
        minv = min(minv, cur)
        return

    x = nlst[depth]
    if a > 0:
        dfs(depth + 1, cur + x, a - 1, s, m, d)
    if s > 0:
        dfs(depth + 1, cur - x, a, s - 1, m, d)
    if m > 0:
        dfs(depth + 1, cur * x, a, s, m - 1, d)
    if d > 0:
        dfs(depth + 1, int(cur / x), a, s, m, d - 1)


n = int(sys.stdin.readline())

nlst = list(map(int, sys.stdin.readline().split()))
a, s, m, d = map(int, sys.stdin.readline().split())

cur = nlst[0]

maxv = -10 ** 18
minv = 10 ** 18

dfs(1, cur, a, s, m, d)

print(maxv)
print(minv)