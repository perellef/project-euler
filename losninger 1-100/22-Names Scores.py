
with open("names.txt", "r") as f:
    linjer = f.readline().replace('"','').split(",")

s = 0
for i, navn in enumerate(sorted(linjer), start=1):
    t = 0
    for tegn in navn:
        t += ord(tegn)-64
    s += t*i
print(s)