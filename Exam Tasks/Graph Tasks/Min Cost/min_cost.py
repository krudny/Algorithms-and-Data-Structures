from queue import PriorityQueue
from math import inf
from testy import runtests

def create_graph(T): 
    n = len(T)
    G = [[] for _ in range(n)]

    min_n = float('inf')
    max_n = 0
    min_idx = 0
    max_idx = 0
    
    for i in range(n):
        T[i] = (i, str(T[i]))

        if min_n > int(T[i][1]): 
            min_n = int(T[i][1])
            min_idx = i
        elif max_n < int(T[i][1]): 
            max_n = int(T[i][1])
            max_idx = i

    flag = True

    for i in range(n): 
        for j in range(i+1, n): 
            for char1 in T[i][1]: 
                for char2 in T[j][1]:
                    if char1 == char2 and flag: 
                        G[T[i][0]].append((T[j][0], abs(int(T[i][1]) - int(T[j][1]))))
                        G[T[j][0]].append((T[i][0], abs(int(T[i][1]) - int(T[j][1]))))
                        flag = False
            flag = True

    return G, min_idx, max_idx

def relax(G, distances, v, u, w):
    if distances[u] + w > distances[v]:
        distances[v] = distances[u] + w
        return True
    else:
        return False

def dijkstra(G, s, t):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    pq = PriorityQueue()
    weights[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight
                pq.put((weights[v], v))
        
        if u == t: break
                
    return weights[t] if weights[t] != inf else -1


def find_cost(P):
    G, s, t = create_graph(P)

    return dijkstra(G, s, t)


runtests(find_cost) 