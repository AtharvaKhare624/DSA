arr = [2,1,5,4,3,0,0]

index = -1
n = len(arr)
ans = []
for i in range(n-2,-1,-1):
    if (arr[i] < arr[i+1]):
        index = i
        break

if index == -1:
    for i in range(n,-1,-1):
        arr.reverse()
        
for i in range(n-1, index, -1):
    if (arr[index] < arr[i]):
        arr[index],arr[i] = arr[i], arr[index]
    break

arr[index + 1:] = reversed(arr[index + 1:])

print (arr)