'''Dane są 2 zbiory o wielkościach m i n gdzie m jest znacznie mniejsze niż n. Sprawdzić czy zbiory są rozłączne'''
'''Sortujemy mniejszą tablice quicksortem, a potem dla kazdego elementu sprawdzamy binary searchem czy jest w duzej tablicy'''

M = [1, 2, 6, 2, 1, 7, 3]
N = [0, 5, 5, 4, -4, 12, 2]

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

def binary_search(array, low, high, x):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

    
def are_disjoint(M, N): 
    quicksort(M, 0, len(M)-1)
    for item in N: 
        if binary_search(M, 0, len(M)-1, item) != -1: return False
    return True


def main(): 
    print(are_disjoint(M, N))

main()