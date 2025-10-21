import sys

lst = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        lst.append(n)

n = max(lst)

pl = [False, False] + [True] * (n*2)

for i in range(2,int((n*2)**0.5)+1):
    if pl[i]:
        for j in range(i*i, (n*2)+1, i):
            pl[j] = False


for i in lst:
    cnt = 0
    for j in range(i+1, (i*2)+1 ):
        if pl[j]:
            cnt += 1
    print(cnt)


'''
베르트랑 공준이란?

n~2n사이에는 소수하나쯤 있지 않을까 하는것

n~2n사이에 에라토스테네스의 체를 갖다대자
'''