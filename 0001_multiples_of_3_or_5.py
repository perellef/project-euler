# https://projecteuler.net/problem=1

s = 0
for k in range(1,1000):
    if 0 in (k % 3, k% 5):
        s += k
print(s)

# 233168