import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]

for i in range(n):
    prefix_sum.append(lst[i] + prefix_sum[-1])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    print(prefix_sum[b] - prefix_sum[a - 1])