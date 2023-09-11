#Mergesort by index, stable

T = [(2,3), (1,5), (1,3), (4,6), (6,2), (8,6), (5,9), (0,0)]

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

print(merge_sort(T,1))