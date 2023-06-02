# Bit全探索
N通りの箇所について、部分集合を列挙することで全探索(2^N通り)できる。

itertoolsを使うと
```
from itertools import product

for bit in product((0, 1), repeat=N)
    bit(長さNのタプル)を使って処理
```

と書ける。