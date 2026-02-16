from collections import defaultdict

N = 1500000

løsninger = defaultdict(set)

m = 0
while True:
    m += 1
    for n in range(1, min(N, m-1)+1):
        inn = True

        a = m**2-n**2
        b = 2*n*m
        c = m**2 + n**2
        
        if a+b+c > N:
            break
        
        skala = 1
        while skala*(a+b+c) <= N:
            løsninger[skala*(a+b+c)].add(tuple(sorted((skala*a, skala*b, skala*c))))
            skala += 1

    if m > N:
        break

print(len([k for k,v in løsninger.items() if len(v) == 1]))
# 161667, 14.671s