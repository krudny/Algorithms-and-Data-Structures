# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

word1 = "horse"
word2 = "ros"

def edit(w1, w2): 
    dp = {}

    def dfs(l, r): 
        if l == 0: 
            return r
        
        if r == 0: 
            return l
        
        if (l, r) in dp: 
            return dp[(l, r)]
        
        if w1[l-1] == w2[r-1]: 
           dp[(l, r)] = dfs(l-1, r-1)
        else: 
            dp[(l, r)] = min(1 + dfs(l, r-1), 1 + dfs(l-1, r), 1 + dfs(l-1, r-1))

        return dp[(l, r)]

    return dfs(len(w1), len(w2))
         

            
        
        




print(edit(word1, word2))