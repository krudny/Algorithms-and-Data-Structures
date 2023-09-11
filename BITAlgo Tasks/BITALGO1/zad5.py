'''Mamy daną tablicę, zawierającą n (n>10) liczb naturalnych w zakresie [0, k]. 
Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu. Proszę zaproponować algorytm, który posortuje tablice w czasie O(n).'''

'''Wyciągamy liczby które są spoza zakresu, i sortujemy je quicksortem, ktorego znaczenie w złożoności jest marginalne. Zakres od [0, k] 
sortujemy liniowo countingsortem, a potem mergeujemy 3 tablice'''

T = [-4363, -4259, -772, -148, 0, 0, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 6, 7, 7, 9, 10, 10, 10, 10, 12, 13, 14, 15, 15, 16, 17, 18, 18, 19, 20, 20, 20, 21, 21, 21, 21, 22, 22, 24, 24, 25, 25, 26, 29, 31, 31, 32, 32, 32, 34, 34, 35, 37, 37, 38, 38, 39, 39, 40, 40, 40, 42, 42, 43, 45, 47, 48, 48, 48, 49, 49, 49, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 52, 53, 54, 54, 54, 54, 55, 55, 55, 56, 56, 59, 59, 60, 60, 62, 62, 63, 64, 65, 65, 66, 67, 69, 69, 72, 72, 73, 73, 73, 75, 75, 75, 75, 77, 78, 78, 78, 79, 79, 79, 80, 80, 82, 83, 83, 84, 85, 86, 87, 87, 87, 87, 88, 88, 88, 90, 90, 91, 91, 91, 92, 93, 93, 93, 94, 94, 95, 95, 95, 96, 96, 97, 97, 97, 98, 99, 99, 99, 100, 100, 100, 100, 3705, 5493, 5608, 8155, 9006, 9984]

def counting_sort(T, k):
    n = len(T)
    C = [0] * k
    B = [0] * n

    for i in range(len(T)):
        C[T[i]] += 1
    
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1, -1, -1):
        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1

    return B

def quicksort(T, p, r):
    if p < r: 
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        quicksort(T, q+1, r)

    return T

def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1
 
def sort(T, k): 
    A = [] #<0
    B = [] #[0, k]
    C = [] #>k
    
    for num in T:
        if 0 <= num <= k: B.append(num)
        elif num < 0: A.append(num)
        else: C.append(num)

    A = quicksort(A, 0, len(A)-1)
    B = counting_sort(B, k + 1)
    C = quicksort(C, 0, len(C)-1)

    return A+B+C
    


def main():
    res = sort(T, 100)
    print(res)
    
main()