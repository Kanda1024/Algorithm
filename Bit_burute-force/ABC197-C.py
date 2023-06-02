N = int(input())
A = list(map(int, input().split()))

ans = 1e20

if len(A) == 1:
    print(A[0])
    exit()

for bit in range(2**(N-1)):
    sum = A[0]
    xor = 0
    for n in range(N-1):
        if (bit >> n)&1:
            sum |= A[n+1]
        else:
            xor ^= sum
            sum = A[n+1]
    xor ^= sum
    ans = min(ans,xor)

print(ans)