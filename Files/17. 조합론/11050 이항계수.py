import sys
import math

n,k = map(int, sys.stdin.readline().split())

print(math.comb(n,k))

#이항계수란? : n개 중에 순서 상관없이 k뽑는거 공식을 외우지말고 함수를 외워라