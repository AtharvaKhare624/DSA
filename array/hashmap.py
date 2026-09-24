arr = [1,2,3,1,1,1,1,4,5]
maxi = 0
psum = 0 
mpp = {}
n = len(arr)
k = 3

for i in range(n):
    psum += arr[i]

    if psum == k:
        maxi = max(maxi, i+1)
    
    rem = psum - k
    if rem in mpp:
        maxi = max(maxi, i - mpp[rem])
    
    if psum not in mpp:
        mpp[psum] = i

print("max is:",maxi)