with open("matrix.txt", "r") as f:
    matrix = [[int(el) for el in e.rstrip().split(",")] for e in f.readlines()]

for r in range(1, len(matrix)):
    matrix[r][0] = matrix[r][0] + matrix[r-1][0]
for k in range(1, len(matrix[0])):
    matrix[0][k] = matrix[0][k] + matrix[0][k-1]

for r in range(1, len(matrix)):
    for k in range(1, len(matrix[0])):
        matrix[r][k] = matrix[r][k] + min(matrix[r][k-1], matrix[r-1][k])
    
print(matrix[len(matrix)-1][len(matrix[0])-1])

