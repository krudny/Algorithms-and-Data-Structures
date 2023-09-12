O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

from math import inf

def min_cost(O, C, T, L):
    M = [(0,0), (L, 0)]

    for i in range(len(O)): 
        M.append((O[i], C[i]))
    
    M.sort()
    n = len(M)

    cache = {(0,0):inf, (0,1):inf}
    
    def dfs(i, used):
        if i == n-1: 
            return 0
        
        if (i, used) in cache and cache[((i, used))] != inf: 
            return cache[(i, used)]
        
        if used == 0: 
            for j in range(i+1, n):
                distance = M[j][0] - M[i][0]

                if distance < 2*T: 
                    res = dfs(j, 1) + M[j][1]
                    if (i, used) in cache: 
                        cache[(i, used)] = min(cache[(i, used)], res)
                    else: 
                        cache[(i, used)] = res
                else: 
                    break
            
            return cache[(i, used)]
        else: 
            for j in range(i+1, n):
                distance = M[j][0] - M[i][0]

                if distance < T: 
                    res = dfs(j, 0) + M[j][1]

                    if (i, used) in cache: 
                        cache[(i, used)] = min(cache[(i, used)], res)
                    else: 
                        cache[(i, used)] = res
                else: 
                    break

            return cache[(i, used)]
    
    dfs(0, 0)

    return min(cache[(0,0)], cache[(0,1)])
    
    
    





print(min_cost(O, C, T, L))