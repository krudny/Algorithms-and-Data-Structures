s1 = "dff"
s2 = "ace"

def lcs(s1, s2): 
    n = len(s1)
    m = len(s2)

    DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1): 
            if s1[i] == s2[j]: 
                DP[i][j] = 1 + DP[i+1][j+1]
            else: 
                DP[i][j] = max(DP[i+1][j], DP[i][j+1])

    return DP[0][0]


print(lcs(s1, s2))