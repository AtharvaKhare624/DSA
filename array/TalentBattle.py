nums = [-2,1,-3,4,-1,2,1,-5,4]
ans_start = -1 
ans_end = -1
sum = 0
maxi = -999
for i in range(len(nums)):
    if sum == 0:
        start = i
    
    sum += nums[i]

    if sum>maxi:
        maxi = sum
        ans_start = start 
        ans_end = i

print(maxi)
