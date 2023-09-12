# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# We use bottom up technique to determine how much coins do we need to use to make i amount

from math import inf 

coins = [1,2,3,4,5]
amount = 7

def coins_change(coins, amount):
    DP = [inf] * (amount + 1)
    DP[0] = 0

    for i in range(1, amount + 1): 
        for coin in coins: 
            DP[i] = min(DP[i], 1 + DP[i - coin])

    return DP[-1] if DP[-1] != inf else -1
    


print(coins_change(coins, amount))