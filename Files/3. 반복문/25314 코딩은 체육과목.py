#a,b,c = map(int, input().split())

x = int(input())

result = ('long ' * (x // 4)) + 'int'

print(result)


s = ''

for i in range(x//4):
    s += 'long '

s += 'int'
print(s)