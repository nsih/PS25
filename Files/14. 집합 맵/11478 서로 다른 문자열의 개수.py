import sys

n,m = map(int, sys.stdin.readline().split())

lst1 = set( map( int, sys.stdin.readline().split() ) )
lst2 = set( map( int, sys.stdin.readline().split() ) )

print(len(lst1 ^ lst2)) #대칭 차집합