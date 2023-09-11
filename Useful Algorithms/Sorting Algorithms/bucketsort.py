#bucket
T = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]


def insert_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucket_sort(T):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])

    for item in T:
        arr[int(slot_num * item)].append(item)

    for i in range(slot_num):
        arr[i] = insert_sort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            T[k] = arr[i][j]
            k += 1
    return T


print(bucket_sort(T))