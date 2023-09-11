from kol3atesty import runtests
from queue import PriorityQueue
from math import inf

def create_graph(E, S, n): 
    G = [[] for _ in range(n+1)]

    for edge in E: 
        s, t, w = edge
        G[s].append((t,w))
        G[t].append((s,w))

    for i in range(len(S)): 
        G[n].append((S[i], 0))
        G[S[i]].append((n, 0))
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
        
    
    return distances[t] if distances[t] != inf else None

def spacetravel(n, E, S, a, b):
    G = create_graph(E, S, n)
    return dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )