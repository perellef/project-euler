# løst, https://projecteuler.net/problem=4

ps = set()
for f1 in range(100,1000):
    for f2 in range(100,1000):
        ps.add(f1*f2)

for p in sorted(ps, reverse=True):
    if str(p) == str(p)[::-1]:
        print(p)
        break
# 906609