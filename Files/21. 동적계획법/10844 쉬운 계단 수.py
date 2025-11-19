import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n)]

for i in range(n):
    for j in range(10):
        if i == 0:
            if j != 0:
                dp[i][j] = 1

        else:
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]

            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]

print(sum(dp[n - 1]) % 1000000000)