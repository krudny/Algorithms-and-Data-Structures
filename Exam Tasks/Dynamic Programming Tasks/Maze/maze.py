L = [   "....",
        "..#.",
        "..#.",
        "...." ]

from math import inf

def maze(L): 
    n = len(L)
    DP = [[[inf for _ in range(n)] for _ in range(n)] for _ in range(n)]

    def dfs(r, c, last_move, from_where): 
        if r == n-1 and c == n-1: 
            return 0
        
        if r < 0 or c < 0 or r >= n or c >= n or L[r][c] == '#': 
            return -1

        if DP[from_where][r][c] != inf: 
            return DP[from_where][r][c]
            

        if last_move == "up": 
            max_value = max(dfs(r-1, c, "up", 0), dfs(r, c+1, "right", 2))

            DP[from_where][r][c] = max_value + 1 if max_value != -1 else -1

            return DP[from_where][r][c]
        
        if last_move == "down": 
            max_value = max(dfs(r+1, c, "down", 1), dfs(r, c+1, "right", 2))

            DP[from_where][r][c] = max_value + 1 if max_value != -1 else -1

            return DP[from_where][r][c]
        
        if last_move == "right": 
            max_value = max(dfs(r-1, c, "up", 0), dfs(r+1, c, "down", 1), dfs(r, c+1, "right", 2))

            DP[from_where][r][c] = max_value + 1 if max_value != -1 else -1

            return DP[from_where][r][c]
        
    dfs(0,0,"down",0)

    return DP[0][0][0]



print(maze(L))
