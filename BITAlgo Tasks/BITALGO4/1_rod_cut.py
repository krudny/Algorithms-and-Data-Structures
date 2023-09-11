# Firma kupuje stalowe pręty o długości n i tnie je na kawałki, 
# które sprzedaje, Dla kawałka o długości i metrów jest podana cena 
# sprzedaży T[i]. Zmaksymalizuj zysk z pocięcia pręta. 

T = [0, 1, 3, 6, 7, 9]
# = [0, 1, 2, 3, 4, 5]

# tniemy 1 i sprawdzamy i-1
# tniemy 2 i sprawdzamy i-2
# tniemy 3 i sprawdzamy i-3

def rod_cut(T): 
    n = len(T)
    DP = [0] * n
    DP[0] = 0
    DP[1] = T[1]

    for i in range(1,n):
        DP[i] = T[i]
        for j in range(1, i):
            DP[i] = max(DP[i], T[j] + DP[i-j])
    
    print(DP[n-1])

def main():
    rod_cut(T)

main()