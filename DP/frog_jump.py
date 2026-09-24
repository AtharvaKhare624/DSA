# def frog(i):
#     if i == 0: return 0
#     if dp[i]!=-1: return dp[i]

#     jump1 = frog(i-1) + abs(arr[i]-arr[i-1])
#     jump2 = float("inf")
#     if i>1:
#         jump2 = frog(i-2) + abs(arr[i]-arr[i-2]) 
#     dp[i] = min(jump1, jump2)
#     return min(jump1, jump2)

arr = [30,10,60,10,60,50]
n = 6
# dp = [-1]*(n+1)
# print(frog(n-1))

# dp[0] = 0

# for i in range(1,len(arr)):
#     fs = dp[i-1] + abs(arr[i]-arr[i-1])
#     ss = float("inf")
#     if i > 1:
#         ss = dp[i-2] + abs(arr[i]-arr[i-2])
#     dp[i] = min(fs,ss)

# print(dp[n-1])

prev = 0
prev2 = 0

for i in range(1,len(arr)):
    fs = prev + abs(arr[i]-arr[i-1])
    ss = float("inf")
    if i>1:
        ss = prev2 + abs(arr[i]-arr[i-2])

    prev2 = prev
    prev = min(fs,ss)

print(prev)