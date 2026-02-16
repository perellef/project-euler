from functools import cache

def primtall():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

@cache
def antall_summer(s, tall):
    if len(tall) == 0:
        return int(s == 0)
    return sum(antall_summer(s-t, tuple(tall[1:])) for t in range(0,s+1,tall[0]))

def summer_5000():
    primes = []
    for p in primtall():
        primes.append(p)
        if len(primes) == 1:
            continue

        for n in range(primes[-2]+1, primes[-1]):
            if antall_summer(n, tuple(primes)) >= 5000:
                return n

print(summer_5000())
# 72