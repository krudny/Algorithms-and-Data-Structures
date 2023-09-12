# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# Order doesnt matter

amount = 5
coins = [1,2,5]

def coin_change(coins, amount): 
    dp = {}

    def dfs(i, sum): 
        if i >= len(coins): 
            return 0
        if (i, sum) in dp: 
            return dp[(i, sum)]
        if sum > amount: 
            return 0
        if sum == amount: 
            return 1
        
        dp[(i, sum)] = dfs(i+1, sum) + dfs(i, sum + coins[i])

        return dp[(i, sum)]
    
    return dfs(0,0)
        




print(coin_change(coins, amount))