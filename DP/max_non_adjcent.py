def funct(i,dp):
    if i == 1: return nums[0]
    if i < 1: return 0
    if dp[i]!=-1 : return dp[i]

    summ1 = funct(i-2,dp) + nums[i-1]
    summ2 = funct(i-1,dp)

    maxi = max(summ1,summ2)
    dp[i] = maxi

nums = [1,2,3,1]
n = len(nums)
dp = [-1]*(n+1)
funct(n,dp)
print( dp[n])