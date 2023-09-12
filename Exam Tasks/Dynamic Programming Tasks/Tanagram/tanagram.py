x = "kamilaaaa"
y = "mkalaiaaa"
t = 2

def tanagram(x, y, t): 
    if len(x) != len(y): return False

    n = len(x)
    A = [0] * 26

    for i in range(n): 
        A[ord(x[i]) - 97] += 1
        A[ord(y[i]) - 97] -= 1
    
    for i in range(26): 
        if A[i] != 0: return False


    for i in range(t + 1): 
        A[ord(x[i]) -  97] += 1


    i = 0
    start = i - t
    end = i + t
    
    while i < n: 
        if start < 0: 
            start = 0
        if end > n - 1: 
            end = n - 1
        
        if A[ord(y[i]) - 97] == 0: return False
        
        i += 1
        start = i - t
        end = i + t

        if start > 0: 
            A[ord(x[start - 1]) - 97] -= 1
        if end < n: 
            A[ord(x[end]) - 97] += 1
        
    return True
        


def main(): 
    print(tanagram(x, y, t))

main()