from kol2testy import runtests
from math import inf
from collections import deque


def list_to_edges(G): 
    n = len(G)
    E = set()

    for i in range(n): 
        for j in range(len(G[i])): 
            if (i, G[i][j][0], G[i][j][1]) not in E and (G[i][j][0], i, G[i][j][1]) not in E:
                E.add((i, G[i][j][0], G[i][j][1]))           

    E = list(E)
    E.sort(key = lambda x:x[2])
    return E

def edge_to_list(E, a, b, n):
    A = [[] for _ in range(n)]

    for i in range(a, b): 
        A[E[i][0]].append(E[i][1])
        A[E[i][1]].append(E[i][0])

    return A

def BFS(G, s):
    n = len(G)
    visited = [0 for _ in range(n)]

    Q = deque()
    visited[s] = 1
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = 1
                Q.append(v)


    for v in visited: 
        if not v: return False
    return True

def beautree(G): 
    n = len(G)
    E = list_to_edges(G)

    for i in range(len(E) - n + 1): 
        A = edge_to_list(E, i, i+n-1, n)


        if BFS(A, E[i][0]): 
            sum = 0
            for j in range(i, i + n - 1): 
                sum += E[j][2]
            return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
