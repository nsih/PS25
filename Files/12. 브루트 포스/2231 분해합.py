import sys

n = int(sys.stdin.readline())

ln = len(str(n))

start = max(1, n - (9 * ln))

for i in range(start, n + 1):
    temp = sum(map(int, str(i)))
    if temp + i == n:
        print(i)
        break
else:
    print(0)
