s = 0

for exp in range(1,100):
    n = 1
    while True:
        p = n**exp
        if len(str(p)) == exp:
            s += 1
        if len(str(p)) > exp:
            break
        n += 1
print(s)
# 49