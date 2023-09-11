from testy import runtests
from queue import PriorityQueue
from math import inf

def dijkstry(G, s,t):
    n = len(G)
    parents = [None] * n
    distances = [inf] * n
    pq = PriorityQueue()
    distances[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parents[v] = u
                pq.put((distances[v], v))
                
    return distances[t]



def create_graph(G): 
    n = len(G)
    M = [[] for _ in range(2*n)]

    for i in range(n): 
        s1, s2 = 2*i, 2*i+1
        for j in range(n): 
            e1, e2 = 2*j, 2*j+1
            if G[i][j] != 0: 
                M[s1].append((e1, G[i][j]))
                if i <= j: 
                    M[s2].append((e1, G[i][j]))

        
        for j in range(n): 
            if G[i][j] != 0: 
                value1 = G[i][j]
                for k in range(n): 
                    x1, x2 = 2*k, 2*k+1
                    if k != i and G[k][j] != 0: 
                        value2 = G[k][j]
                        M[s1].append((x2, max(value1, value2)))
    return M

def jumper(G, s, w):
    M = create_graph(G)

    n = len(G)
    s1, s2 = 2*s, 2*s+1
    w1, w2 = 2*w, 2*w + 1

    return min(dijkstry(M, s1, w1), dijkstry(M, s1, w2))


    

runtests(jumper)
