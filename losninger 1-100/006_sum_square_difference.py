# https://projecteuler.net/problem=6

n = 100
print(int(n*(n+1)/2)**2 - sum(k**2 for k in range(1,n+1)))

# 25164150