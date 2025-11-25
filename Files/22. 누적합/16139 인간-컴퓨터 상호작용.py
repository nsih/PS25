import sys
import math

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

remainder_count = [0] * m

prefix_sum = 0
for i in lst:
    prefix_sum += i
    remainder_count[prefix_sum % m] += 1

# 1. 나머지가 0인 구간은 그 자체로 정답 (0번 인덱스부터 더한 구간)
res = remainder_count[0]

# 2. 나머지가 같은 두 지점을 연결하는 구간 (조합 nC2)
for i in range(m):
    res += math.comb(remainder_count[i], 2)

print(res)