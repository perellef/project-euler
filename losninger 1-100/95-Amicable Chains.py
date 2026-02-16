
def divisors(n):
    s = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s-n

divs = {n: divisors(n) for n in range(1,1000000)}

sykler = set()
besøkte = set()
for n,d in divs.items(): 
    if n in besøkte:
        continue
    besøkte.add(n)

    pot_sykel = [n]
    while True:
        if d not in divs:
            break
        n, d = d, divs[d]

        try:
            i = pot_sykel.index(n)
            sykler.add(tuple(pot_sykel[i:]))
            break
        except ValueError:
            pass
        pot_sykel.append(n)

print(min(max(sykler, key=len)))
# 14316, 113.673s