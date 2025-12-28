import sys

n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def bs(start, end, target, lst):
    res = 0
    while start <= end:
        temp = 0
        mid = (start+end) // 2

        temp = sum(i - mid for i in lst if i > mid)

        if temp >= target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

print(bs(1, max(lst), m, lst))