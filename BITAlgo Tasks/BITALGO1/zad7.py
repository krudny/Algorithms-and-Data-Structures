'''Dana jest tablica zawierająca n liczb z zakresu [0, n^2-1]. Napisz algorytm który posortuje tablice w czasie O(n)'''

A = [8173, 3019, 1257, 5558, 1578, 1070, 1862, 3323, 6892, 1612, 1225, 2178, 9447, 4971, 1828, 1038, 7383, 7431, 5888, 4325, 5272, 1147, 2880, 1921, 9154, 9397, 8041, 6227, 7171, 4767, 1782, 8107, 2541, 2641, 2076, 462, 5813, 6025, 3230, 8060, 8753, 7015, 3306, 7594, 1654, 6543, 5910, 5198, 9417, 6469, 5403, 863, 5328, 2693, 5835, 3491, 639, 1231, 5177, 952, 1634, 3802, 9045, 1952, 6316, 3884, 8045, 3799, 7613, 3679, 4861, 6555, 6698, 6722, 4824, 2257, 3262, 6098, 9408, 8306, 2777, 529, 3730, 2686, 7559, 3283, 3695, 7234, 2997, 567, 7735, 8800, 4342, 8641, 3569, 9310, 5784, 9038, 9673, 1797]

def counting_sort(A, col_idx):
    n = len(A)
    output = [None] * n
    count = [0] * 10

    for i in range(n):
        if A[i]
   

def radix(A):
    max_len = len(str(max(A)))

    for i in range(len(A)):
        A[i] = str(A[i])


    for col_idx in range(max_len-1, -1, -1):
        counting_sort(A, col_idx)
    
    for row in A:
        print(row)

def main():
    radix(A)

main()