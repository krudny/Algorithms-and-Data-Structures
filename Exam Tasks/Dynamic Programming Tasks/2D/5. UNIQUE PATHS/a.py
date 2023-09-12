# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

m = 3
n = 7

def unique_paths(m, n): 
    DP = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m): 
        DP[i][n-1] = 1

    for i in range(n):
        DP[m-1][i] = 1

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1): 
            DP[i][j] = DP[i+1][j] + DP[i][j+1]


    for row in DP: 
        print(row)



print(unique_paths(m, n))