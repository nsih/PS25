#a,b,c = map(int, input().split())
import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

print(min(lst), max(lst))