num_rows = 6
r, c = 5,3
cnt = 0
result = []
for i in range(1, num_rows+1):
    temp = []
    for j in range(i):
        if j == 0 or j == i - 1:
            temp.append(1)
        else:
            e = result[cnt-1][j-1] + result[cnt-1][j]
            temp.append(e)
             
    result.append(temp)
    cnt+=1

# print(result[r-1][c-1])
# print(result[4])
print(result)