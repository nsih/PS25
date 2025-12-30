import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

rLst = []
rLst.append(lst[0])

def bs(n):
    start = 0
    end = len(rLst) - 1
    temp = 0
    while start <= end:
        mid = (start+end)//2
        if rLst[mid] >= n:
            end = mid - 1
            temp = mid
        else:
            start = mid + 1
    rLst[temp] = n
    return

for i in range(1, len(lst)):
    if lst[i] < rLst[-1]:
        bs(lst[i])

    elif lst[i] > rLst[-1]:
        rLst.append(lst[i])

print(len(rLst))