from collections import defaultdict
from functools import cache

ns = defaultdict(set)

@cache
def number_of_factors(k):
    ns = set(((k,1),))
    for divisor in range(2,k):
        if k % divisor == 0:
            for s,v in number_of_factors(divisor):
                ns.add((k//divisor+s, v+1))
    return ns

N = 12000

minimal_produktsum_numre = set()
for n in range(2, N+1):
    k = n
    while True:
        ms = number_of_factors(k)
        if any((n-m == k-s for s,m in ms)):
            minimal_produktsum_numre.add(k)
            break
        k += 1

print(sum(minimal_produktsum_numre))
# 7587457, 19.298s
