import itertools

numbers = list(range(1,11))

permutasjoner = itertools.permutations(numbers)

def transformer_til_løsning(*grupper):
    i = min(range(len(grupper)), key=lambda x: grupper[x][0])
    return ''.join(str(e) for el in grupper[i:]+grupper[:i] for e in el)

løsninger = []
for permutasjon in permutasjoner:
    a1,a2,a3,a4,a5,b1,b2,b3,b4,b5 = permutasjon
    
    if a1+b1+b2 != a2+b2+b3: continue
    if a2+b2+b3 != a3+b3+b4: continue
    if a3+b3+b4 != a4+b4+b5: continue
    if a4+b4+b5 != a5+b5+b1: continue

    løsning = transformer_til_løsning([a1,b1,b2],[a2,b2,b3],[a3,b3,b4],[a4,b4,b5],[a5,b5,b1])

    if len(løsning) != 16:
        continue 

    løsninger.append(løsning)

print(max(løsninger))
# 6531031914842725