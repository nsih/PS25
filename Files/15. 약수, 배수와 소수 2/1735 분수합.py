import sys
import math

a,b = map(int,sys.stdin.readline().split())
c,d = map(int,sys.stdin.readline().split())

lcm = (b*d)//math.gcd(b,d)

numerator = (a*(lcm//b)+c*(lcm//d))

gcd = math.gcd(numerator,lcm)

print(numerator//gcd , lcm//gcd )


#numerator/denominator