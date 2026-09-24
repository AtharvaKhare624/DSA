arr = [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1]
maxi = 0
count = 0
'''i = 0
while i<len(arr):
    if arr[i] == 1:
        count +=1
    if arr[i] == 0:
        if count>max:
            max = count
        count = 0
       
    
    i+=1
if count>max:
    max = count

print(f"max is :{max}")'''

for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
        maxi = max(count, maxi)
    else:
        count = 0
    
print(maxi)