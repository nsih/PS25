import sys
sys.setrecursionlimit(10**6)

def dfs(n, cnt):
    if cnt >= dp[n]:
        return

    dp[n] = cnt

    if n == 1:
        return

    if n % 3 == 0:
        dfs(n//3, cnt + 1)

    if n % 2 == 0:
        dfs(n//2, cnt + 1)

    dfs(n-1, cnt + 1)

n = int(sys.stdin.readline())

dp = [1e6]*(n+1)
dfs(n, 0)

print(dp[1])