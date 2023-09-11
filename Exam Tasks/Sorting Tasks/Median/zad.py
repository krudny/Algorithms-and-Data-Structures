T = [[2, 5, 2, 5], [2, 5, 5, 2], [2, 5, 2, 2], [2, 5, 5, 5]]

from testy import random_tests

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

def median(T): 
    n = len(T)
    A = [] * (n ** 2) 

    for i in range(n): 
        for j in range(len(T[i])):
            A.append(T[i][j])

    a = ((n * n) - n) // 2
    b = a + n - 1

    select(A, 0, len(A) - 1, a)
    select(A, 0, len(A) - 1, b)

    row = 0
    col = 0

    for i in range(a, b + 1): 
        T[row][col] = A[i]
        row += 1
        col += 1

    row = 0
    col = 1

    for i in range(b + 1, n**2): 
        T[row][col] = A[i]
        col += 1
        if col == n: 
            row += 1
            col = row + 1
    
    row = 1
    col = 0
    cnt = 1

    for i in range(0, a): 
        T[row][col] = A[i]
        col += 1
        
        if col == cnt: 
            row += 1
            col = 0
            cnt += 1
    
    return T
        


random_tests(median, samples=25, size=(1, 25))