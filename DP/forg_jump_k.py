def frog(n,dp):
    if n == 0:
        return 0
    if dp[n] != -1: return dp[n]
    ns1 = float("inf")
    for i in range(1,k+1):
        if n > i:
            ns = frog(n-i,dp) + abs(arr[n]-arr[n-i])
            ns1 = min(ns1,ns)

    dp[n] = ns1
    return dp[n]

arr = [10,30,60,10,50,10]
k = 3
no = 6
dp = [-1]*(no+1)
print(frog(no-1,dp))
