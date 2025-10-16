import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

mn = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            temp = lst[i] + lst[j] + lst[k]
            if temp > mn and temp <= m:
                mn = temp

print(mn)