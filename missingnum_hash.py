arr = [4, 1, 2, 1, 2, 3, 4, 5, 6, 7, 6 , 7]
n = len(arr)
maxi = max(arr)
hash = (maxi+1)*[0]

for i in arr:
    hash[i]+=1

for i in arr:
    if hash[i] == 1:
        print(i)