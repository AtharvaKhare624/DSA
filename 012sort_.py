nums = [0, 0, 2, 1, 0, 2, 1, 1, 1]

hash = 3 * [0]

for i in nums:
    hash[i] += 1
print(hash)


"""
BRUTE APPROCH - COUNTER
cot0, cot1, cot2 = 0, 0, 0
for i in range(len(nums)):
    if nums[i] == 0:
        cot0+=1
    elif nums[i] == 1:
        cot1+=1
    else:
        cot2 += 1

for i in range(cot0):
    nums[i] = 0
q = cot0+cot1
for i in range(cot0, q):
    nums[i] = 1

for i in range(q, len(nums)):
    nums[i] = 2

print(nums)
"""