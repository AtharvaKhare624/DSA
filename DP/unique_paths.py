obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

def unique(i, j, dp):
    if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:return 0
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = unique(i-1, j, dp)
    left = unique(i, j-1, dp)

    count = up+left
    dp[i][j] = count
    return dp[i][j]

m = len(obstacleGrid)
n = len(obstacleGrid[0])
dp = [[-1] * n for _ in range(m)]
print(unique(m-1, n-1, dp))