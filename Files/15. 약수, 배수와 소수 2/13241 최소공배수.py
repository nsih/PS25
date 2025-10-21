import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())

    print((a*b)//math.gcd(a,b))

#최소공배수는 a*b//최대공약수