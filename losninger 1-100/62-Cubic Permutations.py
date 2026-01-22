from collections import defaultdict

kube = lambda n: n**3

kuber = defaultdict(set)
n = 1
while True:
    kubepermutasjon = str(sorted(str(kube(n))))
    kuber[kubepermutasjon].add(kube(n))

    if len(kuber[kubepermutasjon]) == 5:
        print(min(kuber[kubepermutasjon]))
        break 

    n += 1

# 127035954683
