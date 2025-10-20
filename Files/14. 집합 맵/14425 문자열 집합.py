import sys

n,m = map(int,sys.stdin.readline().split())

lst1 = set()
lst2 = []

for i in range(n):
    lst1.add(sys.stdin.readline().strip())

cnt = 0
for j in range(m):
    if sys.stdin.readline().strip() in lst1:
        cnt += 1

print(cnt)