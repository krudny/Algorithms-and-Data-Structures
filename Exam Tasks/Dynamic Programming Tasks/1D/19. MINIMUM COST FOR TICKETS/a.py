# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. 
# Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

def min_cost(days, costs): 
    dp = {}

    def dfs(i): 
        if i == len(days): 
            return 0
        if i in dp: 
            return dp[i]
        
        length = 0
        dp[i] = float("inf")

        for c in range(len(costs)): 
            cost = costs[c]
            if c == 0: length = 1
            elif c == 1: length = 7
            else: length = 30

            j = i
            while j < len(days) and days[j] < days[i] + length: 
                j += 1

            dp[i] = min(dp[i], cost + dfs(j))

        return dp[i]


    return dfs(0)




print(min_cost(days, costs))