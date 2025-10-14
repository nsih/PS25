import sys

N = int(sys.stdin.readline())

if N == 1:
    sys.exit()

d = 2

while d * d <= N:
    if N % d == 0:
        print(d)
        N //= d
    else:
        d += 1

if N > 1:
    print(N)