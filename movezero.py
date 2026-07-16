# TWO POINTER APP (optimal)
arr = [1,3,4,5,3,0,0,4,0,5]
t=[]
j=-1
for i in range(len(arr)):
    if(arr[i]==0):
        j=i
        t.append(j)
        break
for i in range(j+1, len(arr)):
    if(arr[i]!=0):
        arr[j],arr[i] = arr[i], arr[j]
        j=j+1
print(arr)
