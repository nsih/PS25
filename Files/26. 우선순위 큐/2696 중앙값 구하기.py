import sys
import math
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    m = int(sys.stdin.readline())
    print((m + 1) // 2)

    lst = []
    while len(lst)<m:
        lst.extend(map(int, sys.stdin.readline().split()))

    left_heap = []
    right_heap = []

    res = []

    for i in range(m):
        #길이가 같으면 왼쪽에 넣고 왼쪽이 더크면 오른쪽에 넣기
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -lst[i])
        else:
            heapq.heappush(right_heap, lst[i])

        #오른쪽힙이 있고, 왼쪽 최대가 오른쪽 최소보다 클때 바꾸기
        if right_heap and (-left_heap[0] > right_heap[0]):
            l_max = -heapq.heappop(left_heap)
            r_min = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -r_min)
            heapq.heappush(right_heap, l_max)

        #홀수마다 왼쪽 최대값 리스트에 넣기
        if i % 2 == 0:
            res.append(-left_heap[0])

    #10개씩 끊어 줄바꾸고 출력
    for idx in range(len(res)):
        print(res[idx], end=' ')
        if (idx + 1) % 10 == 0:
            print()

    if len(res) % 10 != 0:
        print()