arr  = [1,2,-4,-5 , 5,3,-6,-7]
f_arr  = [0 *len(arr)]
n = len(arr)
# BRUTE SOLUTION
pos = []
neg = []
# to create both lists of pos and neg
for i in range(len(arr)):
    if arr[i] > 0 :
        pos.append(arr[i])
    else:
        neg.append(arr[i])

# to create final answer

for i in range (n//2):
    f_arr[2 * i] = pos[i]
    f_arr[2 * i +1] = neg[i]

print(f_arr)
