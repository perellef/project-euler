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

from collections import defaultdict

grupper = defaultdict(list)

m = 0
for p in primtall():
    p_str = str(p)
    if len(p_str) < 4:
        continue
    if len(p_str) > 4:
        break
    
    grupper[''.join(sorted(p_str))].append(p)

perms = []
for k,v in grupper.items():
    for i1 in range(0,len(v)-2):
        for i2 in range(i1+1,len(v)-1):
            for i3 in range(i2+1,len(v)):
                if v[i3]-v[i2] == v[i2]-v[i1]:
                    perms.append((v[i1],v[i2],v[i3]))
    
print(perms)
# [(1487, 4817, 8147), (2969, 6299, 9629)]