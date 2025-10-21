import sys

n,m = map(int, sys.stdin.readline().split())

pl = [False,False,True] + [True]*(m-2)

for i in range(2,int(m**0.5)+1):
    if pl[i]:
        for j in range(i*i, m+1, i):
            pl[j] = False

for i in range(n,m+1):
    if pl[i]:
        print(i)


#에라토스테네스의 체

'''
1. 0,1,2까지 만들어놓고 n-2개 붙임
2. n**0.5까지 체로 거를 준비
3. true면 체로 거름
'''