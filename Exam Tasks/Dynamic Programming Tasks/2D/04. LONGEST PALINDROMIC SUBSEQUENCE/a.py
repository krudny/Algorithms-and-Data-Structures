# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# SOLUTION: LCS on s, and reversed s

s = "baabbbb"

def lcs(s): 
    s1 = s
    s2 = s[::-1]

    n = len(s1)

    DP = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1): 
            if s1[i] == s2[j]: 
                DP[i][j] = 1 + DP[i+1][j+1]
            else: 
                DP[i][j] = max(DP[i+1][j], DP[i][j+1])

    return DP[0][0]


print(lcs(s))