arr = [2,3,1,1,4]

gas = 0
for n in arr:
    if gas < 0:
        print( False)
    elif n > gas:
        gas = n
    gas -= 1
    
print( True)


last_index = len(arr)
max_index = 0
if last_index == 1:print( True)
for i in range(last_index):
    if (i>max_index):print( False)
    max_index = max(max_index, i+arr[i])
    if max_index>=last_index-1:print( True)