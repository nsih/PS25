import sys
import heapq

n = int(sys.stdin.readline())
heap = []

abs_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(x), x))


'''
#튜플을 활용하려 힙의 절대값의 최소값을 빼고 원본 프린트한다.
'''