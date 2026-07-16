'''
OPTIMAL-> (posi=neg)[two pointers]

arr = [3,1,-2,-5,2,-4]
nums = [0]*len(arr)
posindex = 0
negindex = 1

for i in range(len(arr)):
	if (arr[i]<0):
		nums[negindex] = arr[i]
		negindex += 2
	else:
		nums[posindex] = arr[i]
		posindex += 2

print (nums)
'''
'''
BRUTE-> VARIATION FOR (POSI!=NEG)

arr = [3,1,-2,-5,2,4]
nums = [0]*len(arr)
posi = [3,1,2,4]
neg= [-2,-5]

if (len(posi) > len(neg)):
	for i in range(len(neg)):
		nums[i*2] = posi[i]
		nums[i*2+1] = neg[i]

	index = 2*len(neg)

	for i in range(len(neg), len(posi)):
		nums[index] = posi[i]
		index+=1
else:
	for i in range(len(posi)):
		nums[i*2] = posi[i]
		nums[i*2+1] = neg[i]

	index = 2*len(posi)

	for i in range(len(posi), len(neg)):
		nums[index] = posi[i]
		index+=1

print(nums)
'''