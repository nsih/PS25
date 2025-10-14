import sys

lx = []
ly = []

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lx.append(x)
    ly.append(y)

w = max(lx) - min(lx)
h = max(ly) - min(ly)

print(w*h)