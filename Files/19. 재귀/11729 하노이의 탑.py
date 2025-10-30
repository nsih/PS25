import sys
sys.setrecursionlimit(10 ** 6)

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, end, mid)

    print(start, end)

    hanoi(n - 1, mid, start, end)

n = int(sys.stdin.readline())

print(2 ** n - 1)
hanoi(n, 1, 2, 3)