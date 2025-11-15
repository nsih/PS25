import sys
sys.setrecursionlimit(10 ** 6)


def fib(n):
    global cnt

    if mm[n] != -1:
        return mm[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    mm[n] = result
    return result


n = int(sys.stdin.readline())

mm = [-1] * (n + 1)

cnt = 0

print(fib(n),n-2)