from zad4testy import runtests
from collections import deque
from math import inf

def get_path(G, parent, s, t):
    PATH = [(t, parent[t])]

    x = parent[t]

    while parent[x] != None: 
        PATH.append((x, parent[x])) 
        y = parent[x]
        x = y

    return PATH[::-1]

def BFS(G, s, t):
    n = len(G)
    distances = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [0 for _ in range(n)]

    Q = deque()

    distances[s] = 0
    visited[s] = 1
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                distances[v] = distances[u] + 1
                parent[v] = u
                visited[v] = 1
                Q.append(v)
        
        if u == t: break
    
    if distances[t] > -1: 
        return distances[t], parent
    else: 
        return inf, parent

def longer( G, s, t ):
    min_dist, parent = BFS(G, s, t)
    PATH = get_path(G, parent, s, t)
    
    for a, b in PATH: 
        G[a].remove(b)
        G[b].remove(a)
        curr_dist, _ = BFS(G, s, t)
        if curr_dist > min_dist: return((a, b))
        G[a].append(b)
        G[b].append(a)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )