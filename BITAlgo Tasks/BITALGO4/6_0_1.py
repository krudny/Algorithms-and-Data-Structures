#Liczba ciągów binarnych o długości n bez jedynek obok siebie. 
def count(n):
    DP = [0] * n
    DP[0] = 1
    DP[1] = 2
    DP[2] = 3

    for i in range(3,n):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP[n-1])


def main():
    count(10)

main()