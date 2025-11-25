import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

psum = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(26):
        if ord(s[i - 1]) - ord('a') == j:
            psum[i][j] = psum[i - 1][j] + 1
        else:
            psum[i][j] = psum[i - 1][j]

qlst = []
for _ in range(q):
    a, l, r = sys.stdin.readline().split()

    a = ord(a) - ord('a')
    l = int(l)
    r = int(r)

    print(psum[r + 1][a] - psum[l][a])