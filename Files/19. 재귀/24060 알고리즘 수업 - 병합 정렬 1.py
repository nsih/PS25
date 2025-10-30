import sys


def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)
        merge_sort(A, q + 1, r, K)
        merge(A, p, q, r, K)

    # 반으로 나눠서 q를 설정하고 반까지 다시 재귀, 반부터 끝까지 다시재귀 그리고 합친다.


def merge(A, p, q, r, K):
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

        # 왼쪽 반이랑 오른쪽 반 각각 왼쪽보다 작으면 넣고 아니면 오른쪽을 넣는다.

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 왼쪽에 정렬된것을 넣고 오른쪽에 정렬된 것을 넣는다.

    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        merge_sort.counter += 1
        if merge_sort.counter == K:
            merge_sort.value = tmp[t]

        # a의 순서를 tmp의 순서로 바꾸고 counter를 증가시킨다.
        # K번째면 merge_sort.value에 답을 저장한다.


N, K = map(int, sys.stdin.readline().split())
aLst = list(map(int, sys.stdin.readline().split()))

merge_sort.counter = 0
merge_sort.value = 0
merge_sort(aLst, 0, len(aLst) - 1, K)

if merge_sort.value:
    print(merge_sort.value)
else:
    print(-1)

