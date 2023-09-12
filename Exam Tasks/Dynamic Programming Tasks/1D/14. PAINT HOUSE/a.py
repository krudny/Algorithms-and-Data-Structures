# There are a row of N houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a N x 3 cost matrix A.
# For example, A[0][0] is the cost of painting house 0 with color red; A[1][2] is the cost of painting house 1 with color green, and so on.
# Find the minimum total cost to paint all houses.

costs = [[17,2,17], [16,16,5], [14,3,19]]

def paint(costs): 
    n = len(costs)
    DP = [0] * 3

    for i in range(n): 
        DP[i] = costs[0][i]

    for i in range(1, n): 
        dp0 = costs[i][0] + min(DP[1], DP[2])
        dp1 = costs[i][1] + min(DP[0], DP[2])
        dp2 = costs[i][2] + min(DP[0], DP[1])
        DP = [dp0, dp1, dp2]

    return min(DP)


print(paint(costs))