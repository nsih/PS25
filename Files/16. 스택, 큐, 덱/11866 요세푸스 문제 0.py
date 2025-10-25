import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
q = deque(range(1, n + 1))
res = []

while q:
    q.rotate(-(k - 1))
    res.append(q.popleft())

print(f"<{', '.join(map(str, res))}>")