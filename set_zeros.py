arr = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
n = len(arr)
m = len(arr[0])

"""BRUTE APPROACH
def mark_row(i):
    for j in range(m):
        if arr[i][j] != 0:
            arr[i][j] = -1

def mark_col(j):
    for i in range(n):
        if arr[i][j] != 0:
            arr[i][j] = -1

for i in range(len(arr)):

    for j in range(len(arr[0])):

        if arr[i][j] == 0:
            mark_row(i)
            mark_col(j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            arr[i][j] = 0

print(arr)"""

row = [0 for r in range(n)]
col = [0 for i in range(m)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            col[j] = 1
            row[i] = 1

for i in range(n):
    for j in range(m):
        if row[i] == 1 or col[j] == 1:
            arr[i][j] = 0

print(arr)