import sys


def Nt(n):
    if n>=10:
        return chr( (n-10)+ord('A') )
    else:
        return str(n)


n,b = map(str,sys.stdin.readline().strip().split())
n = int(n)
b = int(b)
lst = []

if n == 0:
    print(0)

else:
    while n > 0:
        lst.append( Nt(n%b) )
        n = n//b

print(''.join(lst[::-1]))