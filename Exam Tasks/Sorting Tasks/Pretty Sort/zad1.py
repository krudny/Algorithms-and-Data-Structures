'''Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych'''

T = [794772, 933488, 441001, 42450, 271493, 536110, 509532, 424604, 962838, 821872, 870163, 318046]

def counting_sort_by_index_desc(T, index):
    n = len(T)
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        count[T[i][index]] += 1
    

    for i in range(8, -1, -1): 
        count[i] = count[i+1] + count[i]
    
    for i in range(n-1, -1, -1):
        digit = T[i][index]
        output[count[digit]-1] = T[i]
        count[digit] -= 1
    
    for i in range(n): 
        T[i] = output[i]

def counting_sort_by_index_asc(T, index):
    n = len(T)
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        count[T[i][index]] += 1
    

    for i in range(1,10): 
        count[i] = count[i-1] + count[i]
    
    for i in range(n-1, -1, -1):
        digit = T[i][index]
        output[count[digit]-1] = T[i]
        count[digit] -= 1
    
    for i in range(n): 
        T[i] = output[i]

def count(T): 
    n = len(T)

    for i in range(n):
        num_copy = T[i] 
        A = [0] * 10
        single = 0 
        repeated = 0

        while num_copy > 0: 
            digit = num_copy % 10
            num_copy //= 10
            A[digit] += 1

        for digit in A: 
            if digit == 1: single += 1
            elif digit > 2: repeated += 1
        
        T[i] = (T[i], single, repeated)

def pretty_sort(T):
    count(T)
    counting_sort_by_index_asc(T, 2)
    counting_sort_by_index_desc(T, 1)

    for i in range(len(T)):
        T[i] = T[i][0]
   
    print(T)


def main():
    pretty_sort(T)

main()