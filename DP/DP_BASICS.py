# MEMOIZATION

# def f(n, dp):
#     if n<=1:return n

#     if dp[n] != -1:return dp[n]

#     dp[n] = f(n-1,dp)+f(n-2,dp)
#     return dp[n]

# i = int(input())
# dp = [-1]*(i+1)

# print(f(i,dp))
# print(dp)

# TABULATION

# i = int(input())
# dp = [-1]*(i+1)
# dp[0] = 0
# dp[1] = 1

# for i in range(2,i+1):
#     dp[i] = dp[i-1]+dp[i-2]

# print(dp)

# SPACE OPTI

i = int(input())
prev2,prev = 0,1

for i in range(2,i+1):
    n = prev+prev2
    prev2= prev
    prev= n
print(n)