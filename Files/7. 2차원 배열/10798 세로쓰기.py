#import string
import sys

lst = [str(sys.stdin.readline().strip()) for _ in range(5)]

maxLen = 0
for col in lst:
    if len(col) > maxLen:
        maxLen = len(col)

result = ""
for i in range(maxLen):
    for j in range(5):
        if i < len(lst[j]):
            result += lst[j][i]

print(result)