from collections import defaultdict

with open("poker.txt", "r") as f:
    linjer = f.readlines()

verdi = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

ranker = ["high card", "one pair", "two pairs", "three of a kind","straight", "flush", "full house", "four of a kind", "straightflush"]

def rank(hånd):
    farger = defaultdict(int)
    valører_antall = defaultdict(int)
    valører = []
    for kort in hånd:
        v,f = list(kort)
        valører_antall[verdi[v]] += 1
        valører.append(verdi[v])
        farger[f] += 1

    valører = sorted(valører, reverse=True)

    sorterte_valører = list(sorted(valører_antall.items(), key=lambda x: (x[1], x[0]), reverse=True))

    if len(sorterte_valører) == 5 and min(valører) + 4 == max(valører):
        if len(farger) == 1:
            return ("straightflush", valører)
        return ("straight", valører)
    
    if sorterte_valører[0][1] == 4:
        return ("four of a kind", sorterte_valører[0][0], valører)
    
    if sorterte_valører[0][1] == 3:
        if sorterte_valører[1][1] == 2:
            return ("full house", sorterte_valører[0][0], sorterte_valører[1][0], valører)
        return ("three of a kind", sorterte_valører[0][0], valører)

    if len(farger) == 1:
        return ("flush", valører)
    
    if sorterte_valører[0][1] == 2:
        if sorterte_valører[1][1] == 2:
            return ("two pairs", sorterte_valører[0][0], sorterte_valører[1][0], valører)
        return ("one pair", sorterte_valører[0][0], valører)
    
    return ("high card", valører)

def rankverdi(hånd):
    ranken = rank(hånd)
    return ranker.index(ranken[0]), ranken[1]

s = 0
for linje in linjer:
    spiller1_hånd = linje.split(" ")[:5] 
    spiller2_hånd = linje.rstrip("\n").split(" ")[5:]

    if rankverdi(spiller1_hånd) > rankverdi(spiller2_hånd):
        s += 1
print(s)