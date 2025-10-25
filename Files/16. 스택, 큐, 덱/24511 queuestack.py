import sys
from collections import deque

n = int(sys.stdin.readline())
typelst = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlst = list(map(int, sys.stdin.readline().split()))

q = deque()
res = []

for i in range(n):
    if typelst[i] == 0: #queue
        q.append(lst[i])

for i in range(m):
    q.appendleft(mlst[i])
    res.append(q.pop())

print(*res)