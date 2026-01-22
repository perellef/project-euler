import heapq

with open("matrix.txt", "r") as f:
    matrix = [[int(el) for el in e.rstrip().split(",")] for e in f.readlines()]

lst = [(matrix[0][0],(0,0))]

heapq.heapify(lst)

besøkt = set()
while len(lst) > 0:
    s,(r,k) = heapq.heappop(lst)
    if (r,k) in besøkt:
        continue
    besøkt.add((r,k))

    if (r,k) == (len(matrix)-1, len(matrix[0])-1):
        print(s)
        break

    if k-1 >= 0:
        heapq.heappush(lst, (s+matrix[r][k-1], (r, k-1)))
    if k+1 < len(matrix[0]):
        heapq.heappush(lst, (s+matrix[r][k+1], (r, k+1)))
    if r+1 < len(matrix):
        heapq.heappush(lst, (s+matrix[r+1][k], (r+1, k)))
    if r-1 >= 0:
        heapq.heappush(lst, (s+matrix[r-1][k], (r-1, k)))
