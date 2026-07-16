arr = [7,7,5,7,5,1,7,7,7,1,1,7,7,7,7,5,7,5,5,7,7,5,5,5,5]
arr1 = [2,2,1,1,1,2,2]
"""BRUTE->O^2
for i in range(len(arr)):
    count = 1
    for j in range(1+i, len(arr)):
        if arr[j] == arr[i]:
            count += 1
            
    
    if count > (len(arr) // 2):print(arr[i],":",count)
"""

"""BETTER->HASH MAP [Olog(N)]
maxi = max(arr)
hash_arr = [0] * (maxi+1)
for i in arr:
    hash_arr[i] += 1
for i in range(len(hash_arr)):
    if hash_arr[i] >= (len(arr) / 2):
        print("number is:",i)
"""

"""OPTIMAL->"""
count = 0

for i in range(len(arr1)):
    if count == 0:
        el = arr1[i]
        count += 1 
    elif arr1[i] == el:
        count += 1
    else:
        count -= 1
c = 0
for j in range(len(arr1)):
    if arr1[j] == el:
        c += 1
if c > (len(arr1) // 2):
    print("found number:", el)
else:
    print("no such number")
