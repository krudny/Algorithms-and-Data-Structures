#mergesort
#T = [2, 5, 6, 1, 2, 9, 12, 234, 123, 3, 5, 6, 3, 44, 3]

T = [0,2,1.1,2]

def merge_sort(T):
    if len(T) > 1:
        left_T = T[:len(T)//2]
        right_T = T[len(T)//2:]

        merge_sort(left_T)
        merge_sort(right_T)

        i = 0
        j = 0
        k = 0

        while i < len(left_T) and j < len(right_T):
            if left_T[i] < right_T[j]:
                T[k] = left_T[i]
                i += 1
            else:
                T[k] = right_T[j]
                j += 1
            k += 1

        while i < len(left_T):
            T[k] = left_T[i]
            i += 1
            k += 1

        while j < len(right_T):
            T[k] = right_T[j]
            j += 1
            k += 1


merge_sort(T)
print(T)