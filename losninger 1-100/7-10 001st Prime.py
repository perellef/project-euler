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

i = 1
for p in primtall():
    if i == 10001:
        break
    i += 1

print(p)
# 104743
