nums = [29,47,21,41,13,37,25,7]
maxi = max(nums)
hash_m = [0] * (maxi+1)

element = 0
freq = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        hash_m[nums[i]] += 1

for i in range(len(hash_m)):
    if hash_m[i] > freq:
        freq = hash_m[i]
        element = i
        
    elif hash_m[i] == freq:
        element = min(element , i)

if freq == 0:
    freq = -1
    element = "no element"

print("freq:",freq,"element:",element)