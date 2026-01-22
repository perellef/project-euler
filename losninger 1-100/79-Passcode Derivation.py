
with open("keylog.txt", "r") as f:
    keylog = [e.rstrip("\n") for e in f.readlines()]

sifre = set()

etterfølgere = set()
for key in keylog:
    for i in range(len(key)-1):
        etterfølgere.add(key[i]+key[i+1])
        
    for siffer in key:
        sifre.add(siffer)

passord = ""
while len(passord) < len(sifre):
    foran = set(f for f,b in etterfølgere if b not in passord)
    passord = next(iter(sifre.difference(foran).difference(set(passord)))) + passord

print(passord)