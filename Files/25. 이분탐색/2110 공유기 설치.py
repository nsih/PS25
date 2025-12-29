import sys

n, c = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()

def cnt(dist):
    cnt = 1
    lastP = lst[0]

    for i in range(1,len(lst)):
        if lst[i] - lastP >= dist:
            cnt += 1
            lastP = lst[i]

    return cnt



start = 1
end = lst[-1] - lst[0]

res = 0
while start <= end:
    mid = (start + end) // 2
    if cnt(mid) >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)

#parametric search는 idx가 아니라 결과 값을 추정하고 옮긴다.