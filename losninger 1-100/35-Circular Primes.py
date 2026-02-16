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

primes = set()
for p in primtall():
    if p > 1000000:
        break
    primes.add(str(p))

s = 0
for p in primes:
    if all((p[i:] + p[:i] in primes for i in range(len(p)))):
        s += 1

print(s)
# 55