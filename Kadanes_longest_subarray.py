arr = [-2,1,-3,4,-1,2,1,-5,4]
maxi = float('-inf')
"""BRUTE/BETTER
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        temp = max(sum, temp)

print("max is :",temp)
"""
"""OPTIMAL -> KADANES ALGO"""

ans_start = -1 
ans_end = -1
sum = 0

for i in range(len(arr)):
    if sum == 0:
        start = i
    
    sum += arr[i]

    if sum>maxi:
        maxi = sum
        ans_start = start 
        ans_end = i

print(maxi)

