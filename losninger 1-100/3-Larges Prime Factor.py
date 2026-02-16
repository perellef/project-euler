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

N = 600851475143

m = 0
for p in primtall():
    if p > N**(1/2):
        break
    if N%p == 0:
        m = p
print(m)
# 6857