#a,b,c = map(int, input().split())

x = int(input())
t = int(input())

temp = 0

for i in range(t):
    a,b = map(int, input().split())

    temp += a*b

if x == temp:
    print('Yes')
else:
    print('No')
