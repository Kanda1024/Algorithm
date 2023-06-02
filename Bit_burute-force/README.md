# Bit全探索
N通りの箇所について、部分集合を列挙することで全探索(2^N通り)できる。

'''
from itertools import product
'''
をすると、　
'''
for bit in product((0, 1), repeat=N)
'''

と書ける