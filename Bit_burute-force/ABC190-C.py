N,M = map(int, input().split())

A = []
B = []
C = []
D = []

for i in range(M):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

K = int(input())

for i in range(K):
    c,d = map(int, input().split())
    C.append(c)
    D.append(d)

ans = 0

for bit in range(2**K):
    cnt = 0
    num = [0]*101
    for n in range(K):
        if (bit >> n)&1:
            num[C[n]] = 1
        else:
            num[D[n]] = 1
    for i in range(M):
        if num[A[i]] == 1 and num[B[i]] == 1:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)