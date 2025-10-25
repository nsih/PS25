import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    w, e = map(int, sys.stdin.readline().split())

    print(math.comb(e, w))