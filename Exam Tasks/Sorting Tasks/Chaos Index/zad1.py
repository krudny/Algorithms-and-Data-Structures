from testy import runtests

def merge_sort(T, col):
    if len(T) <= 1:
        return T
    
    mid = len(T) // 2
    left_half = T[:mid]
    right_half = T[mid:]
    
    left_half = merge_sort(left_half, col)
    right_half = merge_sort(right_half, col)
    
    result = []
    i = j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i][col] <= right_half[j][col]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result

def chaos_index( T ):
    n = len(T)

    for i in range(n): 
        T[i] = (T[i], i)

    T = merge_sort(T, 0)

    k = 0

    for i in range(n): 
        k = max(k, abs(T[i][1] - i))

    return k


runtests( chaos_index )
