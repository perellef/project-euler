
n = 1001

s = 1
for k in range(3,n+1,2):
    for i in (1,2,3,4):
        s += (k-2)**2+i*(k-1)
print(s)
# 669171001