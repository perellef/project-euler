s = 0
for n in range(10000000):
    number = str(n)
    if sum(int(a)**5 for a in number) == int(number):
        s += int(number)

print(s)
# 443840