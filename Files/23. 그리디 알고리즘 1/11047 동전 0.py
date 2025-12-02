import sys

n, k = map(int, sys.stdin.readline().split())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst = lst[::-1]
ans = 0

for coin in lst:
    if k == 0:
        break

    if coin <= k:
        ans += k // coin
        k = k % coin

print(ans)