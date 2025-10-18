import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()

for i in range(len(lst)):
    print(*lst[i])