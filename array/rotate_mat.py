matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
for i in range(n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(n):
    for j in range(n//2):
        matrix[i][j],matrix[i][(n-1)-j] = matrix[i][(n-1)-j],matrix[i][j]

print(matrix)
def moment_of_truth():
    if matrix == [[7,4,1],[8,5,2],[9,6,3]]:
        return True
    else:return False
print(moment_of_truth())