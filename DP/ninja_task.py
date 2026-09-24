matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]

def ninja(day, last, dp):
    if day == 0:
        maxi = 0
        for i in range(len(matrix[0])):
            if i != last:
                maxi = max(maxi, matrix[0][i])
        return maxi
    if dp[day][last] != -1:return dp[day][last]

    maxi = 0
    for j in range(len(matrix[0])):
        if j != last:
            maxi = max(maxi, matrix[day][j]+ninja(day-1, j, dp))
    dp[day][last] = maxi
    return dp[day][last]

dp = [[-1] * 4 for _ in range(len(matrix))]
print(ninja(2, 3, dp))
