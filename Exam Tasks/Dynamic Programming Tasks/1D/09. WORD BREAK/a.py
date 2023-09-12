# Given a string s and a dictionary of strings wordDict, return true if s can 
# be segmented into a space-separated sequence of one or more dictionary words.

s = "applepenapple"
wordDict = ["apple","pen"]

def word_break(s, wordDict):
    n = len(s)
    DP = [False] * (n+1)
    DP[n] = True

    for i in range(n-1, -1, -1): 
        for word in wordDict:        
            if i + len(word) <= n and s[i:i+len(word)] == word: 
                DP[i] = DP[i+len(word)]

    return DP[0]


print(word_break(s, wordDict))