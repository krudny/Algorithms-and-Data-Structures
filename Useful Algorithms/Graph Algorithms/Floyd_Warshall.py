import copy
from math import inf 

G = [[inf, 2, inf, inf, inf],
[2, inf, 3, inf, inf],
[inf, 3, inf, inf, inf],
[inf, inf, inf, inf, 1],
[inf, inf, inf, 1, inf]]

def floyd_warshall(G):
    n = len(G)
    W = copy.deepcopy(G)
    
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]
                    
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = -inf
                
    return W

print(floyd_warshall(G))