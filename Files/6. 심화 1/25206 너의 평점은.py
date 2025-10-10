#a,b,c = map(int, input().split())
#import string
import sys

score = 0.0
sum = 0

for _ in range(20):
    lst = list(map(str, sys.stdin.readline().strip().split()))

    if lst[2] == 'A+':
        sum += float(lst[1])
        score += 4.5 * float(lst[1])
    elif lst[2] == 'A0':
        sum += float(lst[1])
        score += 4.0*float(lst[1])
    elif lst[2] == 'B+':
        sum += float(lst[1])
        score += 3.5*float(lst[1])
    elif lst[2] == 'B0':
        sum += float(lst[1])
        score += 3.0*float(lst[1])
    elif lst[2] == 'C+':
        sum += float(lst[1])
        score += 2.5*float(lst[1])
    elif lst[2] == 'C0':
        sum += float(lst[1])
        score += 2.0*float(lst[1])
    elif lst[2] == 'D+':
        sum += float(lst[1])
        score += 1.5*float(lst[1])
    elif lst[2] == 'D0':
        sum += float(lst[1])
        score += 1.0*float(lst[1])
    elif lst[2] == 'F':
        sum += float(lst[1])

print( f'{score/sum:.6f} ')