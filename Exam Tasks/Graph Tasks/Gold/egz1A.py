from egz1Atesty import runtests
from queue import PriorityQueue
from math import inf 

def dijkstry(G, s):
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
                
    return distances

def create_graph(G, V, r): 
    n = len(G)

    for i in range(n): 
        for j in range(len(G[i])): 
            dest, cost = G[i][j] 
            G[i][j] = (dest, 2*cost + r)

    return G

def find_min_cost(D1, D2, V): 
    n = len(D1)
    min_cost = inf

    for i in range(n): 
        cost = D1[i] + D2[i] - V[i]
        min_cost = min(min_cost, cost)

    return min_cost


def gold(G, V, s, t, r): 
    D1 = dijkstry(G, s)
    G = create_graph(G, V, r)
    D2 = dijkstry(G, t)
    return find_min_cost(D1, D2, V)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
