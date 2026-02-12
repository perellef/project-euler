s = set()
for n1 in range(1, int(1e6)):
    for n2 in range(n1+1, int(1e6)):
        p = n1*n2
        størrelse = len(str(n1))+len(str(n2))+len(str(p))
        if størrelse < 9:
            continue
        if størrelse > 9:
            break
        
        if set(str(n1)+str(n2)+str(p)) == set("123456789"):
            s.add(p)
print(sum(s))
# 45228