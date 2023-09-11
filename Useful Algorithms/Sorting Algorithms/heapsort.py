#heapsort
T = [2,5,6,1,2,9,12,234,123,3,5,6,3,44,3]


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
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)


print(T)
heapsort(T)
print(T)






