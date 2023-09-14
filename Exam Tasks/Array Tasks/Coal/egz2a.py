from egz2atesty import runtests

#O(n^2), using interval trees we can get O(nlogn) time complexity

def coal( A, T ):
    n = len(A)
    M = [0] * n

    last = -1

    for i in range(n):
        j = 0
        while A[i] + M[j] > T:
            j += 1

        M[j] += A[i]
        last = j

    return last

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
