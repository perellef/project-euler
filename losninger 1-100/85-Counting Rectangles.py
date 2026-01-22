
rektangler = lambda m,n: m*(m+1)*n*(n+1)//4

beste = 2000000
areal = 0 
for m in range(1,100000):
    for n in range(1,100000):
        if rektangler(m,n)-2000000 > beste:
            break
        if abs(2000000-rektangler(m,n)) < beste:
            areal = m*n
            beste = abs(2000000-rektangler(m,n))

print(areal)
# 2772