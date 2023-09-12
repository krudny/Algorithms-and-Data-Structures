# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

grid = [[1,3,1],[1,5,1],[4,2,1]]

def min_path(grid): 
    n = len(grid)
    m = len(grid[0])

    DP = [[0 for _ in range(m)] for _ in range(n)]

    DP[0][0] = grid[0][0]

    for i in range(1, n): 
        DP[i][0] = grid[i][0] + DP[i-1][0]

    for i in range(1, m): 
        DP[0][i] = grid[0][i] + DP[0][i-1]

    for i in range(1, n): 
        for j in range(1, m): 
            DP[i][j] = grid[i][j] + min(DP[i][j-1], DP[i-1][j])

    return DP[n-1][m-1]

print(min_path(grid))