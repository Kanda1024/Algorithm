# BFS
実装例
```
from collections import deque

N = int(input())

G = []

for i in range(N):
    G.append([])

#連結リストを作成
for i in range(N):
    for j in range(i+1,N):
        G[i].append(j)
        G[j].append(i)

que = deque()
que.append(0)
#訪問済みフラグ
visited = [False] * N
visited[0] = True

#キューが空になるまで探索
while que:
    now = que.popleft()
    #連結成分を調べる
    for v in G[now]:
        #未訪問なら
        if visit[v] == False:
            que.append(v)
            visit[v] = True

for i in range(N):
    if visit[i] == True:
        print("Yes")
    else:
        print("No")
```