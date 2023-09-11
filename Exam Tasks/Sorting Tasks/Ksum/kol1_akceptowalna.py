from kol1testy import runtests

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x: 
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1

def select(A, p, r, k):
    if p == r: 
        return A[p]
    
    q = partition(A, p, r)

    if q == k: return A[q]
    if q > k: return select(A, p, q-1, k)
    else: return select(A, q+1, r, k)

def ksum(T, k, p):
    n = len(T)
    suma = 0
    for i in range(n-p+1):
        suma += select(T[i:i+p], 0, p-1, p-k)

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
