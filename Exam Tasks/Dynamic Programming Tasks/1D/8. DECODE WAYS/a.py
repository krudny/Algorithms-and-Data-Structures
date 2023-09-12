# To decode an encoded message, all the digits must be grouped then mapped back into letters using the 
#reverse of the mapping above (there may be multiple ways). 
# For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it

s = "1233245"

def decode(s): 
    dp = {len(s) : 1}

    def dfs(i): 
        if i in dp: 
            return dp[i]
        if s[i] == "0": 
            return 0
        
        res = dfs(i+1)

        if i + 1 < len(s) and s[i] == "1" or s[i] == "2" and s[i+1] in "0123456":
            res += dfs(i+2)
        
        dp[i] = res

        return res
    
    return dfs(0)

print(decode(s))