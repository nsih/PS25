import sys

t = int(sys.stdin.readline())
lst = []

for _ in range(t):
    n = int(sys.stdin.readline())

    if n == 0:
        lst.pop()

    else:
        lst.append(int(n))

print(sum(lst))