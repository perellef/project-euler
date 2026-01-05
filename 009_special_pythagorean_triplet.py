# https://projecteuler.net/problem=9

def søk():
    for m in range(1,100):
        max_n = (500-m**2)//m
        for n in range(1, min(max_n, m)+1):

            a = m**2-n**2
            b = 2*n*m
            c = m**2 + n**2

            if a == 0:
                continue
            if a + b + c > 1000:
                break
            
            if a+b+c == 1000:
                print(a*b*c)
                return

søk()
# 31875000