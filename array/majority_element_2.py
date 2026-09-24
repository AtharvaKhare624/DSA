arr = [1,1,1,3,3,2,2,2]
l = []

for i in range(len(arr)):
    cnt = 1
    for j in range(i+1, len(arr)):
        if arr[j] == arr[i]:
            cnt+=1
            print("i:",arr[i],"j:",arr[j],"count:",cnt)
    if arr[i] not in l and cnt > len(arr)//3:
        l.append(arr[i])


print(l)

