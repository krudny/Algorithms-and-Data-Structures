''' Mamy 2n liczb, łaczymy je w n par, szukamy takich par, ze ich maksymalna suma w parze bedzie najmniejsza'''
'''quickujemy, a potem laczymy z lewej i prawej elementy'''

A = [2,4,5,10,22,1,17,16,15,7,3,4]

def quicksort(A, p, r): 
    if p < r: 
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r): 
    x = A[r]
    i = p - 1
    for j in range(p,r): 
        if A[j] <= x: 
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

def make_pairs(A):
    B = []
    i = 0
    j = len(A) - 1
    max_def = 0

    while i < j: 
        max_def = max(max_def, A[j] - A[i])
        B.append((A[i], A[j]))
        i+=1
        j-=1

    print(B, max_def)


def main():
    quicksort(A, 0, len(A)-1)
    make_pairs(A)

main()