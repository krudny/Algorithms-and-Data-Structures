from testy import runtests

def match(A, i, j): 
    a, b = A[i]
    c, d = A[j]

    return a <= c and b >= d

def tower(A):
    n = len(A)
    DP = [1] * n

    for i in range(1, n): 
        for j in range(i): 
            if match(A, j, i): 
                DP[i] = max(DP[i], DP[j] + 1)
    return max(DP)


runtests( tower )
