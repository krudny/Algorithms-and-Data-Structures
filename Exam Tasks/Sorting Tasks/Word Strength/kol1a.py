from kol1atesty import runtests

def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p = q+1

def partition(T, p, r):
    if p >= r:
        return p
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def is_palindrome(s):
    n = len(s)
    i = 0
    j = n-1

    while i<j: 
        if s[i] != s[j]: return False
        i+=1
        j-=1
    return True

def g(T):
    n = len(T)
    G = []
    
    for word in T:
        G.append(word)
        if not is_palindrome(word): G.append(word[::-1])
    quicksort(G, 0, len(G)-1)
    
    max_cnt = 0
    curr_cnt = 1
    for i in range(1, len(G)):
        if G[i-1] == G[i]: 
            curr_cnt += 1
            max_cnt = max(max_cnt, curr_cnt)
        else: 
            curr_cnt = 1

    return max_cnt

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
