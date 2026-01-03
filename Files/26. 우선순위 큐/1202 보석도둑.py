import sys
import math
import heapq

n,k = map(int, sys.stdin.readline().split())
gems = []
for _ in range(n):
    gems.append(list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(k):
    bags.append(int(sys.stdin.readline()))

gems.sort()
bags.sort()

total_profit = 0
gem_pool = []
gem_ptr = 0

for limit in bags:
    while gem_ptr < n and gems[gem_ptr][0] <= limit:
        heapq.heappush(gem_pool, -gems[gem_ptr][1])
        gem_ptr += 1

    if gem_pool:
        total_profit += -heapq.heappop(gem_pool)

print(total_profit)

# 그리디 = 정렬해야한다
# 보석 목록, 가방 한계목록 정렬
# 가지고 갈 수 있는 보석 목록(gem pool) 선언

# 각 가방마다
    # 각 가방의 무게한계 안쪽의 보석이면 gem pool에 넣는다
    # 다넣고 gem pool이 있으면 gempool 최댓값 결과값에 추가한다.