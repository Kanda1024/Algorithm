N = 4

ans = []
for bit in range(2**N):
    res = ""
    for i in range(N):
        if (bit >> i)&1:
            res += "1"
        else:
            res += "0"
    ans.append(res)

print(ans)
