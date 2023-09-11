# A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycje. 
# Należy policzyć, na ile sposobów mogę przejść z pozycji 0 na n-1. 

A = [10, 6, 4, 4, 9, 10, 2, 3, 3, 6, 7, 7]

def amazon_stairs(A): 
    n = len(A)
    DP = [0] * n
    DP[n-1] = 1

    for i in range(n-2, -1, -1):
        for j in range(1, A[i]+1):
            if i+j < n: 
                DP[i] += DP[i+j]

    return DP[0]


def main():
    print(amazon_stairs(A))

main()