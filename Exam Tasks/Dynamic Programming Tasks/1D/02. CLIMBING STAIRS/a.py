# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def stairs(n): 
    DP = [0] * (n+1)

    DP[n-1] = 1
    DP[n-2] = 2

    for i in range(n-3, -1, -1): 
        DP[i] = DP[i+1] + DP[i+2]

    return DP[0]

print(stairs(10))