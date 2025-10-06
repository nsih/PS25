#a,b,c = map(int, input().split())
import sys

temp = sys.stdin.readline()

lst = list(map(int,sys.stdin.readline().split()))

f = int(sys.stdin.readline())

print(lst.count(f))