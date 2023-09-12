# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.

cost = [10,15,20]

def min_cost(cost): 
    n = len(cost)
    DP = [0] * (n + 1)
    DP[n-1] = cost[n-1]

    for i in range(n-2, -1, -1): 
        DP[i] = min(DP[i+1], DP[i+2]) + cost[i]

    return min(DP[0], DP[1])

print(min_cost(cost))