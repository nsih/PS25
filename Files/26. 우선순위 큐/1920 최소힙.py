import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        print(heapq.heappop(heap) if heap else 0)

    else:
        heapq.heappush(heap, x)


'''
heapq는 최솟값을 꺼낸다.
그러니까 그냥 최솟값을 꺼낼 수 있다.
'''