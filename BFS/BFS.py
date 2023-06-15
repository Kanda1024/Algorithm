from collections import deque

R,C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

c = []

for i in range(R):
    c.append(list(input()))

que = deque()
que.append([sy-1,sx-1])
c[sy-1][sx-1] = str("0")

ans = 1

while que:
    num = len(que)
    #for i in range(R):
    #    print(c[i])
    #print("-------------------")
    while num > 0:
        now = que.popleft()
        for i in range(4):
            y = now[0] + dy[i]
            x = now[1] + dx[i]
            if x == gx-1 and y == gy-1:
                print(ans)
                exit()
            if c[y][x] == '.':
                que.append([y,x])
                c[y][x] = str(ans)
        num -= 1
    ans += 1