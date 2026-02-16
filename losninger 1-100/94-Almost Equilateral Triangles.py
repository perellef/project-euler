from math import isqrt

N = 1000000000

er_kvadrat = lambda x: isqrt(x)**2 == x

s = 0
for a in range(3, N//3+2, 2):
    if a % 4 == 1:
        for b in (a-1, a+1):
            if er_kvadrat(a**2-b**2//4):
                s += b+a+a   
    else:
        b = a+1
        if er_kvadrat(a**2-b**2//4):
            s += b+a+a   
    
print(s)
# 518408346, 568.861s