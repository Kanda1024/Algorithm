N = int(input())
S = input()

cnt = 0
num = 0

for i in range(N):
    if S[i] == "(":
        cnt += 1
    elif S[i] == ")":
        cnt -= 1
    if cnt < 0:
        num = max(num, -cnt)

for i in range(num):
    S = "(" + S

cnt = 0

for i in range(N + num):
    if S[i] == "(":
        cnt += 1
    elif S[i] == ")":
        cnt -= 1

for i in range(cnt):
    S = S + ")"

print(S)