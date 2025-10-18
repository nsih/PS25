import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: (x[1], x[0]))

for i in range(len(lst)):
    print(*lst[i])