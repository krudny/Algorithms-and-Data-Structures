# There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, 
# return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

piles = [[1,100,3],[7,8,9]]
k = 2

def maximize(piles, k): 
    n = len(piles)
    dp = {}

    def dfs(i, coins): 
        if i == n: 
            return 0

        dp[(i, coins)] = dfs(i + 1, coins)
        curPile = 0

        for j in range(min(coins, len(piles[i]))):
            curPile += piles[i][j]
            dp[(i, coins)] = max(dp[(i, coins)], curPile + dfs(i+1, coins - j - 1)) 

        return dp[(i, coins)]

    return dfs(0, k)

print(maximize(piles, k))