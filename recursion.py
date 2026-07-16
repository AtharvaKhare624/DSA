'''
def f(i, n):
    if i < 1:
        return
    f(i-1, n)
    print(i)
n = 3
f(n, n)
'''


"""PARAMETARIZE RECURSION
def f(i, sum):
    if (i < 1):
        print(sum)
        return

    f(i-1, sum+i)

f(3,0)
"""

"""
def f(i, n):
    if i == 0:
        return
    f(i-1, n)
    print(i)

f(3, 3)
"""
"""
REVERSE A ARRAY
arr = [1,2,3,5,4]

def f(i ,n):
    if i>=n:
        return arr
    arr[i], arr[n] = arr[n], arr[i]
    return f(i+1, n-1)
print(f(0, len(arr)-1))


arr1 = [1,2,3,5,4]
def fa(i, n):
    if i >= n/2:
        return arr1
    arr1[i], arr1[n-i-1] = arr1[n-i-1], arr1[i]
    return fa(i+1, n)
n=len(arr1)
print(fa(0, n))
"""
"""fibonacci number
def f(n):
    if n <= 1: return n

    return f(n-1) + f(n-2)

print(f(5))
"""
arr = []
nums = [3,1,2]
def f(i, arr, nums):
    if i >= 3:
        print (arr)
        return
    
    arr.append(nums[i])
    f(i+1, arr, nums)
    arr.pop()
    f(i+1, arr, nums)

f(0, arr, nums)