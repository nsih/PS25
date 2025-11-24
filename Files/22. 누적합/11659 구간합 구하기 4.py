import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(lst[i] + prefix_sum[-1])

m_sum = []
for i in range(n - m + 1):
    m_sum.append(prefix_sum[i+m] - prefix_sum[i])

print(max(m_sum))