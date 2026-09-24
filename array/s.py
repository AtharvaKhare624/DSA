arr = [2,5,7,8,10,11]
arr.sort()
t = 14
L, R = 0, len(arr)-1

while L<R:
    if arr[L] + arr[R] < t:
        L+=1
    
    elif arr[L] + arr[R] > t:
        R-=1
    else:
        print("present")
        break
    if L==R:
        print("not found")
        break
    