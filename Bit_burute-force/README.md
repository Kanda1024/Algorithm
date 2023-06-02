# Bit全探索
N通りの箇所について、部分集合を列挙することで全探索(2^N通り)できる。


```
for bit in range(2**N):
    for i in range(N):
        if (bit >> i)&1:
            処理1
        else:
            処理2
```


itertoolsを使うと、
```
from itertools import product

for bit in product((0, 1), repeat=N)
    bit(長さNのタプル)を使って処理
```

と書ける。