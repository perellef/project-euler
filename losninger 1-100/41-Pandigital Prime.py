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

# Ingen tall 1-8 eller 1-9 er primtall fordi de har tverrsum delelig på 3.
# Vi trenger derfor kun å sjekke primtall under 10000000.

m = 0
for p in primtall():
    if p >= 10000000:
        break
    p_str = str(p)
    if "0" in p_str:
        continue
    if ''.join(sorted(p_str)) == "123456789"[:len(p_str)]:
        m = p

print(m)
# 7652413