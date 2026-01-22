from collections import defaultdict

with open("words.txt", "r") as f:
    words = f.readline().replace('"',"").split(",")

ord = defaultdict(lambda: defaultdict(list))

for word in words:
    ord[len(word)][tuple(sorted(word))].append(word)

ord = {k: [v2 for v2 in v.values() if len(v2) > 1] for k,v in ord.items()}
ord = {k: v for k,v in ord.items() if len(v) > 0}

kvadrater = defaultdict(set)

n = 1
while n**2<10**(max(ord)+1):
    kvadrat = str(n**2)
    if len(kvadrat) == len(set(kvadrat)):
        kvadrater[len(kvadrat)].add(kvadrat)
    n += 1

anagram_kvadrater = set()

m = 0
for n,lst in ord.items():
    for kvadrat in kvadrater[n]:
        for anagrammer in lst:   
            mapping = {tegn: siffer for siffer, tegn in zip(kvadrat, anagrammer[0])}
            
            mappet1 = ''.join(mapping[tegn] for tegn in anagrammer[0])
            for i in range(1, len(anagrammer)):
                mappet2 = ''.join(mapping[tegn] for tegn in anagrammer[i])
                
                if mappet2 in kvadrater[n]:
                    anagram_kvadrater.add(int(mappet1))
                    anagram_kvadrater.add(int(mappet2))

print(max(anagram_kvadrater))
# 18769
