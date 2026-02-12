
from itertools import permutations

perms = permutations("0123456789")

for i,perm in enumerate(perms, start=1):
    if i == 1000000:
        break

print(''.join(perm))
# 2783915460