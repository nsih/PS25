import sys

def cantor(lst, n):
    if len(lst) == 1:
        return lst

    lst0 = cantor(lst[0 : n//3], n//3)

    lst1 = lst[n//3 : (n*2)//3]
    for i in range(len(lst1)):
        lst1[i] = ' '

    lst2 = cantor(lst[(n*2)//3 : n], n//3)

    return lst0 + lst1 + lst2

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    res = cantor(['-'] * (3**n), 3**n)
    print(''.join(res))
