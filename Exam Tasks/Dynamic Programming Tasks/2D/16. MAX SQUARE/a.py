# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

M = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

def max_area(M): 
    rows, cols = len(M), len(M[0])
    cache = {}

    def helper(r,c): 
        if r >= rows or c >= cols: 
            return 0
        
        if (r, c) in cache: 
            return cache[(r,c)]

        down = helper(r + 1, c)
        right = helper(r, c + 1)
        diag = helper(r + 1, c + 1)

        cache[(r,c)] = 0

        if M[r][c] == "1": 
            cache[(r,c)] = 1 + min(down, right, diag)

        return cache[(r,c)]
    
    helper(0,0) 

    return max(cache.values()) ** 2

print(max_area(M))