#Minimalny koszt przejścia z 0,0 na m-1, n-1 ruszając sie tylko prawo i dół. 
T = [[3, 4, 5, 2, 1], 
     [7, 2, 13, 7, 8], 
     [3, 1, 4, 1, 5], 
     [2, 8, 11, 1, 3], 
     [3, 5, 1, 3, 2]]

def min_cost(T, m, n):
    DP = [[0 for i in range(m)] for i in range(n)]

    DP[0][0] = T[0][0]

    for i in range(1,m): 
        DP[0][i] = DP[0][i-1] + T[0][i]

    for i in range(1,n):
        DP[i][0] = DP[i-1][0] + T[i][0]

    for i in range(1, n): 
        for j in range(1, m): 
            DP[i][j] = min(DP[i][j-1], DP[i-1][j])+T[i][j]

    return DP[m-1][n-1]     

    



def main(): 
    print(min_cost(T, 5, 5))

main()