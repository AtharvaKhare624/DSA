arr = [2,6,5,8,11]
t = 14
n = len(arr)
"""
BRUTE APPROCH
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if (arr[i]+arr[j] == t):
            print("index are:",i,j)"""
"""

BETTER APPROCH - HASHMAP
mpp = {}
for i in range(n):
    rem = t - arr[i]
    if rem in mpp:
        print("index are:",mpp[rem], i)
    mpp[arr[i]] = i
"""
"""OPTIMAL APPROCH - TWOPOINTER
arr.sort()
l = 0
r = n - 1
while l<r:
    s = arr[l] + arr[r]

    if s < t:
        l += 1
    elif s > t:
        r -= 1
    else:
        print("found")
        break
"""
