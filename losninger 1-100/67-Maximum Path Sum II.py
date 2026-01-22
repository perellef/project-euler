with open("triangle.txt", "r") as f:
    triangle = [[int(el) for el in e.rstrip("\n").split(" ")] for e in f.readlines()]

for r in range(len(triangle)-2, -1, -1):
    for k in range(len(triangle[r])):
        triangle[r][k] = triangle[r][k] + max(triangle[r+1][k], triangle[r+1][k+1])

print(triangle[0][0])
# 7273