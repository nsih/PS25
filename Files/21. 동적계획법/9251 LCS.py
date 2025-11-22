import sys

arr0 = sys.stdin.readline().strip()
arr1 = sys.stdin.readline().strip()

h = len(arr0)
w = len(arr1)

dp = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):

        if arr0[i - 1] == arr1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[h][w])