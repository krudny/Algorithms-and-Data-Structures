A = [3,4,5,2,3,4,12,1,3,1,1]

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

print(select(A, 0, len(A) - 1, 5))
A.sort()
print(A)