import sys
import heapq

n = int(sys.stdin.readline())

heap = []


for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        print(-heapq.heappop(heap) if heap else 0)

    else:
        heapq.heappush(heap, -x)


'''
heapq는 최솟값을 꺼낸다.
그러니까 부호를 반대로 넣으면 최댓값을 꺼낼수 있다.
꺼낼때 *-1만 해주자
'''