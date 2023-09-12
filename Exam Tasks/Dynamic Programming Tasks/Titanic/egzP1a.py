from egzP1atesty import runtests 
from math import inf

def convert(W, M):
    S = ""
    for char in W: 
        S += M[ord(char)-65][1]
    return S

def usable(M, D): 
    U = []
    for num in D: 
        U.append(M[num])
    return U

def titanic(W, M, D): 
    S = convert(W, M)
    U = usable(M, D)

    n = len(S)

    DP = [inf] * (n+1)
    DP[n] = 0

    for i in range(n-1, -1, -1): 
        for letter in U: 
            char, code = letter
            if (i + len(code)) <= n and S[i : i + len(code)] == code:
                DP[i] = min(DP[i], 1 + DP[i + len(code)])
    return DP[0]

runtests ( titanic, recursion=False )