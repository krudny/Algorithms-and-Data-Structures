from egz1atesty import runtests

def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return int(i-1/2)

def heapify(T, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r

    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, max_ind, n)

def build_heap(T):
    n = len(T)

    for i in range(parent(n-1), -1, -1):
        heapify(T, i, n)

def heapsort(T):
    n = len(T)
    build_heap(T)
    cnt = 0
    snow = 0
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)
        if T[i] - cnt <= 0: return snow
        snow = snow + T[i] - cnt
        cnt+=1

def snow( S ):
    return heapsort(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
