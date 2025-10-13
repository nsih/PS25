import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m = int(sys.stdin.readline())

    q = m//25
    m = m%25

    d = m//10
    m = m%10

    n = m//5
    m = m%5

    p = m

    print(q,d,n,p)