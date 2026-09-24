arr = [-1,0,1,2,-1,-4]
i, j, k = 0, 1, 2
result = []
for i in range(len(arr)-2):
    temp = []
    k = i+2
    for j in range(i+1,len(arr)-1):

        if arr[i]+arr[j]+arr[k] == 0:
            temp.append(i)
            temp.append(j)
            temp.append(k)
        k+=1
    result.append(temp)
    
print(result)