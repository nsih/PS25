#a,b,c = map(int, input().split())
import sys

dic = { int(sys.stdin.readline()) % 42 : 0 for _ in range(10) }

print(len(dic))

'''
s = set()

s = {int(sys.stdin.readline()) % 42 for _ in range(10)}

print(len(s))
'''