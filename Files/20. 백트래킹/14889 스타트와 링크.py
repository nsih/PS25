import sys


def cal():
    start_sum = 0
    link_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            if selected[i] and selected[j]:
                start_sum += s[i][j] + s[j][i]
            elif not selected[i] and not selected[j]:
                link_sum += s[i][j] + s[j][i]
    return abs(start_sum - link_sum)


def dfs(i, cnt):
    global res

    if cnt == n // 2:
        res = min(res, cal())

        return

    if n == i:
        return
    if cnt > n // 2:
        return
    if cnt + (n - i) < n // 2:
        return

    # 선택 1
    selected[i] = True
    dfs(i + 1, cnt + 1)

    # 선택 2
    selected[i] = False
    dfs(i + 1, cnt)


n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = float('inf')

selected = [False] * n
selected[0] = True

dfs(1, 1)
print(res)