import sys
import heapq

input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
    row = map(int, input().split())
    for item in row:
        if len(min_heap) < n:
            heapq.heappush(min_heap, item)
        else:
            if min_heap[0] < item:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, item)

print(min_heap[0])

#크기 n인 최소힙을 유지하면서 최소값보다 크면 최소값을 빼고 새 값을 넣는다.