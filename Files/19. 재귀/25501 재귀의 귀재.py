import sys

def recursion(s, l, r):
    if l >= r:
        return 1, 1
    elif s[l] != s[r]:
        return 0, 1
    else:
        result, count = recursion(s, l + 1, r - 1)
        return result, count + 1

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()

    res, cnt = isPalindrome(s)

    print(res, cnt)