import sys

def Nt(i):
    if ord(i) >= 65:
        return ord(i)-ord('A')+10
    else:
        return int(i)

b, n = map(str, sys.stdin.readline().strip().split())

b = b[::-1]
n = int(n)

result = 0

for i in range(len(b)):
    temp = Nt(b[i]) 
    result += temp * (n**i)

print(result)