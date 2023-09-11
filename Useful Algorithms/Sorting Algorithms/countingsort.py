#counting
T = [2, 5, 6, 1, 2, 9, 12, 234, 123, 3, 5, 6, 3, 44, 3]

def counting_sort(T, k):
    n = len(T)
    C = [0] * k
    B = [0] * n

    for item in T:
        C[item] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[T[i]]-1] = T[i]
        C[T[i]] -= 1
    for i in range(n):
        T[i] = B[i]


print(T)
counting_sort(T, 235)
print(T)