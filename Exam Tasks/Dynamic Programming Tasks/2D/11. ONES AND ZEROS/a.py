# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.

m = 5
n = 3

strs = ["10","0001","111001","1","0"]

def count(m, n): 
    dp = {}

    def dfs(i, m, n):
        if i == len(strs): 
            return 0
        if (i, m, n) in dp: 
            return dp[(i, m, n)]
        

        mCNT, nCNT = strs[i].count("0"), strs[i].count("1")
        dp[(i, m, n)] = dfs(i+1, m, n)
        
        if mCNT <= m and nCNT <= n: 
            dp[(i,m,n)] = 1 + max(dfs(i+1, m - mCNT, n - nCNT), dp[(i, m, n)])
        
        return dp[(i, m, n)]
    
    return dfs(0, m, n)


print(count(m, n))