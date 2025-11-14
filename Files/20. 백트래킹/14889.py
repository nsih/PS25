import sys

def sl(depth):
    global res

    if len(lst1) > n//2 or len(lst2) > n//2:
        return

    if depth == n and len(lst1) == n//2 and len(lst2) == n//2:
        s1 = 0
        s2 = 0

        for i in lst1:
            for j in lst1:
                if i < j:
                    s1 += team[i][j] + team[j][i]
        for i in lst2:
            for j in lst2:
                if i < j:
                    s2 += team[i][j] + team[j][i]

        res = min(res, abs(s1-s2))
        return

    lst1.append(depth)
    sl(depth+1)
    lst1.pop()

    lst2.append(depth)
    sl(depth+1)
    lst2.pop()

n = int(sys.stdin.readline())

team = []

for _ in range(n):
    team.append(list(map(int, sys.stdin.readline().split())))


lst1 = []
lst2 = []

res = 10**9

sl(0)

print(res)