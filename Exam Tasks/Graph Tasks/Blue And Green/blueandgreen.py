from math import inf 
import collections

T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ["B", "B", "G", "G", "B"]
D = 2

#------------------------------------
G1 = [
      [0, 1, 1, 0, 1],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 0, 1],
      [0, 1, 0, 0, 1],
      [1, 0, 1, 1, 0],
     ]
K1 = ['B', 'B', 'G', 'G', 'B']
D1 = 2
R1 = 2
T1 = [G1, K1, D1, R1]
#------------------------------------
G2 = [
      [0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0],
     ]
K2 = ['B', 'G', 'G', 'B']
D2 = 1
R2 = 2
T2 = [G2, K2, D2, R2]
#------------------------------------
G3 = [
      [0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0],
     ]
K3 = ['B', 'G', 'G', 'B']
D3 = 2
R3 = 0
T3 = [G3, K3, D3, R3]
#------------------------------------
G4 = [
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 1, 1],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
     ]
K4 = ['G', 'B', 'G', 'G', 'G', 'G', 'B', 'G']
D4 = 3
R4 = 2
T4 = [G4, K4, D4, R4]
#------------------------------------

TESTS = [ T1, T2, T3, T4 ]

def runtests(f):
    OK = True
    for T in TESTS:
        print("-----------------------------------------")
        print("Dane:")
        res = f(T[0], T[1], T[2])
        print("Oczekiwany rezultat: {}, Wynik: {}".format(T[3], res))

        if res != T[3]:
            print("Blad!")
            OK = False
        else:
            print("OK")
    print("-----------------------------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")

def floyd_warshall(G):
    n = len(G)
    W = [[inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]:
                W[i][j] = G[i][j]
            elif i == j:
                W[i][j] = 0

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    return W

def create_graph(T, DIST, K, D):
    n = len(T) 
    G = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(n): 
        for j in range(n): 
            if DIST[i][j] >= D and K[i] != K[j]: 
                G[i][j] = 1
    
    for j in range(len(K)):
        if K[j] == "B": 
            G[n][j] = 1
        else: 
            G[j][n+1] = 1


    return G

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = inf
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

def BlueAndGreen(T, K, D):
    DIST = floyd_warshall(T)
    G = create_graph(T, DIST, K, D)
    max_flow = edmonds_karp(G, len(T), len(T)+1)
    
    return max_flow

runtests(BlueAndGreen)