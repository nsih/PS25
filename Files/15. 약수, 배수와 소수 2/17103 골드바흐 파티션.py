import sys

lst = []

t = int(sys.stdin.readline())

for _ in range(t):
    lst.append( int(sys.stdin.readline()) )

n = max(lst)

pl = bytearray([False, False] + [True] * (n-1))

limit = int(n**0.5)+1

for i in range(2, limit):
    if pl[i]:
        for j in range(i*i, n+1, i):
            pl[j] = False


for i in lst:
    cnt = 0
    for p in range(2,i//2+1):
        if pl[p] and pl[i-p]:
            cnt += 1
    print(cnt)

'''
1. t만큼의 테스트 케이스를 lst에 입력 받는다
2. lst 중 최대값 n까지 소수를 판별하기 위해 에라토스테네스의 체(pl)를 생성
3. √n까지 반복(limit = int(n**0.5)+1)하며 소수 리스트 생성
4. 테스트 케이스 lst를 순회하며 결과 출력
5. 각 테스트 케이스 i에 대해:
   - 2부터 i//2까지의 p를 탐색
   - p가 소수이고 i - p도 소수이면 cnt 증가
   - 이렇게 하면 중복 쌍 없이 i를 만드는 모든 소수 쌍 카운트 가능
'''