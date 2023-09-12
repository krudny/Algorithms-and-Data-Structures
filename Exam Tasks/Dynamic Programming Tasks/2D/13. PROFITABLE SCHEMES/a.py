# There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] 
# and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.
# Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, 
# and the total number of members participating in that subset of crimes is at most n.
# Return the number of schemes that can be chosen

n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]

def profit_schemes(n, minProfit, group, profit): 

    dp = {}

    def dfs(i, n, p): 
        if i == len(group): 
            return 1 if p >= minProfit else 0 
        
        if (i, n, p) in dp:
            return dp[(i,n,p)]
        
        dp[(i,n,p)] = dfs(i+1, n, p)
        if n - group[i] >= 0: 
            dp[(i,n,p)] += dfs(i+1, n - group[i], p + profit[i])
        
        return dp[(i,n,p)]
    
    return dfs(0, n, 0)



print(profit_schemes(n, minProfit, group, profit))