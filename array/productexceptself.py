arr = [5, 2, 3, 4]
n = len(arr)

output = [1] * n

# Left products
left = 1
for i in range(n):
    output[i] = left
    left *= arr[i]

# Right products
right = 1
for i in range(n - 1, -1, -1):
    output[i] *= right
    right *= arr[i]

print(output)