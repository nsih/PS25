import sys
import math

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))


if n == 1:
    print(0)

else:
    gap = []
    for i in range(n-1):
        gap.append( lst[i+1]-lst[i] )

    gcd = gap[0]
    for i in gap:
        gcd = math.gcd(gcd,i)


    print( (lst[-1] - lst[0]) // gcd + 1 - n )
    
#당황하지 말고 입력조건을 봐

#막-첫 최소공배수로 나눠서 가중치