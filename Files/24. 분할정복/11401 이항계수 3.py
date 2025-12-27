import sys

# 1. 입력 받기
N, K = map(int, sys.stdin.readline().split())
P = 1000000007

fac = [1] * (N + 1)

for i in range(2, N + 1):
    fac[i] = (fac[i - 1] * i) % P


def power(a, b):
    if b == 0: return 1
    if b == 1: return a % P

    temp = power(a, b // 2)

    if b % 2 == 0:
        return (temp * temp) % P
    else:
        return (temp * temp * a) % P


ja = fac[N]
mo = (fac[K] * fac[N - K]) % P

result = (ja * power(mo, P - 2)) % P

print(result)