import sys

k,n = map(int, sys.stdin.readline().split())

lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))
lst.sort()

def bs(start, end, target):
    res = 0

    while start <= end:
        count = 0

        mid = (start+end) // 2

        for i in lst:
            count += (i//mid)

        if count >= target:
            res = mid
            start = mid + 1

        else:
            end = mid - 1

    return res

print(bs(1, max(lst), n))