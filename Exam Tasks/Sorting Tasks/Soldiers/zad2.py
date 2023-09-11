''' Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie'''

T = [3,4,12,1,2,3,4,5,6,7,2,3,4,5,5]

def partition(T, p, r):
    x = T[r]
    i = p-1

    for j in range(p,r):
        if T[j] <= x: 
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    
    return i+1
        
def select(T, p,r,k):
    if p == r: 
        return T[p]
    else: 
        q = partition(T, p, r)

        if q == k: return T[q]
        if q > k: return select(T, p, q-1, k)
        else: return select(T, q+1, r, k)

def selection(T, p, q):
    n = len(T)
    select(T,0, n-1, p)
    select(T, p, n-1, q)
 
    print(T[p:q+1])

def main():
    selection(T,3,7)

main()