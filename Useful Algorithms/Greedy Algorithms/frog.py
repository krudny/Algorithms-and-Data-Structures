#Frog has to move from 0 to n-1 and on i'th position has certain amount of energy. It requires j energy to move to i+j position.

A = [10,0,0,0,0,0,0,0,0,0,1,0]

def zbigniew(L): 
    n = len(L)
    l = r = 0
    res = 0

    while r < n:
        distance = 0
        for i in range(l, r + 1): 
            for jump in range(1, min(i + L[i], n-1)): 
                if i + jump < n - 1: 
                   L[i+jump] = max(L[i + jump], L[i + jump] + L[i] - jump)   
            distance = max(distance, i + L[i])

        l = r + 1
        r = distance
        res += 1
    
    return res 

print(zbigniew(A))