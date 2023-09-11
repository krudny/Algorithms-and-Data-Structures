from kol3btesty import runtests
from math import inf
from queue import PriorityQueue

def graph_transform(G, A): 
    n = len(G)
    G.append([])

    for i in range(n):
        G[n].append((i, A[i]))
        G[i].append((n, A[i]))

    return G

def dijkstra(G, s, t):
    n = len(G)
    distances = [inf] * n
    pq = PriorityQueue()
    distances[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                pq.put((distances[v], v))
        
        if u == t: break
                
    return distances[t]

def airports( G, A, s, t ):
    G = graph_transform(G, A)
    return dijkstra(G, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )