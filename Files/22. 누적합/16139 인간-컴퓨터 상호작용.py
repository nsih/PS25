import sys
import math

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

rcnt = [0] * m	#누적합을 m으로 나눴을때 나머지 기록
psum = 0	#누적합 기록

#누적합 갱신하면서 rcnt 갱신
for i in lst:
    psum += i
    rcnt[psum % m] += 1

res = rcnt[0] #이미 나눠떨어지는거 기록

#나머지가 같은거 두개를 빼면 m으로 나눠떨어지기 때문에
#같은 나머지 개수마다 두개씩 묶는 누적합 두개의 Combination을 res 추가
for i in range(m):
    res += math.comb(rcnt[i], 2)

print(res)