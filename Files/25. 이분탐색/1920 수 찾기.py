import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

m = int(sys.stdin.readline())
tlst = list(map(int, sys.stdin.readline().split()))


def exists(array, target):
    idx = bisect_left(array, target)

    if idx < len(array) and array[idx] == target:
        return 1
    else:
        return 0


for t in tlst:
    print(exists(lst, t))