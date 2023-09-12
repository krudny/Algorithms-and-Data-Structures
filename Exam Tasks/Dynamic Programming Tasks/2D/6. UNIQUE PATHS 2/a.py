# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as -1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# M = [[0,0,0,0,0,0,0], 
#      [0,0,0,0,-1,0,0], 
#      [0,-1,0,0,0,0,0]]

M = [[0,-1],[0,0]]

def unique_paths(M): 
    n = len(M) 
    m = len(M[0]) 

    DP = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n-1,-1,-1): 
        if M[i][m-1] == 0:  
            DP[i][m-1] = 1 
        else: 
            break

    for i in range(m-1,-1,-1): 
        if M[n-1][i] == 0:
            DP[n-1][i] = 1
        else: 
            break

    for i in range(m-2, -1, -1): 
        for j in range(n-2, -1, -1):
            if M[j][i] == 0: 
                DP[j][i] = DP[j+1][i] + DP[j][i+1]



    return DP[0][0]

print(unique_paths(M))