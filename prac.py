arr = [1,1,2,2,2,3,3,4,5,5,6,7,8,8]
L, R = 0,1
while R<len(arr):
    if arr[L] == arr[R]:
        R+=1
    else:
        L+=1
        arr[L], arr[R] = arr[R], arr[L]
        R+=1

print(arr)
