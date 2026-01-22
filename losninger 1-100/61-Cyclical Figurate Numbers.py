from collections import defaultdict

triangle = lambda n: n*(n+1)//2
square = lambda n: n**2
pentagonal = lambda n: n*(3*n-1)//2
hexagonal = lambda n: n*(2*n-1)
heptagonal = lambda n: n*(5*n-3)//2
octagonal = lambda n: n*(3*n-2)

numbers = defaultdict(set)
for i,f in enumerate((triangle, square, pentagonal, hexagonal, heptagonal, octagonal)):
    for n in range(1,10000):
        p = f(n)
        if p < 1000:
            continue
        if p>=10000:
            break
        numbers[str(p)[:2]].add((i, str(p)[2:]))

#trianglenumbers = [k+e for k,v in triangles.items() for e in v]

løsninger = []
def _løs_(k, ier, ver):
    if len(ier) == 6:
        if ver[-1] == k:
            løsninger.append(ver)
        return
    
    for (i,v) in numbers[ver[-1]]:
        if i in ier:
            continue
        _løs_(k, ier.union((i,)), ver+[v])

for k,lst in list(numbers.items()):
    _løs_(k, set(), [k])

tall = []
for i in range(len(løsninger[0])-1):
    tall.append(int(løsninger[0][i]+løsninger[0][i+1]))

print(tall)
print(sum(tall))

# [1281, 8128, 2882, 8256, 5625, 2512]
# 28684