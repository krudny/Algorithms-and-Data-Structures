L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
W = "kokotok"

'''L = ["m","a","g","a","g","m","i","i","a"]
E = [(0,2,3),(0,1,1),(1,2,2),(1,4,5),(2,3,1),(3,4,4),(3,5,2),(4,6,1),(4,8,100),(4,7,3),(5,7,7),(5,8,1),(7,8,6) ]
W = "magia"'''

from math import inf

def create_graph(E):
    n = 0
    for edge in E: 
        n = max(n, edge[0], edge[1])
    
    n += 1

    G = [[] for _ in range(n)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))

    return G

def find(G, W): 
    n = len(G)
    m = len(W)

    DP = [[inf for _ in range(m)] for _ in range(n)]

    for i in range(len(L)):
        if L[i] == W[0]: 
            DP[i][0] = 0
    
    for i in range(m-1):
        for j in range(n):
            if DP[j][i] != inf: 
                for v, weight in G[j]: 
                    if L[v] == W[i+1]:
                        DP[v][i+1] = min(DP[v][i+1], DP[j][i] + weight)         

    res = inf

    for i in range(n): 
        res = min(DP[i][m-1], res)
    
    print(res)


def main(): 
    G = create_graph(E)
    find(G, W)

main()