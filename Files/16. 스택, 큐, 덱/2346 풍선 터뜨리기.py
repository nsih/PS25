import sys
from collections import deque

n = int(sys.stdin.readline())

rotations = list(map(int, sys.stdin.readline().split()))
b = deque( enumerate(rotations) )
res = []

while b:
    idx, move = b.popleft()
    res.append(idx+1)

    if not b:
        break

    if move > 0:
        b.rotate(-(move - 1))
    else:
        b.rotate(-move)

print(*res)