# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.

#SOLUTION: LIS implementation if b > c on sorted array

pairs = [[1,2],[2,3],[3,4]]

def chain(pairs): 
    n = len(pairs)
    pairs.sort()
    DP = [1] * n

    for i in range(1, n): 
        for j in range(i): 
            if pairs[i][0] > pairs[j][1]: 
                DP[i] = max(DP[i], DP[j] + 1)

    return DP[-1]


print(chain(pairs))