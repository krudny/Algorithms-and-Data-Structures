from kol1btesty import runtests

def counting(word):
    n = len(word)
    count = [0] * 27
    output = [0] * n

    for i in range(n):
        letter = ord(word[i]) - ord('a')
        count[letter] += 1
   
    for i in range(1,27):
        count[i] = count[i] + count[i-1]

    for i in range(n-1, -1, -1):
        letter = ord(word[i]) - ord('a')
        output[count[letter]-1] = word[i]
        count[letter] -= 1
    
    s = ''

    for i in range(n):
        s += output[i]

    return s

def counting_sort(A, col):
    n = len(A)
    count = [0] * 27
    output = [0] * n

    for i in range(n):
        if col < len(A[i]): 
            letter = ord(A[i][col]) - ord('a')
        else:
            letter = 0
        count[letter] += 1

    for i in range(1,27):
        count[i] = count[i] + count[i-1]

    for i in range(n-1, -1, -1):
        if col < len(A[i]):
            letter = ord(A[i][col]) - ord('a')
            output[count[letter]-1] = A[i]
            count[letter] -= 1
        else: 
            output[count[0] - 1] = A[i]
            count[0] -= 1

    for i in range(n): 
        A[i] = output[i]

def radix_sort(A): 
    n = len(A)
    max_len = 0

    for word in A:
        max_len = max(max_len, len(word))
    
    for col in range(max_len, -1, -1):
        counting_sort(A, col)

def f(T):
    for i in range(len(T)):
        T[i] = counting(T[i])

    radix_sort(T)
    
    curr = 1
    max_len = 0

    for i in range(1,len(T)):
        if T[i-1] == T[i]: 
            curr+=1
            max_len = max(max_len, curr)
        else: 
            curr = 1
    return max_len


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
