# arr = [-7,1,2,3,4]
# nums = [0]*len(arr)
# posindex = 0
# negindex = 1

# for i in range(len(arr)):
# 	if (arr[i]<0):
# 		nums[negindex] = arr[i]
# 		negindex += 2
# 	else:
# 		nums[posindex] = arr[i]
# 		posindex += 2

# print (nums)

arr = [-7,1,2,3,4]
posi = []
neg = []
for i in range(len(arr)):
    if arr[i] > 0:
        posi.append(arr[i])
    else:
        neg.append(arr[i])
i, j = 0,1

while i<len(posi) and j<len(neg):
    arr[i] = posi[i]
    arr[j] = neg[i]
    i+=2
    j+=2
if len(posi)>len(neg):
     i = len(neg)+1
     while i < len(posi):
          arr[i] = posi[i]
          i+=1
else:
     j=len(posi)+1
     while j < len(neg):
          arr[j] = neg[j]
          j+=1
print(arr)