import sys

a, b, c = map(int, sys.stdin.readline().split())


def sol(a, b, c):
    if b == 1:
        return a % c

    temp = sol(a, b // 2, c)

    if b % 2 == 0:
        return (temp ** 2) % c

    else:
        return (temp ** 2 * a) % c


print(sol(a, b, c))