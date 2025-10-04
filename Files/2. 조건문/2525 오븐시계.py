H,M = map(int, input().split())

A = int(input())

H_ = A//60
M_ = A%60

H += H_
M += M_

if M >= 60:
    H += M//60
    M = M%60

if H >= 24:
    H = H%24

print(H,M)
