arr1 = [1,2,3,4,5]
arr2= [2,3,4,4,5]
u = []
n = 5
m = 5
i = 0
j = 0
while i<n and j<m:
    if arr1[i]<arr2[j]:
        u.append(arr1[i])
        i+=1
    
    elif arr1[i]>arr2[j]:
        u.append(arr2[j])
        j+=1

    else:
        u.append(arr1[i])
        i+=1
        j+=1

while i<n:
    if len(u)==0 or u[-1]!=arr1[i]:
        u.append(arr1[i])
    i+=1
while j<m:
    if len(u)==0 or u[-1]!=arr2[j]:
        u.append(arr2[j])
    j+=1
print(u)
