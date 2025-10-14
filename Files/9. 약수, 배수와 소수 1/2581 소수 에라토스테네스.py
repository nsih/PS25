import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

isPrime = [False, False] + [True] * (m - 1) #0,1,2 - true*(m-1)

for i in range(2,int(m**0.5) + 1):
    if isPrime[i]:
        for j in range(i*i, m+1, i):
            isPrime[j] = False

primes = []
for i in range(n,m+1):
    if isPrime[i]:
        primes.append(i)

if len(primes) > 0:
    print(sum(primes))
    print(min(primes))

else:
    print(-1)
