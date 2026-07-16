arr = [1,2,3,1,1,1,1,1,4,5]
left = 0
right = 0
maxi = 0
n = len(arr)
k = 5
sum = 0

while right < n:
    sum += arr[right]

    if sum == k:
        maxi = max(maxi, right-left+1)

    while left < right and sum>k:
        sum -= arr[left]
        left += 1
    
    right += 1

print("max is:",maxi)