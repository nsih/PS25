import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
def cnt(n,mid):     #mid보다 작은놈 개수
    count = 0
    for i in range(1, n + 1):
        count += min(n, mid // i)

    return count

start = 1
end = k

res = 0
while start <= end:
    mid = (start + end) // 2

    if cnt(n,mid) >= k:
        end = mid - 1
        res = mid
    else:
        start = mid + 1

print(res)

'''
cnt는 2차원 배열을 1차원으로 정렬했을때 mid 보다 작은놈의 개수를 카운팅하고
이 함수를 이용해서 mid의 숫자를 조절해가면서 k의 인덱스에 뭐가 있을지 알아내는 것?
'''