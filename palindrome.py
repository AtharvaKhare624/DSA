x = 121
arr = []

for i in str(x):
     arr.append(i)
def isPalindrome(arr):
        half = len(arr)//2
        for i,j in zip(range(half),range(len(arr)-1,-1,-1)):
            if(arr[i]!=arr[j]):
                return False
        return True

print(isPalindrome(arr))