from collections import defaultdict

mynter = [1, 2, 5, 10, 20, 50, 100, 200]

TOTAL = 200

lst = defaultdict(int)
lst[0] = 1

for mynt in mynter[-1:0:-1]:
    ny_lst = defaultdict(int)
    for s,v in lst.items():
        for k in range((TOTAL-s)//mynt+1):
            ny_lst[s+k*mynt] += v
    lst = ny_lst

print(sum(lst.values()))
# 73682