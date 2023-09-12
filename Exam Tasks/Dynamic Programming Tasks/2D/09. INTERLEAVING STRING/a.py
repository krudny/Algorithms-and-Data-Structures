# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
# substrings
# respectively, such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

def string(s1, s2, s3): 
    dp = {}

    def dfs(l, r):         
        if l == len(s1) and r == len(s2): 
            return True
        
        if (l, r) in dp: 
            return dp[(l,r)]
        
        if l < len(s1) and s1[l] == s3[l+r] and dfs(l+1, r): 
            return True

        if r < len(s2) and s2[r] == s3[l+r] and dfs(l, r+1): 
            return True

       
        dp[(l, r)] = False
        
        return False

    return dfs(0,0)
    


print(string(s1, s2, s3))