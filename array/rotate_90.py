row ,col = int(input()),int(input())
matrix = []
for i in range(row):
    temp = []
    for j in range(col):
        w = int(input())
        temp.append(w)
    matrix.append(temp)
print(matrix)
summ = 0
i, j = 0, 0
while i < row-1:
    while j < col-1:
        if matrix[i+1][j] < matrix[i][j+1]:
            summ += matrix[i+1][j]
            i+=1
        else:
            summ += matrix[i][j+1]
            j+=1

print(summ)
