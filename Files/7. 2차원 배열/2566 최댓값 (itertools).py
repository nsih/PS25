#import string
import sys
from itertools import  zip_longest

lst = [str(sys.stdin.readline().strip()) for _ in range(5)]

result = ''

for col in zip_longest(*lst, fillvalue=''):
    result += ''.join(col)

print(result)